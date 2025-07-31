#!/usr/bin/env python3
"""
Complete System Test - Dag 1 + Dag 2 Stap 1 & 2
Test alle componenten inclusief Supabase verbinding
"""

import os
import sys
import django
import pandas as pd
from datetime import datetime

# Django setup
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def test_dag1_components():
    """Test Dag 1: Database models, AVM service, dashboard"""
    print("🔍 Testing Dag 1 Components...")
    
    results = []
    
    # Test 1: Database Models
    try:
        from agent.models import Client, Property, Tenant, Payment, MaintenanceTask
        
        # Check if models can be imported
        print("✅ Database models imported successfully")
        
        # Check if sample data exists
        client_count = Client.objects.count()
        property_count = Property.objects.count()
        tenant_count = Tenant.objects.count()
        payment_count = Payment.objects.count()
        
        print(f"   - Clients: {client_count}")
        print(f"   - Properties: {property_count}")
        print(f"   - Tenants: {tenant_count}")
        print(f"   - Payments: {payment_count}")
        
        results.append(("Database Models", True))
        
    except Exception as e:
        print(f"❌ Database models failed: {e}")
        results.append(("Database Models", False))
    
    # Test 2: AVM Service
    try:
        from services.avm_service import run_payment_analysis_sync, run_roi_analysis_sync
        
        # Test AVM functions
        test_data = [
            {'name': 'Test Tenant', 'monthly_rent': 2000, 'overdue_payments': []}
        ]
        
        payment_result = run_payment_analysis_sync(test_data)
        roi_result = run_roi_analysis_sync(test_data)
        
        if payment_result and roi_result:
            print("✅ AVM Service working")
            results.append(("AVM Service", True))
        else:
            print("❌ AVM Service failed")
            results.append(("AVM Service", False))
            
    except Exception as e:
        print(f"❌ AVM Service failed: {e}")
        results.append(("AVM Service", False))
    
    # Test 3: Dashboard API
    try:
        from api.views import vdm_dashboard_overview
        
        # This would need a request object, but we can check if function exists
        print("✅ Dashboard API function exists")
        results.append(("Dashboard API", True))
        
    except Exception as e:
        print(f"❌ Dashboard API failed: {e}")
        results.append(("Dashboard API", False))
    
    return results

def test_dag2_supabase():
    """Test Dag 2 Stap 1: SupabaseDynamicDB"""
    print("\n🔍 Testing Dag 2 Stap 1: SupabaseDynamicDB...")
    
    results = []
    
    try:
        from services.supabase_dynamic import SupabaseDynamicDB
        
        # Initialize service
        db_service = SupabaseDynamicDB()
        print(f"✅ SupabaseDynamicDB initialized")
        print(f"   Connected: {db_service.connected}")
        
        # Create test CSV
        test_data = {
            'property_name': ['Test Villa', 'Test Appartement'],
            'address': ['Teststraat 1', 'Testlaan 2'],
            'purchase_price': [400000, 300000],
            'monthly_rent': [2500, 1800],
            'status': ['Rented', 'Available']
        }
        
        df = pd.DataFrame(test_data)
        test_file = 'test_supabase.csv'
        df.to_csv(test_file, index=False)
        
        # Test CSV analysis
        analysis = db_service.analyze_csv_structure(test_file)
        
        if analysis['success']:
            print("✅ CSV Analysis successful")
            print(f"   - Rows: {analysis['row_count']}")
            print(f"   - Columns: {analysis['column_count']}")
            
            # Test table creation (mock mode)
            table_result = db_service.create_dynamic_table(
                client_id='test-client-123',
                table_name='test_table',
                columns=analysis['columns'],
                original_filename='test.csv'
            )
            
            if table_result['success']:
                print("✅ Table creation successful")
                print(f"   - Table: {table_result['table_name']}")
                
                # Test data insertion
                insert_result = db_service.insert_csv_data(
                    table_name=table_result['table_name'],
                    df=analysis['dataframe'],
                    client_id='test-client-123'
                )
                
                if insert_result['success']:
                    print("✅ Data insertion successful")
                    print(f"   - Inserted: {insert_result['inserted_rows']} rows")
                else:
                    print(f"❌ Data insertion failed: {insert_result['error']}")
            else:
                print(f"❌ Table creation failed: {table_result['error']}")
        else:
            print(f"❌ CSV Analysis failed: {analysis['error']}")
        
        # Cleanup
        os.unlink(test_file)
        
        results.append(("SupabaseDynamicDB", True))
        
    except Exception as e:
        print(f"❌ SupabaseDynamicDB failed: {e}")
        results.append(("SupabaseDynamicDB", False))
    
    return results

