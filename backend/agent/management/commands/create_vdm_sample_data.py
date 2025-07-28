# backend/agent/management/commands/create_vdm_sample_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from datetime import date, timedelta
import random
from decimal import Decimal

from agent.models import (
    Client, ClientUser, Property, Tenant, Payment, MaintenanceTask, AgentConfig
)

class Command(BaseCommand):
    help = 'Creëert sample data voor Van der Meulen Vastgoed'

    def handle(self, *args, **options):
        self.stdout.write('Creëren Van der Meulen sample data...')
        
        # 1. Client aanmaken
        client, created = Client.objects.get_or_create(
            subdomain='vandermeulen',
            defaults={
                'name': 'Van der Meulen Vastgoed',
                'industry': 'vastgoed',
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Client aangemaakt: {client.name}')
        else:
            self.stdout.write(f'ℹ️ Client bestaat al: {client.name}')
        
        # 2. Admin user aanmaken
        admin_user, created = User.objects.get_or_create(
            username='vdm_admin',
            defaults={
                'email': 'admin@vandermeulen.nl',
                'first_name': 'Van der Meulen',
                'last_name': 'Admin',
                'is_staff': True,
                'is_superuser': False
            }
        )
        
        if created:
            admin_user.set_password('vdm123!')
            admin_user.save()
            self.stdout.write(f'✅ Admin user aangemaakt: {admin_user.username}')
        
        # User koppelen aan client
        ClientUser.objects.get_or_create(
            user=admin_user,
            client=client,
            defaults={'role': 'admin'}
        )
        
        # 3. Agent configuratie
        agent_config, created = AgentConfig.objects.get_or_create(
            client=client,
            defaults={
                'agent_name': 'VDM Business Assistent',
                'agent_personality': 'Professionele, Nederlandse vastgoed expert. Spreekt informeel maar respectvol. Focus op ROI optimalisatie en risicomanagement.',
                'monitoring_frequency': 'daily',
                'auto_approval_threshold': Decimal('500.00'),
                'business_rules': {
                    'payment_overdue_threshold': 7,
                    'urgent_overdue_threshold': 30,
                    'minimum_roi_threshold': 4.0,
                    'maintenance_budget_per_property': 2000
                },
                'notification_settings': {
                    'email_notifications': True,
                    'overdue_payments': True,
                    'maintenance_alerts': True,
                    'roi_warnings': True
                }
            }
        )
        
        # 4. Properties aanmaken
        properties_data = [
            {
                'address': 'Kerkstraat 15, 1234 AB Amsterdam',
                'property_type': 'apartment',
                'purchase_price': Decimal('285000'),
                'current_value': Decimal('310000'),
                'monthly_rent': Decimal('1450'),
                'purchase_date': date(2019, 3, 15)
            },
            {
                'address': 'Hoofdstraat 89, 1234 CD Rotterdam',
                'property_type': 'house',
                'purchase_price': Decimal('420000'),
                'current_value': Decimal('465000'),
                'monthly_rent': Decimal('1850'),
                'purchase_date': date(2020, 7, 22)
            },
            {
                'address': 'Marktplein 7A, 1234 EF Utrecht',
                'property_type': 'apartment',
                'purchase_price': Decimal('195000'),
                'current_value': Decimal('215000'),
                'monthly_rent': Decimal('1150'),
                'purchase_date': date(2018, 11, 8)
            },
            {
                'address': 'Wilhelminastraat 45, 1234 GH Den Haag',
                'property_type': 'commercial',
                'purchase_price': Decimal('750000'),
                'current_value': Decimal('825000'),
                'monthly_rent': Decimal('3200'),
                'purchase_date': date(2021, 1, 10)
            },
            {
                'address': 'Parkweg 12, 1234 IJ Eindhoven',
                'property_type': 'apartment',
                'purchase_price': Decimal('165000'),
                'current_value': Decimal('178000'),
                'monthly_rent': Decimal('925'),
                'purchase_date': date(2017, 5, 30)
            }
        ]
        
        properties = []
        for prop_data in properties_data:
            prop, created = Property.objects.get_or_create(
                client=client,
                address=prop_data['address'],
                defaults=prop_data
            )
            properties.append(prop)
            if created:
                self.stdout.write(f'✅ Property aangemaakt: {prop.address}')
        
        # 5. Tenants aanmaken
        tenants_data = [
            {
                'name': 'Familie Jansen',
                'email': 'jansen@email.com',
                'phone': '06-12345678',
                'contract_start': date(2022, 1, 1),
                'deposit': Decimal('2900')
            },
            {
                'name': 'M. de Vries',
                'email': 'devries@email.com',
                'phone': '06-87654321',
                'contract_start': date(2021, 8, 15),
                'deposit': Decimal('3700')
            },
            {
                'name': 'Stichting Zonnebloem',
                'email': 'contact@zonnebloem.nl',
                'phone': '030-1234567',
                'contract_start': date(2023, 3, 1),
                'deposit': Decimal('2300')
            },
            {
                'name': 'TechStart BV',
                'email': 'info@techstart.nl',
                'phone': '070-9876543',
                'contract_start': date(2021, 6, 1),
                'deposit': Decimal('6400')
            },
            {
                'name': 'Student R. Bakker',
                'email': 'r.bakker@student.nl',
                'phone': '06-55555555',
                'contract_start': date(2023, 9, 1),
                'deposit': Decimal('1850')
            }
        ]
        
        tenants = []
        for i, tenant_data in enumerate(tenants_data):
            if i < len(properties):
                tenant_data['property'] = properties[i]
                tenant_data['monthly_rent'] = properties[i].monthly_rent
                
                tenant, created = Tenant.objects.get_or_create(
                    property=properties[i],
                    name=tenant_data['name'],
                    defaults=tenant_data
                )
                tenants.append(tenant)
                if created:
                    self.stdout.write(f'✅ Tenant aangemaakt: {tenant.name}')
        
        # 6. Payments aanmaken (laatste 6 maanden)
        self.stdout.write('Creëren payment history...')
        today = date.today()
        
        for tenant in tenants:
            # Laatste 6 maanden payments
            for month_offset in range(6, 0, -1):
                due_date = today.replace(day=1) - timedelta(days=month_offset * 30)
                
                # Sommige payments zijn on-time, sommige te laat
                payment_status = random.choices(
                    ['paid', 'paid', 'paid', 'overdue', 'paid'],
                    weights=[30, 25, 20, 15, 10]
                )[0]
                
                paid_date = None
                if payment_status == 'paid':
                    # Betaald tussen -5 en +10 dagen van due date
                    days_diff = random.randint(-5, 10)
                    paid_date = due_date + timedelta(days=days_diff)
                
                Payment.objects.get_or_create(
                    tenant=tenant,
                    due_date=due_date,
                    defaults={
                        'amount': tenant.monthly_rent,
                        'paid_date': paid_date,
                        'paid_amount': tenant.monthly_rent if payment_status == 'paid' else None,
                        'status': payment_status
                    }
                )
            
            # Huidige maand payment (sommige nog pending)
            current_due = today.replace(day=1)
            current_status = random.choices(['paid', 'pending', 'overdue'], weights=[60, 30, 10])[0]
            
            Payment.objects.get_or_create(
                tenant=tenant,
                due_date=current_due,
                defaults={
                    'amount': tenant.monthly_rent,
                    'status': current_status,
                    'paid_date': current_due - timedelta(days=2) if current_status == 'paid' else None,
                    'paid_amount': tenant.monthly_rent if current_status == 'paid' else None
                }
            )
        
        # 7. Maintenance Tasks aanmaken
        maintenance_tasks = [
            {
                'title': 'Jaarlijkse CV keuring',
                'description': 'Verplichte jaarlijkse keuring van CV installatie volgens NEN3378',
                'priority': 'medium',
                'status': 'planned',
                'estimated_cost': Decimal('150'),
                'scheduled_date': today + timedelta(days=15)
            },
            {
                'title': 'Lekkage badkamer repareren',
                'description': 'Tenant meldt lekkage bij douche. Loodgieter inschakelen.',
                'priority': 'high',
                'status': 'in_progress',
                'estimated_cost': Decimal('450'),
                'scheduled_date': today + timedelta(days=2)
            },
            {
                'title': 'Schilderwerk hal en trap',
                'description': 'Schilderwerk gemeenschappelijke ruimtes na 5 jaar',
                'priority': 'low',
                'status': 'planned',
                'estimated_cost': Decimal('1200'),
                'scheduled_date': today + timedelta(days=45)
            }
        ]
        
        for i, task_data in enumerate(maintenance_tasks):
            if i < len(properties):
                task_data['property'] = properties[i]
                
                MaintenanceTask.objects.get_or_create(
                    property=properties[i],
                    title=task_data['title'],
                    defaults=task_data
                )
        
        self.stdout.write(self.style.SUCCESS('✅ Van der Meulen sample data succesvol aangemaakt!'))
        self.stdout.write('')
        self.stdout.write('Login credentials:')
        self.stdout.write(f'Username: vdm_admin')
        self.stdout.write(f'Password: vdm123!')
        self.stdout.write(f'Subdomain: vandermeulen.vdmnexus.com')
        self.stdout.write('')
        self.stdout.write('Dashboard statistieken:')
        self.stdout.write(f'- {len(properties)} Properties')
        self.stdout.write(f'- {len(tenants)} Tenants')
        self.stdout.write(f'- {Payment.objects.filter(tenant__property__client=client).count()} Payments')
        self.stdout.write(f'- {MaintenanceTask.objects.filter(property__client=client).count()} Maintenance Tasks')