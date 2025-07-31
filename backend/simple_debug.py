#!/usr/bin/env python3
"""
Simple Debug - Quick diagnose van Supabase en AVM problemen
"""

import os
import sys

def check_supabase():
    """Check Supabase probleem"""
    print("🔍 Checking Supabase...")
    
    # Check 1: Is Supabase geïnstalleerd?
    try:
        import supabase
        print("✅ Supabase library installed")
    except ImportError:
        print("❌ Supabase not installed")
        print("   Run: pip install supabase")
        return False
    
    # Check 2: Zijn credentials ingesteld?
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_ANON_KEY')
    
    if not supabase_url:
        print("❌ SUPABASE_URL not set")
        print("   Set: export SUPABASE_URL='your-url'")
        return False
    
    if not supabase_key:
        print("❌ SUPABASE_ANON_KEY not set")
        print("   Set: export SUPABASE_ANON_KEY='your-key'")
        return False
    
    print("✅ Supabase credentials set")
    return True

def check_avm():
    """Check AVM API probleem"""
    print("\n🔍 Checking AVM API...")
    
    # Check 1: Is AVM API key ingesteld?
    avm_key = os.getenv('AVM_API_KEY')
    
    if not avm_key:
        print("❌ AVM_API_KEY not set")
        print("   Set: export AVM_API_KEY='your-key'")
        print("   Get key from: https://avm.codes/")
        return False
    
    print("✅ AVM API key set")
    return True

def main():
    print("🚀 Simple Debug - Supabase & AVM")
    print("=" * 40)
    
    supabase_ok = check_supabase()
    avm_ok = check_avm()
    
    print("\n📊 RESULTS:")
    print(f"   Supabase: {'✅ OK' if supabase_ok else '❌ BROKEN'}")
    print(f"   AVM API: {'✅ OK' if avm_ok else '❌ BROKEN'}")
    
    if not supabase_ok:
        print("\n🔧 To fix Supabase:")
        print("   1. Go to https://supabase.com")
        print("   2. Create a project")
        print("   3. Get URL and ANON_KEY from Settings > API")
        print("   4. Set environment variables:")
        print("      export SUPABASE_URL='your-project-url'")
        print("      export SUPABASE_ANON_KEY='your-anon-key'")
    
    if not avm_ok:
        print("\n🔧 To fix AVM API:")
        print("   1. Go to https://avm.codes/")
        print("   2. Get an API key")
        print("   3. Set environment variable:")
        print("      export AVM_API_KEY='your-api-key'")

if __name__ == "__main__":
    main() 