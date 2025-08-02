# QGEN_IMPFRAG Architecture Documentation

## System Architecture Overview

QGEN_IMPFRAG implements a three-stage pipeline for IFC file processing and 3D visualization:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Stage 1:      │    │   Stage 2:      │    │   Stage 3:      │
│   Backend       │────▶   Frontend      │────▶ Containerization│
│   Preparation   │    │   Visualization │    │   Deployment    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Stage 1: Backend Preparation

### Components
- **IFC Processor**: Main Python application (`ifc_processor.py`)
- **Fragment Converter**: Integration with `/data/XVUE/frag_convert/`
- **File Watcher**: Automatic processing of new IFC files
- **API Server**: REST API for frontend communication

### Technology Stack
- **Python 3.11**: Core processing logic
- **Flask**: Web API framework
- **Node.js 18+**: ThatOpen Components integration
- **@thatopen/fragments**: Fragment conversion library
- **Watchdog**: File system monitoring

### Data Flow
```
IFC Files → Validation → Fragment Conversion → Storage → API Exposure
```

## Stage 2: Frontend Visualization

### Components
- **3D Viewer**: ThatOpen Components-based viewer
- **File Manager**: Backend integration and file operations
- **UI Manager**: User interface and interactions
- **Property Inspector**: Element property display

### Technology Stack
- **TypeScript**: Type-safe JavaScript development
- **Three.js**: 3D graphics rendering
- **Vite**: Build tool and development server
- **ThatOpen Components**: BIM-specific utilities

### Interaction Flow
```
User Interface → File Selection → Fragment Loading → 3D Rendering → Property Display
```

## Stage 3: Containerization

### Container Architecture
```
┌─────────────────────────────────────┐
│             Production Container     │
├─────────────────┬───────────────────┤
│     Nginx       │     Supervisor    │
│   (Frontend)    │    (Process Mgmt) │
├─────────────────┼───────────────────┤
│  Static Files   │   Backend API     │
│     Serving     │   (Python/Flask)  │
└─────────────────┴───────────────────┘
```

### Multi-Stage Build
1. **Backend Builder**: Python + Node.js dependencies
2. **Frontend Builder**: TypeScript compilation and bundling
3. **Production Runtime**: Optimized Alpine Linux image

## Data Storage

### Directory Structure
```
/app/
├── data/
│   ├── ifc/           # Input IFC files
│   ├── fragments/     # Generated fragment files
│   └── reports/       # Conversion reports
├── backend/
│   ├── src/           # Python source code
│   └── logs/          # Application logs
└── frontend/
    ├── src/           # TypeScript source
    └── dist/          # Built static files
```

### File Persistence
- **Docker Volumes**: Persistent data storage
- **Bind Mounts**: Development file sharing
- **Network Storage**: Production deployment options

## API Architecture

### REST Endpoints
```
GET  /health                    # Health check
GET  /api/files                 # List IFC files and status
POST /api/convert               # Convert IFC to fragments
GET  /api/status/{filename}     # Conversion status
GET  /api/fragments/{filename}  # Download fragment file
```

### WebSocket (Future)
- Real-time conversion progress
- Live file system updates
- Multi-user collaboration

## Security Considerations

### Input Validation
- File type verification
- Size limits enforcement
- Path traversal prevention

### Container Security
- Non-root user execution
- Minimal attack surface
- Resource limitations

### Network Security
- Proxy configuration
- CORS policy enforcement
- HTTPS termination

## Performance Optimization

### Backend
- **Streaming Processing**: Large file handling
- **Async Operations**: Non-blocking I/O
- **Caching**: Fragment file caching
- **Resource Management**: Memory and CPU limits

### Frontend
- **Code Splitting**: Lazy loading
- **Asset Optimization**: Compression and caching
- **3D Rendering**: WebGL optimization
- **Progressive Loading**: Incremental model loading

## Monitoring and Observability

### Logging
- **Structured Logging**: JSON format
- **Log Aggregation**: Centralized collection
- **Error Tracking**: Exception monitoring
- **Performance Metrics**: Response times and throughput

### Health Checks
- **Container Health**: Docker health checks
- **Service Health**: Application-level monitoring
- **Dependency Health**: External service monitoring

## Scalability Considerations

### Horizontal Scaling
- **Load Balancing**: Multiple backend instances
- **Database Sharding**: Metadata distribution
- **CDN Integration**: Global static file delivery

### Vertical Scaling
- **Resource Allocation**: CPU and memory optimization
- **GPU Acceleration**: 3D rendering optimization
- **Storage Optimization**: SSD and NVMe utilization

## Integration Points

### External Dependencies
- **Fragment Converter**: `/data/XVUE/frag_convert/`
- **QGEN_DATAVIS**: UI pattern inheritance
- **ThatOpen Ecosystem**: Component library updates

### Extension Points
- **Plugin Architecture**: Custom processing modules
- **Webhook Integration**: External system notifications
- **API Extensions**: Additional endpoints and features

## Deployment Patterns

### Development
```bash
npm run dev  # Local development with hot reload
```

### Staging
```bash
docker-compose -f docker-compose.dev.yml up
```

### Production
```bash
docker-compose up --build
```

### Kubernetes (Future)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: qgen-impfrag
spec:
  replicas: 3
  # ... additional K8s configuration
```

## Error Handling and Recovery

### Backend Resilience
- **Graceful Degradation**: Partial functionality on failures
- **Circuit Breakers**: External service failure protection
- **Retry Logic**: Transient error recovery
- **Backup Processing**: Alternative conversion paths

### Frontend Resilience
- **Error Boundaries**: React-style error containment
- **Offline Support**: Local caching and queue
- **Progressive Enhancement**: Feature detection
- **Fallback UI**: Graceful degradation

## Future Enhancements

### Short Term
- Real-time collaboration features
- Advanced property filtering
- Custom material rendering
- Batch processing optimization

### Long Term
- AI-powered model analysis
- Cloud-native deployment
- Mobile application support
- VR/AR visualization integration
