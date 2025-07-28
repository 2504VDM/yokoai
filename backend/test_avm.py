# backend/test_avm.py
"""
Test script voor AVM Service met Van der Meulen data
"""

import os
import sys
import django
from decimal import Decimal

# Django setup
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from agent.models import Client, Property, Tenant, Payment
from services.avm_service import run_payment_analysis_sync, run_roi_analysis_sync

def test_payment_analysis():
    """Test payment analysis met echte Van der Meulen data"""
    print("🔍 Testing Payment Analysis...")
    
    try:
        # Haal Van der Meulen client op
        client = Client.objects.get(subdomain='vandermeulen')
        print(f"✅ Client gevonden: {client.name}")
        
        # Haal tenants met payments op
        tenants = Tenant.objects.filter(property__client=client).prefetch_related('payments')
        print(f"✅ {tenants.count()} tenants gevonden")
        
        # Prepareer data voor AVM
        tenant_data = []
        for tenant in tenants:
            overdue_payments = []
            for payment in tenant.payments.filter(status__in=['overdue', 'pending']):
                if payment.days_overdue > 0:
                    overdue_payments.append({
                        'amount': float(payment.amount),
                        'days_overdue': payment.days_overdue,
                        'due_date': str(payment.due_date)
                    })
            
            tenant_data.append({
                'name': tenant.name,
                'monthly_rent': float(tenant.monthly_rent),
                'overdue_payments': overdue_payments
            })
        
        print(f"✅ Data voorbereid voor {len(tenant_data)} tenants")
        
        # Run AVM analysis
        result = run_payment_analysis_sync(tenant_data)
        
        # Print results
        print("\n📊 PAYMENT ANALYSIS RESULTS:")
        print(f"Total tenants: {result['total_tenants']}")
        print(f"Overdue tenants: {len(result['overdue_tenants'])}")
        print(f"Total overdue amount: €{result['total_overdue_amount']:.2f}")
        print(f"On-time percentage: {result['payment_trends']['on_time_percentage']}%")
        
        if result['urgent_cases']:
            print(f"\n⚠️ URGENT CASES ({len(result['urgent_cases'])}):")
            for case in result['urgent_cases']:
                print(f"  - {case['tenant']}: {case['issue']} (€{case['amount']:.2f})")
        
        if result['recommendations']:
            print(f"\n💡 RECOMMENDATIONS ({len(result['recommendations'])}):")
            for rec in result['recommendations']:
                print(f"  - [{rec['priority']}] {rec['message']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in payment analysis: {e}")
        return False

def test_roi_analysis():
    """Test ROI analysis met echte Van der Meulen data"""
    print("\n🏠 Testing ROI Analysis...")
    
    try:
        # Haal Van der Meulen properties op
        client = Client.objects.get(subdomain='vandermeulen')
        properties = Property.objects.filter(client=client)
        print(f"✅ {properties.count()} properties gevonden")
        
        # Prepareer data voor AVM
        property_data = []
        for prop in properties:
            property_data.append({
                'address': prop.address,
                'purchase_price': float(prop.purchase_price),
                'current_value': float(prop.current_value) if prop.current_value else float(prop.purchase_price),
                'monthly_rent': float(prop.monthly_rent)
            })
        
        # Run AVM analysis
        result = run_roi_analysis_sync(property_data)
        
        # Print results
        print("\n📈 ROI ANALYSIS RESULTS:")
        summary = result['portfolio_summary']
        print(f"Total properties: {summary['total_properties']}")
        print(f"Total investment: €{summary['total_investment']:,.2f}")
        print(f"Monthly income: €{summary['total_monthly_income']:,.2f}")
        print(f"Portfolio value: €{summary['total_portfolio_value']:,.2f}")
        print(f"Average ROI: {summary['average_roi']}%")
        
        print(f"\n🏘️ PROPERTY PERFORMANCE:")
        for prop in result['property_performance']:
            rating_emoji = "🟢" if prop['performance_rating'] == 'EXCELLENT' else "🟡" if prop['performance_rating'] == 'GOOD' else "🟠" if prop['performance_rating'] == 'FAIR' else "🔴"
            print(f"  {rating_emoji} {prop['address']}")
            print(f"     ROI: {prop['roi_percentage']}% | Rent: €{prop['monthly_rent']}/month | Rating: {prop['performance_rating']}")
        
        if result['recommendations']:
            print(f"\n💡 ROI RECOMMENDATIONS:")
            for rec in result['recommendations']:
                print(f"  - [{rec['priority']}] {rec['message']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in ROI analysis: {e}")
        return False

def main():
    """Run alle AVM tests"""
    print("🚀 Starting AVM Service Tests...\n")
    
    payment_success = test_payment_analysis()
    roi_success = test_roi_analysis()
    
    print(f"\n📋 TEST RESULTS:")
    print(f"Payment Analysis: {'✅ PASSED' if payment_success else '❌ FAILED'}")
    print(f"ROI Analysis: {'✅ PASSED' if roi_success else '❌ FAILED'}")
    
    if payment_success and roi_success:
        print(f"\n🎉 All AVM tests PASSED! Ready for dashboard integration.")
    else:
        print(f"\n⚠️ Some tests failed. Check the errors above.")

if __name__ == "__main__":
    main()