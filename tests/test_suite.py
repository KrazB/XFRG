#!/usr/bin/env python3
"""
QGEN_IMPFRAG Test Suite
======================

Comprehensive test suite for validating application functionality
"""

import os
import sys
import json
import requests
import subprocess
from pathlib import Path
from typing import Dict, Any

# Test configuration
TEST_CONFIG = {
    "backend_url": "http://localhost:8111",
    "frontend_url": "http://localhost:3111",
    "test_data_dir": Path(__file__).parent.parent / "data" / "test",
    "timeout": 30
}

class QgenTestSuite:
    """Main test suite for QGEN_IMPFRAG application"""
    
    def __init__(self):
        self.backend_url = TEST_CONFIG["backend_url"]
        self.frontend_url = TEST_CONFIG["frontend_url"]
        self.timeout = TEST_CONFIG["timeout"]
    
    def test_backend_health(self) -> Dict[str, Any]:
        """Test backend health endpoint"""
        try:
            response = requests.get(f"{self.backend_url}/health", timeout=self.timeout)
            result = {
                "test": "backend_health",
                "status": "PASS" if response.status_code == 200 else "FAIL",
                "response_code": response.status_code,
                "response_time_ms": response.elapsed.total_seconds() * 1000
            }
            
            if response.status_code == 200:
                data = response.json()
                result["service_name"] = data.get("service")
                result["backend_status"] = data.get("status")
            
            return result
            
        except Exception as e:
            return {
                "test": "backend_health",
                "status": "FAIL",
                "error": str(e)
            }
    
    def test_frontend_availability(self) -> Dict[str, Any]:
        """Test frontend availability"""
        try:
            response = requests.get(self.frontend_url, timeout=self.timeout)
            return {
                "test": "frontend_availability",
                "status": "PASS" if response.status_code == 200 else "FAIL",
                "response_code": response.status_code,
                "response_time_ms": response.elapsed.total_seconds() * 1000
            }
        except Exception as e:
            return {
                "test": "frontend_availability",
                "status": "FAIL",
                "error": str(e)
            }
    
    def test_api_endpoints(self) -> Dict[str, Any]:
        """Test critical API endpoints"""
        endpoints = [
            "/api/fragments",
            "/api/ifc",
            "/api/status"
        ]
        
        results = []
        
        for endpoint in endpoints:
            try:
                response = requests.get(f"{self.backend_url}{endpoint}", timeout=self.timeout)
                results.append({
                    "endpoint": endpoint,
                    "status": "PASS" if response.status_code == 200 else "FAIL",
                    "response_code": response.status_code,
                    "response_time_ms": response.elapsed.total_seconds() * 1000
                })
            except Exception as e:
                results.append({
                    "endpoint": endpoint,
                    "status": "FAIL",
                    "error": str(e)
                })
        
        return {
            "test": "api_endpoints",
            "results": results,
            "overall_status": "PASS" if all(r.get("status") == "PASS" for r in results) else "FAIL"
        }
    
    def test_docker_services(self) -> Dict[str, Any]:
        """Test Docker service status"""
        try:
            # Check if docker-compose services are running
            result = subprocess.run(
                ["docker-compose", "ps", "--format", "json"],
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent.parent
            )
            
            if result.returncode == 0:
                services = []
                for line in result.stdout.strip().split('\n'):
                    if line.strip():
                        try:
                            service = json.loads(line)
                            services.append({
                                "name": service.get("Name"),
                                "state": service.get("State"),
                                "status": service.get("Status")
                            })
                        except json.JSONDecodeError:
                            continue
                
                return {
                    "test": "docker_services",
                    "status": "PASS" if all(s.get("state") == "running" for s in services) else "FAIL",
                    "services": services
                }
            else:
                return {
                    "test": "docker_services",
                    "status": "FAIL",
                    "error": result.stderr
                }
                
        except Exception as e:
            return {
                "test": "docker_services",
                "status": "FAIL",
                "error": str(e)
            }
    
    def test_file_system_permissions(self) -> Dict[str, Any]:
        """Test file system permissions and directory structure"""
        required_dirs = [
            "data/ifc",
            "data/fragments", 
            "data/reports",
            "backend/logs"
        ]
        
        base_path = Path(__file__).parent.parent
        results = []
        
        for dir_path in required_dirs:
            full_path = base_path / dir_path
            try:
                # Check if directory exists
                exists = full_path.exists()
                
                # Check if readable and writable
                readable = os.access(full_path, os.R_OK) if exists else False
                writable = os.access(full_path, os.W_OK) if exists else False
                
                results.append({
                    "directory": dir_path,
                    "exists": exists,
                    "readable": readable,
                    "writable": writable,
                    "status": "PASS" if exists and readable and writable else "FAIL"
                })
                
            except Exception as e:
                results.append({
                    "directory": dir_path,
                    "status": "FAIL",
                    "error": str(e)
                })
        
        return {
            "test": "file_system_permissions",
            "results": results,
            "overall_status": "PASS" if all(r.get("status") == "PASS" for r in results) else "FAIL"
        }
    
    def run_all_tests(self) -> Dict[str, Any]:
        """Run all tests and return comprehensive results"""
        tests = [
            self.test_backend_health,
            self.test_frontend_availability,
            self.test_api_endpoints,
            self.test_docker_services,
            self.test_file_system_permissions
        ]
        
        results = []
        for test in tests:
            try:
                result = test()
                results.append(result)
            except Exception as e:
                results.append({
                    "test": test.__name__,
                    "status": "FAIL",
                    "error": str(e)
                })
        
        # Calculate overall status
        passed_tests = sum(1 for r in results if r.get("status") == "PASS" or r.get("overall_status") == "PASS")
        total_tests = len(results)
        
        return {
            "test_suite": "QGEN_IMPFRAG",
            "timestamp": str(subprocess.run(["date", "-Iseconds"], capture_output=True, text=True).stdout.strip()),
            "summary": {
                "total_tests": total_tests,
                "passed": passed_tests,
                "failed": total_tests - passed_tests,
                "success_rate": f"{(passed_tests / total_tests * 100):.1f}%"
            },
            "overall_status": "PASS" if passed_tests == total_tests else "FAIL",
            "detailed_results": results
        }

def main():
    """Main test runner"""
    print("🧪 Running QGEN_IMPFRAG Test Suite...")
    print("=" * 50)
    
    suite = QgenTestSuite()
    results = suite.run_all_tests()
    
    # Print summary
    print(f"\n📊 Test Results Summary:")
    print(f"Total Tests: {results['summary']['total_tests']}")
    print(f"Passed: {results['summary']['passed']}")
    print(f"Failed: {results['summary']['failed']}")
    print(f"Success Rate: {results['summary']['success_rate']}")
    print(f"Overall Status: {'✅ PASS' if results['overall_status'] == 'PASS' else '❌ FAIL'}")
    
    # Print detailed results
    print(f"\n📋 Detailed Results:")
    for result in results['detailed_results']:
        test_name = result.get('test', 'unknown')
        status = result.get('status', result.get('overall_status', 'UNKNOWN'))
        status_icon = "✅" if status == "PASS" else "❌"
        print(f"{status_icon} {test_name}: {status}")
        
        if 'error' in result:
            print(f"   Error: {result['error']}")
    
    # Save results to file
    output_file = Path(__file__).parent.parent / "test_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📄 Detailed results saved to: {output_file}")
    
    # Exit with appropriate code
    sys.exit(0 if results['overall_status'] == 'PASS' else 1)

if __name__ == "__main__":
    main()
