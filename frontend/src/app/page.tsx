'use client'

import { useState } from 'react'
import { Chat } from '@/components/ui/chat'

const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/chat/'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

interface AgentMessage {
  content: string;
  additional_kwargs: Record<string, any>;
  [key: string]: any;
}

interface ResponseMessage {
  role: 'user' | 'assistant';
  content: string;
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(false)

  const handleSend = async (content: string) => {
    setIsLoading(true);

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          messages: [...messages, { role: 'user', content }]
        }),
      });

      if (!response.ok) throw new Error('Failed to send message');

      const data = await response.json();

      setMessages(prev => [
        ...prev,
        { role: 'user', content },
        { role: 'assistant', content: data.content }
      ]);
    } catch (error) {
      setMessages(prev => [
        ...prev,
        { role: 'user', content },
        { role: 'assistant', content: 'Sorry, there was an error processing your message.' }
      ]);
    } finally {
      setIsLoading(false);
    }
  }

  // Handle editing a user message and getting a new agent response
  const handleEdit = async (index: number, newContent: string) => {
    // Update the user message at index
    const newMessages = messages.map((msg, i) =>
      i === index ? { ...msg, content: newContent } : msg
    )
    // Truncate conversation after the edited user message
    const truncated = newMessages.slice(0, index + 1)
    setMessages(truncated)
    setIsLoading(true)
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: truncated }),
      })
      if (!response.ok) throw new Error('Failed to send message')
      const data = await response.json()
      setMessages(prev => [
        ...prev,
        { role: 'assistant', content: data.content }
      ])
    } catch (error) {
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
        <h1 className="text-4xl font-bold mb-8 text-center">Yoko, the smartest dog in the world:</h1>
        <div className="bg-white rounded-lg shadow-lg p-4">
          <Chat 
            messages={messages} 
            onSend={handleSend} 
            onEdit={handleEdit}
            isLoading={isLoading}
          />
        </div>
        <div className="w-full text-center mt-4 text-xs text-gray-400">
          v0.2
          Made by VDM Nexus
        </div>
      </div>
    </main>
  )
}
