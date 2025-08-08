# XFRG → XSBH Automation Pipeline

## Overview

This automation pipeline manages the complete workflow from XFRG (development) to XSBH (distribution), including build automation, Docker deployment, and CI/CD integration.

## 🚀 Quick Start

### Prerequisites
- Windows 10/11 with cmd.exe
- Docker Desktop installed and running
- Node.js 18+ and npm
- Python 3.11+
- Git configured

### Basic Usage

1. **Build Everything:**
   ```cmd
   scripts\build-automation.bat all
   ```

2. **Sync XFRG → XSBH:**
   ```cmd
   scripts\sync-to-xsbh.bat
   ```

3. **Deploy to Staging:**
   ```cmd
   scripts\deploy-production.bat staging
   ```

4. **Deploy to Production:**
   ```cmd
   scripts\deploy-production.bat production yourdomain.com
   ```

## 📋 Available Scripts

### `scripts\build-automation.bat`
Complete build automation for both XFRG and XSBH projects.

**Usage:**
```cmd
build-automation.bat [mode]
```

**Modes:**
- `all` - Build everything (XFRG → sync → XSBH → Docker)
- `xfrg` - Build XFRG only
- `xsbh` - Build XSBH only
- `docker` - Build Docker image only
- `test` - Run tests only

**Example:**
```cmd
scripts\build-automation.bat all
```

### `scripts\sync-to-xsbh.bat`
Synchronizes XFRG development changes to XSBH distribution.

**Features:**
- Intelligent file filtering (excludes dev files)
- Build verification
- Rollback on failure
- Comprehensive logging

**Usage:**
```cmd
scripts\sync-to-xsbh.bat
```

### `scripts\deploy-production.bat`
Production deployment with health checks and rollback capability.

**Usage:**
```cmd
deploy-production.bat [mode] [domain]
```

**Modes:**
- `staging` - Deploy to staging environment
- `production` - Deploy to production environment
- `rollback` - Rollback to previous version
- `health` - Run health checks only

**Examples:**
```cmd
# Deploy to staging
scripts\deploy-production.bat staging

# Deploy to production
scripts\deploy-production.bat production yourdomain.com

# Health check
scripts\deploy-production.bat health
```

## 🐳 Docker Configuration

### Development (`docker-compose.yml`)
- Frontend: http://localhost:3111
- Backend: http://localhost:8111
- Simplified configuration for development

### Production (`docker-compose.prod.yml`)
- Frontend: http://localhost (port 80)
- Backend: http://localhost/api
- Nginx reverse proxy
- Redis caching
- Enhanced security headers
- Health checks and monitoring
- SSL/TLS support

### Multi-stage Dockerfile (`Dockerfile.prod`)
- Optimized for production
- Security hardening
- Non-root user execution
- Minimal attack surface
- Health checks

## 🔧 CI/CD Pipeline

### GitHub Actions (`.github/workflows/ci-cd.yml`)

**Workflow Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main`
- Manual workflow dispatch

**Pipeline Stages:**
1. **Build XFRG** - Test and build development version
2. **Sync to XSBH** - Automatically sync changes to distribution repo
3. **Build XSBH** - Build and test distribution version
4. **Build Docker** - Create production Docker images
5. **Deploy Staging** - Auto-deploy develop branch
6. **Deploy Production** - Manual deployment for main branch
7. **Security Scan** - Vulnerability scanning with Trivy

**Required Secrets:**
- `XSBH_TOKEN` - GitHub token for XSBH repository access

## 📊 Monitoring and Logging

### Log Files
- Build: `logs\build-automation.log`
- Sync: `logs\sync-to-xsbh.log`
- Deployment: `logs\deployment.log`

### Health Checks
- Frontend: `http://localhost:3111` (dev) or `http://localhost/health` (prod)
- Backend: `http://localhost:8111/health` (dev) or `http://localhost/api/health` (prod)

### Docker Health Checks
- Built-in container health monitoring
- Automatic restart on failure
- Comprehensive logging

## 🔒 Security Features

### Production Security
- Non-root container execution
- Security headers (HSTS, CSP, XSS protection)
- Rate limiting
- SSL/TLS configuration
- Vulnerability scanning

### File Filtering
- Automatic exclusion of development files
- Sensitive data protection
- Clean distribution builds

## 🚀 Deployment Strategies

### Staging Deployment
```cmd
scripts\deploy-production.bat staging
```
- Automatic deployment from develop branch
- Testing environment
- Full feature validation

### Production Deployment
```cmd
scripts\deploy-production.bat production yourdomain.com
```
- Manual confirmation required
- Automatic backup creation
- Health checks and monitoring
- Rollback capability

### Rollback
```cmd
scripts\deploy-production.bat rollback
```
- Instant rollback to previous version
- Automatic health verification

## 🔧 Configuration

### Environment Variables
Set these in your deployment environment:

**Development:**
```cmd
set NODE_ENV=development
set FLASK_ENV=development
set FLASK_DEBUG=1
```

**Production:**
```cmd
set NODE_ENV=production
set FLASK_ENV=production
set FLASK_DEBUG=0
set VITE_API_BASE_URL=https://api.yourdomain.com
set CORS_ORIGINS=https://yourdomain.com
```

### Domain Configuration
Update these files for your domain:
- `docker-compose.prod.yml` - Update domain references
- `docker\nginx.prod.conf` - Update server_name
- Frontend environment variables

## 📈 Performance Optimization

### Docker Optimizations
- Multi-stage builds for minimal image size
- Layer caching for faster builds
- Production-optimized configurations

### Nginx Optimizations
- Gzip compression
- Static asset caching
- Connection keep-alive
- Rate limiting

### Build Optimizations
- Parallel builds where possible
- Dependency caching
- Incremental builds

## 🛠️ Troubleshooting

### Common Issues

**Build Failures:**
```cmd
# Check build logs
type logs\build-automation.log

# Clean and rebuild
scripts\build-automation.bat all
```

**Docker Issues:**
```cmd
# Check container status
docker ps

# View container logs
docker-compose logs

# Restart services
docker-compose restart
```

**Sync Issues:**
```cmd
# Check sync logs
type logs\sync-to-xsbh.log

# Manual sync verification
scripts\sync-to-xsbh.bat
```

### Debug Mode
Add `set DEBUG=1` at the top of any script for verbose output.

## 📞 Support

### Logs Location
- All logs: `D:\XFRG\logs\`
- Build automation: `logs\build-automation.log`
- Sync operations: `logs\sync-to-xsbh.log`
- Deployments: `logs\deployment.log`

### Health Check URLs
- **Development:**
  - Frontend: http://localhost:3111
  - Backend: http://localhost:8111/health

- **Production:**
  - Frontend: http://yourdomain.com/health
  - Backend: http://yourdomain.com/api/health

For additional support, check the logs and verify all prerequisites are installed.