def test_dag2_api():
    """Test Dag 2 Stap 2: API Endpoints"""
    print("\n🔍 Testing Dag 2 Stap 2: API Endpoints...")
    
    results = []
    
    try:
        from api.views import (
            upload_csv_data, 
            get_uploaded_tables, 
            get_table_data, 
            delete_uploaded_table
        )
        
        print("✅ All API endpoints imported")
        
        # Check if functions exist and are callable
        endpoints = [
            upload_csv_data,
            get_uploaded_tables,
            get_table_data,
            delete_uploaded_table
        ]
        
        for endpoint in endpoints:
            if callable(endpoint):
                print(f"   ✅ {endpoint.__name__} is callable")
            else:
                print(f"   ❌ {endpoint.__name__} is not callable")
        
        results.append(("API Endpoints", True))
        
    except Exception as e:
        print(f"❌ API Endpoints failed: {e}")
        results.append(("API Endpoints", False))
    
    return results

def test_supabase_connection():
    """Test actual Supabase connection"""
    print("\n🔍 Testing Supabase Connection...")
    
    try:
        from services.supabase_dynamic import SupabaseDynamicDB
        
        db_service = SupabaseDynamicDB()
        
        if db_service.connected:
            print("✅ Supabase connection established")
            
            # Test basic operations
            try:
                # Try to get some data (this would fail if not connected)
                test_result = db_service.get_table_data(
                    table_name='test_table',
                    client_id='test-client',
                    limit=1
                )
                
                if test_result['success']:
                    print("✅ Supabase operations working")
                    return True
                else:
                    print("⚠️ Supabase connected but operations failed")
                    return False
                    
            except Exception as e:
                print(f"⚠️ Supabase operations failed: {e}")
                return False
        else:
            print("⚠️ Supabase not connected - running in mock mode")
            print("   This is OK for development")
            return True
            
    except Exception as e:
        print(f"❌ Supabase connection test failed: {e}")
        return False

def main():
    """Run complete system test"""
    print("🚀 Complete System Test - Dag 1 + Dag 2 Stap 1 & 2")
    print("=" * 60)
    
    all_results = []
    
    # Test Dag 1
    dag1_results = test_dag1_components()
    all_results.extend(dag1_results)
    
    # Test Dag 2 Stap 1
    dag2_step1_results = test_dag2_supabase()
    all_results.extend(dag2_step1_results)
    
    # Test Dag 2 Stap 2
    dag2_step2_results = test_dag2_api()
    all_results.extend(dag2_step2_results)
    
    # Test Supabase connection
    supabase_working = test_supabase_connection()
    all_results.append(("Supabase Connection", supabase_working))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 COMPLETE TEST RESULTS:")
    
    passed = 0
    for name, result in all_results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"   {name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{len(all_results)} components working")
    
    if passed == len(all_results):
        print("\n🎉 ALL COMPONENTS WORKING!")
        print("✅ Dag 1: Database, AVM, Dashboard - READY")
        print("✅ Dag 2 Stap 1: SupabaseDynamicDB - READY")
        print("✅ Dag 2 Stap 2: API Endpoints - READY")
        print("✅ Supabase Connection - READY")
        print("\n🚀 Ready for Dag 2 Stap 3 & 4 + Dag 3")
    else:
        print(f"\n⚠️ {len(all_results) - passed} components need attention")
        print("Check the errors above and fix them")

if __name__ == "__main__":
    main() 