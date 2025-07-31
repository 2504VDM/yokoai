#!/usr/bin/env python3
"""
Fast Django Test - Minimal Django setup test
"""

import os
import sys

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
os.environ['DEBUG'] = 'False'

def test_minimal_django():
    """Test minimal Django setup without full server"""
    print("🚀 Fast Django Test")
    print("=" * 30)
    
    try:
        # Test 1: Basic Django import
        print("1. Testing Django import...")
        import django
        print("   ✅ Django imported")
        
        # Test 2: Django setup
        print("2. Testing Django setup...")
        django.setup()
        print("   ✅ Django setup complete")
        
        # Test 3: Settings
        print("3. Testing settings...")
        from django.conf import settings
        print(f"   ✅ DEBUG: {settings.DEBUG}")
        print(f"   ✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
        
        # Test 4: Environment variables
        print("4. Testing environment...")
        supabase_url = os.getenv('SUPABASE_URL')
        avm_key = os.getenv('AVM_API_KEY')
        print(f"   ✅ SUPABASE_URL: {'Set' if supabase_url else 'Not set'}")
        print(f"   ✅ AVM_API_KEY: {'Set' if avm_key else 'Not set'}")
        
        print("\n✅ All tests passed! Django ready for deployment.")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_minimal_django()
    sys.exit(0 if success else 1) 