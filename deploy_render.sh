#!/bin/bash

# VDM Nexus Render Deployment Script
# Deploys backend to Render

echo "🚀 VDM Nexus Render Deployment"
echo "================================"

# Check if we're on development branch
if [[ $(git branch --show-current) != "development" ]]; then
    echo "❌ Error: Must be on development branch"
    echo "Run: git checkout development"
    exit 1
fi

echo "✅ Current branch: development"

# Push latest changes
echo "📤 Pushing to GitHub..."
git add .
git commit -m "feat: prepare for Render deployment"
git push origin development

echo "✅ Code pushed to GitHub"

echo ""
echo "🌐 Next Steps:"
echo "1. Go to https://render.com"
echo "2. Sign up/Login with GitHub"
echo "3. Click 'New Web Service'"
echo "4. Connect to GitHub repository: 2504VDM/yokoai"
echo "5. Configure service:"
echo "   - Name: vdmnexus-backend"
echo "   - Root Directory: backend"
echo "   - Environment: Python"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: gunicorn config.wsgi:application --bind 0.0.0.0:\$PORT"
echo ""
echo "🔧 Environment Variables to set in Render:"
echo "SUPABASE_URL=https://oldsyjgsvpdqhcyrbray.supabase.co"
echo "SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9sZHN5amdzdnBkcWhjeXJicmF5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM5NjMyNjUsImV4cCI6MjA2OTUzOTI2NX0.5X_FEyYMYf5kIK2Ynyw3PIaMoTLhYSy6x2cgnvDO0Jo"
echo "AVM_API_KEY=avm_27af1a74-14e5-487c-8b10-7176002f74b1"
echo "DEBUG=False"
echo "ALLOWED_HOSTS=vdmnexus-backend.onrender.com,localhost,127.0.0.1"
echo ""
echo "🎯 After deployment, update frontend API URL to:"
echo "https://vdmnexus-backend.onrender.com" 