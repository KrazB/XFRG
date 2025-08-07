# XFRG - IFC Processing and Fragment Viewer - Quick Start Guide

## 🚀 Overview

XFRG is a complete IFC file processing and 3D visualization application with a fully functional conversion pipeline:

1. **Backend**: Python Flask API + Node.js IFC converter using ThatOpen Components
2. **Frontend**: TypeScript/Vite 3D viewer with real-time progress tracking
3. **Converter**: Node.js script with ThatOpen Components IfcImporter for IFC→Fragment conversion

## ⚡ Quick Start (5 minutes)

### Option 1: Development Mode (Recommended)
```bash
cd D:\XFRG

# Start Frontend (Terminal 1)
cd frontend
npm run dev
# Runs on http://localhost:3111

# Start Backend (Terminal 2 or VS Code Task)
cd D:\XFRG
python backend/app.py
# Runs on http://localhost:8111
```

### Option 2: VS Code Tasks
```bash
# From VS Code Command Palette (Ctrl+Shift+P):
Tasks: Run Task → "Start Frontend Dev Server"
Tasks: Run Task → "Start Backend Server"
```

### Option 3: Docker (Complete Stack)
```bash
cd D:\XFRG

# Build and start all services
docker-compose up --build

# Access at:
# Frontend: http://localhost:3111
# Backend:  http://localhost:8111
```

## 📁 IFC Conversion Workflow

### 1. Web Interface Upload
1. Open frontend: http://localhost:3111
2. Drag & drop IFC files or click "Browse Files"
3. Watch real-time conversion progress
4. Auto-load converted fragments in 3D viewer

### 2. Pre-converted Fragments
- Load existing fragments from `data/fragments/`
- Example: `Village_ARCH_Building C_R22-1_detached.frag` (62.6 MB)
- Instant loading with full 3D navigation

### 3. Command Line Conversion
```bash
cd D:\XFRG\backend
node ifc_converter.js --input "path/to/file.ifc" --output "path/to/output.frag"
```

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    XFRG Application                         │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Frontend      │    Backend      │    IFC Converter        │
│   (Port 3111)   │   (Port 8111)   │   (Node.js Process)     │
│                 │                 │                         │
│ • TypeScript    │ • Python Flask │ • ThatOpen Components   │
│ • Vite          │ • File Upload   │ • IfcImporter.process() │
│ • Three.js      │ • Progress API  │ • 82% Compression       │
│ • Progress UI   │ • Error Handling│ • WASM (web-ifc)        │
└─────────────────┴─────────────────┴─────────────────────────┘
```

## 🛠️ Development

### Project Structure
```
XFRG/
├── backend/                   # Python Flask API + Node.js converter
│   ├── app.py                # Flask server (port 8111)
│   ├── ifc_converter.js      # Node.js converter with ThatOpen Components
│   ├── package.json          # Node.js dependencies (@thatopen/*)
│   └── requirements.txt      # Python dependencies (flask, flask-cors)
├── frontend/                 # TypeScript 3D viewer
│   ├── src/
│   │   ├── main.ts          # Main app with IFC upload & progress UI
│   │   └── utils/           # API helpers and UI managers
│   ├── package.json         # Frontend dependencies (vite, three.js)
│   ├── tsconfig.json        # TypeScript configuration
│   └── vite.config.js       # Vite dev server (port 3111)
├── data/                    # IFC files and converted fragments
│   ├── ifc/                # Input IFC files
│   └── fragments/          # Generated .frag files
├── .vscode/
│   └── tasks.json          # VS Code tasks for dev servers
└── node_modules/           # Root dependencies (ThatOpen Components)
```

### Key Technologies & Dependencies
**Backend Stack:**
- **Python 3.12**: Flask web server
- **Node.js 18+**: ThatOpen Components converter
- **@thatopen/components@2.4.11**: BIM processing library
- **@thatopen/fragments@3.0.7**: Fragment format library  
- **web-ifc@0.0.68**: WASM IFC parser

**Frontend Stack:**
- **TypeScript**: Type-safe development
- **Vite**: Fast dev server and build tool
- **Three.js@0.175.0**: 3D graphics engine
- **ThatOpen UI**: BIM-specific UI components

**Conversion Performance:**
- **Input**: 359 MB IFC file
- **Output**: 62.6 MB fragment file
- **Compression**: 82% size reduction
- **Processing Time**: ~2-3 minutes for large models

## 📋 Available Commands

### Development (VS Code Tasks)
```bash
# From Command Palette (Ctrl+Shift+P)
Tasks: Run Task → "Start Frontend Dev Server"
Tasks: Run Task → "Start Backend Server"  
Tasks: Run Task → "Install Backend Dependencies"
```

### Manual Development
```bash
# Frontend development server
cd frontend && npm run dev

