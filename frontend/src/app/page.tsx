'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'

export default function Home() {
  const router = useRouter()
  const [isHovered, setIsHovered] = useState(false)

  return (
    <main style={{
      minHeight: '100vh',
      backgroundColor: '#000',
      color: '#fff',
      fontFamily: 'Arial, sans-serif'
    }}>
      <div style={{
        maxWidth: '1200px',
        margin: '0 auto',
        padding: '64px 16px'
      }}>
        <div style={{
          maxWidth: '1000px',
          margin: '0 auto',
          textAlign: 'center'
        }}>
          <h1 style={{
            fontSize: '64px',
            fontWeight: 'bold',
            marginBottom: '24px',
            background: 'linear-gradient(to right, #fff, #9ca3af)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text'
          }}>
            Yoko AI
          </h1>
          <p style={{
            fontSize: '20px',
            color: '#d1d5db',
            marginBottom: '48px'
          }}>
            Your intelligent AI Border Collie for seamless conversations and task management
          </p>
          
          <button
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            onClick={() => router.push('/chat')}
            style={{
              padding: '16px 32px',
              backgroundColor: isHovered ? '#f3f4f6' : '#fff',
              color: '#000',
              borderRadius: '8px',
              fontWeight: '600',
              fontSize: '18px',
              border: 'none',
              cursor: 'pointer',
              transition: 'all 0.3s ease',
              transform: isHovered ? 'scale(1.05)' : 'scale(1)'
            }}
          >
            Get Yoko
          </button>
        </div>

        <div style={{
          marginTop: '96px',
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '32px'
        }}>
          <div style={{
            backgroundColor: '#1f2937',
            padding: '24px',
            borderRadius: '12px'
          }}>
            <h3 style={{
              fontSize: '20px',
              fontWeight: '600',
              marginBottom: '16px',
              color: '#fff'
            }}>
              Smart Conversations
            </h3>
            <p style={{ color: '#9ca3af' }}>
              Engage in natural, context-aware discussions with our advanced AI
            </p>
          </div>

          <div style={{
            backgroundColor: '#1f2937',
            padding: '24px',
            borderRadius: '12px'
          }}>
            <h3 style={{
              fontSize: '20px',
              fontWeight: '600',
              marginBottom: '16px',
              color: '#fff'
            }}>
              Task Management
            </h3>
            <p style={{ color: '#9ca3af' }}>
              Efficiently organize and track your tasks with AI assistance
            </p>
          </div>

          <div style={{
            backgroundColor: '#1f2937',
            padding: '24px',
            borderRadius: '12px'
          }}>
            <h3 style={{
              fontSize: '20px',
              fontWeight: '600',
              marginBottom: '16px',
              color: '#fff'
            }}>
              24/7 Availability
            </h3>
            <p style={{ color: '#9ca3af' }}>
              Get instant help whenever you need it, day or night
            </p>
          </div>
        </div>
        
        <div style={{
          marginTop: '96px',
          textAlign: 'center',
          color: '#6b7280',
          fontSize: '14px'
        }}>
          v0.2.3 | Made by VDM Nexus
        </div>
      </div>
    </main>
  )
}
