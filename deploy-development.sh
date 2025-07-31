#!/bin/bash

# VDM Nexus Development Deployment Script
# Deploys to development subdomain

echo "🚀 Deploying VDM Nexus to Development Environment..."

# Check if we're on development branch
if [[ $(git branch --show-current) != "development" ]]; then
    echo "❌ Error: Must be on development branch to deploy"
    echo "Run: git checkout development"
    exit 1
fi

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Set environment variables for development
export VERCEL_ENV=development
export VERCEL_PROJECT_NAME=vdmnexus-dev

echo "📦 Building frontend..."
cd frontend
npm run build

echo "🚀 Deploying to Vercel..."
vercel --prod --confirm

echo "✅ Development deployment complete!"
echo "🌐 Your development site is live at: https://vdmnexus-dev.vercel.app"
echo "🔧 For custom domain setup, configure in Vercel dashboard" 