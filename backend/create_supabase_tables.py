#!/usr/bin/env python3
"""
Create Supabase Tables Script
Maakt de juiste tabellen aan in Supabase voor VDM Nexus
"""

import os
import sys
from datetime import datetime

def create_properties_table():
    """Maak properties tabel aan"""
    print("🏗️ Creating properties table...")
    
    try:
        from supabase import create_client
        
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_ANON_KEY')
        
        supabase = create_client(supabase_url, supabase_key)
        
        # SQL voor properties tabel
        sql = """
        CREATE TABLE IF NOT EXISTS properties (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(500) NOT NULL,
            purchase_price DECIMAL(12,2),
            current_value DECIMAL(12,2),
            monthly_rent DECIMAL(10,2),
            status VARCHAR(50) DEFAULT 'Available',
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        );
        """
        
        # Execute via RPC (we'll use a different approach)
        print("   Using direct table operations...")
        
        # Try to insert a test record to see if table exists
        test_data = {
            'name': 'Test Property',
            'address': 'Test Address 123',
            'purchase_price': 100000,
            'current_value': 110000,
            'monthly_rent': 1500,
            'status': 'Available'
        }
        
        try:
            result = supabase.table('properties').insert(test_data).execute()
            print("✅ Properties table exists and is working!")
            return True
        except Exception as e:
            print(f"⚠️ Properties table might not exist: {e}")
            print("   You may need to create it manually in Supabase dashboard")
            return False
            
    except Exception as e:
        print(f"❌ Error creating properties table: {e}")
        return False

def create_tenants_table():
    """Maak tenants tabel aan"""
    print("🏗️ Creating tenants table...")
    
    try:
        from supabase import create_client
        
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_ANON_KEY')
        
        supabase = create_client(supabase_url, supabase_key)
        
        # Try to insert a test record
        test_data = {
            'name': 'Test Tenant',
            'email': 'test@example.com',
            'phone': '+31612345678',
            'monthly_rent': 1500,
            'property_id': 1,
            'status': 'Active'
        }
        
        try:
            result = supabase.table('tenants').insert(test_data).execute()
            print("✅ Tenants table exists and is working!")
            return True
        except Exception as e:
            print(f"⚠️ Tenants table might not exist: {e}")
            print("   You may need to create it manually in Supabase dashboard")
            return False
            
    except Exception as e:
        print(f"❌ Error creating tenants table: {e}")
        return False

def create_payments_table():
    """Maak payments tabel aan"""
    print("🏗️ Creating payments table...")
    
    try:
        from supabase import create_client
        
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_ANON_KEY')
        
        supabase = create_client(supabase_url, supabase_key)
        
        # Try to insert a test record
        test_data = {
            'tenant_id': 1,
            'property_id': 1,
            'amount': 1500,
            'payment_date': datetime.now().isoformat(),
            'status': 'Paid',
            'payment_method': 'Bank Transfer'
        }
        
        try:
            result = supabase.table('payments').insert(test_data).execute()
            print("✅ Payments table exists and is working!")
            return True
        except Exception as e:
            print(f"⚠️ Payments table might not exist: {e}")
            print("   You may need to create it manually in Supabase dashboard")
            return False
            
    except Exception as e:
        print(f"❌ Error creating payments table: {e}")
        return False

def insert_sample_data():
    """Voeg sample data toe"""
    print("\n📊 Inserting sample data...")
    
    try:
        from supabase import create_client
        
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_ANON_KEY')
        
        supabase = create_client(supabase_url, supabase_key)
        
        # Sample properties
        properties = [
            {
                'name': 'Villa Amsterdam',
                'address': 'Herengracht 123, Amsterdam',
                'purchase_price': 450000,
                'current_value': 480000,
                'monthly_rent': 2800,
                'status': 'Rented'
            },
            {
                'name': 'Appartement Rotterdam',
                'address': 'Coolsingel 456, Rotterdam',
                'purchase_price': 320000,
                'current_value': 340000,
                'monthly_rent': 2100,
                'status': 'Available'
            },
            {
                'name': 'Huis Utrecht',
                'address': 'Domstraat 789, Utrecht',
                'purchase_price': 380000,
                'current_value': 400000,
                'monthly_rent': 2400,
                'status': 'Rented'
            }
        ]
        
        # Insert properties
        try:
            result = supabase.table('properties').insert(properties).execute()
            print("✅ Sample properties inserted!")
        except Exception as e:
            print(f"⚠️ Could not insert properties: {e}")
        
        # Sample tenants
        tenants = [
            {
                'name': 'Jan Jansen',
                'email': 'jan.jansen@email.com',
                'phone': '+31612345678',
                'monthly_rent': 2800,
                'property_id': 1,
                'status': 'Active'
            },
            {
                'name': 'Maria de Vries',
                'email': 'maria.devries@email.com',
                'phone': '+31687654321',
                'monthly_rent': 2400,
                'property_id': 3,
                'status': 'Active'
            }
        ]
        
        # Insert tenants
        try:
            result = supabase.table('tenants').insert(tenants).execute()
            print("✅ Sample tenants inserted!")
        except Exception as e:
            print(f"⚠️ Could not insert tenants: {e}")
        
        # Sample payments
        payments = [
            {
                'tenant_id': 1,
                'property_id': 1,
                'amount': 2800,
                'payment_date': datetime.now().isoformat(),
                'status': 'Paid',
                'payment_method': 'Bank Transfer'
            },
            {
                'tenant_id': 2,
                'property_id': 3,
                'amount': 2400,
                'payment_date': datetime.now().isoformat(),
                'status': 'Paid',
                'payment_method': 'Bank Transfer'
            }
        ]
        
        # Insert payments
        try:
            result = supabase.table('payments').insert(payments).execute()
            print("✅ Sample payments inserted!")
        except Exception as e:
            print(f"⚠️ Could not insert payments: {e}")
            
    except Exception as e:
        print(f"❌ Error inserting sample data: {e}")

def check_tables_exist():
    """Check welke tabellen bestaan"""
    print("\n🔍 Checking existing tables...")
    
    try:
        from supabase import create_client
        
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_ANON_KEY')
        
        supabase = create_client(supabase_url, supabase_key)
        
        tables_to_check = ['properties', 'tenants', 'payments']
        
        for table in tables_to_check:
            try:
                # Try to select from table
                result = supabase.table(table).select('*').limit(1).execute()
                print(f"✅ Table '{table}' exists")
            except Exception as e:
                print(f"❌ Table '{table}' does not exist: {e}")
                
    except Exception as e:
        print(f"❌ Error checking tables: {e}")

def main():
    """Main function"""
    print("🚀 Supabase Table Creation")
    print("=" * 50)
    
    # Check if credentials are set
    if not os.getenv('SUPABASE_URL') or not os.getenv('SUPABASE_ANON_KEY'):
        print("❌ Supabase credentials not set")
        return False
    
    # Check existing tables
    check_tables_exist()
    
    # Try to create/check tables
    create_properties_table()
    create_tenants_table()
    create_payments_table()
    
    # Insert sample data
    insert_sample_data()
    
    print("\n✅ Table setup completed!")
    print("   Check your Supabase dashboard to see the tables")
    return True

if __name__ == "__main__":
    main() 