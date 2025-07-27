# backend/api/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from agent.models import Client, ClientKnowledgeBase, BusinessFunction
import json

def health_check(request):
    return JsonResponse({'status': 'OK', 'message': 'VDM Nexus API is running'})

@csrf_exempt
@require_http_methods(["GET"])
def vandermeulen_data(request):
    """Get Van der Meulen Vastgoed data"""
    try:
        client = Client.objects.get(subdomain="vandermeulen")
        knowledge_bases = ClientKnowledgeBase.objects.filter(client=client)
        business_functions = BusinessFunction.objects.filter(client=client)
        
        data = {
            'client': {
                'id': str(client.id),
                'name': client.name,
                'subdomain': client.subdomain
            },
            'knowledge_bases': [
                {
                    'id': str(kb.id),
                    'name': kb.name,
                    'description': kb.description
                } for kb in knowledge_bases
            ],
            'business_functions': [
                {
                    'id': str(bf.id),
                    'name': bf.name,
                    'description': bf.description,
                    'keywords': bf.keywords
                } for bf in business_functions
            ]
        }
        
        return JsonResponse(data)
        
    except Client.DoesNotExist:
        return JsonResponse({'error': 'Van der Meulen Vastgoed not found'}, status=404)

@csrf_exempt
@require_http_methods(["POST"])
def test_roi_analysis(request):
    """Test Portfolio ROI Analysis function"""
    try:
        data = json.loads(request.body)
        user_input = data.get('question', '')
        
        # Simulate AI response for now
        response = f"""
        🏢 Van der Meulen Vastgoed - Portfolio ROI Analyse
        
        Vraag: {user_input}
        
        📊 Portfolio Overzicht:
        • Totaal aantal panden: 4
        • Totale waarde: €1.850.000
        • Gemiddeld rendement: 5.8%
        
        🏠 Top Performers:
        1. Kerkstraat 25: 6.8% ROI (€28.800 jaar inkomsten)
        2. Industrieweg 8: 6.2% ROI (€45.600 jaar inkomsten)
        3. Hoofdstraat 12: 5.1% ROI (€22.400 jaar inkomsten)
        4. Parkstraat 4: 3.2% ROI (€15.200 jaar inkomsten)
        
        💡 Aanbevelingen:
        • Parkstraat 4: Overwegen verkoop (laag rendement)
        • Kerkstraat 25: Behouden (beste performer)
        • Industrieweg 8: Uitbreiden in dit gebied
        
        Gebaseerd op: Financiële data, marktanalyse en pand specifieke informatie
        """
        
        return JsonResponse({
            'response': response,
            'function_used': 'Portfolio ROI Analysis',
            'client': 'Van der Meulen Vastgoed'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)