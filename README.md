# VDM Nexus Platform

**Multi-tenant Business Intelligence Platform met Dynamic Databases**

## 🚀 Quick Start

### Development Environment
```bash
# Clone repository
git clone <repository-url>
cd yokoai

# Switch to development branch
git checkout development

# Setup backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Setup frontend
cd ../frontend
npm install
cp env.example .env.local
# Edit .env.local with your API keys

# Start development servers
# Terminal 1: Backend
cd backend && python manage.py runserver

# Terminal 2: Frontend
cd frontend && npm run dev
```

### Production Deployment
```bash
# Switch to production branch
git checkout production

# Deploy to production
./deploy-production.sh
```

## 🌐 Environment Setup

### Development URLs
- **Main Site**: http://localhost:3000
- **Van der Meulen Demo**: http://localhost:3000/vdmvastgoed
- **Contact Form**: http://localhost:3000/contact
- **Backend API**: http://localhost:8000

### Production URLs
- **Main Site**: https://vdmnexus.com
- **Van der Meulen Demo**: https://vdmvastgoed.vdmnexus.com
- **Development**: https://dev.vdmnexus.com

## 🔧 Configuration

### Environment Variables

#### Frontend (.env.local)
```bash
# AVM API Configuration
NEXT_PUBLIC_AVM_API_KEY=your_avm_api_key_here

# Supabase Configuration
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url_here
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key_here

# Backend API URL
NEXT_PUBLIC_API_URL=http://localhost:8000

# Environment
NEXT_PUBLIC_ENVIRONMENT=development
```

#### Backend (Environment Variables)
```bash
# Supabase
SUPABASE_URL=https://oldsyjgsvpdqhcyrbray.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# AVM API
AVM_API_KEY=avm_27af1a74-14e5-487c-8b10-7176002f74b1

# Django
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 🏗️ Architecture

### Multi-Tenant System
- **Client Isolation**: Each client has their own subdomain
- **Dynamic Databases**: CSV uploads create custom tables
- **AI Analysis**: AVM MCP integration for business intelligence
- **White-Label**: Custom branding per client

### Tech Stack
- **Frontend**: Next.js 14 + TypeScript + TailwindCSS
- **Backend**: Django + Django REST Framework
- **Database**: Supabase (PostgreSQL)
- **AI/Analysis**: AVM (Agent Virtual Machine)
- **Deployment**: Vercel (Frontend) + Render (Backend)

## 📊 Features

### Core Platform
- ✅ **Multi-tenant Architecture**
- ✅ **Dynamic Database Creation**
- ✅ **CSV Upload & Processing**
- ✅ **AI-Powered Analysis**
- ✅ **Real-time Dashboards**
- ✅ **White-label Subdomains**

### Business Intelligence
- ✅ **Payment Analysis** (AVM-powered)
- ✅ **ROI Analysis** (AVM-powered)
- ✅ **Custom Data Analysis**
- ✅ **Risk Assessment**
- ✅ **Market Trends**

### Client Management
- ✅ **Client Onboarding**
- ✅ **Subdomain Routing**
- ✅ **Data Isolation**
- ✅ **Custom Branding**
- ✅ **Usage Analytics**

## 🚀 Deployment

### Development Branch
```bash
git checkout development
./deploy-development.sh
```

### Production Branch
```bash
git checkout production
./deploy-production.sh
```

### Custom Domain Setup
1. **Namecheap DNS Configuration**
   - A Record: `@` → Vercel IP
   - CNAME: `www` → `vdmnexus.com`
   - CNAME: `dev` → `vdmnexus-dev.vercel.app`
   - CNAME: `vdmvastgoed` → `vdmvastgoed.vdmnexus.com`

2. **Vercel Domain Configuration**
   - Add custom domain in Vercel dashboard
   - Configure SSL certificates
   - Set up redirects

## 🧪 Testing

### Backend Tests
```bash
cd backend
python test_multi_tenant.py
python test_avm.py
python manage.py test
```

### Frontend Tests
```bash
cd frontend
npm run test
npm run build
```

### AVM Integration Test
```bash
cd backend
python setup_avm.py
```

## 📈 Business Model

### Pricing Tiers
- **Starter**: €199/maand
- **Business**: €499/maand  
- **Enterprise**: €1.299/maand
- **Enterprise Pro**: Op maat

### Target Market
- Nederlandse SME bedrijven
- Accountantskantoren
- Advocatenkantoren
- Makelaardijen
- Consultancy bureaus

## 🔐 Security

### Data Protection
- **Row Level Security** (RLS) in Supabase
- **Client Data Isolation**
- **Encrypted API Keys**
- **HTTPS Only**
- **GDPR Compliance**

### Access Control
- **Multi-tenant Authentication**
- **Role-based Permissions**
- **API Rate Limiting**
- **Audit Logging**

## 📞 Support

### Development Support
- **Documentation**: This README
- **Issues**: GitHub Issues
- **Testing**: Automated test suite

### Business Support
- **Demo Requests**: Contact form on website
- **Sales**: LinkedIn outreach program
- **Onboarding**: Automated workflow

## 🎯 Roadmap

### Phase 1 (Current)
- ✅ Multi-tenant platform
- ✅ AVM integration
- ✅ Basic dashboards
- ✅ CSV upload system

### Phase 2 (Next 3 months)
- 🔄 Advanced analytics
- 🔄 Enterprise features
- 🔄 International expansion
- 🔄 API marketplace

### Phase 3 (6-12 months)
- 🔄 AI agents
- 🔄 Predictive analytics
- 🔄 White-label SaaS
- 🔄 Global deployment

## 📝 License

MIT License - see LICENSE file for details.

---

**VDM Nexus** - Revolutionizing Business Intelligence for Dutch SMEs