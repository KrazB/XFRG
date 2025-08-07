@echo off
echo 🔧 Installing Node.js dependencies for XFRG backend converter...
cd /d "D:\XFRG\backend"

echo 📁 Current directory: %CD%

echo 🔧 Installing @thatopen/components...
npm install @thatopen/components@^2.4.11

echo 🔧 Installing @thatopen/fragments...
npm install @thatopen/fragments@^3.0.7

echo 🔧 Installing web-ifc...
npm install web-ifc@^0.0.68

echo ✅ Dependencies installed!

echo 📁 Checking node_modules...
if exist "node_modules" (
    echo ✅ node_modules directory exists
    dir node_modules | findstr "@thatopen web-ifc"
) else (
    echo ❌ node_modules directory not found
)

echo 🧪 Testing converter script...
node ifc_converter.js --help

echo 🎉 Setup complete!
pause
