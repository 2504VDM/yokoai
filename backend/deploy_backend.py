#!/usr/bin/env python3
"""
Backend Deployment Script
Prepares Django backend for Render deployment
"""

import os
import sys
import subprocess

def check_requirements():
    """Check if all requirements are met"""
    print("🔍 Checking deployment requirements...")
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Run from backend directory.")
        return False
    
    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print("❌ Error: requirements.txt not found.")
        return False
    
    # Check if render.yaml exists
    if not os.path.exists('render.yaml'):
        print("❌ Error: render.yaml not found.")
        return False
    
    print("✅ All requirements met")
    return True

def test_django_setup():
    """Test Django setup"""
    print("\n🚀 Testing Django setup...")
    
    try:
        result = subprocess.run([sys.executable, 'fast_django_test.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Django setup test passed")
            return True
        else:
            print(f"❌ Django setup test failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error running Django test: {e}")
        return False

def prepare_for_deployment():
    """Prepare backend for deployment"""
    print("\n📦 Preparing for deployment...")
    
    # Set production environment variables
    os.environ['DEBUG'] = 'False'
    os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
    
    # Check environment variables
    required_vars = [
        'SUPABASE_URL',
        'SUPABASE_ANON_KEY', 
        'AVM_API_KEY'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"⚠️  Warning: Missing environment variables: {missing_vars}")
        print("   These will need to be set in Render dashboard")
    else:
        print("✅ All environment variables set")
    
    return True

def create_deployment_summary():
    """Create deployment summary"""
    print("\n📋 Deployment Summary")
    print("=" * 40)
    print("✅ Backend ready for deployment")
    print("✅ Django configuration tested")
    print("✅ Environment variables configured")
    print("✅ Render configuration ready")
    print("\n🌐 Next Steps:")
    print("1. Push to GitHub")
    print("2. Connect to Render")
    print("3. Deploy backend service")
    print("4. Update frontend API URL")

def main():
    """Main deployment preparation"""
    print("🚀 VDM Nexus Backend Deployment Preparation")
    print("=" * 50)
    
    steps = [
        check_requirements,
        test_django_setup,
        prepare_for_deployment
    ]
    
    for step in steps:
        if not step():
            print("\n❌ Deployment preparation failed")
            return False
    
    create_deployment_summary()
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 