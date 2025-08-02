# Multi-stage Dockerfile for QGEN_IMPFRAG Application
# Stage 1: Backend preparation and IFC processing
# Stage 2: Frontend build and serving
# Stage 3: Production runtime with both services

# ================================
# Stage 1: Backend Build
# ================================
FROM python:3.11-alpine AS backend-builder

# Install system dependencies for Python and Node.js
RUN apk add --no-cache \
    nodejs \
    npm \
    build-base \
    python3-dev \
    linux-headers

# Set working directory for backend
WORKDIR /app/backend

# Copy backend package files
COPY backend/package.json backend/package-lock.json* ./
COPY backend/requirements.txt ./

# Install Node.js dependencies for ThatOpen Components
RUN npm ci --only=production

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY backend/src/ ./src/

# ================================
# Stage 2: Frontend Build
# ================================
FROM node:18-alpine AS frontend-builder

# Set working directory for frontend
WORKDIR /app/frontend

# Copy frontend package files
COPY frontend/package.json frontend/package-lock.json* ./

# Install dependencies
RUN npm ci

# Copy frontend source code
COPY frontend/ .

# Build the frontend application
RUN npm run build

# ================================
# Stage 3: Production Runtime
# ================================
FROM python:3.11-alpine AS production

# Install runtime dependencies
RUN apk add --no-cache \
    nodejs \
    npm \
    nginx \
    supervisor

# Create application directories
WORKDIR /app
RUN mkdir -p /app/backend /app/frontend /app/data/ifc /app/data/fragments /app/logs

# Copy backend from builder stage
COPY --from=backend-builder /app/backend /app/backend

# Copy frontend build from builder stage
COPY --from=frontend-builder /app/frontend/dist /app/frontend/dist

# Copy configuration files
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Create nginx directories and set permissions
RUN mkdir -p /var/log/nginx /var/lib/nginx/tmp \
    && chown -R nginx:nginx /var/log/nginx /var/lib/nginx \
    && chmod -R 755 /app

# Copy startup scripts
COPY scripts/docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Expose ports
EXPOSE 80 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:80/health || exit 1

# Set environment variables
ENV PYTHONPATH=/app/backend
ENV NODE_ENV=production
ENV FRAGMENTS_DATA_DIR=/app/data

# Volume for persistent data
VOLUME ["/app/data"]

# Start supervisor to manage multiple services
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
