import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  poweredByHeader: false,
  eslint: {
    ignoreDuringBuilds: true,
  },
  typescript: {
    ignoreBuildErrors: true,
  },
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || (
      process.env.VERCEL_ENV === 'production' 
        ? 'https://yokoai.onrender.com'
        : process.env.VERCEL_ENV === 'preview' 
          ? 'https://yokoai-staging.onrender.com'
          : 'http://localhost:8000'
    ),
    NEXT_PUBLIC_APP_URL: process.env.NEXT_PUBLIC_APP_URL || (
      process.env.VERCEL_ENV === 'production'
        ? 'https://yoko.vdmnexus.com'
        : process.env.VERCEL_ENV === 'preview'
          ? 'https://yokoai-staging.vercel.app'
          : 'http://localhost:3000'
    )
  },
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          {
            key: "X-Frame-Options",
            value: "DENY",
          },
          {
            key: "X-Content-Type-Options",
            value: "nosniff",
          },
          {
            key: "Referrer-Policy",
            value: "origin-when-cross-origin",
          },
        ],
      },
    ];
  },
  async rewrites() {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL || (
      process.env.VERCEL_ENV === 'production' 
        ? 'https://yokoai.onrender.com'
        : process.env.VERCEL_ENV === 'preview' 
          ? 'https://yokoai-staging.onrender.com'
          : 'http://localhost:8000'
    );
    return {
      beforeFiles: [
        // Handle paths without trailing slash
        {
          source: '/api/:path*',
          destination: `${apiUrl}/api/:path*/`
        },
        // Handle paths with trailing slash
        {
          source: '/api/:path*/',
          destination: `${apiUrl}/api/:path*/`
        }
      ]
    };
  },
  async redirects() {
    return [
      {
        source: '/',
        has: [
          {
            type: 'host',
            value: 'yokoai.vercel.app',
          },
        ],
        destination: 'https://yoko.vdmnexus.com',
        permanent: true,
      },
    ];
  }
};

export default nextConfig;
