import type { Metadata } from "next";
import { Inter } from "next/font/google";
// import "./globals.css";  // ← UITGESCHAKELD

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: "YokoAI - Jouw AI Team",
  description: "Bouw je perfecte AI werkteam. 24/7 beschikbaar.",
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