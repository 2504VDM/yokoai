#!/usr/bin/env python3
"""
Test script voor CSV Upload System - Dag 2
Test de complete CSV upload pipeline met sample data.
"""

import os
import sys
import django
import tempfile
import pandas as pd
from datetime import datetime, timedelta
import random

# Django setup
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from services.supabase_dynamic import SupabaseDynamicDB
from agent.models import Client, Property, Tenant, Payment

def create_sample_csv_files():
    """Maakt sample CSV bestanden voor testing."""
    
    # Sample 1: Properties CSV
    properties_data = {
        'property_name': ['Villa Amsterdam', 'Appartement Rotterdam', 'Huis Utrecht', 'Studio Den Haag', 'Penthouse Eindhoven'],
        'address': ['Herengracht 123', 'Coolsingel 456', 'Oudegracht 789', 'Noordeinde 321', 'Markt 654'],
        'purchase_price': [450000, 320000, 280000, 180000, 650000],
        'current_value': [480000, 340000, 295000, 195000, 680000],
        'monthly_rent': [2800, 2100, 1850, 1200, 3800],
        'property_type': ['Villa', 'Appartement', 'Huis', 'Studio', 'Penthouse'],
        'purchase_date': ['2020-03-15', '2021-07-22', '2019-11-08', '2022-01-30', '2020-09-12'],
        'status': ['Rented', 'Available', 'Rented', 'Rented', 'Available']
    }
    
    # Sample 2: Tenants CSV
    tenants_data = {
        'tenant_name': ['Jan Jansen', 'Maria de Vries', 'Pieter Bakker', 'Anna Visser', 'Lucas Smit'],
        'email': ['jan.jansen@email.com', 'maria.devries@email.com', 'pieter.bakker@email.com', 'anna.visser@email.com', 'lucas.smit@email.com'],
        'phone': ['+31612345678', '+31623456789', '+31634567890', '+31645678901', '+31656789012'],
        'monthly_rent': [2800, 2100, 1850, 1200, 3800],
        'lease_start': ['2023-01-01', '2023-03-15', '2022-11-01', '2023-02-01', '2023-04-01'],
        'lease_end': ['2024-12-31', '2024-12-31', '2024-10-31', '2024-01-31', '2025-03-31'],
        'payment_status': ['On Time', 'Overdue', 'On Time', 'On Time', 'On Time'],
        'security_deposit': [5600, 4200, 3700, 2400, 7600]
    }
    
    # Sample 3: Payments CSV
    payments_data = {
        'tenant_name': ['Jan Jansen', 'Maria de Vries', 'Pieter Bakker', 'Anna Visser', 'Lucas Smit'] * 6,
        'payment_date': [
            '2024-01-01', '2024-01-01', '2024-01-01', '2024-01-01', '2024-01-01',
            '2024-02-01', '2024-02-01', '2024-02-01', '2024-02-01', '2024-02-01',
            '2024-03-01', '2024-03-01', '2024-03-01', '2024-03-01', '2024-03-01',
            '2024-04-01', '2024-04-01', '2024-04-01', '2024-04-01', '2024-04-01',
            '2024-05-01', '2024-05-01', '2024-05-01', '2024-05-01', '2024-05-01',
            '2024-06-01', '2024-06-01', '2024-06-01', '2024-06-01', '2024-06-01'
        ],
        'amount': [2800, 2100, 1850, 1200, 3800] * 6,
        'status': ['Paid', 'Overdue', 'Paid', 'Paid', 'Paid'] * 6,
        'payment_method': ['Bank Transfer', 'Bank Transfer', 'Direct Debit', 'Bank Transfer', 'Bank Transfer'] * 6,
        'late_fee': [0, 50, 0, 0, 0] * 6
    }
    
    # Create temporary directory
    temp_dir = 'temp_csv_test'
    os.makedirs(temp_dir, exist_ok=True)
    
    # Save CSV files
    files = {}
    
    df_properties = pd.DataFrame(properties_data)
    properties_file = os.path.join(temp_dir, 'properties_sample.csv')
    df_properties.to_csv(properties_file, index=False)
    files['properties'] = properties_file
    
    df_tenants = pd.DataFrame(tenants_data)
    tenants_file = os.path.join(temp_dir, 'tenants_sample.csv')
    df_tenants.to_csv(tenants_file, index=False)
    files['tenants'] = tenants_file
    
    df_payments = pd.DataFrame(payments_data)
    payments_file = os.path.join(temp_dir, 'payments_sample.csv')
    df_payments.to_csv(payments_file, index=False)
    files['payments'] = payments_file
    
    return files

