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
- `