# Backend API server  
cd D:\XFRG && python backend/app.py

# Manual IFC conversion
cd backend && node ifc_converter.js --input "file.ifc" --output "file.frag"
```

### Docker Production
```bash
docker-compose up --build     # Full application stack
docker-compose up frontend   # Frontend only
docker-compose up backend    # Backend only
```

### Dependency Management
```bash
# Install all dependencies
npm install                   # Root ThatOpen Components packages
cd backend && npm install    # Node.js converter dependencies  
cd frontend && npm install   # Frontend UI dependencies

# Python dependencies
pip install flask flask-cors
```

## 🔗 API Endpoints

### Backend REST API (localhost:8111)
- **POST /api/convert**: Upload IFC file for conversion
- **GET /health**: Health check endpoint
- **GET /api/status**: Get conversion status

### Frontend Dev Server (localhost:3111)
- **GET /**: Main application interface
- **Static assets**: Vite-served frontend files

## 🔗 Integration

- **Fragment Converter**: Uses `/data/XVUE/frag_convert/`
- **UI Patterns**: Inherits from `/data/XVUE/XQG4_AXIS/QGEN_DATAVIS/`
- **Containerization**: Production-ready Docker setup

## 📊 Performance & Features

### Conversion Performance
- **Compression Ratio**: 82%+ size reduction (IFC → fragments)
- **Large File Support**: Successfully tested with 359+ MB IFC files
- **Processing Speed**: ~2-3 minutes for complex architectural models
- **Memory Efficiency**: Optimized for large model processing

### 3D Viewer Features
- **Real-time Loading**: Sub-second fragment loading
- **Interactive Navigation**: Mouse orbit, pan, zoom controls
- **Object Selection**: Click objects to view properties
- **Element Filtering**: Filter by IFC categories (walls, slabs, etc.)
- **Progress Tracking**: Real-time conversion progress bars

### System Requirements
- **Memory**: 4GB+ RAM recommended for large IFC files
- **Storage**: ~40% of original IFC file size for fragments
- **Browser**: Modern browser with WebGL 2.0 support
- **Node.js**: Version 18+ for optimal ThatOpen Components performance

## 🔧 Port Configuration

| Service | Development URL | Production URL | Purpose |
|---------|----------------|----------------|---------|
| **Frontend** | `http://localhost:3111` | `http://localhost:80` | 3D viewer interface |
| **Backend** | `http://localhost:8111` | `http://localhost:8111` | IFC conversion API |
| **Vite HMR** | `http://localhost:24678` | N/A | Hot module reload |

## 🆘 Troubleshooting

### Common Issues & Solutions

**1. "Cannot find ThatOpen Components"**
```bash
# Solution: Install root dependencies
cd D:\XFRG
npm install
```

**2. "FRAGS.Serializer.export is not a function"**  
✅ **Fixed**: Updated to use `FRAGS.IfcImporter().process()` API

**3. "WASM file not found"**
```bash
# Solution: Verify web-ifc installation
cd D:\XFRG && dir node_modules\web-ifc
```

**4. "Port 3111/8111 already in use"**
```bash
# Solution: Kill existing processes
tasklist | findstr node
taskkill /PID [process_id] /F
```

**5. Backend connection failed**
- Ensure backend is running on localhost:8111
- Check Windows Firewall settings
- Verify Python Flask server started successfully

### Health Checks
```bash
# Test backend API
curl http://localhost:8111/health

# Test frontend loading  
curl http://localhost:3111

# Test IFC converter directly
cd backend && node ifc_converter.js --help
```

## 📚 Documentation

- [Architecture](docs/ARCHITECTURE.md) - Technical deep dive
- [Deployment](docs/DEPLOYMENT.md) - Production deployment guide
- [Strategy](STRATEGY.md) - Implementation roadmap

## 🎯 Next Steps

1. **Place IFC files** in `data/ifc/` directory
2. **Start the application** using Docker or development mode
3. **Open the viewer** and explore the 3D models
4. **Customize** the application for your specific needs

---

**Need Help?** Check the docs/ directory or the troubleshooting section above.
