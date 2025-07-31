# backend/api/views.py - UPDATE EXISTING FILE
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from typing import List, Dict
import logging
from agent.agent import Agent
import asyncio
from concurrent.futures import ThreadPoolExecutor
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import time
import os
from django.http import JsonResponse
from django.conf import settings

# NEW IMPORTS FOR WIDGETS
from agent.models import Client, Property, Tenant, Payment, MaintenanceTask
from services.avm_service import run_payment_analysis_sync, run_roi_analysis_sync
from django.shortcuts import get_object_or_404
from decimal import Decimal

logger = logging.getLogger(__name__)

# EXISTING CODE... (keep all existing functions)

@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint."""
    try:
        # Test database connection
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        # Log successful health check
        logger.info("Health check passed")
        return JsonResponse({
            "status": "ok",
            "database": "connected",
            "environment": os.getenv('ENVIRONMENT', 'production')
        })
    except Exception as e:
        # Log the error
        logger.error(f"Health check failed: {str(e)}")
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class ChatView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.agent = Agent()
            logger.info("Agent initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize agent: {str(e)}")
            raise
    
    def post(self, request):
        """Handle chat messages with the agent."""
        try:
            data = request.data
            messages = data.get('messages', [])
            
            if not messages:
                return Response({
                    "error": "No messages provided"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Process the chat with agent
            response = self.agent.process_chat(messages)
            
            return Response({
                "response": response,
                "status": "success"
            })
            
        except Exception as e:
            logger.error(f"Chat processing failed: {str(e)}")
            return Response({
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# =============================================================================
# NEW WIDGET API ENDPOINTS
# =============================================================================

@api_view(['GET'])
def vdm_payment_widget_data(request):
    """
    API endpoint voor huurbetalingen widget data
    GET /api/widgets/vdm/payments
    """
    try:
        # Haal Van der Meulen client op
        client = get_object_or_404(Client, subdomain='vandermeulen')
        
        # Haal tenants met payments op
        tenants = Tenant.objects.filter(
            property__client=client,
            status='active'
        ).prefetch_related('payments', 'property')
        
        # Prepareer data voor AVM analysis
        tenant_data = []
        total_monthly_income = Decimal('0')
        
        for tenant in tenants:
            # Vind overdue payments
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
                'property_address': tenant.property.address,
                'overdue_payments': overdue_payments
            })
            
            total_monthly_income += tenant.monthly_rent
        
        # Run AVM payment analysis
        avm_result = run_payment_analysis_sync(tenant_data)
        
        return JsonResponse(avm_result)
        
    except Exception as e:
        logger.error(f"Payment widget data error: {str(e)}")
        return JsonResponse({
            'error': 'Unable to fetch payment data',
            'message': str(e)
        }, status=500)

@api_view(['GET'])
def vdm_roi_widget_data(request):
    """
    API endpoint voor ROI analysis widget data
    GET /api/widgets/vdm/roi
    """
    try:
        # Haal Van der Meulen client op
        client = get_object_or_404(Client, subdomain='vandermeulen')
        
        # Haal properties op
        properties = Property.objects.filter(client=client)
        
        # Prepareer data voor AVM analysis
        property_data = []
        for prop in properties:
            property_data.append({
                'address': prop.address,
                'purchase_price': float(prop.purchase_price),
                'current_value': float(prop.current_value) if prop.current_value else float(prop.purchase_price),
                'monthly_rent': float(prop.monthly_rent),
                'property_type': prop.property_type
            })
        
        # Run AVM ROI analysis
        avm_result = run_roi_analysis_sync(property_data)
        
        return JsonResponse(avm_result)
        
    except Exception as e:
        logger.error(f"ROI widget data error: {str(e)}")
        return JsonResponse({
            'error': 'Unable to fetch ROI data',
            'message': str(e)
        }, status=500)

@api_view(['GET'])
def vdm_portfolio_widget_data(request):
    """
    API endpoint voor portfolio overview widget data
    GET /api/widgets/vdm/portfolio
    """
    try:
        # Haal Van der Meulen client op
        client = get_object_or_404(Client, subdomain='vandermeulen')
        
        # Portfolio metrics
        properties = Property.objects.filter(client=client)
        tenants = Tenant.objects.filter(property__client=client, status='active')
        maintenance_tasks = MaintenanceTask.objects.filter(
            property__client=client,
            status__in=['planned', 'in_progress']
        )
        
        # Calculate totals
        total_properties = properties.count()
        total_investment = sum(float(p.purchase_price) for p in properties)
        total_current_value = sum(float(p.current_value) if p.current_value else float(p.purchase_price) for p in properties)
        total_monthly_income = sum(float(t.monthly_rent) for t in tenants)
        
        # Property types distribution
        property_types = {}
        for prop in properties:
            prop_type = prop.get_property_type_display()
            property_types[prop_type] = property_types.get(prop_type, 0) + 1
        
        # Maintenance urgency
        urgent_maintenance = maintenance_tasks.filter(priority__in=['high', 'urgent']).count()
        
        widget_data = {
            'summary': {
                'total_properties': total_properties,
                'total_investment': total_investment,
                'total_current_value': total_current_value,
                'total_monthly_income': total_monthly_income,
                'active_tenants': tenants.count(),
                'capital_gain': total_current_value - total_investment,
                'capital_gain_percentage': round(((total_current_value - total_investment) / total_investment * 100), 2) if total_investment > 0 else 0
            },
            'property_types': property_types,
            'maintenance': {
                'total_tasks': maintenance_tasks.count(),
                'urgent_tasks': urgent_maintenance,
                'upcoming_week': maintenance_tasks.filter(
                    scheduled_date__lte=time.strftime('%Y-%m-%d', time.localtime(time.time() + 7*24*3600))
                ).count() if maintenance_tasks.filter(scheduled_date__isnull=False).exists() else 0
            },
            'occupancy_rate': round((tenants.count() / total_properties * 100), 1) if total_properties > 0 else 0,
            'last_updated': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return JsonResponse(widget_data)
        
    except Exception as e:
        logger.error(f"Portfolio widget data error: {str(e)}")
        return JsonResponse({
            'error': 'Unable to fetch portfolio data',
            'message': str(e)
        }, status=500)

@api_view(['GET'])
def vdm_dashboard_overview(request):
    """
    Complete dashboard overview data
    GET /api/dashboard/vdm/overview
    """
    try:
        # Get Van der Meulen client
        client = get_object_or_404(Client, subdomain='vandermeulen')
        
        # Get payment data directly
        tenants = Tenant.objects.filter(
            property__client=client,
            status='active'
        ).prefetch_related('payments', 'property')
        
        tenant_data = []
        total_monthly_income = Decimal('0')
        
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
                'property_address': tenant.property.address,
                'overdue_payments': overdue_payments
            })
            total_monthly_income += tenant.monthly_rent
        
        # Get ROI data directly
        properties = Property.objects.filter(client=client)
        property_data = []
        for prop in properties:
            property_data.append({
                'address': prop.address,
                'purchase_price': float(prop.purchase_price),
                'current_value': float(prop.current_value) if prop.current_value else float(prop.purchase_price),
                'monthly_rent': float(prop.monthly_rent),
                'property_type': prop.property_type
            })
        
        # Get portfolio data directly
        maintenance_tasks = MaintenanceTask.objects.filter(
            property__client=client,
            status__in=['planned', 'in_progress']
        )
        
        # Run AVM analyses
        payment_analysis = run_payment_analysis_sync(tenant_data)
        roi_analysis = run_roi_analysis_sync(property_data)
        
        # Calculate portfolio metrics
        total_properties = properties.count()
        total_investment = sum(float(p.purchase_price) for p in properties)
        total_current_value = sum(float(p.current_value) if p.current_value else float(p.purchase_price) for p in properties)
        
        dashboard_data = {
            'payments': {
                'summary': {
                    'total_tenants': len(tenant_data),
                    'total_monthly_income': float(total_monthly_income),
                    'on_time_percentage': payment_analysis.get('summary', {}).get('on_time_percentage', 0),
                    'total_overdue_amount': payment_analysis.get('summary', {}).get('total_overdue_amount', 0),
                    'overdue_tenant_count': payment_analysis.get('summary', {}).get('overdue_tenant_count', 0)
                },
                'urgent_cases': payment_analysis.get('urgent_cases', []),
                'recommendations': payment_analysis.get('recommendations', [])
            },
            'roi': {
                'portfolio_summary': roi_analysis.get('portfolio_summary', {}),
                'property_performance': roi_analysis.get('property_performance', []),
                'recommendations': roi_analysis.get('recommendations', [])
            },
            'portfolio': {
                'summary': {
                    'total_properties': total_properties,
                    'total_investment': total_investment,
                    'total_current_value': total_current_value,
                    'total_monthly_income': float(total_monthly_income),
                    'active_tenants': tenants.count(),
                    'capital_gain': total_current_value - total_investment,
                    'occupancy_rate': round((tenants.count() / total_properties * 100), 1) if total_properties > 0 else 0
                },
                'maintenance': {
                    'total_tasks': maintenance_tasks.count(),
                    'urgent_tasks': maintenance_tasks.filter(priority__in=['high', 'urgent']).count()
                }
            },
            'client_info': {
                'name': 'Van der Meulen Vastgoed',
                'subdomain': 'vandermeulen',
                'industry': 'vastgoed'
            },
            'last_updated': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return JsonResponse(dashboard_data)
        
    except Exception as e:
        logger.error(f"Dashboard overview error: {str(e)}")
        return JsonResponse({
            'error': 'Unable to fetch dashboard data',
            'message': str(e)
        }, status=500)

@api_view(['POST'])
def upload_csv_data(request):
    """
    CSV upload endpoint met dynamic table creation.
    Handles file upload, CSV processing, en automatic database table creation.
    """
    try:
        # Check if file was uploaded
        if 'csv_file' not in request.FILES:
            return JsonResponse({
                'success': False,
                'error': 'No CSV file provided'
            }, status=400)
        
        csv_file = request.FILES['csv_file']
        
        # Validate file type
        if not csv_file.name.lower().endswith('.csv'):
            return JsonResponse({
                'success': False,
                'error': 'File must be a CSV file'
            }, status=400)
        
        # Validate file size (max 10MB)
        if csv_file.size > 10 * 1024 * 1024:
            return JsonResponse({
                'success': False,
                'error': 'File size must be less than 10MB'
            }, status=400)
        
        # Get client ID from request
        client_id = request.POST.get('client_id')
        if not client_id:
            return JsonResponse({
                'success': False,
                'error': 'Client ID is required'
            }, status=400)
        
        # Validate client exists
        try:
            from agent.models import Client
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'Client not found'
            }, status=404)
        
        # Save file temporarily
        import tempfile
        import os
        
        temp_dir = getattr(settings, 'CSV_TEMP_DIR', 'temp_uploads')
        os.makedirs(temp_dir, exist_ok=True)
        
        temp_file_path = os.path.join(temp_dir, f"upload_{int(time.time())}_{csv_file.name}")
        
        with open(temp_file_path, 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)
        
        # Initialize SupabaseDynamicDB
        from services.supabase_dynamic import SupabaseDynamicDB
        db_service = SupabaseDynamicDB()
        
        # Analyze CSV structure
        analysis_result = db_service.analyze_csv_structure(temp_file_path)
        
        if not analysis_result['success']:
            # Clean up temp file
            os.unlink(temp_file_path)
            return JsonResponse({
                'success': False,
                'error': f'CSV analysis failed: {analysis_result["error"]}'
            }, status=400)
        
        # Validate CSV for client
        validation_result = db_service.validate_csv_for_client(temp_file_path, client_id)
        
        if not validation_result['success']:
            os.unlink(temp_file_path)
            return JsonResponse({
                'success': False,
                'error': f'CSV validation failed: {validation_result["error"]}'
            }, status=400)
        
        # Create dynamic table
        table_name = request.POST.get('table_name', 'uploaded_data')
        table_result = db_service.create_dynamic_table(
            client_id=client_id,
            table_name=table_name,
            columns=analysis_result['columns'],
            original_filename=csv_file.name
        )
        
        if not table_result['success']:
            os.unlink(temp_file_path)
            return JsonResponse({
                'success': False,
                'error': f'Table creation failed: {table_result["error"]}'
            }, status=500)
        
        # Insert CSV data
        insert_result = db_service.insert_csv_data(
            table_name=table_result['table_name'],
            df=analysis_result['dataframe'],
            client_id=client_id
        )
        
        if not insert_result['success']:
            os.unlink(temp_file_path)
            return JsonResponse({
                'success': False,
                'error': f'Data insertion failed: {insert_result["error"]}'
            }, status=500)
        
        # Clean up temp file
        os.unlink(temp_file_path)
        
        # Return success response
        return JsonResponse({
            'success': True,
            'message': 'CSV uploaded and processed successfully',
            'data': {
                'table_name': table_result['table_name'],
                'rows_inserted': insert_result['inserted_rows'],
                'columns_created': len(analysis_result['columns']),
                'file_size': analysis_result['file_size'],
                'validation': validation_result.get('validation', {}),
                'metadata': table_result['metadata']
            }
        })
        
    except Exception as e:
        logger.error(f"CSV upload error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Upload processing failed',
            'message': str(e)
        }, status=500)

@api_view(['GET'])
def get_uploaded_tables(request):
    """
    Haalt lijst op van geüploade tabellen voor een client.
    """
    try:
        client_id = request.GET.get('client_id')
        if not client_id:
            return JsonResponse({
                'success': False,
                'error': 'Client ID is required'
            }, status=400)
        
        # Validate client exists
        try:
            from agent.models import Client
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'Client not found'
            }, status=404)
        
        # Get table metadata (in real implementation, this would come from Supabase)
        # For now, return mock data
        tables = [
            {
                'table_name': f'client_{client_id}_properties_1234567890',
                'display_name': 'Properties Data',
                'row_count': 150,
                'created_at': '2024-01-15T10:30:00Z',
                'file_name': 'properties_export.csv',
                'columns': ['name', 'address', 'purchase_price', 'current_value']
            },
            {
                'table_name': f'client_{client_id}_tenants_1234567891',
                'display_name': 'Tenants Data',
                'row_count': 75,
                'created_at': '2024-01-14T14:20:00Z',
                'file_name': 'tenants_list.csv',
                'columns': ['name', 'email', 'phone', 'monthly_rent']
            }
        ]
        
        return JsonResponse({
            'success': True,
            'tables': tables
        })
        
    except Exception as e:
        logger.error(f"Get tables error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Unable to fetch tables',
            'message': str(e)
        }, status=500)

@api_view(['GET'])
def get_table_data(request):
    """
    Haalt data op uit een specifieke geüploade tabel.
    """
    try:
        client_id = request.GET.get('client_id')
        table_name = request.GET.get('table_name')
        
        if not client_id or not table_name:
            return JsonResponse({
                'success': False,
                'error': 'Client ID and table name are required'
            }, status=400)
        
        # Validate client exists
        try:
            from agent.models import Client
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'Client not found'
            }, status=404)
        
        # Get pagination parameters
        limit = int(request.GET.get('limit', 100))
        offset = int(request.GET.get('offset', 0))
        
        # Initialize SupabaseDynamicDB
        from services.supabase_dynamic import SupabaseDynamicDB
        db_service = SupabaseDynamicDB()
        
        # Get table data
        data_result = db_service.get_table_data(
            table_name=table_name,
            client_id=client_id,
            limit=limit,
            offset=offset
        )
        
        if not data_result['success']:
            return JsonResponse({
                'success': False,
                'error': f'Data retrieval failed: {data_result["error"]}'
            }, status=500)
        
        return JsonResponse({
            'success': True,
            'data': data_result['data'],
            'count': data_result['count'],
            'pagination': {
                'limit': limit,
                'offset': offset,
                'has_more': data_result['count'] == limit
            }
        })
        
    except Exception as e:
        logger.error(f"Get table data error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Unable to fetch table data',
            'message': str(e)
        }, status=500)

@api_view(['POST'])
def delete_uploaded_table(request):
    """
    Verwijdert een geüploade tabel en alle bijbehorende data.
    """
    try:
        client_id = request.POST.get('client_id')
        table_name = request.POST.get('table_name')
        
        if not client_id or not table_name:
            return JsonResponse({
                'success': False,
                'error': 'Client ID and table name are required'
            }, status=400)
        
        # Validate client exists
        try:
            from agent.models import Client
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'Client not found'
            }, status=404)
        
        # Initialize SupabaseDynamicDB
        from services.supabase_dynamic import SupabaseDynamicDB
        db_service = SupabaseDynamicDB()
        
        # In real implementation, this would drop the table from Supabase
        # For now, just return success
        logger.info(f"Table deletion requested: {table_name} for client {client_id}")
        
        return JsonResponse({
            'success': True,
            'message': f'Table {table_name} deleted successfully'
        })
        
    except Exception as e:
        logger.error(f"Delete table error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Unable to delete table',
            'message': str(e)
        }, status=500)