// pages/api/health.ts
import { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const healthCheck = {
    timestamp: new Date().toISOString(),
    status: 'healthy',
    version: '1.0.0',
    environment: process.env.NODE_ENV || 'development',
    checks: {
      database: false,
      supabase_connection: false,
      backend_api: false,
    },
    performance: {
      uptime: process.uptime(),
      memory: process.memoryUsage(),
      node_version: process.version,
    },
    deployment: {
      vercel_region: process.env.VERCEL_REGION || 'unknown',
      vercel_url: process.env.VERCEL_URL || 'localhost',
      git_commit: process.env.VERCEL_GIT_COMMIT_SHA?.slice(0, 7) || 'local',
    }
  }

  try {
    // Test 1: Supabase connection
    const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
    const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
    
    if (supabaseUrl && supabaseKey) {
      try {
        const response = await fetch(`${supabaseUrl}/rest/v1/`, {
          headers: {
            'apikey': supabaseKey,
            'Authorization': `Bearer ${supabaseKey}`
          }
        })
        healthCheck.checks.supabase_connection = response.ok
      } catch (error) {
        healthCheck.checks.supabase_connection = false
      }
    }

    // Test 2: Database health (via Supabase)
    if (healthCheck.checks.supabase_connection) {
      try {
        const response = await fetch(`${supabaseUrl}/rest/v1/profiles?select=count&limit=1`, {
          headers: {
            'apikey': supabaseKey!,
            'Authorization': `Bearer ${supabaseKey!}`
          }
        })
        healthCheck.checks.database = response.ok
      } catch (error) {
        healthCheck.checks.database = false
      }
    }

    // Test 3: Backend API (if configured)
    const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL
    if (backendUrl) {
      try {
        const response = await fetch(`${backendUrl}/api/health`, {
          timeout: 5000
        } as any)
        healthCheck.checks.backend_api = response.ok
      } catch (error) {
        healthCheck.checks.backend_api = false
      }
    } else {
      healthCheck.checks.backend_api = true // No backend configured, that's OK
    }

    // Overall status
    const allChecks = Object.values(healthCheck.checks)
    const healthyChecks = allChecks.filter(check => check === true).length
    const totalChecks = allChecks.length
    
    if (healthyChecks === totalChecks) {
      healthCheck.status = 'healthy'
    } else if (healthyChecks >= totalChecks * 0.5) {
      healthCheck.status = 'degraded'
    } else {
      healthCheck.status = 'unhealthy'
    }

    // Return appropriate status code
    const statusCode = healthCheck.status === 'healthy' ? 200 : 
                      healthCheck.status === 'degraded' ? 207 : 503

    res.status(statusCode).json(healthCheck)
    
  } catch (error) {
    healthCheck.status = 'unhealthy'
    res.status(503).json({
      ...healthCheck,
      error: error instanceof Error ? error.message : 'Unknown error'
    })
  }
}