#!/usr/bin/env python3
"""
XFRG Application Test Suite
==========================

Comprehensive test suite to verify:
1. Backend API functionality
2. Frontend serving
3. Fragment loading
4. Complete workflow
"""

import requests
import json
import time
import os
from pathlib import Path

def test_backend_health():
    """Test backend health endpoint"""
    try:
        response = requests.get("http://localhost:8111/health")
        if response.status_code == 200:
            print("✅ Backend health check passed")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend connection failed: {e}")
        return False

def test_api_endpoints():
    """Test key API endpoints"""
    endpoints = [
        "/api/fragments",
        "/api/ifc-files",
        "/",
    ]
    
    results = {}
    for endpoint in endpoints:
        try:
            url = f"http://localhost:8111{endpoint}"
            response = requests.get(url)
            results[endpoint] = {
                "status": response.status_code,
                "success": response.status_code == 200,
                "content_type": response.headers.get("content-type", "")
            }
            if response.status_code == 200:
                print(f"✅ {endpoint} - Status: {response.status_code}")
            else:
                print(f"❌ {endpoint} - Status: {response.status_code}")
        except Exception as e:
            print(f"❌ {endpoint} - Error: {e}")
            results[endpoint] = {"success": False, "error": str(e)}
    
    return results

def test_frontend_serving():
    """Test frontend server availability"""
    try:
        response = requests.get("http://localhost:3111")
        if response.status_code == 200:
            print("✅ Frontend server is serving content")
            print(f"   Content type: {response.headers.get('content-type', 'unknown')}")
            return True
        else:
            print(f"❌ Frontend server error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Frontend connection failed: {e}")
        return False

def test_fragment_files():
    """Check if fragment files are available"""
    fragment_dir = Path("./data/fragments")
    
    if not fragment_dir.exists():
        print("❌ Fragment directory not found")
        return False
    
    fragment_files = list(fragment_dir.glob("*.frag"))
    if fragment_files:
        print(f"✅ Found {len(fragment_files)} fragment files:")
        for frag in fragment_files:
            size_mb = frag.stat().st_size / (1024 * 1024)
            print(f"   📦 {frag.name} ({size_mb:.2f} MB)")
        return True
    else:
        print("❌ No fragment files found")
        return False

def test_fragment_serving():
    """Test if fragments are properly served via API"""
    try:
        # Get list of fragments
        response = requests.get("http://localhost:8111/api/fragments")
        if response.status_code != 200:
            print("❌ Could not get fragment list")
            return False
        
        fragments = response.json()
        if not fragments:
            print("❌ No fragments available via API")
            return False
        
        # Test downloading a fragment
        first_fragment = fragments[0]["filename"]
        download_url = f"http://localhost:8111/api/fragments/{first_fragment}"
        download_response = requests.get(download_url)
        
        if download_response.status_code == 200:
            print(f"✅ Successfully downloaded fragment: {first_fragment}")
            print(f"   Size: {len(download_response.content)} bytes")
            return True
        else:
            print(f"❌ Fragment download failed: {download_response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Fragment serving test failed: {e}")
        return False

def run_comprehensive_test():
    """Run all tests and provide summary"""
    print("🚀 XFRG Application Test Suite")
    print("=" * 50)
    
    tests = [
        ("Backend Health", test_backend_health),
        ("API Endpoints", test_api_endpoints),
        ("Frontend Serving", test_frontend_serving),
        ("Fragment Files", test_fragment_files),
        ("Fragment Serving", test_fragment_serving),
    ]
    
    results = {}
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing: {test_name}")
        print("-" * 30)
        try:
            result = test_func()
            results[test_name] = result
            if result:
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results[test_name] = False
    
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! XFRG application is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the application setup.")
    
    return results

if __name__ == "__main__":
    results = run_comprehensive_test()
