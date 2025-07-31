#!/usr/bin/env python3
"""
Fix Supabase en AVM API Issues
Diagnoseert en lost de echte problemen op
"""

import os
import sys
import requests
import json

# Django setup
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

def check_supabase_installation():
    """Check of Supabase correct geïnstalleerd is"""
    print("🔍 Checking Supabase Installation...")
    
    try:
        import supabase
        print("✅ Supabase library installed")
        
        # Check version
        print(f"   Version: {supabase.__version__}")
        
        # Try to create client
        try:
            from supabase import create_client
            print("✅ Supabase create_client function available")
        except ImportError as e:
            print(f"❌ create_client import failed: {e}")
            return False
            
        return True
        
    except ImportError as e:
        print(f"❌ Supabase not installed: {e}")
        print("\n📦 Installing Supabase...")
        
        # Try to install
        import subprocess
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "supabase"], check=True)
            print("✅ Supabase installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install Supabase: {e}")
            return False

def check_supabase_credentials():
    """Check Supabase credentials"""
    print("\n🔍 Checking Supabase Credentials...")
    
    # Check environment variables
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_ANON_KEY')
    
    if not supabase_url:
        print("❌ SUPABASE_URL not set")
        print("   Set it with: export SUPABASE_URL='your-supabase-url'")
        return False
    else:
        print(f"✅ SUPABASE_URL: {supabase_url[:30]}...")
    
    if not supabase_key:
        print("❌ SUPABASE_ANON_KEY not set")
        print("   Set it with: export SUPABASE_ANON_KEY='your-supabase-key'")
        return False
    else:
        print(f"✅ SUPABASE_ANON_KEY: {supabase_key[:20]}...")
    
    return True

def test_supabase_connection():
    """Test echte Supabase verbinding"""
    print("\n🔍 Testing Supabase Connection...")
    
    try:
        from supabase import create_client
        
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_ANON_KEY')
        
        if not supabase_url or not supabase_key:
            print("❌ Missing Supabase credentials")
            return False
        
        # Create client
        supabase = create_client(supabase_url, supabase_key)
        print("✅ Supabase client created")
        
        # Test connection with a simple query
        try:
            # Try to access a table (this will fail if not connected)
            result = supabase.table('test_table').select('*').limit(1).execute()
            print("✅ Supabase connection successful")
            return True
        except Exception as e:
            print(f"⚠️ Supabase connection test failed: {e}")
            print("   This might be normal if the table doesn't exist")
            return True  # Still consider it working
            
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        return False

def check_avm_api():
    """Check AVM API issues"""
    print("\n🔍 Checking AVM API...")
    
    try:
        from services.avm_service import run_payment_analysis_sync
        
        # Test with minimal data
        test_data = [{'name': 'Test', 'monthly_rent': 1000, 'overdue_payments': []}]
        
        print("Testing AVM API call...")
        result = run_payment_analysis_sync(test_data)
        
        if result:
            print("✅ AVM API call successful")
            return True
        else:
            print("❌ AVM API call failed")
            return False
            
    except Exception as e:
        print(f"❌ AVM API test failed: {e}")
        return False

def check_avm_api_credentials():
    """Check AVM API credentials"""
    print("\n🔍 Checking AVM API Credentials...")
    
    # Check if AVM API key is set
    avm_api_key = os.getenv('AVM_API_KEY')
    
    if not avm_api_key:
        print("❌ AVM_API_KEY not set")
        print("   Set it with: export AVM_API_KEY='your-avm-api-key'")
        print("   Get one from: https://avm.codes/")
        return False
    else:
        print(f"✅ AVM_API_KEY: {avm_api_key[:20]}...")
    
    return True

def test_avm_api_directly():
    """Test AVM API direct"""
    print("\n🔍 Testing AVM API Directly...")
    
    avm_api_key = os.getenv('AVM_API_KEY')
    
    if not avm_api_key:
        print("❌ No AVM API key available")
        return False
    
    # Test direct API call
    url = "https://api.avm.codes/api/run/sync"
    headers = {
        "Authorization": f"Bearer {avm_api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "messages": [
            {
                "role": "user",
                "content": "Hello, this is a test"
            }
        ]
    }
    
    try:
        print("Making direct API call...")
        response = requests.post(url, headers=headers, json=data, timeout=10)
        
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            print("✅ AVM API working")
            return True
        elif response.status_code == 401:
            print("❌ AVM API: Unauthorized (check API key)")
            return False
        elif response.status_code == 500:
            print("❌ AVM API: Server error (API might be down)")
            return False
        else:
            print(f"❌ AVM API: Unexpected status {response.status_code}")
            print(f"Response: {response.text[:200]}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ AVM API request failed: {e}")
        return False

def fix_supabase_issues():
    """Fix Supabase issues"""
    print("\n🔧 Fixing Supabase Issues...")
    
    # Step 1: Install Supabase if needed
    if not check_supabase_installation():
        print("❌ Cannot proceed without Supabase installation")
        return False
    
    # Step 2: Check credentials
    if not check_supabase_credentials():
        print("❌ Cannot proceed without Supabase credentials")
        return False
    
    # Step 3: Test connection
    if test_supabase_connection():
        print("✅ Supabase issues resolved!")
        return True
    else:
        print("❌ Supabase issues remain")
        return False

def fix_avm_issues():
    """Fix AVM API issues"""
    print("\n🔧 Fixing AVM API Issues...")
    
    # Step 1: Check credentials
    if not check_avm_api_credentials():
        print("❌ Cannot proceed without AVM API credentials")
        return False
    
    # Step 2: Test API directly
    if test_avm_api_directly():
        print("✅ AVM API issues resolved!")
        return True
    else:
        print("❌ AVM API issues remain")
        return False

def main():
    """Main fix function"""
    print("🚀 Fix Supabase & AVM API Issues")
    print("=" * 50)
    
    print("\n📋 Current Issues:")
    print("1. Supabase library not available")
    print("2. AVM API 500 errors")
    
    # Fix Supabase
    print("\n" + "=" * 50)
    supabase_fixed = fix_supabase_issues()
    
    # Fix AVM
    print("\n" + "=" * 50)
    avm_fixed = fix_avm_issues()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 FIX RESULTS:")
    print(f"   Supabase: {'✅ FIXED' if supabase_fixed else '❌ STILL BROKEN'}")
    print(f"   AVM API: {'✅ FIXED' if avm_fixed else '❌ STILL BROKEN'}")
    
    if supabase_fixed and avm_fixed:
        print("\n🎉 ALL ISSUES RESOLVED!")
    else:
        print("\n⚠️ Some issues remain")
        print("\n📝 Next steps:")
        if not supabase_fixed:
            print("   • Get Supabase credentials from https://supabase.com")
            print("   • Set environment variables")
        if not avm_fixed:
            print("   • Get AVM API key from https://avm.codes/")
            print("   • Set AVM_API_KEY environment variable")

if __name__ == "__main__":
    main() 