#!/usr/bin/env python3
"""
QGEN_IMPFRAG Backend API Server
=============================

Simple Flask API server to serve converted fragment files to the frontend.
"""

import os
import json
from pathlib import Path
from datetime import datetime
from flask import Flask, jsonify, send_file, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration
FRAGMENTS_DIR = Path("/data/XVUE/XQG4_AXIS/QGEN_IMPFRAG/data/fragments")
IFC_DIR = Path("/data/XVUE/XQG4_AXIS/QGEN_IMPFRAG/data/ifc")

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "qgen-impfrag-backend"
    })

@app.route('/api/fragments', methods=['GET'])
def list_fragments():
    """List available fragment files"""
    fragments = []
    
    for frag_file in FRAGMENTS_DIR.glob("*.frag"):
        stat = frag_file.stat()
        fragments.append({
            "filename": frag_file.name,
            "size_mb": round(stat.st_size / (1024 * 1024), 2),
            "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "url": f"/api/fragments/{frag_file.name}"
        })
    
    return jsonify({
        "fragments": fragments,
        "count": len(fragments),
        "total_size_mb": round(sum(f["size_mb"] for f in fragments), 2)
    })

@app.route('/api/fragments/<filename>', methods=['GET'])
def serve_fragment(filename):
    """Serve a fragment file"""
    fragment_file = FRAGMENTS_DIR / filename
    
    if not fragment_file.exists():
        return jsonify({"error": f"Fragment file not found: {filename}"}), 404
    
    return send_file(fragment_file, as_attachment=False, mimetype='application/octet-stream')

@app.route('/api/ifc', methods=['GET'])
def list_ifc_files():
    """List available IFC files and their conversion status"""
    files = []
    
    for ifc_file in IFC_DIR.glob("*.ifc"):
        # Look for corresponding fragment file
        fragment_name = f"{ifc_file.stem.replace(' ', '_').replace('(', '').replace(')', '')}.frag"
        fragment_file = FRAGMENTS_DIR / fragment_name
        
        stat = ifc_file.stat()
        files.append({
            "filename": ifc_file.name,
            "size_mb": round(stat.st_size / (1024 * 1024), 2),
            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "has_fragments": fragment_file.exists(),
            "fragment_file": fragment_name if fragment_file.exists() else None,
            "fragment_size_mb": round(fragment_file.stat().st_size / (1024 * 1024), 2) if fragment_file.exists() else None
        })
    
    return jsonify({
        "ifc_files": files,
        "count": len(files),
        "total_size_mb": round(sum(f["size_mb"] for f in files), 2)
    })

@app.route('/api/status', methods=['GET'])
def get_status():
    """Get overall system status"""
    ifc_count = len(list(IFC_DIR.glob("*.ifc")))
    fragment_count = len(list(FRAGMENTS_DIR.glob("*.frag")))
    
    return jsonify({
        "status": "running",
        "ifc_files": ifc_count,
        "fragment_files": fragment_count,
        "conversion_complete": fragment_count > 0,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🚀 Starting QGEN_IMPFRAG Backend API Server...")
    print(f"📁 IFC Directory: {IFC_DIR}")
    print(f"📁 Fragments Directory: {FRAGMENTS_DIR}")
    print(f"🌐 Server will run on http://0.0.0.0:8111")
    
    app.run(host='0.0.0.0', port=8111, debug=True)
