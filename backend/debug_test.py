# backend/debug_test.py - Super snelle test

import pandas as pd
import tempfile
import os
from datetime import datetime

print("🚀 Quick Debug Test - VDM Nexus")
print("-" * 40)

# Test 1: Pandas werkt
try:
    df = pd.DataFrame({'test': [1, 2, 3]})
    print("✅ Pandas works")
except Exception as e:
    print(f"❌ Pandas failed: {e}")
    exit(1)

# Test 2: CSV creation werkt
try:
    test_data = {
        'naam': ['Jan', 'Marie'],
        'huur': [1250, 1850],
        'email': ['jan@test.nl', 'marie@test.nl']
    }
    
    df = pd.DataFrame(test_data)
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        df.to_csv(f.name, index=False)
        csv_path = f.name
    
    print(f"✅ Test CSV created: {os.path.basename(csv_path)}")
    
    # Read it back
    df_read = pd.read_csv(csv_path)
    print(f"✅ CSV read back: {len(df_read)} rows, {len(df_read.columns)} columns")
    
    # Cleanup
    os.unlink(csv_path)
    
except Exception as e:
    print(f"❌ CSV test failed: {e}")
    exit(1)

# Test 3: Try service import (WITHOUT Django)
try:
    # Add current directory to path
    import sys
    sys.path.append('.')
    
    # Try importing our service class definition
    with open('services/supabase_dynamic.py', 'r') as f:
        content = f.read()
        if 'class SupabaseDynamicDB' in content:
            print("✅ SupabaseDynamicDB class found in file")
        else:
            print("❌ SupabaseDynamicDB class not found")
    
except Exception as e:
    print(f"❌ Service file check failed: {e}")

# Test 4: Environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
    
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_ANON_KEY')
    
    if supabase_url:
        print(f"✅ SUPABASE_URL found: {supabase_url[:50]}...")
    else:
        print("❌ SUPABASE_URL not found")
        
    if supabase_key:
        print("✅ SUPABASE_ANON_KEY found")
    else:
        print("❌ SUPABASE_ANON_KEY not found")
        
except Exception as e:
    print(f"❌ Environment test failed: {e}")

print("\n🎯 Quick Debug Complete!")
print("If all ✅ then CSV system basics work")
print("Django setup might be the slow part")