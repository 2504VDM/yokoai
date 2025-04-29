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
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || 'https://yokoai.onrender.com',
    NEXT_PUBLIC_APP_URL: process.env.NEXT_PUBLIC_APP_URL || 'https://yoko.vdmnexus.com'
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
    const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'https://yokoai.onrender.com';
    return {
      beforeFiles: [
        {
          source: '/api/:path*',
          destination: `${apiUrl}/api/:path*/`
        },
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
