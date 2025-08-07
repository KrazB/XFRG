# XFRG - IFC Processing and Fragment Viewer Application

**Repository:** KrazB/XFRG | **Domain:** XQG4_AXIS | **Tenant:** QGEN | **Project:** IMPFRAG

## 🎯 Project Status: ✅ FULLY FUNCTIONAL

**Current Status**: Complete IFC conversion pipeline working perfectly!

### ✅ What's Working Right Now
- **IFC Upload & Conversion**: Drag & drop IFC files for instant conversion
- **Real-time Progress**: Live progress bars show conversion status  
- **3D Fragment Viewer**: Interactive navigation with object selection
- **Performance**: 82%+ compression (359MB IFC → 62.6MB fragments)
- **Development Servers**: Hot reload for frontend, Flask API backend
- **VS Code Integration**: Tasks for easy server management

### 🚀 Quick Start (2 Minutes)
```bash
# Terminal 1: Backend (port 8111)
cd D:\XFRG && python backend/app.py

# Terminal 2: Frontend (port 3111)
cd D:\XFRG\frontend && npm run dev

# Open: http://localhost:3111
# Upload IFC → Watch conversion → View in 3D ✨
```

### Prerequisites
- **Node.js 18+** (for ThatOpen Components and frontend)
- **Python 3.12+** (for Flask backend API)
- **4GB+ RAM** (recommended for large IFC files)
- **Modern Browser** (WebGL 2.0 support required)

### Quick Start (Development - Recommended)
```bash
# Clone the repository
git clone https://github.com/KrazB/XFRG.git
cd XFRG

# Install all dependencies
npm install

# Start Frontend (Terminal 1)
cd frontend && npm run dev
# Runs on http://localhost:3111

# Start Backend (Terminal 2)  
cd D:\XFRG && python backend/app.py
# Runs on http://localhost:8111

# Ready! Upload IFC files through the web interface
```

### Quick Start (VS Code Tasks)
```bash
# From VS Code Command Palette (Ctrl+Shift+P):
Tasks: Run Task → "Start Frontend Dev Server"
Tasks: Run Task → "Start Backend Server"

# Or use the Run and Debug panel
```

### Quick Start (Docker Only)
```bash
# Clone and navigate to the project
git clone https://github.com/KrazB/XFRG.git
cd XFRG

# Build and run the application
docker-compose up --build

# Access the application
# Backend: http://localhost:8111
# Frontend: http://localhost:3111
```nts **immediate protection** measures for intellectual property:

- **🐳 Encrypted Container Distribution**: Docker images secured with GPG/AES256
- **🎭 Code Obfuscation**: JavaScript minification + Python bytecode compilation  
- **🔑 Environment Licensing**: Hardware fingerprinting + time-limited licenses| **Tenant:** QGEN | **Project:** IMPFRAG

## 🎯 Project Overview

XFRG is a comprehensive three-stage application designed for IFC file processing, fragments conversion, and 3D visualization. The application provides a complete pipeline from IFC import to containerized deployment, making it easily portable and deployable across different environments.

## 🏗️ Application Architecture

The application operates with a modern three-tier architecture:

### Frontend (Port 3111)
- **Technology**: TypeScript + Vite + Three.js + ThatOpen Components
- **Purpose**: Interactive 3D viewer with IFC upload interface
- **Features**: 
  - Real-time progress bars during conversion
  - Drag & drop IFC file upload
  - 3D navigation and object selection
  - Element filtering and property viewing

### Backend (Port 8111)  
- **Technology**: Python Flask + REST API
- **Purpose**: File upload handling and conversion orchestration
- **Features**:
  - IFC file upload endpoint (`/api/convert`)
  - Progress tracking and status updates
  - Error handling and logging
  - CORS support for frontend communication

### IFC Converter (Node.js Process)
- **Technology**: Node.js + ThatOpen Components + web-ifc WASM
- **Purpose**: IFC to fragments conversion using industry-standard libraries
- **Features**:
  - `IfcImporter.process()` API integration
  - 82%+ compression ratio (359MB → 62.6MB tested)
  - Progress callbacks for real-time updates
  - Robust error handling and validation

