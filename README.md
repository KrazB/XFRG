# XFRG - IFC Processing and Fragment Viewer Application

**Repository:** KrazB/XFRG | **Domain:** XQG4_AXIS | **Tenant:** QGEN | **Project:** IMPFRAG

## 🎯 Project Overview

XFRG is a comprehensive three-stage application designed for IFC file processing, fragments conversion, and 3D visualization. The application provides a complete pipeline from IFC import to containerized deployment, making it easily portable and deployable across different environments.

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.9+ (for local development)

### Quick Start (GitHub Clone)
```bash
# Clone the repository
git clone https://github.com/KrazB/XFRG.git
cd XFRG

# Automatic cross-platform setup
# Linux/macOS:
chmod +x scripts/setup-cross-platform.sh
./scripts/setup-cross-platform.sh

# Windows:
scripts\setup-cross-platform.bat

# Run application
docker-compose up
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

The application operates in three distinct stages:

### Stage 1: Backend Preparation
- **Purpose**: IFC file import and conversion to fragments format
- **Technology**: Python + Node.js + ThatOpen Components
- **Process**: 
  1. Import IFC files from the project root folder
  2. Convert IFC to optimized fragments format using ThatOpen Components
  3. Store fragments files locally for frontend consumption

### Stage 2: Frontend Visualization
- **Purpose**: 3D viewing and interaction with fragments files
- **Technology**: Vite + TypeScript + Three.js + ThatOpen Components
- **Process**:
  1. Load fragments files in a browser-based 3D viewer
  2. Provide interactive navigation and object selection
  3. Display model properties and metadata

### Stage 3: Containerization
- **Purpose**: Full application packaging for deployment
- **Technology**: Docker + Multi-stage builds
- **Process**:
  1. Containerize all dependencies and runtime environments
  2. Create lean, production-ready container images
  3. Enable lift-and-shift deployment to any Docker-compatible environment

## 🚀 Project Structure

```
XFRG/
├── README.md                   # This file
├── docker-compose.yml          # Multi-service orchestration
├── Dockerfile                  # Multi-stage container build
├── .dockerignore              # Docker build context exclusions
├── package.json               # Root project configuration
├── requirements.txt           # Python dependencies
├── backend/                   # Stage 1: IFC Processing
│   ├── src/
│   │   ├── ifc_processor.py   # Main IFC processing module
│   │   ├── fragments_converter.py # Fragment conversion utilities
│   │   └── config.py          # Backend configuration
│   ├── package.json           # Node.js dependencies for conversion
│   ├── requirements.txt       # Python-specific dependencies
│   └── logs/                  # Processing logs and reports
├── frontend/                  # Stage 2: 3D Viewer
│   ├── src/
│   │   ├── main.ts            # Main application entry point
│   │   ├── viewer/            # 3D viewer components
│   │   ├── ui/                # User interface components
│   │   └── utils/             # Utility functions
│   ├── public/                # Static assets
│   ├── dist/                  # Built frontend assets
│   ├── package.json           # Frontend dependencies
│   ├── tsconfig.json          # TypeScript configuration
│   └── vite.config.js         # Vite build configuration
├── data/                      # Data directory
│   ├── ifc/                   # Input IFC files
│   ├── fragments/             # Generated fragments files
│   └── reports/               # Conversion and processing reports
├── scripts/                   # Utility and automation scripts
│   ├── setup.sh               # Environment setup
│   ├── build.sh               # Build automation
│   ├── run-dev.sh             # Development server
│   └── deploy.sh              # Deployment automation
└── docs/                      # Documentation
    ├── ARCHITECTURE.md         # Technical architecture
    ├── DEPLOYMENT.md           # Deployment guide
    └── API.md                  # API documentation
```

## 🛠️ Technology Stack

### Backend (Stage 1)
- **Python 3.9+**: Main processing logic
- **Node.js 18+**: ThatOpen Components integration
- **@thatopen/fragments**: Fragment conversion library
- **@thatopen/components**: BIM processing utilities

### Frontend (Stage 2)
- **Vite**: Fast build tool and development server
- **TypeScript**: Type-safe JavaScript development
- **Three.js**: 3D graphics and rendering
- **ThatOpen Components**: BIM-specific UI and utilities
- **ThatOpen Fragments**: Fragment loading and visualization

### Containerization (Stage 3)
- **Docker**: Application containerization
- **Docker Compose**: Multi-service orchestration
- **Multi-stage builds**: Optimized production images
- **Alpine Linux**: Lightweight base images

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

## �🚦 Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.9+ (for local development)

### Quick Start (Containerized)
```bash
# Clone and navigate to the project
cd /data/XVUE/XQG4_AXIS/QGEN_IMPFRAG

# Build and run the application
docker-compose up --build

# Access the application
# Backend: http://localhost:8111
# Frontend: http://localhost:3111
```

### Development Setup
```bash
# Install dependencies
npm run setup

# Run in development mode
npm run dev

# Or run individual stages
npm run dev:backend    # Stage 1
npm run dev:frontend   # Stage 2
```

## 📋 Usage Workflow

1. **Place IFC files** in the `data/ifc/` directory
2. **Run Stage 1**: Process IFC files and generate fragments
3. **Run Stage 2**: Launch the 3D viewer to visualize fragments
4. **Deploy**: Use Docker containers for production deployment

## 🔄 Integration Points

- **Fragment Converter**: Leverages `/data/XVUE/frag_convert/` utilities
- **Viewer Components**: Inherits patterns from `/data/XVUE/XQG4_AXIS/QGEN_DATAVIS/U7_FR/`
- **Architecture**: Follows QGEN project structure and conventions

## 📊 Performance Goals

- **Conversion**: 90%+ compression ratio for IFC to fragments
- **Loading**: Sub-second fragment loading for typical models
- **Container Size**: <500MB total application size
- **Startup Time**: <30 seconds cold start including all services

## 🔒 Security Considerations

- Input validation for IFC file uploads
- Sandboxed processing environment
- Container security best practices
- Network isolation between services

## 📈 Monitoring and Logging

- Conversion progress tracking
- Performance metrics collection
- Error logging and recovery
- Container health monitoring

---

**Version**: 1.0.0  
**Last Updated**: July 28, 2025  
**Maintainer**: XQG4_AXIS Team
