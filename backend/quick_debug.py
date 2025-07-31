#!/usr/bin/env python3
"""
Quick Debug - Identificeert specifieke problemen
"""

import os
import sys

def check_supabase_import():
    """Check waarom Supabase import lang duurt"""
    print("🔍 Checking Supabase import issue...")
    
    try:
        print("Trying to import supabase...")
        import supabase
        print("✅ Supabase imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Supabase not installed: {e}")
        return False
    except Exception as e:
        print(f"❌ Supabase import error: {e}")
        return False

def check_django_setup():
    """Check Django setup issues"""
    print("\n🔍 Checking Django setup...")
    
    try:
        import django
        print("✅ Django imported")
        
        # Check if we're in the right directory
        if not os.path.exists('config/settings.py'):
            print("❌ config/settings.py not found")
            print(f"Current directory: {os.getcwd()}")
            return False
        
        print("✅ config/settings.py found")
        
        # Try Django setup
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
        
        print("Setting up Django...")
        django.setup()
        print("✅ Django setup completed")
        return True
        
    except Exception as e:
        print(f"❌ Django setup failed: {e}")
        return False

def check_models():
    """Check database models"""
    print("\n🔍 Checking database models...")
    
    try:
        from agent.models import Client, Property, Tenant, Payment
        print("✅ Models imported")
        
        # Check counts
        client_count = Client.objects.count()
        print(f"✅ Clients: {client_count}")
        
        return True
    except Exception as e:
        print(f"❌ Models failed: {e}")
        return False

def check_services():
    """Check services"""
    print("\n🔍 Checking services...")
    
    try:
        from services.supabase_dynamic import SupabaseDynamicDB
        print("✅ SupabaseDynamicDB imported")
        
        db_service = SupabaseDynamicDB()
        print(f"✅ Service initialized, connected: {db_service.connected}")
        
        return True
    except Exception as e:
        print(f"❌ Services failed: {e}")
        return False

def main():
    print("🚀 Quick Debug - VDM Nexus")
    print("=" * 40)
    
    # Check 1: Supabase import
    supabase_ok = check_supabase_import()
    
    # Check 2: Django setup
    django_ok = check_django_setup()
    
    # Check 3: Models (only if Django works)
    models_ok = False
    if django_ok:
        models_ok = check_models()
    
    # Check 4: Services (only if Django works)
    services_ok = False
    if django_ok:
        services_ok = check_services()
    
    # Summary
    print("\n" + "=" * 40)
    print("📊 QUICK DEBUG RESULTS:")
    print(f"   Supabase Import: {'✅' if supabase_ok else '❌'}")
    print(f"   Django Setup: {'✅' if django_ok else '❌'}")
    print(f"   Database Models: {'✅' if models_ok else '❌'}")
    print(f"   Services: {'✅' if services_ok else '❌'}")
    
    if all([supabase_ok, django_ok, models_ok, services_ok]):
        print("\n🎉 ALL SYSTEMS WORKING!")
    else:
        print("\n⚠️ Some systems need attention")

if __name__ == "__main__":
    main() 