## 🚀 Project Structure

```
XFRG/
├── README.md                       # Project documentation
├── QUICKSTART.md                   # 5-minute setup guide
├── package.json                    # Root dependencies (ThatOpen Components)
├── docker-compose.yml              # Multi-service orchestration
├── .vscode/
│   └── tasks.json                  # VS Code dev server tasks
├── backend/                        # Python Flask API + Node.js converter
│   ├── app.py                      # Flask server (port 8111) 
│   ├── ifc_converter.js            # Node.js converter with ThatOpen Components
│   ├── package.json                # Node.js dependencies (@thatopen/*)
│   └── requirements.txt            # Python dependencies (flask, flask-cors)
├── frontend/                       # TypeScript 3D viewer
│   ├── src/
│   │   ├── main.ts                 # Main app with IFC upload & progress UI
│   │   └── utils/                  # API helpers, UI managers, file handling
│   ├── package.json                # Frontend dependencies (vite, three.js)
│   ├── tsconfig.json               # TypeScript configuration
│   ├── vite.config.js              # Vite dev server (port 3111)
│   └── index.html                  # Main HTML template
├── data/                           # IFC files and converted fragments
│   ├── ifc/                        # Input IFC files (place files here)
│   └── fragments/                  # Generated .frag files (62.6MB example)
├── node_modules/                   # Root ThatOpen Components dependencies
│   ├── @thatopen/
│   │   ├── components@2.4.11       # BIM processing library
│   │   └── fragments@3.0.7         # Fragment format library
│   └── web-ifc@0.0.68              # WASM IFC parser
└── scripts/                        # Utility scripts (Docker, deployment)
```

## 🛠️ Technology Stack & Dependencies

### Backend Stack
- **Python 3.12**: Flask web server and API endpoints
- **Flask + Flask-CORS**: RESTful API with cross-origin support
- **Node.js 18+**: ThatOpen Components integration layer
- **@thatopen/components@2.4.11**: BIM processing and conversion library
- **@thatopen/fragments@3.0.7**: Fragment format handling and export
- **web-ifc@0.0.68**: WebAssembly IFC parser (high performance)

### Frontend Stack  
- **TypeScript**: Type-safe JavaScript development
- **Vite**: Fast development server with hot module replacement
- **Three.js@0.175.0**: 3D graphics engine for WebGL rendering
- **ThatOpen UI@2.4.4**: BIM-specific user interface components
- **Modern Browser APIs**: File upload, progress tracking, WebGL 2.0

### Development & Deployment
- **VS Code Tasks**: Integrated development workflow
- **Docker + Docker Compose**: Containerization and orchestration  
- **Multi-stage builds**: Optimized production container images
- **Hot Reload**: Real-time development feedback

### Performance Characteristics
- **Conversion Speed**: 2-3 minutes for 359MB IFC files
- **Compression Ratio**: 82%+ size reduction (IFC → fragments)
- **Memory Usage**: 4GB+ recommended for large models
- **Loading Time**: Sub-second fragment loading in viewer

## � Security & IP Protection

QGEN_IMPFRAG implements **immediate protection** measures for intellectual property:

- **🐳 Encrypted Container Distribution**: Docker images secured with GPG/AES256
- **🎭 Code Obfuscation**: JavaScript minification + Python bytecode compilation  
- **🔑 Environment Licensing**: Hardware fingerprinting + time-limited licenses

### Secure Deployment
```bash
# For development/testing
./quick-start.sh

# For secure production distribution  
./scripts/secure-build.sh
```

See [`docs/IP_PROTECTION.md`](docs/IP_PROTECTION.md) for complete security documentation.

## 🚦 Getting Started

### Development Setup (Recommended)
```bash
# 1. Clone and install dependencies
git clone https://github.com/KrazB/XFRG.git
cd XFRG
npm install  # Installs ThatOpen Components in root node_modules

# 2. Start frontend development server
cd frontend
npm run dev  # Runs on http://localhost:3111

# 3. Start backend API server (new terminal)
cd D:\XFRG  
python backend/app.py  # Runs on http://localhost:8111

# 4. Ready! Open browser to http://localhost:3111
```

