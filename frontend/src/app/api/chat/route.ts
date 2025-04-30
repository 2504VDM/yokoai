import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'https://yokoai.onrender.com';
  
  try {
    const body = await req.json();
    console.log('Received request body:', body);
    console.log('Forwarding to:', `${apiUrl}/api/chat/`);
    
    // Forward all relevant headers from the original request
    const headers = new Headers({
      'Content-Type': 'application/json',
      'Origin': 'https://yoko.vdmnexus.com',
      'Accept': 'application/json',
      'User-Agent': req.headers.get('user-agent') || 'Next.js API route',
      'Referer': req.headers.get('referer') || 'https://yoko.vdmnexus.com'
    });

    const response = await fetch(`${apiUrl}/api/chat/`, {
      method: 'POST',
      headers,
      body: JSON.stringify(body),
      credentials: 'include'
    });

    console.log('Backend response status:', response.status);
    console.log('Backend response headers:', Object.fromEntries(response.headers.entries()));
    
    if (!response.ok) {
      const errorText = await response.text();
      console.error('Backend error response:', errorText);
      console.error('Request headers:', Object.fromEntries(headers.entries()));
      throw new Error(`API responded with status ${response.status}: ${errorText}`);
    }

    const data = await response.json();
    console.log('Backend response data:', data);
    
    // Return response with CORS headers
    return new NextResponse(JSON.stringify(data), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': 'https://yoko.vdmnexus.com',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type'
      }
    });
  } catch (error) {
    console.error('Error in chat API route:', error);
    return new NextResponse(
      JSON.stringify({ 
        error: error instanceof Error ? error.message : 'Failed to process request',
        timestamp: new Date().toISOString()
      }),
      { 
        status: 500,
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': 'https://yoko.vdmnexus.com'
        }
      }
    );
  }
} 