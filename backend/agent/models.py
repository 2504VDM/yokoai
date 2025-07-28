# backend/agent/models.py
from django.db import models
from django.contrib.auth.models import User
import uuid

class Client(models.Model):
    """Base client model voor multi-tenant platform"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    subdomain = models.CharField(max_length=50, unique=True)
    industry = models.CharField(max_length=50)  # 'vastgoed', 'juridisch', etc.
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.subdomain})"

class ClientUser(models.Model):
    """Koppeling tussen Django users en clients"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, default='user')  # 'admin', 'user'
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'client']

# =============================================================================
# VASTGOED SPECIFIEKE MODELS (VAN DER MEULEN)
# =============================================================================

class Property(models.Model):
    """Vastgoed objecten"""
    PROPERTY_TYPES = [
        ('apartment', 'Appartement'),
        ('house', 'Eengezinswoning'),
        ('commercial', 'Commercieel'),
        ('parking', 'Parkeerplaats'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monthly_rent = models.DecimalField(max_digits=8, decimal_places=2)
    purchase_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.address} - €{self.monthly_rent}/maand"
    
    @property
    def current_roi(self):
        """Berekening van huidige ROI percentage"""
        if self.current_value and self.current_value > 0:
            annual_rent = self.monthly_rent * 12
            return round((annual_rent / self.current_value) * 100, 2)
        return 0

class Tenant(models.Model):
    """Huurders per property"""
    STATUS_CHOICES = [
        ('active', 'Actief'),
        ('notice', 'Opzegging'),
        ('ended', 'Beëindigd'),
    ]
    
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='tenants')
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    contract_start = models.DateField()
    contract_end = models.DateField(null=True, blank=True)
    monthly_rent = models.DecimalField(max_digits=8, decimal_places=2)
    deposit = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.property.address}"

class Payment(models.Model):
    """Huurbetalingen tracking"""
    STATUS_CHOICES = [
        ('pending', 'Wachtend'),
        ('paid', 'Betaald'),
        ('overdue', 'Achterstallig'),
        ('partial', 'Gedeeltelijk'),
    ]
    
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.tenant.name} - €{self.amount} ({self.due_date})"
    
    @property
    def days_overdue(self):
        """Berekening dagen achterstallig"""
        from datetime import date
        if self.status in ['paid'] or not self.due_date:
            return 0
        return max(0, (date.today() - self.due_date).days)

class MaintenanceTask(models.Model):
    """Onderhouds taken"""
    PRIORITY_CHOICES = [
        ('low', 'Laag'),
        ('medium', 'Gemiddeld'),
        ('high', 'Hoog'),
        ('urgent', 'Urgent'),
    ]
    
    STATUS_CHOICES = [
        ('planned', 'Gepland'),
        ('in_progress', 'In uitvoering'),
        ('completed', 'Voltooid'),
        ('cancelled', 'Geannuleerd'),
    ]
    
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    estimated_cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    actual_cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    scheduled_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    contractor = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.property.address}"

# =============================================================================
# DYNAMIC DATABASE MODELS (MULTI-TENANT)
# =============================================================================

class ClientTable(models.Model):
    """Dynamisch aangemaakte tabellen per client"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=200)
    original_filename = models.CharField(max_length=255)
    columns_metadata = models.JSONField()  # Column names, types, descriptions
    supabase_table_name = models.CharField(max_length=150)
    row_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['client', 'table_name']
    
    def __str__(self):
        return f"{self.client.name} - {self.display_name}"

class ClientKnowledgeBase(models.Model):
    """Knowledge base per client voor AI context"""
    DOCUMENT_TYPES = [
        ('csv_data', 'CSV Data'),
        ('pdf_doc', 'PDF Document'),
        ('text_doc', 'Text Document'),
        ('business_rules', 'Business Rules'),
        ('industry_knowledge', 'Industry Knowledge'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)
    source_table = models.ForeignKey(ClientTable, null=True, blank=True, on_delete=models.SET_NULL)
    metadata = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client.name} - {self.title}"

# =============================================================================
# AUTONOMOUS AGENT MODELS
# =============================================================================

class AgentAction(models.Model):
    """Agent acties en besluiten"""
    ACTION_TYPES = [
        ('analysis', 'Data Analyse'),
        ('recommendation', 'Aanbeveling'),
        ('alert', 'Waarschuwing'),
        ('automation', 'Automatisering'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Wachtend op goedkeuring'),
        ('approved', 'Goedgekeurd'),
        ('rejected', 'Afgewezen'),
        ('completed', 'Voltooid'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50, choices=ACTION_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    data_analysis = models.JSONField(null=True, blank=True)  # AVM analysis results
    requires_approval = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    approved_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    approved_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client.name} - {self.title}"

class AgentConfig(models.Model):
    """Agent configuratie per client"""
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    agent_name = models.CharField(max_length=100, default='Business Assistent')
    agent_personality = models.TextField(default='Professioneel en behulpzaam')
    monitoring_frequency = models.CharField(max_length=20, default='daily')  # 'hourly', 'daily', 'weekly'
    auto_approval_threshold = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Voor automatische goedkeuring
    business_rules = models.JSONField(default=dict)  # Industry-specific rules
    notification_settings = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client.name} - {self.agent_name}"