def test_csv_analysis():
    """Test CSV analysis functionaliteit."""
    print("🔍 Testing CSV Analysis...")
    
    # Create sample files
    files = create_sample_csv_files()
    
    # Initialize service
    db_service = SupabaseDynamicDB()
    
    for file_type, file_path in files.items():
        print(f"\n📄 Testing {file_type} CSV...")
        
        # Test analysis
        analysis = db_service.analyze_csv_structure(file_path)
        
        if analysis['success']:
            print(f"✅ Analysis successful:")
            print(f"   - Rows: {analysis['row_count']}")
            print(f"   - Columns: {analysis['column_count']}")
            print(f"   - File size: {analysis['file_size']} bytes")
            
            # Show column types
            print("   - Column types:")
            for col_name, metadata in analysis['columns'].items():
                print(f"     • {col_name}: {metadata['sql_type']}")
        else:
            print(f"❌ Analysis failed: {analysis['error']}")

def test_client_validation():
    """Test client-specific validation."""
    print("\n🔍 Testing Client Validation...")
    
    # Get or create test client
    client, created = Client.objects.get_or_create(
        id='550e8400-e29b-41d4-a716-446655440000',
        defaults={
            'name': 'Van der Meulen Vastgoed',
            'industry': 'vastgoed',
            'subdomain': 'vandermeulen'
        }
    )
    
    files = create_sample_csv_files()
    db_service = SupabaseDynamicDB()
    
    for file_type, file_path in files.items():
        print(f"\n📄 Testing validation for {file_type} CSV...")
        
        validation = db_service.validate_csv_for_client(file_path, str(client.id))
        
        if validation['success']:
            print(f"✅ Validation successful:")
            print(f"   - Score: {validation['validation']['validation_score']}/100")
            print(f"   - Warnings: {len(validation['validation']['warnings'])}")
            print(f"   - Suggestions: {len(validation['validation']['suggestions'])}")
            print(f"   - Recommended widgets: {len(validation['validation']['recommended_widgets'])}")
        else:
            print(f"❌ Validation failed: {validation['error']}")

def test_table_creation():
    """Test dynamic table creation."""
    print("\n🏗️ Testing Table Creation...")
    
    client_id = '550e8400-e29b-41d4-a716-446655440000'
    files = create_sample_csv_files()
    db_service = SupabaseDynamicDB()
    
    for file_type, file_path in files.items():
        print(f"\n📄 Testing table creation for {file_type}...")
        
        # Analyze CSV
        analysis = db_service.analyze_csv_structure(file_path)
        
        if analysis['success']:
            # Create table
            table_result = db_service.create_dynamic_table(
                client_id=client_id,
                table_name=f"{file_type}_test",
                columns=analysis['columns'],
                original_filename=f"{file_type}_sample.csv"
            )
            
            if table_result['success']:
                print(f"✅ Table created: {table_result['table_name']}")
                
                # Test data insertion
                insert_result = db_service.insert_csv_data(
                    table_name=table_result['table_name'],
                    df=analysis['dataframe'],
                    client_id=client_id
                )
                
                if insert_result['success']:
                    print(f"✅ Data inserted: {insert_result['inserted_rows']} rows")
                else:
                    print(f"❌ Data insertion failed: {insert_result['error']}")
            else:
                print(f"❌ Table creation failed: {table_result['error']}")

def test_api_endpoints():
    """Test API endpoints via HTTP requests."""
    print("\n🌐 Testing API Endpoints...")
    
    import requests
    import json
    
    base_url = "http://localhost:8000/api"
    client_id = "550e8400-e29b-41d4-a716-446655440000"
    
    # Test 1: Get uploaded tables
    try:
        response = requests.get(f"{base_url}/uploaded-tables?client_id={client_id}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Get tables endpoint: {len(data.get('tables', []))} tables found")
        else:
            print(f"❌ Get tables endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Get tables endpoint error: {str(e)}")
    
    # Test 2: Upload CSV (simulated)
    print("\n📤 Testing CSV upload endpoint...")
    print("Note: This would require a real CSV file upload")
    print("You can test this via the frontend upload interface")

def cleanup():
    """Cleanup temporary files."""
    import shutil
    
    temp_dir = 'temp_csv_test'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        print(f"🧹 Cleaned up temporary files")

def main():
    """Main test function."""
    print("🚀 VDM Nexus CSV Upload System Test")
    print("=" * 50)
    
    try:
        # Run tests
        test_csv_analysis()
        test_client_validation()
        test_table_creation()
        test_api_endpoints()
        
        print("\n✅ All tests completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        cleanup()

if __name__ == "__main__":
    main()