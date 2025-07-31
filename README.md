# VDM Nexus - Multi-Tenant Business Intelligence Platform

## 🎯 Project Overview

VDM Nexus is een white-label business intelligence platform waar elke client hun eigen subdomain krijgt en CSV files kan uploaden voor automatische database creation en AI-powered analysis.

### Current Status: Week 1 Development
- ✅ Database models (Client, Property, Tenant, Payment)
- ✅ Multi-tenant architecture setup
- 🔄 **DAG 2**: CSV Upload System (In Progress)
- ⏳ Dashboard widgets
- ⏳ AVM integration

## 🏗️ Architecture

### Backend
- **Django 5.0+** - REST API
- **Supabase** - Dynamic database creation
- **AVM Sandbox** - Safe Python execution
- **Multi-LLM** - Claude, OpenAI, Groq

### Frontend  
- **React/Next.js** - Modern UI
- **TailwindCSS** - Styling
- **Bento-box** - Dashboard layout

### Database
- **PostgreSQL** (Supabase) - Main