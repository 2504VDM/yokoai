'use client'

import { useRouter } from 'next/navigation'

export default function Home() {
  const router = useRouter()

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-gradient-to-br from-blue-50 to-gray-100">
      <div className="z-10 max-w-2xl w-full text-center">
        <div className="animate-bounce mb-8">
          <span className="text-6xl">🐾</span>
        </div>
        <h1 className="text-5xl font-bold mb-6 text-gray-800">
          Welkom bij YokoAI
        </h1>
        <p className="text-xl text-gray-600 mb-12">
          Je persoonlijke AI Border Collie assistent is klaar om je te helpen! 
          Klik op de knop hieronder om Yoko te roepen.
        </p>
        <button
          onClick={() => router.push('/chat')}
          className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-4 px-8 rounded-full 
                   text-xl transition-all duration-300 transform hover:scale-105 hover:shadow-lg
                   flex items-center justify-center mx-auto space-x-3"
        >
          <span className="text-2xl">🐾</span>
          <span>Roep Yoko</span>
        </button>
        <div className="mt-16 text-sm text-gray-400">
          v0.2.2
          <br />
          Made by VDM Nexus
        </div>
      </div>
    </main>
  )
}
