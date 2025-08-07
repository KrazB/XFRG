@echo off
REM XFRG Complete Application Test Script
REM ====================================
REM Tests the complete XFRG IFC processing and 3D viewer application

setlocal enabledelayedexpansion

echo.
echo ========================================
echo    XFRG Application Complete Test
echo ========================================
echo.

REM Set color codes for better output
set "GREEN=[32m"
set "RED=[31m"
set "YELLOW=[33m"
set "RESET=[0m"

echo %YELLOW%Phase 1: Environment Verification%RESET%
echo ----------------------------------------

REM Check prerequisites
echo Checking Python...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo %GREEN%✅ Python available%RESET%
    python --version
) else (
    echo %RED%❌ Python not found%RESET%
    exit /b 1
)

echo.
echo Checking Node.js...
node --version >nul 2>&1
if %errorlevel% equ 0 (
    echo %GREEN%✅ Node.js available%RESET%
    node --version
) else (
    echo %RED%❌ Node.js not found%RESET%
    exit /b 1
)

echo.
echo Checking Docker...
docker --version >nul 2>&1
if %errorlevel% equ 0 (
    echo %GREEN%✅ Docker available%RESET%
    docker --version
) else (
    echo %YELLOW%⚠️  Docker not available - containerized deployment will not work%RESET%
)

echo.
echo %YELLOW%Phase 2: Data Verification%RESET%
echo ----------------------------------------

echo Checking IFC files...
if exist "data\ifc\*.ifc" (
    echo %GREEN%✅ IFC files found:%RESET%
    for %%f in (data\ifc\*.ifc) do (
        set /a size=%%~zf/1048576
        echo    📄 %%~nxf (!size! MB)
    )
) else (
    echo %RED%❌ No IFC files found in data\ifc\%RESET%
)

echo.
echo Checking Fragment files...
if exist "data\fragments\*.frag" (
    echo %GREEN%✅ Fragment files found:%RESET%
    for %%f in (data\fragments\*.frag) do (
        set /a size=%%~zf/1048576
        echo    📦 %%~nxf (!size! MB)
    )
) else (
    echo %YELLOW%⚠️  No fragment files found in data\fragments\%RESET%
)

echo.
echo %YELLOW%Phase 3: Dependencies Check%RESET%
echo ----------------------------------------

echo Installing/verifying frontend dependencies...
cd frontend
npm install --silent >nul 2>&1
if %errorlevel% equ 0 (
    echo %GREEN%✅ Frontend dependencies ready%RESET%
) else (
    echo %RED%❌ Frontend dependency installation failed%RESET%
)
cd ..

echo.
echo Installing/verifying backend dependencies...
cd backend
pip install -r requirements.txt --quiet >nul 2>&1
if %errorlevel% equ 0 (
    echo %GREEN%✅ Backend dependencies ready%RESET%
) else (
    echo %RED%❌ Backend dependency installation failed%RESET%
)
cd ..

echo.
echo %YELLOW%Phase 4: Application Launch%RESET%
echo ----------------------------------------

echo Starting backend server...
start /B cmd /c "cd backend && python app.py >nul 2>&1"

REM Wait for backend to start
timeout /t 3 /nobreak >nul

echo Testing backend health...
powershell -Command "try { Invoke-RestMethod -Uri 'http://localhost:8111/health' -Method Get -TimeoutSec 5 | Out-Null; Write-Host '✅ Backend server responding' -ForegroundColor Green } catch { Write-Host '❌ Backend server not responding' -ForegroundColor Red }"

echo.
echo Starting frontend server...
start /B cmd /c "cd frontend && npm run dev >nul 2>&1"

REM Wait for frontend to start
timeout /t 5 /nobreak >nul

echo Testing frontend server...
powershell -Command "try { Invoke-WebRequest -Uri 'http://localhost:3111' -Method Get -TimeoutSec 5 | Out-Null; Write-Host '✅ Frontend server responding' -ForegroundColor Green } catch { Write-Host '❌ Frontend server not responding' -ForegroundColor Red }"

echo.
echo %YELLOW%Phase 5: API Endpoint Testing%RESET%
echo ----------------------------------------

echo Testing /health endpoint...
powershell -Command "try { $r = Invoke-RestMethod -Uri 'http://localhost:8111/health' -TimeoutSec 5; Write-Host '✅ Health endpoint OK' -ForegroundColor Green } catch { Write-Host '❌ Health endpoint failed' -ForegroundColor Red }"

echo.
echo Testing /api/fragments endpoint...
powershell -Command "try { $r = Invoke-RestMethod -Uri 'http://localhost:8111/api/fragments' -TimeoutSec 5; Write-Host '✅ Fragments API OK' -ForegroundColor Green } catch { Write-Host '❌ Fragments API failed' -ForegroundColor Red }"

echo.
echo Testing /api/ifc-files endpoint...
powershell -Command "try { $r = Invoke-RestMethod -Uri 'http://localhost:8111/api/ifc-files' -TimeoutSec 5; Write-Host '✅ IFC Files API OK' -ForegroundColor Green } catch { Write-Host '❌ IFC Files API failed' -ForegroundColor Red }"

echo.
echo ========================================
echo           TEST COMPLETE
echo ========================================
echo.
echo %GREEN%🚀 XFRG Application is now running!%RESET%
echo.
echo Access the application:
echo   🌐 Frontend: http://localhost:3111
echo   🔧 Backend:  http://localhost:8111
echo   📊 Health:   http://localhost:8111/health
echo.
echo %YELLOW%Next Steps:%RESET%
echo 1. Open http://localhost:3111 in your browser
echo 2. Load fragment files from the interface
echo 3. Navigate the 3D models with mouse controls
echo 4. Click elements to view properties
echo.
echo %YELLOW%To stop the application:%RESET%
echo Press Ctrl+C in both terminal windows
echo.
pause
