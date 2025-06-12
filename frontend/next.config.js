/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    // appDir is removed - it's default in Next.js 14
  },

  // Fixed rewrites configuration with proper TypeScript types
  async rewrites() {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL || (
      process.env.VERCEL_ENV === 'production' 
        ? 'https://yokoai.onrender.com'
        : 'http://localhost:8000'
    );

    return {
      beforeFiles: [
        {
          source: '/api/chat',
          destination: `${apiUrl}/api/chat/`,
        },
        {
          source: '/api/chat/:path*',
          destination: `${apiUrl}/api/chat/:path*`,
        },
      ],
      afterFiles: [],
      fallback: [],
    };
  },

  // Headers for API calls
  async headers() {
    return [
      {
        source: '/api/:path*',
        headers: [
          { key: 'Access-Control-Allow-Origin', value: '*' },
          { key: 'Access-Control-Allow-Methods', value: 'GET, POST, PUT, DELETE, OPTIONS' },
          { key: 'Access-Control-Allow-Headers', value: 'Content-Type, Authorization' },
        ],
      },
    ];
  },
};

export default nextConfig;