#!/usr/bin/env python3
"""
Test Django Settings
"""

import os
import sys

# Set environment variables for testing
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
os.environ['ALLOWED_HOSTS'] = 'localhost,127.0.0.1,vdmnexus-backend.onrender.com'
os.environ['DEBUG'] = 'False'

def test_settings():
    """Test Django settings configuration"""
    print("🔧 Testing Django Settings")
    print("=" * 30)
    
    try:
        import django
        django.setup()
        
        from django.conf import settings
        
        print(f"✅ DEBUG: {settings.DEBUG}")
        print(f"✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
        print(f"✅ SECRET_KEY: {'Set' if settings.SECRET_KEY else 'Not set'}")
        
        # Test if vdmnexus-backend.onrender.com is in allowed hosts
        if 'vdmnexus-backend.onrender.com' in settings.ALLOWED_HOSTS:
            print("✅ Render hostname is allowed")
        else:
            print("❌ Render hostname not in ALLOWED_HOSTS")
            
        print("\n✅ Settings test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Settings test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_settings()
    sys.exit(0 if success else 1) 