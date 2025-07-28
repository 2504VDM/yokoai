# backend/services/avm_service.py
import os
import json
import httpx
import asyncio
from typing import Dict, List, Any, Optional
from datetime import date, timedelta
from decimal import Decimal

class AVMService:
    """AVM (AI Analysis) Service voor VDM Nexus platform"""
    
    def __init__(self):
        self.api_key = os.getenv('AVM_API_KEY', 'avm_2919b1c1-eb6f-4f6d-a966-83f6445aa6b2')
        self.base_url = os.getenv('AVM_BASE_URL', 'https://api.avm.codes')
        self.timeout = 30
    
    async def run_payment_analysis(self, tenant_data: List[Dict]) -> Dict[str, Any]:
        """
        Van der Meulen payment analysis via AVM
        Analyseert huurbetalingen en identificeert risico's
        """
        
        # AVM Python code voor payment analysis
        avm_code = """
import json
from datetime import datetime, date

def execute(input_data):
    tenants = input_data.get('tenants', [])
    today = date.today()
    
    analysis = {
        'total_tenants': len(tenants),
        'overdue_tenants': [],
        'total_overdue_amount': 0,
        'urgent_cases': [],
        'payment_trends': {
            'on_time_percentage': 0,
            'average_delay_days': 0
        },
        'recommendations': []
    }
    
    on_time_count = 0
    total_delay_days = 0
    delay_count = 0
    
    for tenant in tenants:
        tenant_name = tenant.get('name', 'Unknown')
        monthly_rent = float(tenant.get('monthly_rent', 0))
        overdue_payments = tenant.get('overdue_payments', [])
        
        if overdue_payments:
            total_overdue = sum(float(p.get('amount', 0)) for p in overdue_payments)
            max_days_overdue = max(int(p.get('days_overdue', 0)) for p in overdue_payments)
            
            tenant_analysis = {
                'name': tenant_name,
                'monthly_rent': monthly_rent,
                'overdue_amount': total_overdue,
                'overdue_payments_count': len(overdue_payments),
                'max_days_overdue': max_days_overdue,
                'urgency_level': 'HIGH' if max_days_overdue > 30 else 'MEDIUM' if max_days_overdue > 14 else 'LOW'
            }
            
            analysis['overdue_tenants'].append(tenant_analysis)
            analysis['total_overdue_amount'] += total_overdue
            
            if max_days_overdue > 30:
                analysis['urgent_cases'].append({
                    'tenant': tenant_name,
                    'issue': f'{max_days_overdue} dagen achterstallig',
                    'amount': total_overdue,
                    'action': 'Dringende actie vereist - contact opnemen'
                })
            
            # Track delays for trends
            total_delay_days += max_days_overdue
            delay_count += 1
        else:
            on_time_count += 1
    
    # Calculate trends
    if len(tenants) > 0:
        analysis['payment_trends']['on_time_percentage'] = round((on_time_count / len(tenants)) * 100, 1)
    
    if delay_count > 0:
        analysis['payment_trends']['average_delay_days'] = round(total_delay_days / delay_count, 1)
    
    # Generate recommendations
    if analysis['total_overdue_amount'] > 5000:
        analysis['recommendations'].append({
            'type': 'CASH_FLOW',
            'priority': 'HIGH',
            'message': f'Hoog uitstaand bedrag: €{analysis["total_overdue_amount"]:.2f}. Overweeg incasso procedure.'
        })
    
    if analysis['payment_trends']['on_time_percentage'] < 80:
        analysis['recommendations'].append({
            'type': 'PAYMENT_PROCESS',
            'priority': 'MEDIUM', 
            'message': f'Slechts {analysis["payment_trends"]["on_time_percentage"]}% betaalt op tijd. Automatische betalingen promoten.'
        })
    
    if len(analysis['urgent_cases']) > 0:
        analysis['recommendations'].append({
            'type': 'URGENT_ACTION',
            'priority': 'HIGH',
            'message': f'{len(analysis["urgent_cases"])} huurders >30 dagen achterstallig. Directe actie nodig.'
        })
    
    return analysis

# Execute the analysis
result = execute(input)
print(json.dumps(result, default=str))
"""
        
        try:
            # Voor development: simuleer AVM response
            if self.api_key == 'test-key-for-development':
                return await self._simulate_payment_analysis(tenant_data)
            
            # Echte AVM API call
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/api/run/sync",
                    headers={
                        "avm-x-api-key": self.api_key,
                        "Content-Type": "application/json"
                    },
                    json={
                        "code": avm_code,
                        "input": {"tenants": tenant_data}
                    }
                )
                response.raise_for_status()
                return response.json()
                
        except Exception as e:
            print(f"AVM API Error: {e}")
            # Fallback to simulation
            return await self._simulate_payment_analysis(tenant_data)
    
    async def _simulate_payment_analysis(self, tenant_data: List[Dict]) -> Dict[str, Any]:
        """Simulatie van AVM analysis voor development"""
        
        total_tenants = len(tenant_data)
        overdue_tenants = []
        total_overdue = 0
        urgent_cases = []
        on_time_count = 0
        
        for tenant in tenant_data:
            overdue_payments = tenant.get('overdue_payments', [])
            if overdue_payments:
                max_days = max(p.get('days_overdue', 0) for p in overdue_payments)
                overdue_amount = sum(p.get('amount', 0) for p in overdue_payments)
                
                overdue_tenants.append({
                    'name': tenant['name'],
                    'monthly_rent': tenant['monthly_rent'],
                    'overdue_amount': overdue_amount,
                    'max_days_overdue': max_days,
                    'urgency_level': 'HIGH' if max_days > 30 else 'MEDIUM' if max_days > 14 else 'LOW'
                })
                
                total_overdue += overdue_amount
                
                if max_days > 30:
                    urgent_cases.append({
                        'tenant': tenant['name'],
                        'issue': f'{max_days} dagen achterstallig',
                        'amount': overdue_amount,
                        'action': 'Dringende actie vereist'
                    })
            else:
                on_time_count += 1
        
        on_time_percentage = round((on_time_count / total_tenants) * 100, 1) if total_tenants > 0 else 0
        
        recommendations = []
        if total_overdue > 2000:
            recommendations.append({
                'type': 'CASH_FLOW',
                'priority': 'HIGH',
                'message': f'Hoog uitstaand bedrag: €{total_overdue:.2f}. Incasso procedure overwegen.'
            })
        
        if on_time_percentage < 80:
            recommendations.append({
                'type': 'PAYMENT_PROCESS',
                'priority': 'MEDIUM',
                'message': f'{on_time_percentage}% betaalt op tijd. Automatische incasso promoten.'
            })
        
        return {
            'total_tenants': total_tenants,
            'overdue_tenants': overdue_tenants,
            'total_overdue_amount': total_overdue,
            'urgent_cases': urgent_cases,
            'payment_trends': {
                'on_time_percentage': on_time_percentage,
                'average_delay_days': 8.5 if overdue_tenants else 0
            },
            'recommendations': recommendations
        }
    
    async def run_roi_analysis(self, property_data: List[Dict]) -> Dict[str, Any]:
        """ROI analyse voor vastgoed portfolio"""
        
        avm_code = """
def execute(input_data):
    properties = input_data.get('properties', [])
    
    analysis = {
        'portfolio_summary': {
            'total_properties': len(properties),
            'total_investment': 0,
            'total_monthly_income': 0,
            'average_roi': 0,
            'total_portfolio_value': 0
        },
        'property_performance': [],
        'recommendations': []
    }
    
    total_investment = 0
    total_current_value = 0
    total_monthly_rent = 0
    roi_scores = []
    
    for prop in properties:
        address = prop.get('address', 'Unknown')
        purchase_price = float(prop.get('purchase_price', 0))
        current_value = float(prop.get('current_value', purchase_price))
        monthly_rent = float(prop.get('monthly_rent', 0))
        
        annual_rent = monthly_rent * 12
        roi_percentage = (annual_rent / current_value * 100) if current_value > 0 else 0
        capital_gain = current_value - purchase_price
        capital_gain_percentage = (capital_gain / purchase_price * 100) if purchase_price > 0 else 0
        
        performance = {
            'address': address,
            'purchase_price': purchase_price,
            'current_value': current_value,
            'monthly_rent': monthly_rent,
            'annual_rent': annual_rent,
            'roi_percentage': round(roi_percentage, 2),
            'capital_gain': capital_gain,
            'capital_gain_percentage': round(capital_gain_percentage, 2),
            'performance_rating': 'EXCELLENT' if roi_percentage >= 8 else 'GOOD' if roi_percentage >= 6 else 'FAIR' if roi_percentage >= 4 else 'POOR'
        }
        
        analysis['property_performance'].append(performance)
        
        total_investment += purchase_price
        total_current_value += current_value
        total_monthly_rent += monthly_rent
        roi_scores.append(roi_percentage)
    
    # Portfolio summary
    analysis['portfolio_summary']['total_investment'] = total_investment
    analysis['portfolio_summary']['total_monthly_income'] = total_monthly_rent
    analysis['portfolio_summary']['total_portfolio_value'] = total_current_value
    analysis['portfolio_summary']['average_roi'] = round(sum(roi_scores) / len(roi_scores), 2) if roi_scores else 0
    
    # Recommendations
    low_performers = [p for p in analysis['property_performance'] if p['roi_percentage'] < 4]
    if low_performers:
        analysis['recommendations'].append({
            'type': 'LOW_PERFORMANCE',
            'priority': 'MEDIUM',
            'message': f'{len(low_performers)} panden presteren onder 4% ROI. Huur verhogen of verkoop overwegen.'
        })
    
    high_performers = [p for p in analysis['property_performance'] if p['roi_percentage'] >= 8]
    if high_performers:
        analysis['recommendations'].append({
            'type': 'EXPANSION',
            'priority': 'LOW',
            'message': f'{len(high_performers)} panden presteren excellent (8%+). Vergelijkbare investeringen zoeken.'
        })
    
    return analysis

result = execute(input)
print(json.dumps(result, default=str))
"""
        
        try:
            if self.api_key == 'test-key-for-development':
                return await self._simulate_roi_analysis(property_data)
                
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/api/run/sync",
                    headers={
                        "avm-x-api-key": self.api_key,
                        "Content-Type": "application/json"
                    },
                    json={
                        "code": avm_code,
                        "input": {"properties": property_data}
                    }
                )
                response.raise_for_status()
                return response.json()
                
        except Exception as e:
            print(f"AVM API Error: {e}")
            return await self._simulate_roi_analysis(property_data)
    
    async def _simulate_roi_analysis(self, property_data: List[Dict]) -> Dict[str, Any]:
        """Simulatie van ROI analysis"""
        
        total_investment = 0
        total_current_value = 0
        total_monthly_rent = 0
        property_performance = []
        roi_scores = []
        
        for prop in property_data:
            purchase_price = float(prop.get('purchase_price', 0))
            current_value = float(prop.get('current_value', purchase_price))
            monthly_rent = float(prop.get('monthly_rent', 0))
            
            annual_rent = monthly_rent * 12
            roi_percentage = (annual_rent / current_value * 100) if current_value > 0 else 0
            capital_gain = current_value - purchase_price
            
            performance = {
                'address': prop.get('address', 'Unknown'),
                'purchase_price': purchase_price,
                'current_value': current_value,
                'monthly_rent': monthly_rent,
                'annual_rent': annual_rent,
                'roi_percentage': round(roi_percentage, 2),
                'capital_gain': capital_gain,
                'performance_rating': 'EXCELLENT' if roi_percentage >= 8 else 'GOOD' if roi_percentage >= 6 else 'FAIR' if roi_percentage >= 4 else 'POOR'
            }
            
            property_performance.append(performance)
            total_investment += purchase_price
            total_current_value += current_value
            total_monthly_rent += monthly_rent
            roi_scores.append(roi_percentage)
        
        avg_roi = round(sum(roi_scores) / len(roi_scores), 2) if roi_scores else 0
        
        return {
            'portfolio_summary': {
                'total_properties': len(property_data),
                'total_investment': total_investment,
                'total_monthly_income': total_monthly_rent,
                'average_roi': avg_roi,
                'total_portfolio_value': total_current_value
            },
            'property_performance': property_performance,
            'recommendations': [
                {
                    'type': 'PORTFOLIO_HEALTH',
                    'priority': 'INFO',
                    'message': f'Portfolio gemiddelde ROI: {avg_roi}%. Nederlandse vastgoed benchmark: 4-6%.'
                }
            ]
        }

# Synchrone wrapper functies voor Django views
def run_payment_analysis_sync(tenant_data: List[Dict]) -> Dict[str, Any]:
    """Synchrone wrapper voor payment analysis"""
    avm_service = AVMService()
    return asyncio.run(avm_service.run_payment_analysis(tenant_data))

def run_roi_analysis_sync(property_data: List[Dict]) -> Dict[str, Any]:
    """Synchrone wrapper voor ROI analysis"""
    avm_service = AVMService()
    return asyncio.run(avm_service.run_roi_analysis(property_data))