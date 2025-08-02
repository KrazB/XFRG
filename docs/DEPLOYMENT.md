# QGEN_IMPFRAG Deployment Guide

## Overview

This guide covers deployment options for the QGEN_IMPFRAG application, from local development to production environments.

## Prerequisites

### System Requirements
- **Operating System**: Linux, macOS, or Windows with WSL2
- **Docker**: Version 20.10+ with Docker Compose
- **Memory**: Minimum 4GB RAM, 8GB+ recommended
- **Storage**: 10GB+ available space
- **Network**: Internet access for dependency downloads

### Software Dependencies
- **Docker Desktop**: For containerized deployment
- **Node.js 18+**: For local development
- **Python 3.9+**: For local development
- **Git**: For source code management

## Deployment Options

### 1. Local Development

#### Quick Start
```bash
# Clone the repository
cd /data/XVUE/XQG4_AXIS/QGEN_IMPFRAG

# Setup development environment
chmod +x scripts/setup.sh
./scripts/setup.sh

# Start development servers
chmod +x scripts/run-dev.sh
./scripts/run-dev.sh
```

#### Manual Setup
```bash
# Install backend dependencies
cd backend
npm install
pip3 install -r requirements.txt

# Install frontend dependencies
cd ../frontend
npm install

# Start backend
cd ../backend
python3 src/ifc_processor.py --dev --watch

# Start frontend (in another terminal)
cd ../frontend
npm run dev
```

**Access Points:**
- Frontend: http://localhost:3111
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### 2. Docker Development

```bash
# Start development with Docker
docker-compose -f docker-compose.dev.yml up --build

# View logs
docker-compose -f docker-compose.dev.yml logs -f

# Stop services
docker-compose -f docker-compose.dev.yml down
```

### 3. Production Deployment

#### Single-Node Production
```bash
# Build and start production services
docker-compose up --build -d

# Check service status
docker-compose ps

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

#### Production with Profiles
```bash
# Start with database
docker-compose --profile database up -d

# Start complete production stack
docker-compose --profile production up -d
```

## Configuration

### Environment Variables

Create a `.env` file for environment-specific configuration:

```bash
# Production Configuration
QGEN_IMPFRAG_HOST=0.0.0.0
QGEN_IMPFRAG_PORT=8000
QGEN_IMPFRAG_DEBUG=false
QGEN_IMPFRAG_LOG_LEVEL=INFO

# Data Persistence
QGEN_IMPFRAG_IFC_INPUT_DIR=/app/data/ifc
QGEN_IMPFRAG_FRAGMENTS_OUTPUT_DIR=/app/data/fragments

# Security
FLASK_SECRET_KEY=your-secret-key-here
CORS_ORIGINS=https://yourdomain.com

# Database (if using)
DATABASE_URL=postgresql://user:pass@db:5432/qgen_impfrag
```

### Volume Configuration

#### Development
```yaml
volumes:
  - ./data:/app/data                    # Data persistence
  - ./backend:/app/backend              # Code hot-reload
  - ./frontend:/app/frontend            # Code hot-reload
```

#### Production
```yaml
volumes:
  - qgen_data:/app/data                 # Named volume
  - qgen_logs:/app/logs                 # Log persistence
```

## Network Configuration

### Port Mapping
- **80**: Frontend (Nginx)
- **8000**: Backend API
- **3111**: Development frontend
- **5432**: PostgreSQL (if enabled)

### Reverse Proxy Setup

#### Nginx Configuration
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    
    location / {
        proxy_pass http://localhost:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### Traefik Configuration
```yaml
version: '3.8'
services:
  qgen-impfrag:
    image: qgen-impfrag:latest
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.qgen.rule=Host(`yourdomain.com`)"
      - "traefik.http.services.qgen.loadbalancer.server.port=80"
```

## SSL/TLS Configuration

### Using Certbot
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Obtain certificate
sudo certbot --nginx -d yourdomain.com

# Auto-renewal
sudo systemctl enable certbot.timer
```

### Using Docker with SSL
```yaml
version: '3.8'
services:
  nginx:
    image: nginx:alpine
    ports:
      - "443:443"
      - "80:80"
    volumes:
      - ./nginx-ssl.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/ssl/certs
```

## Monitoring and Logging

### Application Logs
```bash
# View application logs
docker-compose logs qgen-impfrag-app

# Follow logs in real-time
docker-compose logs -f qgen-impfrag-app

# View specific service logs
docker-compose logs backend
docker-compose logs frontend
```

