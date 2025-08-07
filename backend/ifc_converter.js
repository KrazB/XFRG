#!/usr/bin/env node
/**
 * IFC to Fragments Converter using ThatOpen Components
 * ==================================================
 * 
 * This script converts IFC files to fragment format using ThatOpen Components.
 * It can be used standalone or called from the Python backend.
 * 
 * Usage:
 *   node ifc_converter.js --input input.ifc --output output.frag
 *   node ifc_converter.js --input-dir ./data/ifc --output-dir ./data/fragments
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Get current directory for ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Use root node_modules where all packages are actually installed
const rootNodeModules = path.resolve(__dirname, '../node_modules');
let nodeModulesPath = rootNodeModules;

console.log(`🔍 Looking for dependencies in: ${nodeModulesPath}`);

// ThatOpen Components imports
let OBC, FRAGS, WEBIFC;

try {
    // Use standard ES module imports
    console.log('🔧 Loading ThatOpen Components...');
    
    const obcModule = await import('@thatopen/components');
    OBC = obcModule.default || obcModule;
    console.log('✅ @thatopen/components loaded');
    
    const fragsModule = await import('@thatopen/fragments');
    FRAGS = fragsModule.default || fragsModule;
    console.log('✅ @thatopen/fragments loaded');
    
    const webifcModule = await import('web-ifc');
    WEBIFC = webifcModule.default || webifcModule;
    console.log('✅ web-ifc loaded');
    
    console.log('✅ All ThatOpen Components loaded successfully');
} catch (error) {
    console.error('❌ Failed to load ThatOpen Components:', error.message);
    console.error('   Make sure to run: npm install @thatopen/components @thatopen/fragments web-ifc');
    process.exit(1);
}

class IfcFragmentsConverter {
    constructor() {
        console.log('🔧 IFC Fragments Converter initialized (using IfcImporter)');
    }

    async convertFile(inputPath, outputPath) {
        try {
            console.log(`🔄 Converting: ${inputPath} -> ${outputPath}`);
            
            // Check if input file exists
            if (!fs.existsSync(inputPath)) {
                throw new Error(`Input file not found: ${inputPath}`);
            }
            
            // Read IFC file as Buffer
            const ifcData = fs.readFileSync(inputPath);
            console.log(`📖 Read IFC file: ${(ifcData.length / 1024 / 1024).toFixed(2)} MB`);
            
            // Create IFC importer
            const serializer = new FRAGS.IfcImporter();
            
            // Configure WASM path
            serializer.wasm = {
                path: nodeModulesPath + '/web-ifc/',
                absolute: true
            };
            
            console.log('🏗️  Converting IFC to fragments...');
            
            // Convert IFC to fragments using the correct API
            const fragmentsData = await serializer.process({
                bytes: new Uint8Array(ifcData),
                raw: false, // Compressed output
                progressCallback: (progress) => {
                    console.log(`Progress: ${Math.round(progress * 100)}%`);
                }
            });
            
            // Save to output file
            fs.writeFileSync(outputPath, fragmentsData);
            
            const outputSize = fs.statSync(outputPath).size;
            const inputSize = fs.statSync(inputPath).size;
            const compressionRatio = ((1 - outputSize / inputSize) * 100).toFixed(1);
            
            console.log(`✅ Conversion completed:`);
            console.log(`   Input:  ${(inputSize / 1024 / 1024).toFixed(2)} MB`);
            console.log(`   Output: ${(outputSize / 1024 / 1024).toFixed(2)} MB`);
            console.log(`   Compression: ${compressionRatio}%`);
            
            return {
                success: true,
                inputSize,
                outputSize,
                compressionRatio: parseFloat(compressionRatio),
                outputPath
            };
            
        } catch (error) {
            console.error(`❌ Conversion failed: ${error.message}`);
            return {
                success: false,
                error: error.message
            };
        }
    }

    async convertDirectory(inputDir, outputDir) {
        try {
            console.log(`🔄 Converting directory: ${inputDir} -> ${outputDir}`);
            
            // Ensure output directory exists
            fs.mkdirSync(outputDir, { recursive: true });
            
            // Find all IFC files
            const ifcFiles = fs.readdirSync(inputDir)
                .filter(file => file.toLowerCase().endsWith('.ifc'))
                .map(file => path.join(inputDir, file));
            
            if (ifcFiles.length === 0) {
                console.log('⚠️  No IFC files found in input directory');
                return { success: true, converted: 0 };
            }
            
            console.log(`📁 Found ${ifcFiles.length} IFC files`);
            
            const results = [];
            for (const ifcFile of ifcFiles) {
                const baseName = path.basename(ifcFile, '.ifc');
                const outputFile = path.join(outputDir, `${baseName}.frag`);
                
                const result = await this.convertFile(ifcFile, outputFile);
                results.push({ inputFile: ifcFile, outputFile, ...result });
            }
            
            const successful = results.filter(r => r.success).length;
            console.log(`🎉 Batch conversion completed: ${successful}/${results.length} files`);
            
            return {
                success: true,
                converted: successful,
                total: results.length,
                results
            };
            
        } catch (error) {
            console.error(`❌ Directory conversion failed: ${error.message}`);
            return {
                success: false,
                error: error.message
            };
        }
    }
}

// CLI interface
async function main() {
    const args = process.argv.slice(2);
    
    if (args.length === 0) {
        console.log(`
Usage:
  Single file:    node ifc_converter.js --input file.ifc --output file.frag
  Directory:      node ifc_converter.js --input-dir ./ifc --output-dir ./fragments
  Test mode:      node ifc_converter.js --test
        `);
        process.exit(1);
    }
    
    const converter = new IfcFragmentsConverter();
    
    if (args.includes('--test')) {
        // Test mode - convert sample files if available
        const testInputDir = path.join(__dirname, '../data/ifc');
        const testOutputDir = path.join(__dirname, '../data/fragments');
        
        console.log('🧪 Running in test mode');
        console.log(`   Input dir:  ${testInputDir}`);
        console.log(`   Output dir: ${testOutputDir}`);
        
        const result = await converter.convertDirectory(testInputDir, testOutputDir);
        process.exit(result.success ? 0 : 1);
    }
    
    const inputIndex = args.indexOf('--input');
    const outputIndex = args.indexOf('--output');
    const inputDirIndex = args.indexOf('--input-dir');
    const outputDirIndex = args.indexOf('--output-dir');
    
    if (inputIndex !== -1 && outputIndex !== -1) {
        // Single file conversion
        const inputFile = args[inputIndex + 1];
        const outputFile = args[outputIndex + 1];
        
        const result = await converter.convertFile(inputFile, outputFile);
        process.exit(result.success ? 0 : 1);
        
    } else if (inputDirIndex !== -1 && outputDirIndex !== -1) {
        // Directory conversion
        const inputDir = args[inputDirIndex + 1];
        const outputDir = args[outputDirIndex + 1];
        
        const result = await converter.convertDirectory(inputDir, outputDir);
        process.exit(result.success ? 0 : 1);
        
    } else {
        console.error('❌ Invalid arguments. Use --help for usage information.');
        process.exit(1);
    }
}

// Run if called directly
if (process.argv[1] && process.argv[1].endsWith('ifc_converter.js')) {
    main().catch(error => {
        console.error('❌ Unhandled error:', error);
        process.exit(1);
    });
}

export { IfcFragmentsConverter };
