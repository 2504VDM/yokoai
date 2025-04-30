'use client'

import { useState } from 'react'
import { Chat } from '@/components/ui/chat'
import { useRouter } from 'next/navigation'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

interface ApiResponse {
  content: string
}

export default function ChatPage() {
  const router = useRouter()
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(false)

  const handleSend = async (content: string) => {
    setIsLoading(true);
    console.log('Request payload:', {
      messages: [...messages, { role: 'user', content }]
    });

    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/chat/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          messages: [...messages, { role: 'user', content }]
        }),
      });

      console.log('Response status:', response.status);
      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error response:', errorText);
        throw new Error('Failed to send message');
      }

      const data = await response.json() as ApiResponse;
      console.log('Response data:', data);

      setMessages(prev => [
        ...prev,
        { role: 'user', content },
        { role: 'assistant', content: data.content }
      ]);
    } catch (error) {
      console.error('Error in handleSend:', error);
      setMessages(prev => [
        ...prev,
        { role: 'user', content },
        { role: 'assistant', content: 'Sorry, there was an error processing your message.' }
      ]);
    } finally {
      setIsLoading(false);
    }
  }

  const handleEdit = async (index: number, newContent: string) => {
    const newMessages = messages.map((msg, i) =>
      i === index ? { ...msg, content: newContent } : msg
    )
    const truncated = newMessages.slice(0, index + 1)
    setMessages(truncated)
    setIsLoading(true)
    
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/chat/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: truncated }),
      })
      console.log('Edit response status:', response.status);
      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error response:', errorText);
        throw new Error('Failed to send message');
      }
      const data = await response.json() as ApiResponse;
      console.log('Edit response data:', data);
      setMessages(prev => [
        ...prev,
        { role: 'assistant', content: data.content }
      ])
    } catch (error) {
      console.error('Error in handleEdit:', error);
      setMessages(prev => [
        ...prev,
        { role: 'assistant', content: 'Sorry, there was an error processing your message.' }
      ])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-4xl font-bold">Yoko, the smartest dog in the world:</h1>
          <button 
            onClick={() => router.push('/')}
            className="bg-gray-100 hover:bg-gray-200 text-gray-800 px-4 py-2 rounded-full
                     transition-all duration-300 flex items-center space-x-2"
          >
            <span>←</span>
            <span>Terug</span>
          </button>
        </div>
        <div className="bg-white rounded-lg shadow-lg p-4">
          <Chat 
            messages={messages} 
            onSend={handleSend} 
            onEdit={handleEdit}
            isLoading={isLoading}
          />
        </div>
        <div className="w-full text-center mt-4 text-xs text-gray-400">
          v0.2.2
          Made by VDM Nexus
        </div>
      </div>
    </main>
  )
} 