### System Monitoring
```bash
# Container resource usage
docker stats

# Service health status
docker-compose ps

# System resources
docker system df
```

### Log Aggregation
```yaml
# Add to docker-compose.yml
services:
  app:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## Backup and Recovery

### Data Backup
```bash
# Backup data volumes
docker run --rm -v qgen_data:/data -v $(pwd):/backup \
  alpine tar czf /backup/qgen_data_backup.tar.gz -C /data .

# Backup database (if using)
docker-compose exec db pg_dump -U qgen qgen_impfrag > backup.sql
```

### Data Recovery
```bash
# Restore data volumes
docker run --rm -v qgen_data:/data -v $(pwd):/backup \
  alpine tar xzf /backup/qgen_data_backup.tar.gz -C /data

# Restore database
docker-compose exec -T db psql -U qgen qgen_impfrag < backup.sql
```

## Scaling and Load Balancing

### Horizontal Scaling
```yaml
version: '3.8'
services:
  backend:
    image: qgen-impfrag-backend:latest
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
```

### Load Balancer Configuration
```yaml
version: '3.8'
services:
  loadbalancer:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx-lb.conf:/etc/nginx/nginx.conf
    depends_on:
      - backend-1
      - backend-2
      - backend-3
```

## Security Hardening

### Container Security
```dockerfile
# Use non-root user
RUN addgroup -g 1001 -S appgroup && \
    adduser -u 1001 -S appuser -G appgroup

USER appuser
```

### Network Security
```yaml
version: '3.8'
services:
  app:
    networks:
      - internal
    
networks:
  internal:
    driver: bridge
    internal: true
```

### Secrets Management
```yaml
version: '3.8'
services:
  app:
    secrets:
      - flask_secret_key
      - database_password

secrets:
  flask_secret_key:
    file: ./secrets/flask_secret_key.txt
  database_password:
    file: ./secrets/db_password.txt
```

## Troubleshooting

### Common Issues

#### Port Conflicts
```bash
# Check port usage
sudo netstat -tulpn | grep :8000

# Use different ports
QGEN_IMPFRAG_PORT=8001 docker-compose up
```

#### Permission Issues
```bash
# Fix file permissions
sudo chown -R $USER:$USER data/
chmod -R 755 data/
```

#### Memory Issues
```bash
# Increase Docker memory limit
# Docker Desktop: Settings > Resources > Memory

# Monitor memory usage
docker stats --no-stream
```

#### Fragment Converter Access
```bash
# Ensure frag_convert is accessible
ls -la /data/XVUE/frag_convert/

# Check mount in container
docker-compose exec app ls -la /data/XVUE/frag_convert/
```

### Health Checks
```bash
# Backend health
curl http://localhost:8000/health

# Frontend availability
curl http://localhost:3111

# Container health
docker-compose exec app /bin/sh -c "curl -f http://localhost:80/health"
```

### Debug Mode
```bash
# Enable debug logging
QGEN_IMPFRAG_DEBUG=true docker-compose up

# Access container shell
docker-compose exec app /bin/sh
```

## Performance Optimization

### Resource Limits
```yaml
version: '3.8'
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 4G
        reservations:
          cpus: '1.0'
          memory: 2G
```

### Caching Strategy
```yaml
version: '3.8'
services:
  redis:
    image: redis:alpine
    volumes:
      - redis_data:/data
```

### Database Optimization
```yaml
version: '3.8'
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_SHARED_PRELOAD_LIBRARIES: pg_stat_statements
      POSTGRES_MAX_CONNECTIONS: 100
      POSTGRES_SHARED_BUFFERS: 256MB
```

## Migration and Updates

### Application Updates
```bash
# Pull latest changes
git pull origin main

# Rebuild containers
docker-compose build --no-cache

# Update with zero downtime
docker-compose up -d --no-deps --build app
```

### Database Migrations
```bash
# Run database migrations
docker-compose exec app python src/migrations/migrate.py

# Backup before migration
docker-compose exec db pg_dump -U qgen qgen_impfrag > pre_migration_backup.sql
```

## Production Checklist

- [ ] Environment variables configured
- [ ] SSL/TLS certificates installed
- [ ] Backup strategy implemented
- [ ] Monitoring and alerting configured
- [ ] Security hardening applied
- [ ] Performance optimization completed
- [ ] Health checks validated
- [ ] Documentation updated
- [ ] Team training completed
