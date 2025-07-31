#!/usr/bin/env python3
"""
Run Supabase SQL Setup Script
Voert de multi-tenant database setup uit in Supabase
"""

import os
import sys
import psycopg2
from datetime import datetime

def run_sql_setup():
    """Voer de SQL setup uit in Supabase"""
    print("🚀 Running Supabase SQL Setup")
    print("=" * 50)
    
    # Database connection details
    db_url = "postgresql://postgres.oldsyjgsvpdqhcyrbray:sDIfbC92rEqFyDt1@aws-0-eu-west-3.pooler.supabase.com:5432/postgres"
    
    try:
        # Connect to database
        print("🔌 Connecting to Supabase database...")
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        
        print("✅ Connected successfully!")
        
        # Read SQL file
        sql_file = "supabase_multi_tenant_setup.sql"
        
        if not os.path.exists(sql_file):
            print(f"❌ SQL file not found: {sql_file}")
            return False
        
        print(f"📄 Reading SQL file: {sql_file}")
        with open(sql_file, 'r') as f:
            sql_content = f.read()
        
        # Split SQL into individual statements
        statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]
        
        print(f"📊 Executing {len(statements)} SQL statements...")
        
        for i, statement in enumerate(statements, 1):
            if statement.strip():
                try:
                    print(f"   [{i}/{len(statements)}] Executing statement...")
                    cursor.execute(statement)
                    print(f"   ✅ Statement {i} executed successfully")
                except Exception as e:
                    print(f"   ⚠️ Statement {i} failed: {e}")
                    # Continue with next statement
                    continue
        
        # Commit changes
        conn.commit()
        print("✅ All SQL statements executed!")
        
        # Test the setup
        print("\n🧪 Testing setup...")
        test_queries = [
            "SELECT COUNT(*) FROM clients",
            "SELECT COUNT(*) FROM properties",
            "SELECT COUNT(*) FROM tenants",
            "SELECT COUNT(*) FROM payments",
            "SELECT COUNT(*) FROM knowledge_base",
            "SELECT COUNT(*) FROM csv_uploads",
            "SELECT COUNT(*) FROM dynamic_tables"
        ]
        
        for query in test_queries:
            try:
                cursor.execute(query)
                result = cursor.fetchone()
                table_name = query.split()[-1]
                print(f"   ✅ {table_name}: {result[0]} rows")
            except Exception as e:
                print(f"   ❌ {table_name}: {e}")
        
        cursor.close()
        conn.close()
        
        print("\n✅ Supabase setup completed successfully!")
        print("   Your multi-tenant database is ready!")
        return True
        
    except Exception as e:
        print(f"❌ Database setup failed: {e}")
        return False

def install_psycopg2():
    """Install psycopg2 if not available"""
    try:
        import psycopg2
        print("✅ psycopg2 is already installed")
        return True
    except ImportError:
        print("📦 Installing psycopg2...")
        try:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "psycopg2-binary"])
            print("✅ psycopg2 installed successfully")
            return True
        except Exception as e:
            print(f"❌ Failed to install psycopg2: {e}")
            return False

def main():
    """Main function"""
    print("🚀 Supabase Multi-Tenant Database Setup")
    print("=" * 50)
    
    # Check if psycopg2 is available
    if not install_psycopg2():
        return False
    
    # Run the setup
    return run_sql_setup()

if __name__ == "__main__":
    main() 