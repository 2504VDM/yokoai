#!/bin/bash

# VDM Nexus Production Deployment Script
# Deploys to vdmnexus.com

echo "🚀 Deploying VDM Nexus to Production Environment..."

# Check if we're on production branch
if [[ $(git branch --show-current) != "production" ]]; then
    echo "❌ Error: Must be on production branch to deploy"
    echo "Run: git checkout production"
    exit 1
fi

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Set environment variables for production
export VERCEL_ENV=production
export VERCEL_PROJECT_NAME=vdmnexus

echo "📦 Building frontend..."
cd frontend
npm run build

echo "🚀 Deploying to Vercel..."
vercel --prod --confirm

echo "✅ Production deployment complete!"
echo "🌐 Your production site is live at: https://vdmnexus.com"
echo "🔧 Custom domain should be configured in Vercel dashboard" 