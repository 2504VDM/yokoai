# Yoko AI Agent

A powerful AI agent system built with Django and React, leveraging LangChain and Anthropic's Claude for intelligent interactions.

## Features

- Django backend with REST API
- React frontend with modern UI components
- Integration with Anthropic's Claude AI
- Real-time chat interface
- Secure environment configuration
- Production-ready setup with Render deployment

## Tech Stack

- Backend:
  - Django 5.0+
  - Django REST Framework
  - LangChain
  - Anthropic Claude
  - PostgreSQL (via Supabase)

- Frontend:
  - React
  - Next.js
  - Shadcn/ui
  - TailwindCSS

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in `.env`
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment

The project is configured for deployment on:
- Backend: Render
- Frontend: Vercel
- Database: Supabase

## Environment Variables

Required environment variables:
- `DATABASE_URL`: PostgreSQL connection string
- `DJANGO_SECRET_KEY`: Django secret key
- `ANTHROPIC_API_KEY`: Anthropic API key
- `DEBUG`: Boolean for debug mode
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Project Structure

- `agent/`: Contains the core agent implementation
- `api/`: Django REST framework endpoints

## Development Workflow

This project uses a staging-production workflow with automated deployments.

### Environments

#### Frontend
- Production: https://yoko.vdmnexus.com
- Staging: https://yokoai-staging.vercel.app
- Development: http://localhost:3000

#### Backend
- Production: https://yokoai.onrender.com
- Staging: https://yokoai-staging.onrender.com
- Development: http://localhost:8000

### Branch Strategy

- `main` - Production branch
- `develop` - Staging branch
- Feature branches - For new features/fixes

### Development Process

1. Create a feature branch from `develop`:
   ```bash
   git checkout develop
   git pull
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

3. Push your feature branch:
   ```bash
   git push -u origin feature/your-feature-name
   ```

4. Create a Pull Request to merge into `develop`
   - This will automatically deploy to staging when merged

5. Test on staging environment
   - Frontend: https://yokoai-staging.vercel.app
   - Backend: https://yokoai-staging.onrender.com

6. When ready for production:
   - Create a Pull Request from `develop` to `main`
   - Review and merge
   - This will automatically deploy to production

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/2504VDM/yokoai.git
   cd yokoai
   ```

2. Switch to develop branch:
   ```bash
   git checkout develop
   ```

3. Install dependencies:
   ```bash
   # Backend
   cd backend
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt

   # Frontend
   cd frontend
   npm install
   ```

4. Run locally:
   ```bash
   # Backend
   cd backend
   python manage.py runserver

   # Frontend
   cd frontend
   npm run dev
   ```

### Deployment

- Pushing to `develop` automatically deploys to staging
- Pushing to `main` automatically deploys to production

### Environment Variables

Make sure to set up these environment variables in GitHub Actions:

- `RENDER_API_KEY`
- `RENDER_SERVICE_ID_STAGING`
- `RENDER_SERVICE_ID_PROD`
- `VERCEL_TOKEN`
- `VERCEL_ORG_ID`
- `VERCEL_PROJECT_ID`