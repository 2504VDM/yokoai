import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'https://yokoai.onrender.com';
  
  try {
    const body = await req.json();
    console.log('Received request body:', body);
    console.log('Forwarding to:', `${apiUrl}/api/chat/`);
    
    const response = await fetch(`${apiUrl}/api/chat/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Origin': 'https://yoko.vdmnexus.com'
      },
      body: JSON.stringify(body),
    });

    console.log('Backend response status:', response.status);
    
    if (!response.ok) {
      const errorText = await response.text();
      console.error('Backend error response:', errorText);
      throw new Error(`API responded with status ${response.status}: ${errorText}`);
    }

    const data = await response.json();
    console.log('Backend response data:', data);
    return NextResponse.json(data);
  } catch (error) {
    console.error('Error in chat API route:', error);
    return NextResponse.json(
      { error: error instanceof Error ? error.message : 'Failed to process request' },
      { status: 500 }
    );
  }
} 