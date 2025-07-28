from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from agent.models import Client, ClientKnowledgeBase, AgentAction, AgentConfig
import json

def api_vandermeulen(request):
    try:
        client = Client.objects.get(subdomain="vandermeulen")
        knowledge_bases = ClientKnowledgeBase.objects.filter(client=client)
        business_functions = AgentAction.objects.filter(client=client)
        documents = ClientKnowledgeBase.objects.filter(knowledge_base__client=client)
        
        return JsonResponse({
            'status': 'success',
            'client': {
                'name': client.name,
                'subdomain': client.subdomain,
                'id': str(client.id)
            },
            'knowledge_bases': [
                {
                    'id': str(kb.id), 
                    'name': kb.name, 
                    'description': kb.description,
                    'document_count': ClientKnowledgeBase.objects.filter(knowledge_base=kb).count()
                } for kb in knowledge_bases
            ],
            'business_functions': [
                {
                    'id': str(bf.id), 
                    'name': bf.name, 
                    'description': bf.description,
                    'keywords': bf.keywords
                } for bf in business_functions
            ],
            'documents': [
                {
                    'id': str(doc.id),
                    'filename': doc.filename,
                    'type': doc.file_type,
                    'knowledge_base': doc.knowledge_base.name,
                    'uploaded_at': doc.uploaded_at.isoformat()
                } for doc in documents
            ]
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

@csrf_exempt
@require_http_methods(["POST"])
def upload_document(request):
    try:
        data = json.loads(request.body)
        filename = data.get('filename')
        knowledge_base_id = data.get('knowledge_base_id')
        
        if not filename or not knowledge_base_id:
            return JsonResponse({'status': 'error', 'message': 'filename and knowledge_base_id required'})
        
        kb = ClientKnowledgeBase.objects.get(id=knowledge_base_id)
        
        # Simulate document processing
        doc = ClientKnowledgeBase.objects.create(
            knowledge_base=kb,
            filename=filename,
            file_type=filename.split('.')[-1] if '.' in filename else 'unknown',
            file_path=f"/uploads/{kb.client.subdomain}/{kb.name}/{filename}",
            processed=True
        )
        
        return JsonResponse({
            'status': 'success',
            'message': f'Document "{filename}" uploaded to {kb.name}',
            'document': {
                'id': str(doc.id),
                'filename': doc.filename,
                'knowledge_base': kb.name
            }
        })
        
    except ClientKnowledgeBase.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Knowledge base not found'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

@csrf_exempt
@require_http_methods(["POST"])
def test_business_function(request):
    try:
        data = json.loads(request.body)
        function_name = data.get('function_name')
        user_question = data.get('question', 'Algemene analyse vraag')
        
        # Get Van der Meulen client
        client = Client.objects.get(subdomain="vandermeulen")
        
        # Simulate AI responses based on function
        responses = {
            "Portfolio ROI Analysis": f"""
🏢 Van der Meulen Vastgoed - Portfolio ROI Analyse

Vraag: {user_question}

📊 Portfolio Overzicht (2025):
- Totaal aantal panden: 4
- Totale waarde: €1.850.000
- Gemiddeld rendement: 5.8%
- Totale maandelijkse huur: €4.800

🏠 Pand Performance:
1. Kerkstraat 25: 6.8% ROI (€1.200/maand)
   - Aankoopprijs: €385.000, Huidige waarde: €420.000
   - Status: Top performer, behouden
   
2. Industrieweg 8: 6.2% ROI (€2.100/maand)  
   - Aankoopprijs: €740.000, Huidige waarde: €825.000
   - Status: Commercieel, sterke groei
   
3. Hoofdstraat 12: 5.1% ROI (€850/maand)
   - Aankoopprijs: €310.000, Huidige waarde: €340.000
   - Status: Gemiddeld, stabiel
   
4. Parkstraat 4: 3.2% ROI (€650/maand)
   - Aankoopprijs: €280.000, Huidige waarde: €285.000
   - Status: Onderpresterend

💡 Strategische Aanbevelingen:
- Verkoop Parkstraat 4 (laag rendement + minimale waardegroei)
- Behoud Kerkstraat 25 & Industrieweg 8 (beste performers)
- Overweeg renovatie Hoofdstraat 12 voor hogere huur

📈 Marktcontext: +8.2% waardestijging dit jaar in jouw gebied
✅ Gebaseerd op: Financiële administratie, marktdata, pand specifieke informatie
            """,
            
            "Huurder Management": f"""
👥 Van der Meulen Vastgoed - Huurder Management

Vraag: {user_question}

📋 Huidige Huurders Status (Januari 2025):
- Familie van der Berg (Hoofdstraat 12): €850/maand
  - Contract: Tot 31-12-2025
  - Status: ✅ Altijd op tijd betaald
  - Laatste betaling: 15-01-2025
  
- M. Janssen (Kerkstraat 25): €1.200/maand
  - Contract: Tot 30-06-2026  
  - Status: ⚠️ 3 dagen achterstand (januari huur)
  - Actie: Vriendelijke herinnering verstuurd
  
- TechStart B.V. (Industrieweg 8): €2.100/maand
  - Contract: Tot 31-03-2027
  - Status: ✅ Automatische incasso actief
  - Laatste betaling: 01-01-2025
  
- Familie de Wit (Parkstraat 4): €650/maand
  - Contract: Tot 30-09-2025
  - Status: ✅ Betrouwbare huurders
  - Opzegtermijn: Let op verlenging Q3

💰 Financieel Overzicht:
- Totale maand inkomsten: €4.800
- Openstaand bedrag: €1.200 (M. Janssen)
- Gemiddelde betaaltermijn: 2.1 dagen
- Leegstand percentage: 0%

📊 Actiepunten:
- Follow-up M. Janssen (dag 5 achterstand)
- Contract verlenging Familie de Wit voorbereiden
- Jaarlijkse huurverhoging Hoofdstraat 12 overwegen (+2.3%)

✅ Gebaseerd op: Contract database, betalingshistorie, communicatie logs
            """,
            
            "Vastgoed Waardebepaling": f"""
🏠 Van der Meulen Vastgoed - Waardebepaling & Marktanalyse

Vraag: {user_question}

📈 Actuele Marktwaarden (Januari 2025):

1. Kerkstraat 25 (Woonhuis)
   - Aankoopprijs (2022): €385.000
   - Huidige waarde: €420.000 (+9.1%)
   - WOZ waarde 2025: €415.000
   - Markttrend: +3.2% dit jaar
   - Advies: ❌ Niet verkopen, sterke wijk

2. Industrieweg 8 (Commercieel)  
   - Aankoopprijs (2021): €740.000
   - Huidige waarde: €825.000 (+11.5%)
   - Markthuur: €25-28/m²
   - Trend: +8% vraag naar kantoorruimte
   - Advies: ❌ Behouden, groeigebied

3. Hoofdstraat 12 (Woonhuis)
   - Aankoopprijs (2023): €310.000  
   - Huidige waarde: €340.000 (+9.7%)
   - Vergelijkbare verkopen: €335k-€350k
   - Renovatiepotentieel: +€25k waarde
   - Advies: 🔄 Renoveren of verkopen

4. Parkstraat 4 (Woonhuis)
   - Aankoopprijs (2020): €280.000
   - Huidige waarde: €285.000 (+1.8%)
   - Marktpositie: Ondergemiddeld
   - Onderhoudskosten: Hoog (oud pand)
   - Advies: ✅ Verkopen Q2 2025

🎯 Verkoop Strategie 2025:
- Parkstraat 4: Verkopen voor €290k (5 biedingen verwacht)
- Opbrengst investeren in renovatie Hoofdstraat 12
- Portfolio focus op Kerkstraat + Industrieweg

📊 Marktcontext:
- Gemeente groeiplannen: +15% nieuwbouw 2025-2027
- Renteontwikkeling: Stabiel rond 4.2%
- Koopkracht: +2.1% in doelgroep

✅ Gebaseerd op: Funda data, makelaar rapporten, gemeente informatie
            """,
            
            "Onderhoudsplanning": f"""
🔧 Van der Meulen Vastgoed - Onderhoudsplanning 2025

Vraag: {user_question}

🚨 URGENT (binnen 2 weken):
- Hoofdstraat 12: Lekkage badkamer reparatie
  - Geschatte kosten: €2.800
  - Aannemer: Bouwbedrijf Jansen (offerte klaar)
  - Impact: Vochtschade preventie kritiek
  - Doorberekening: 70% aan huurder mogelijk

- Industrieweg 8: CV ketel vervanging  
  - Geschatte kosten: €4.200 (HR++ ketel)
  - Energiebesparing: €800/jaar
  - Planning: Week 6-7 (buiten kantooruren)
  - ROI: 5.2 jaar

⚠️ BELANGRIJK (binnen 2 maanden):
- Kerkstraat 25: Schilderwerk buitenkant
  - Geschatte kosten: €6.500
  - Laatste keer: 2019 (6 jaar geleden)
  - Preventief tegen houtworm/weer
  - Planning: Maart-April (droog weer)

- Parkstraat 4: Elektrische installatie check
  - Geschatte kosten: €1.800 (update + check)
  - Verplicht voor verkoop 2025
  - Energielabel verbetering: E → C mogelijk
  - Waardestijging: +€8.000

📅 PREVENTIEF (binnen 6 maanden):
- Alle panden: Jaarlijkse inspectie €400
- Industrieweg 8: Dakbedekking check €600
- Hoofdstraat 12: Tuin onderhoud €300

💰 Budget Planning 2025:
- Totaal onderhoud: €16.600
- Urgente werkzaamheden: €7.000 (42%)
- Preventief onderhoud: €1.300 (8%)
- Waarde-toevoegende investeringen: €8.300 (50%)

🎯 Prioritering:
1. Hoofdstraat 12 lekkage (schade preventie)
2. Industrieweg 8 CV ketel (huurder comfort)
3. Parkstraat 4 elektra (verkoop voorbereiding)
4. Kerkstraat 25 schilderwerk (waardevehoud)

📊 Aannemer Vergelijking:
- Bouwbedrijf Jansen: €2.800 (bekend, betrouwbaar)
- Installatiebedrijf Peters: €4.200 (specialiteit CV)
- Schilderbedrijf Willems: €6.500 (5-jaar garantie)

✅ Gebaseerd op: Onderhoudshistorie, aannemers offertes, prioriteitsmatrix
            """
        }
        
        response_text = responses.get(function_name, f"Functie '{function_name}' nog niet geïmplementeerd voor Van der Meulen Vastgoed.")
        
        return JsonResponse({
            'status': 'success',
            'response': response_text,
            'function_used': function_name,
            'client': client.name,
            'timestamp': '2025-01-27T16:30:00Z'
        })
        
    except Client.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Van der Meulen Vastgoed not found'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vandermeulen', api_vandermeulen),
    path('api/upload', upload_document),
    path('api/test-function', test_business_function),
]