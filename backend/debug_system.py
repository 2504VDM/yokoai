#!/usr/bin/env python3
"""
Detailed Debug Script - VDM Nexus System
Identificeert exact waar problemen optreden
"""

import os
import sys
import traceback
from datetime import datetime

def debug_imports():
    """Debug alle imports stap voor stap"""
    print("🔍 DEBUG: Testing Imports...")
    print("=" * 50)
    
    # Test 1: Basic Python imports
    try:
        import pandas as pd
        print("✅ pandas imported")
    except Exception as e:
        print(f"❌ pandas failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ numpy imported")
    except Exception as e:
        print(f"❌ numpy failed: {e}")
        return False
    
    # Test 2: Django setup
    try:
        import django
        print("✅ django imported")
    except Exception as e:
        print(f"❌ django failed: {e}")
        return False
    
    try:
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
        django.setup()
        print("✅ Django setup completed")
    except Exception as e:
        print(f"❌ Django setup failed: {e}")
        traceback.print_exc()
        return False
    
    return True

def debug_database_models():
    """Debug database models"""
    print("\n🔍 DEBUG: Database Models...")
    print("=" * 50)
    
    try:
        from agent.models import Client, Property, Tenant, Payment, MaintenanceTask
        print("✅ All models imported")
        
        # Test model counts
        try:
            client_count = Client.objects.count()
            print(f"✅ Client count: {client_count}")
        except Exception as e:
            print(f"❌ Client count failed: {e}")
        
        try:
            property_count = Property.objects.count()
            print(f"✅ Property count: {property_count}")
        except Exception as e:
            print(f"❌ Property count failed: {e}")
        
        try:
            tenant_count = Tenant.objects.count()
            print(f"✅ Tenant count: {tenant_count}")
        except Exception as e:
            print(f"❌ Tenant count failed: {e}")
        
        try:
            payment_count = Payment.objects.count()
            print(f"✅ Payment count: {payment_count}")
        except Exception as e:
            print(f"❌ Payment count failed: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Database models failed: {e}")
        traceback.print_exc()
        return False

def debug_avm_service():
    """Debug AVM service"""
    print("\n🔍 DEBUG: AVM Service...")
    print("=" * 50)
    
    try:
        from services.avm_service import run_payment_analysis_sync, run_roi_analysis_sync
        print("✅ AVM functions imported")
        
        # Test with minimal data
        test_data = [{'name': 'Test', 'monthly_rent': 1000, 'overdue_payments': []}]
        
        try:
            payment_result = run_payment_analysis_sync(test_data)
            print("✅ Payment analysis completed")
            print(f"   Result type: {type(payment_result)}")
        except Exception as e:
            print(f"❌ Payment analysis failed: {e}")
            traceback.print_exc()
        
        try:
            roi_result = run_roi_analysis_sync(test_data)
            print("✅ ROI analysis completed")
            print(f"   Result type: {type(roi_result)}")
        except Exception as e:
            print(f"❌ ROI analysis failed: {e}")
            traceback.print_exc()
        
        return True
        
    except Exception as e:
        print(f"❌ AVM service import failed: {e}")
        traceback.print_exc()
        return False

def debug_supabase_dynamic():
    """Debug SupabaseDynamicDB"""
    print("\n🔍 DEBUG: SupabaseDynamicDB...")
    print("=" * 50)
    
    try:
        from services.supabase_dynamic import SupabaseDynamicDB
        print("✅ SupabaseDynamicDB imported")
        
        # Test initialization
        try:
            db_service = SupabaseDynamicDB()
            print("✅ SupabaseDynamicDB initialized")
            print(f"   Connected: {db_service.connected}")
        except Exception as e:
            print(f"❌ SupabaseDynamicDB initialization failed: {e}")
            traceback.print_exc()
            return False
        
        # Test CSV analysis
        try:
            import pandas as pd
            
            # Create test CSV
            test_data = {
                'name': ['Test Property'],
                'address': ['Test Address'],
                'price': [100000]
            }
            
            df = pd.DataFrame(test_data)
            test_file = 'debug_test.csv'
            df.to_csv(test_file, index=False)
            
            print(f"✅ Created test CSV: {test_file}")
            
            # Test analysis
            analysis = db_service.analyze_csv_structure(test_file)
            
            if analysis['success']:
                print("✅ CSV analysis successful")
                print(f"   Rows: {analysis['row_count']}")
                print(f"   Columns: {analysis['column_count']}")
            else:
                print(f"❌ CSV analysis failed: {analysis['error']}")
            
            # Cleanup
            os.unlink(test_file)
            
        except Exception as e:
            print(f"❌ CSV analysis test failed: {e}")
            traceback.print_exc()
        
        return True
        
    except Exception as e:
        print(f"❌ SupabaseDynamicDB import failed: {e}")
        traceback.print_exc()
        return False

