# QGEN_IMPFRAG - Quick Start Guide

## 🚀 Overview

QGEN_IMPFRAG is a three-stage application for IFC file processing and 3D visualization:

1. **Backend**: Convert IFC files to optimized fragments format
2. **Frontend**: Visualize fragments in an interactive 3D viewer  
3. **Container**: Deploy as a portable, containerized application

## ⚡ Quick Start (5 minutes)

### Option 1: Docker (Recommended)
```bash
cd /data/XVUE/XQG4_AXIS/QGEN_IMPFRAG

# Start the application
docker-compose up --build

# Access the viewer at http://localhost:80
```

### Option 2: Development Mode
```bash
cd /data/XVUE/XQG4_AXIS/QGEN_IMPFRAG

# Setup environment
./scripts/setup.sh

# Start development servers
./scripts/run-dev.sh

# Frontend: http://localhost:3111
# Backend:  http://localhost:8000
```

## 📁 Adding IFC Files

1. Place IFC files in: `data/ifc/`
2. Files are automatically detected and converted
3. View converted fragments in the 3D viewer
4. Click objects to see properties

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Stage 1:      │────▶   Stage 2:      │────▶   Stage 3:      │
│   Backend       │    │   Frontend      │    │ Containerization│
│   (IFC → Frag)  │    │   (3D Viewer)   │    │   (Docker)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Development

### Project Structure
```
QGEN_IMPFRAG/
├── backend/           # Python Flask API + conversion
├── frontend/          # TypeScript + Three.js viewer
├── data/             # IFC input, fragments output
├── docker/           # Container configuration
├── scripts/          # Automation scripts
└── docs/             # Documentation
```

### Key Technologies
- **Backend**: Python, Flask, Node.js, ThatOpen Components
- **Frontend**: TypeScript, Vite, Three.js, ThatOpen Fragments
- **Container**: Docker, Nginx, Supervisor

## 📋 Commands

### Development
```bash
npm run dev              # Start both backend and frontend
npm run dev:backend      # Backend only
npm run dev:frontend     # Frontend only
```

### Production
```bash
docker-compose up        # Production deployment
docker-compose --profile production up  # Full stack
```

### Utility
```bash
./scripts/setup.sh       # Initial setup
./scripts/build.sh       # Build application
npm run convert          # Convert IFC files manually
```

## 🔗 Integration

- **Fragment Converter**: Uses `/data/XVUE/frag_convert/`
- **UI Patterns**: Inherits from `/data/XVUE/XQG4_AXIS/QGEN_DATAVIS/`
- **Containerization**: Production-ready Docker setup

## 📊 Performance

- **Compression**: 90%+ size reduction (IFC → fragments)
- **Loading**: Sub-second fragment loading
- **Container**: <30 second startup time
- **Memory**: <2GB for typical models

## � Port Configuration

| Mode | Frontend URL | Backend URL | Notes |
|------|-------------|-------------|-------|
| **Development** | `http://localhost:3111` | `http://localhost:8000` | Hot reload, debugging |
| **Production** | `http://localhost:80` | `http://localhost:8000` | Complete application |
| **Docker Dev** | `http://localhost:3111` | `http://localhost:8000` | Containerized development |

## �🆘 Troubleshooting

### Common Issues
1. **Port conflicts**: Change ports in docker-compose.yml
2. **Permission errors**: Run `chmod +x scripts/*.sh`
3. **Memory issues**: Increase Docker memory limit
4. **Fragment converter**: Ensure `/data/XVUE/frag_convert/` is accessible

### Health Checks
```bash
curl http://localhost:8000/health    # Backend
curl http://localhost:3111           # Frontend
docker-compose ps                    # Container status
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
