# backend/setup_vandermeulen.py
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from agent.models import Client, ClientKnowledgeBase, AgentAction

def setup_vandermeulen_vastgoed():
    # 1. Create client
    client, created = Client.objects.get_or_create(
        subdomain="vandermeulen",
        defaults={
            "name": "Van der Meulen Vastgoed",
        }
    )
    
    if created:
        print(f"✅ Client created: {client.name}")
    else:
        print(f"📁 Client exists: {client.name}")
    
    # 2. Create knowledge bases (folders)
    knowledge_bases = [
        {
            "name": "Contracten & Huurovereenkomsten",
            "description": "Alle huurcontracten, koopcontracten en juridische documenten"
        },
        {
            "name": "Financiële Administratie", 
            "description": "Facturen, betalingen, ROI rapporten, belastingdocumenten"
        },
        {
            "name": "Pand Informatie",
            "description": "Technische specificaties, foto's, taxaties, onderhoudsgeschiedenis"
        },
        {
            "name": "Markt Analyse",
            "description": "Marktprijzen, concurrentie analyse, waarderingen"
        }
    ]
    
    for kb_data in knowledge_bases:
        kb, created = ClientKnowledgeBase.objects.get_or_create(
            client=client,
            name=kb_data["name"],
            defaults={"description": kb_data["description"]}
        )
        if created:
            print(f"✅ Knowledge base created: {kb.name}")
    
    # 3. Create business functions
    business_functions = [
        {
            "name": "Portfolio ROI Analysis",
            "description": "Analyseer rendement en ROI per pand of voor hele portfolio",
            "keywords": ["roi", "rendement", "opbrengst", "winst", "verlies", "investering", "return"],
            "prompt_template": """Je bent een vastgoed finance expert voor Van der Meulen Vastgoed. 
            Analyseer de ROI en rendement op basis van de beschikbare financiële data en pand informatie.
            
            Gegeven vraag: {user_input}
            Relevante documenten: {context}
            
            Geef een concrete analyse met:
            - ROI percentage per pand
            - Vergelijking met andere panden  
            - Aanbevelingen voor verbetering
            - Concrete cijfers en berekeningen"""
        },
        {
            "name": "Huurder Management",
            "description": "Beheer huurders, contracten, betalingen en communicatie",
            "keywords": ["huurder", "huur", "betaling", "contract", "factuur", "achterstand"],
            "prompt_template": """Je bent een huurder management specialist voor Van der Meulen Vastgoed.
            Help met alle aspecten van huurder beheer en administratie.
            
            Gegeven vraag: {user_input}
            Relevante documenten: {context}
            
            Geef praktische hulp met:
            - Huurder informatie en status
            - Betalingsoverzichten
            - Contract details
            - Communicatie templates"""
        },
        {
            "name": "Vastgoed Waardebepaling",
            "description": "Bepaal marktwaarde en optimale verkoop/verhuur prijzen",
            "keywords": ["waarde", "prijs", "taxatie", "verkoop", "verhuur", "markt"],
            "prompt_template": """Je bent een vastgoed taxatie expert voor Van der Meulen Vastgoed.
            Analyseer vastgoed waarden en marktposities.
            
            Gegeven vraag: {user_input}
            Relevante documenten: {context}
            
            Geef waardebepaling met:
            - Huidige marktwaarde schatting
            - Vergelijking met vergelijkbare panden
            - Optimale timing voor verkoop/verhuur
            - Prijs aanbevelingen"""
        },
        {
            "name": "Onderhoudsplanning",
            "description": "Plan preventief onderhoud en beheer kosten",
            "keywords": ["onderhoud", "reparatie", "renovatie", "kosten", "planning"],
            "prompt_template": """Je bent een vastgoed onderhoud specialist voor Van der Meulen Vastgoed.
            Help met onderhoudsplanning en kostenbeheer.
            
            Gegeven vraag: {user_input}
            Relevante documenten: {context}
            
            Geef onderhoud advies met:
            - Prioritering van werkzaamheden
            - Kostenschattingen
            - Preventieve planning
            - Aannemer vergelijkingen"""
        }
    ]
    
    for func_data in business_functions:
        func, created = AgentAction.objects.get_or_create(
            client=client,
            name=func_data["name"],
            defaults={
                "description": func_data["description"],
                "keywords": func_data["keywords"],
                "prompt_template": func_data["prompt_template"]
            }
        )
        if created:
            print(f"✅ Business function created: {func.name}")
    
    print(f"\n🎉 Van der Meulen Vastgoed setup complete!")
    print(f"📁 Client ID: {client.id}")
    print(f"🌐 Subdomain: {client.subdomain}.vdmnexus.com")
    print(f"📚 Knowledge bases: {ClientKnowledgeBase.objects.filter(client=client).count()}")
    print(f"⚙️ Business functions: {AgentAction.objects.filter(client=client).count()}")

if __name__ == "__main__":
    setup_vandermeulen_vastgoed()