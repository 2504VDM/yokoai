# backend/agent/admin.py
from django.contrib import admin
from .models import Client, ClientKnowledgeBase, ClientDocument, BusinessFunction, Conversation, Message

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'subdomain', 'created_at']
    search_fields = ['name', 'subdomain']
    readonly_fields = ['id', 'created_at']

@admin.register(ClientKnowledgeBase)
class ClientKnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'client', 'created_at']
    list_filter = ['client', 'created_at']
    search_fields = ['name', 'client__name']

@admin.register(ClientDocument)
class ClientDocumentAdmin(admin.ModelAdmin):
    list_display = ['filename', 'knowledge_base', 'file_type', 'processed', 'uploaded_at']
    list_filter = ['file_type', 'processed', 'knowledge_base__client']
    search_fields = ['filename']

@admin.register(BusinessFunction)
class BusinessFunctionAdmin(admin.ModelAdmin):
    list_display = ['name', 'client', 'is_active']
    list_filter = ['client', 'is_active']
    search_fields = ['name', 'description']

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'created_at']
    list_filter = ['client', 'created_at']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['conversation', 'role', 'content_preview', 'function_used', 'created_at']
    list_filter = ['role', 'function_used', 'created_at']
    
    def content_preview(self, obj):
        return obj.content[:100] + "..." if len(obj.content) > 100 else obj.content
    content_preview.short_description = 'Content Preview'