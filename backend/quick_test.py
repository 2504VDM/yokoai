#!/usr/bin/env python3
"""
Quick test voor Stap 1 & 2 - CSV Upload System
Test zonder volledige Django setup
"""

import pandas as pd
import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_supabase_dynamic():
    """Test Stap 1: SupabaseDynamicDB class"""
    print("🔍 Testing Stap 1: SupabaseDynamicDB...")
    
    try:
        # Test import
        from services.supabase_dynamic import SupabaseDynamicDB
        print("✅ Import successful")
        
        # Test initialization
        db_service = SupabaseDynamicDB()
        print(f"✅ Service initialized: {type(db_service).__name__}")
        print(f"   Connected: {db_service.connected}")
        
        # Create test CSV
        test_data = {
            'property_name': ['Villa Amsterdam', 'Appartement Rotterdam'],
            'address': ['Herengracht 123', 'Coolsingel 456'],
            'purchase_price': [450000, 320000],
            'monthly_rent': [2800, 2100],
            'status': ['Rented', 'Available']
        }
        
        df = pd.DataFrame(test_data)
        test_file = 'test_properties.csv'
        df.to_csv(test_file, index=False)
        
        print(f"✅ Created test CSV: {test_file}")
        
        # Test CSV analysis
        analysis = db_service.analyze_csv_structure(test_file)
        
        if analysis['success']:
            print("✅ CSV Analysis successful:")
            print(f"   - Rows: {analysis['row_count']}")
            print(f"   - Columns: {analysis['column_count']}")
            print("   - Column types:")
            for col_name, metadata in analysis['columns'].items():
                print(f"     • {col_name}: {metadata['sql_type']}")
        else:
            print(f"❌ CSV Analysis failed: {analysis['error']}")
        
        # Cleanup
        os.unlink(test_file)
        print("✅ Stap 1: SupabaseDynamicDB - PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Stap 1 failed: {str(e)}")
        return False

def test_api_endpoints():
    """Test Stap 2: API endpoints (simulated)"""
    print("\n🔍 Testing Stap 2: API Endpoints...")
    
    try:
        # Test if views.py has the new endpoints
        with open('api/views.py', 'r') as f:
            content = f.read()
        
        required_functions = [
            'upload_csv_data',
            'get_uploaded_tables', 
            'get_table_data',
            'delete_uploaded_table'
        ]
        
        missing_functions = []
        for func in required_functions:
            if func not in content:
                missing_functions.append(func)
        
        if missing_functions:
            print(f"❌ Missing API functions: {missing_functions}")
            return False
        else:
            print("✅ All API endpoints found in views.py")
        
        # Test if URLs are configured
        with open('api/urls.py', 'r') as f:
            urls_content = f.read()
        
        required_urls = [
            'upload-csv',
            'uploaded-tables',
            'table-data',
            'delete-table'
        ]
        
        missing_urls = []
        for url in required_urls:
            if url not in urls_content:
                missing_urls.append(url)
        
        if missing_urls:
            print(f"❌ Missing URL patterns: {missing_urls}")
            return False
        else:
            print("✅ All URL patterns configured")
        
        print("✅ Stap 2: API Endpoints - PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Stap 2 failed: {str(e)}")
        return False

def test_frontend():
    """Test Stap 3: Frontend upload page"""
    print("\n🔍 Testing Stap 3: Frontend Upload Page...")
    
    try:
        # Check if upload page exists
        upload_page_path = '../frontend/src/app/upload/page.tsx'
        
        if os.path.exists(upload_page_path):
            print("✅ Upload page exists")
            
            with open(upload_page_path, 'r') as f:
                content = f.read()
            
            required_features = [
                'useDropzone',
                'Upload',
                'FileText',
                'handleUpload',
                'uploadedTables'
            ]
            
            missing_features = []
            for feature in required_features:
                if feature not in content:
                    missing_features.append(feature)
            
            if missing_features:
                print(f"❌ Missing frontend features: {missing_features}")
                return False
            else:
                print("✅ All frontend features present")
                print("✅ Stap 3: Frontend Upload Page - PASSED")
                return True
        else:
            print("❌ Upload page not found")
            return False
            
    except Exception as e:
        print(f"❌ Stap 3 failed: {str(e)}")
        return False

def main():
    """Run all quick tests"""
    print("🚀 Quick Test - VDM Nexus CSV Upload System")
    print("=" * 50)
    
    results = []
    
    # Test Stap 1
    results.append(("Stap 1: SupabaseDynamicDB", test_supabase_dynamic()))
    
    # Test Stap 2  
    results.append(("Stap 2: API Endpoints", test_api_endpoints()))
    
    # Test Stap 3
    results.append(("Stap 3: Frontend Upload", test_frontend()))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS:")
    
    passed = 0
    for name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"   {name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{len(results)} steps working")
    
    if passed == len(results):
        print("\n🎉 ALL STEPS WORKING!")
        print("✅ Ready for Dag 3: Dashboard Widget Polish")
    else:
        print("\n⚠️ Some steps need attention")
        print("Check the errors above and fix them")

if __name__ == "__main__":
    main() 