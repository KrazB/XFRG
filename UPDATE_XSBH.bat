@echo off
:: XSBH Update Script - Run this in your XSBH repository folder
:: Syncs all changes from XFRG automation pipeline
:: Generated: August 8, 2025

echo.
echo ===============================================
echo 🔄 XSBH Repository Update from XFRG Pipeline
echo ===============================================
echo.

:: Step 1: Sync Frontend
echo 📁 Syncing frontend source code...
robocopy "D:\XFRG\frontend\src" "frontend\src" /E /XO
copy "D:\XFRG\frontend\package.json" "frontend\package.json" /Y
robocopy "D:\XFRG\frontend\public" "frontend\public" /E /XO

:: Step 2: Sync Backend  
echo ⚙️  Syncing backend source code...
robocopy "D:\XFRG\backend" "backend" /E /XO

:: Step 3: Update Docker (Simple XSBH Configuration)
echo 🐳 Updating Docker configuration for XSBH...
copy "D:\XFRG\Dockerfile.prod" "Dockerfile" /Y
robocopy "D:\XFRG\docker" "docker" /E /XO

:: Create XSBH-compatible docker-compose.yml
echo # XSBH - Simple BIM Fragment Viewer > docker-compose.yml
echo version: '3.8' >> docker-compose.yml
echo. >> docker-compose.yml
echo services: >> docker-compose.yml
echo   xsbh-viewer: >> docker-compose.yml
echo     build: . >> docker-compose.yml
echo     container_name: xsbh-bim-viewer >> docker-compose.yml
echo     ports: >> docker-compose.yml
echo       - "8080:80" >> docker-compose.yml
echo     volumes: >> docker-compose.yml
echo       - ./data:/app/data >> docker-compose.yml
echo       - ./user-fragments:/app/data/fragments >> docker-compose.yml
echo     environment: >> docker-compose.yml
echo       - NODE_ENV=production >> docker-compose.yml
echo       - FRAGMENTS_DATA_DIR=/app/data >> docker-compose.yml
echo     restart: unless-stopped >> docker-compose.yml
echo     healthcheck: >> docker-compose.yml
echo       test: ["CMD", "curl", "-f", "http://localhost:80/health"] >> docker-compose.yml
echo       interval: 30s >> docker-compose.yml
echo       timeout: 10s >> docker-compose.yml
echo       retries: 3 >> docker-compose.yml
echo       start_period: 60s >> docker-compose.yml
echo. >> docker-compose.yml
echo volumes: >> docker-compose.yml
echo   user-fragments: >> docker-compose.yml
echo     driver: local >> docker-compose.yml

:: Step 4: Sync Scripts
echo 🛠️  Syncing automation scripts...
robocopy "D:\XFRG\scripts" "scripts" /E /XO

:: Step 5: Clean Development Files
echo 🧹 Cleaning development-only files...
del "frontend\debug_api.js" >nul 2>nul
del "frontend\test_itemsfinder.ts" >nul 2>nul
del "frontend\check_exports.js" >nul 2>nul
del "frontend\corrected_function.ts" >nul 2>nul
del "frontend\fixed_function.ts" >nul 2>nul
if exist "logs" rmdir /s /q "logs" >nul 2>nul
if exist "temp" rmdir /s /q "temp" >nul 2>nul

:: Step 6: Test Build
echo 🔨 Testing frontend build...
cd frontend
call npm install
call npm run build
cd ..

echo.
echo ✅ Sync completed! Ready for git commit.
echo.
echo 📝 Suggested commit message:
echo "🚀 Complete Automation Pipeline + Production Infrastructure"
echo.
echo Run: git add . && git commit -m "..." && git push
pause