### VS Code Integration
```bash
# Use Command Palette (Ctrl+Shift+P)
Tasks: Run Task → "Start Frontend Dev Server"
Tasks: Run Task → "Start Backend Server"

# Or use integrated terminal with tasks
Terminal → Run Task → Select desired task
```

### Docker Deployment
```bash
# Build and run containerized application
docker-compose up --build

# Access services:
# Frontend: http://localhost:3111  
# Backend:  http://localhost:8111
```

## 📋 Usage Workflow

### Complete IFC Conversion Process

1. **Start Development Servers**
   ```bash
   # Terminal 1: Frontend
   cd frontend && npm run dev
   
   # Terminal 2: Backend  
   cd D:\XFRG && python backend/app.py
   ```

2. **Upload and Convert IFC Files**
   - Open http://localhost:3111 in browser
   - Drag & drop IFC files or click "Browse Files"
   - Watch real-time conversion progress
   - Converted fragments auto-load in 3D viewer

3. **Explore 3D Models**
   - Mouse navigation: orbit, pan, zoom
   - Click objects to view properties
   - Filter elements by category (walls, slabs, etc.)
   - Export/download converted fragments

### Alternative: Load Pre-converted Fragments
- Place .frag files in `data/fragments/`
- Use "Browse Files" to load existing fragments  
- Example: `Village_ARCH_Building C_R22-1_detached.frag` (62.6 MB)

### Command Line Conversion
```bash
# Direct conversion without web interface
cd backend
node ifc_converter.js --input "path/to/model.ifc" --output "path/to/model.frag"
```

## 🔄 Integration Points

- **Fragment Converter**: Leverages `/data/XVUE/frag_convert/` utilities
- **Viewer Components**: Inherits patterns from `/data/XVUE/XQG4_AXIS/QGEN_DATAVIS/U7_FR/`
- **Architecture**: Follows QGEN project structure and conventions

## 📊 Performance & Technical Specifications

### Conversion Performance
- **Tested File Size**: 359 MB IFC → 62.6 MB fragments
- **Compression Ratio**: 82%+ size reduction
- **Processing Time**: 2-3 minutes for large architectural models
- **Memory Requirements**: 4GB+ RAM recommended
- **Supported Formats**: IFC 2x3, IFC4, IFC4x3

### 3D Viewer Performance  
- **Loading Speed**: Sub-second fragment loading
- **Browser Support**: Modern browsers with WebGL 2.0
- **Navigation**: Smooth 60fps orbit, pan, zoom controls
- **Selection**: Real-time object picking and highlighting
- **Properties**: Instant property panel updates

### System Requirements
- **Operating System**: Windows 10+, macOS 10.15+, Linux
- **Node.js**: Version 18+ (for ThatOpen Components)
- **Python**: Version 3.12+ (Flask backend)
- **Browser**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **Hardware**: 4GB RAM, dedicated graphics recommended

## 🔒 Security & Development Considerations

### Input Validation & Processing
- File type validation for IFC uploads
- File size limits and memory management
- Sandboxed Node.js conversion processes  
- Error handling and graceful failure recovery

### Development Security
- CORS configuration for local development
- Environment-based configuration management
- Secure file handling and temporary file cleanup
- Process isolation between frontend and conversion

### Container Security (Production)
- Multi-stage Docker builds for minimal attack surface
- Non-root user execution in containers
- Network isolation between services
- Secure secrets management

## 📈 Monitoring and Logging

- Conversion progress tracking
- Performance metrics collection
- Error logging and recovery
- Container health monitoring

---

**Version**: 1.0.0  
**Status**: ✅ Fully Functional IFC Conversion Pipeline  
**Last Updated**: August 7, 2025  
**Maintainer**: KrazB/XFRG Team

### 🎯 Quick Links
- **Frontend**: http://localhost:3111 (3D viewer & upload interface)
- **Backend**: http://localhost:8111 (conversion API)  
- **Documentation**: [QUICKSTART.md](QUICKSTART.md) for 5-minute setup
- **Issues**: Submit via GitHub Issues for support
