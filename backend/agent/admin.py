# backend/agent/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Client, ClientUser, Property, Tenant, Payment, MaintenanceTask,
    ClientTable, ClientKnowledgeBase, AgentAction, AgentConfig
)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'subdomain', 'industry', 'is_active', 'created_at')
    list_filter = ('industry', 'is_active', 'created_at')
    search_fields = ('name', 'subdomain')
    readonly_fields = ('id', 'created_at')

@admin.register(ClientUser)
class ClientUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'role', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('user__username', 'client__name')

# =============================================================================
# VASTGOED ADMIN
# =============================================================================

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('address', 'client', 'property_type', 'monthly_rent', 'current_roi_display', 'purchase_date')
    list_filter = ('client', 'property_type', 'purchase_date')
    search_fields = ('address', 'client__name')
    readonly_fields = ('created_at', 'current_roi_display')
    
    def current_roi_display(self, obj):
        roi = obj.current_roi
        color = 'green' if roi >= 5 else 'orange' if roi >= 3 else 'red'
        return format_html(
            '<span style="color: {};">{:.2f}%</span>',
            color, roi
        )
    current_roi_display.short_description = 'Huidige ROI'

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'property', 'monthly_rent', 'status', 'contract_start', 'contract_end')
    list_filter = ('status', 'contract_start', 'property__client')
    search_fields = ('name', 'email', 'property__address')
    readonly_fields = ('created_at',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'amount', 'due_date', 'status', 'days_overdue_display', 'paid_date')
    list_filter = ('status', 'due_date', 'tenant__property__client')
    search_fields = ('tenant__name', 'tenant__property__address')
    readonly_fields = ('created_at', 'days_overdue_display')
    
    def days_overdue_display(self, obj):
        days = obj.days_overdue
        if days == 0:
            return format_html('<span style="color: green;">Op tijd</span>')
        elif days <= 7:
            return format_html('<span style="color: orange;">{} dagen</span>', days)
        else:
            return format_html('<span style="color: red; font-weight: bold;">{} dagen</span>', days)
    days_overdue_display.short_description = 'Achterstallig'

@admin.register(MaintenanceTask)
class MaintenanceTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'property', 'priority', 'status', 'scheduled_date', 'estimated_cost')
    list_filter = ('priority', 'status', 'scheduled_date', 'property__client')
    search_fields = ('title', 'description', 'property__address')
    readonly_fields = ('created_at',)

# =============================================================================
# DYNAMIC DATABASE ADMIN
# =============================================================================

@admin.register(ClientTable)
class ClientTableAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'client', 'table_name', 'row_count', 'created_at')
    list_filter = ('client', 'created_at')
    search_fields = ('display_name', 'table_name', 'original_filename')
    readonly_fields = ('created_at', 'supabase_table_name')

@admin.register(ClientKnowledgeBase)
class ClientKnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'document_type', 'is_active', 'created_at')
    list_filter = ('document_type', 'is_active', 'created_at', 'client')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at',)

# =============================================================================
# AGENT ADMIN
# =============================================================================

@admin.register(AgentAction)
class AgentActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'action_type', 'status', 'requires_approval', 'created_at')
    list_filter = ('action_type', 'status', 'requires_approval', 'created_at')
    search_fields = ('title', 'description', 'client__name')
    readonly_fields = ('created_at',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('client', 'approved_by')

@admin.register(AgentConfig)
class AgentConfigAdmin(admin.ModelAdmin):
    list_display = ('client', 'agent_name', 'monitoring_frequency', 'auto_approval_threshold')
    list_filter = ('monitoring_frequency',)
    search_fields = ('client__name', 'agent_name')
    readonly_fields = ('created_at',)