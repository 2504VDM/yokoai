import type { Metadata } from "next";
import { Inter } from "next/font/google";
// import "./globals.css";  // ← UITGESCHAKELD

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: "VDM Nexus",
  description: "Business Intelligence Platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="nl">
      <body className={`${inter.variable} font-sans`} style={{ margin: 0, padding: 0 }}>
        {children}
      </body>
    </html>
  );
}