def debug_api_endpoints():
    """Debug API endpoints"""
    print("\n🔍 DEBUG: API Endpoints...")
    print("=" * 50)
    
    try:
        from api.views import (
            upload_csv_data, 
            get_uploaded_tables, 
            get_table_data, 
            delete_uploaded_table
        )
        print("✅ All API endpoints imported")
        
        # Test each endpoint
        endpoints = [
            ('upload_csv_data', upload_csv_data),
            ('get_uploaded_tables', get_uploaded_tables),
            ('get_table_data', get_table_data),
            ('delete_uploaded_table', delete_uploaded_table)
        ]
        
        for name, endpoint in endpoints:
            try:
                if callable(endpoint):
                    print(f"✅ {name} is callable")
                else:
                    print(f"❌ {name} is not callable")
            except Exception as e:
                print(f"❌ {name} test failed: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ API endpoints import failed: {e}")
        traceback.print_exc()
        return False

def debug_supabase_connection():
    """Debug Supabase connection"""
    print("\n🔍 DEBUG: Supabase Connection...")
    print("=" * 50)
    
    try:
        from services.supabase_dynamic import SupabaseDynamicDB
        
        db_service = SupabaseDynamicDB()
        
        if db_service.connected:
            print("✅ Supabase connected")
            
            # Test operations
            try:
                result = db_service.get_table_data(
                    table_name='test',
                    client_id='test',
                    limit=1
                )
                print("✅ Supabase operations working")
            except Exception as e:
                print(f"⚠️ Supabase operations failed: {e}")
        else:
            print("⚠️ Supabase not connected - running in mock mode")
            print("   This is normal for development")
        
        return True
        
    except Exception as e:
        print(f"❌ Supabase connection test failed: {e}")
        traceback.print_exc()
        return False

def debug_file_structure():
    """Debug file structure"""
    print("\n🔍 DEBUG: File Structure...")
    print("=" * 50)
    
    required_files = [
        'services/supabase_dynamic.py',
        'services/avm_service.py',
        'api/views.py',
        'api/urls.py',
        'agent/models.py',
        'config/settings.py'
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")
    
    # Check file sizes
    for file_path in required_files:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"   {file_path}: {size} bytes")

def debug_environment():
    """Debug environment variables"""
    print("\n🔍 DEBUG: Environment...")
    print("=" * 50)
    
    # Check Python version
    print(f"Python version: {sys.version}")
    
    # Check Django version
    try:
        import django
        print(f"Django version: {django.get_version()}")
    except:
        print("Django version: Unknown")
    
    # Check working directory
    print(f"Working directory: {os.getcwd()}")
    
    # Check environment variables
    env_vars = ['SUPABASE_URL', 'SUPABASE_ANON_KEY', 'DJANGO_SETTINGS_MODULE']
    for var in env_vars:
        value = os.getenv(var)
        if value:
            print(f"{var}: {value[:20]}..." if len(value) > 20 else f"{var}: {value}")
        else:
            print(f"{var}: Not set")

def main():
    """Run complete debug"""
    print("🚀 Detailed Debug - VDM Nexus System")
    print("=" * 60)
    print(f"Timestamp: {datetime.now()}")
    
    results = []
    
    # Debug environment first
    debug_environment()
    
    # Debug file structure
    debug_file_structure()
    
    # Debug imports
    if debug_imports():
        results.append(("Imports", True))
        
        # Only continue if imports work
        results.append(("Database Models", debug_database_models()))
        results.append(("AVM Service", debug_avm_service()))
        results.append(("SupabaseDynamicDB", debug_supabase_dynamic()))
        results.append(("API Endpoints", debug_api_endpoints()))
        results.append(("Supabase Connection", debug_supabase_connection()))
    else:
        results.append(("Imports", False))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 DEBUG RESULTS:")
    
    passed = sum(results)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"   {name}: {status}")
    
    print(f"\n🎯 Overall: {passed}/{total} components working")
    
    if passed == total:
        print("\n🎉 ALL COMPONENTS WORKING!")
    else:
        print(f"\n⚠️ {total - passed} components have issues")
        print("Check the detailed errors above")

if __name__ == "__main__":
    main() 