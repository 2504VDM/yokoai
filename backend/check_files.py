#!/usr/bin/env python3
"""
Ultra-quick check voor Stap 1 & 2 - File verification only
"""

import os

def check_file_exists(path, description):
    """Check if file exists"""
    if os.path.exists(path):
        print(f"✅ {description}: {path}")
        return True
    else:
        print(f"❌ {description}: {path} - MISSING")
        return False

def check_file_content(path, required_strings, description):
    """Check if file contains required strings"""
    if not os.path.exists(path):
        print(f"❌ {description}: File not found")
        return False
    
    try:
        with open(path, 'r') as f:
            content = f.read()
        
        missing = []
        for string in required_strings:
            if string not in content:
                missing.append(string)
        
        if missing:
            print(f"❌ {description}: Missing {missing}")
            return False
        else:
            print(f"✅ {description}: All required code found")
            return True
    except Exception as e:
        print(f"❌ {description}: Error reading file - {e}")
        return False

def main():
    print("🚀 Quick File Check - VDM Nexus CSV Upload")
    print("=" * 50)
    
    results = []
    
    # Check Stap 1: SupabaseDynamicDB
    print("\n📁 Stap 1: SupabaseDynamicDB")
    results.append(check_file_exists(
        'services/supabase_dynamic.py',
        'SupabaseDynamicDB service file'
    ))
    
    if results[-1]:  # If file exists, check content
        results.append(check_file_content(
            'services/supabase_dynamic.py',
            ['class SupabaseDynamicDB', 'analyze_csv_structure', 'create_dynamic_table'],
            'SupabaseDynamicDB class methods'
        ))
    
    # Check Stap 2: API Endpoints
    print("\n📁 Stap 2: API Endpoints")
    results.append(check_file_exists(
        'api/views.py',
        'API views file'
    ))
    
    if results[-1]:  # If file exists, check content
        results.append(check_file_content(
            'api/views.py',
            ['upload_csv_data', 'get_uploaded_tables', 'get_table_data', 'delete_uploaded_table'],
            'CSV upload API endpoints'
        ))
    
    results.append(check_file_exists(
        'api/urls.py',
        'API URLs file'
    ))
    
    if results[-1]:  # If file exists, check content
        results.append(check_file_content(
            'api/urls.py',
            ['upload-csv', 'uploaded-tables', 'table-data', 'delete-table'],
            'CSV upload URL patterns'
        ))
    
    # Check Stap 3: Frontend
    print("\n📁 Stap 3: Frontend Upload")
    results.append(check_file_exists(
        '../frontend/src/app/upload/page.tsx',
        'Frontend upload page'
    ))
    
    if results[-1]:  # If file exists, check content
        results.append(check_file_content(
            '../frontend/src/app/upload/page.tsx',
            ['useDropzone', 'Upload', 'FileText', 'handleUpload'],
            'Frontend upload features'
        ))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 CHECK RESULTS:")
    
    passed = sum(results)
    total = len(results)
    
    print(f"✅ Passed: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 ALL FILES AND CODE IN PLACE!")
        print("✅ Stap 1: SupabaseDynamicDB - READY")
        print("✅ Stap 2: API Endpoints - READY") 
        print("✅ Stap 3: Frontend Upload - READY")
        print("\n🚀 Ready for Dag 3: Dashboard Widget Polish")
    else:
        print(f"\n⚠️ {total - passed} checks failed")
        print("Check the missing items above")

if __name__ == "__main__":
    main() 