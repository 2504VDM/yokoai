#!/usr/bin/env python3
"""
AVM AI Analysis Setup Script
Helpt met het opzetten van echte AVM AI analysis
"""

import os
import sys
import requests
import json

def check_avm_credentials():
    """Check of AVM API key is ingesteld"""
    print("🔍 Checking AVM API Credentials...")
    
    avm_api_key = os.getenv('AVM_API_KEY')
    
    if not avm_api_key:
        print("❌ AVM_API_KEY not set")
        print("   Get it from: https://avm.codes/")
        return False
    
    if avm_api_key == 'avm_2919b1c1-eb6f-4f6d-a966-83f6445aa6b2':
        print("❌ Using default AVM API key - get a real one")
        print("   Get it from: https://avm.codes/")
        return False
    
    print(f"✅ AVM_API_KEY: {avm_api_key[:20]}...")
    return True

def test_avm_api():
    """Test echte AVM API verbinding"""
    print("\n🔍 Testing AVM API Connection...")
    
    avm_api_key = os.getenv('AVM_API_KEY')
    
    if not avm_api_key:
        print("❌ No AVM API key available")
        return False
    
    # Test API call
    url = "https://api.avm.codes/api/run/sync"
    headers = {
        "avm-x-api-key": avm_api_key,
        "Content-Type": "application/json"
    }
    
    # Simple test code
    test_code = """
def execute(input_data):
    return {
        "message": "AVM API is working!",
        "input_received": input_data
    }
"""
    
    data = {
        "code": test_code,
        "input": {"test": "Hello AVM!"}
    }
    
    try:
        print("Making test API call...")
        response = requests.post(url, headers=headers, json=data, timeout=10)
        
        print(f"Response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ AVM API working successfully!")
            print(f"   Response: {result}")
            return True
        elif response.status_code == 401:
            print("❌ AVM API: Unauthorized - check API key")
            return False
        elif response.status_code == 500:
            print("❌ AVM API: Server error (500) - API might be down")
            return False
        else:
            print(f"❌ AVM API: Unexpected status {response.status_code}")
            print(f"Response: {response.text[:200]}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ AVM API request failed: {e}")
        return False

def test_payment_analysis():
    """Test echte payment analysis"""
    print("\n🔍 Testing Payment Analysis...")
    
    try:
        from services.avm_service import AVMService
        
        avm_service = AVMService()
        
        # Test data
        test_tenants = [
            {
                'name': 'Jan Jansen',
                'monthly_rent': 2500,
                'overdue_payments': [
                    {'amount': 2500, 'days_overdue': 15}
                ]
            },
            {
                'name': 'Maria de Vries',
                'monthly_rent': 1800,
                'overdue_payments': []
            }
        ]
        
        # Test the analysis
        import asyncio
        result = asyncio.run(avm_service.run_payment_analysis(test_tenants))
        
        if result:
            print("✅ Payment analysis working!")
            print(f"   Total tenants: {result.get('total_tenants', 0)}")
            print(f"   Overdue amount: €{result.get('total_overdue_amount', 0)}")
            return True
        else:
            print("❌ Payment analysis failed")
            return False
            
    except Exception as e:
        print(f"❌ Payment analysis test failed: {e}")
        return False

def test_roi_analysis():
    """Test echte ROI analysis"""
    print("\n🔍 Testing ROI Analysis...")
    
    try:
        from services.avm_service import AVMService
        
        avm_service = AVMService()
        
        # Test data
        test_properties = [
            {
                'address': 'Herengracht 123',
                'purchase_price': 450000,
                'current_value': 480000,
                'monthly_rent': 2800
            },
            {
                'address': 'Coolsingel 456',
                'purchase_price': 320000,
                'current_value': 340000,
                'monthly_rent': 2100
            }
        ]
        
        # Test the analysis
        import asyncio
        result = asyncio.run(avm_service.run_roi_analysis(test_properties))
        
        if result:
            print("✅ ROI analysis working!")
            portfolio = result.get('portfolio_summary', {})
            print(f"   Total properties: {portfolio.get('total_properties', 0)}")
            print(f"   Average ROI: {portfolio.get('average_roi', 0)}%")
            return True
        else:
            print("❌ ROI analysis failed")
            return False
            
    except Exception as e:
        print(f"❌ ROI analysis test failed: {e}")
        return False

def setup_environment_variables():
    """Help met het instellen van environment variables"""
    print("\n🔧 Environment Variables Setup...")
    
    print("\n📝 To set up AVM AI Analysis, follow these steps:")
    print("1. Go to https://avm.codes/")
    print("2. Sign up for an account")
    print("3. Get your API key")
    print("4. Set the environment variable:")
    print()
    print("export AVM_API_KEY='your-api-key'")
    print()
    print("Or add it to your .env file:")
    print("AVM_API_KEY=your-api-key")

def main():
    """Main setup function"""
    print("🚀 AVM AI Analysis Setup")
    print("=" * 50)
    
    # Check credentials
    if not check_avm_credentials():
        print("\n❌ AVM credentials not configured")
        setup_environment_variables()
        return False
    
    # Test API connection
    if not test_avm_api():
        print("\n❌ AVM API connection failed")
        return False
    
    # Test payment analysis
    if not test_payment_analysis():
        print("\n❌ Payment analysis failed")
        return False
    
    # Test ROI analysis
    if not test_roi_analysis():
        print("\n❌ ROI analysis failed")
        return False
    
    print("\n✅ AVM AI Analysis setup completed!")
    print("   Your AI analysis is ready for real data")
    return True

if __name__ == "__main__":
    main() 