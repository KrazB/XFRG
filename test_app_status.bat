@echo off
echo ========================================
echo XFRG Application Status Check
echo ========================================

echo.
echo 1. Checking Backend Server (Port 8111)
echo ----------------------------------------
powershell -Command "try { $response = Invoke-WebRequest -Uri 'http://localhost:8111/health' -TimeoutSec 5; Write-Host 'Backend Status: SUCCESS' -ForegroundColor Green; Write-Host 'Response:' $response.Content } catch { Write-Host 'Backend Status: FAILED' -ForegroundColor Red; Write-Host 'Error:' $_.Exception.Message }"

echo.
echo 2. Checking Frontend Server (Port 3111)
echo ----------------------------------------
powershell -Command "try { $response = Invoke-WebRequest -Uri 'http://localhost:3111' -TimeoutSec 5; Write-Host 'Frontend Status: SUCCESS' -ForegroundColor Green; Write-Host 'Content Type:' $response.Headers.'Content-Type' } catch { Write-Host 'Frontend Status: FAILED' -ForegroundColor Red; Write-Host 'Error:' $_.Exception.Message }"

echo.
echo 3. Checking Fragment Files
echo ----------------------------------------
if exist "data\fragments\*.frag" (
    echo Fragment files found:
    dir /b "data\fragments\*.frag"
    echo SUCCESS: Fragment files are available
) else (
    echo WARNING: No fragment files found
)

echo.
echo 4. Testing API Endpoints
echo ----------------------------------------
powershell -Command "try { $response = Invoke-WebRequest -Uri 'http://localhost:8111/api/fragments' -TimeoutSec 5; Write-Host 'Fragments API: SUCCESS' -ForegroundColor Green } catch { Write-Host 'Fragments API: FAILED' -ForegroundColor Red }"

powershell -Command "try { $response = Invoke-WebRequest -Uri 'http://localhost:8111/api/ifc-files' -TimeoutSec 5; Write-Host 'IFC Files API: SUCCESS' -ForegroundColor Green } catch { Write-Host 'IFC Files API: FAILED' -ForegroundColor Red }"

echo.
echo ========================================
echo Test Complete
echo ========================================
echo.
echo Access URLs:
echo Backend:  http://localhost:8111
echo Frontend: http://localhost:3111
echo.
