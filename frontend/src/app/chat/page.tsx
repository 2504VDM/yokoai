'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function ChatPage() {
  const router = useRouter();
  const [isClient, setIsClient] = useState(false);
  const [messages, setMessages] = useState<Array<{
    id: string;
    text: string;
    sender: 'user' | 'yoko';
    time: string;
  }>>([]);
  const [input, setInput] = useState('');
  const [typing, setTyping] = useState(false);

  useEffect(() => {
    setIsClient(true);
  }, []);

  useEffect(() => {
    if (isClient) {
      setTimeout(() => {
        setMessages([{
          id: '1',
          text: "Hello! I'm YokoAI, your virtual employee that delivers. How can I assist you today?",
          sender: 'yoko',
          time: new Date().toLocaleTimeString('nl-NL', { hour: '2-digit', minute: '2-digit' })
        }]);
      }, 100);
    }
  }, [isClient]);

  const send = () => {
    if (!input.trim() || typing) return;

    const userMsg = {
      id: Date.now().toString(),
      text: input,
      sender: 'user' as const,
      time: new Date().toLocaleTimeString('nl-NL', { hour: '2-digit', minute: '2-digit' })
    };

    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setTyping(true);

    setTimeout(() => {
      const responses = [
        "I understand your request. Let me analyze this and provide you with a comprehensive solution.",
        "Excellent question. As your virtual employee, I'm processing the optimal approach for this task.",
        "I'm on it. Let me deliver exactly what you need with precision and efficiency.",
        "Processing your request now. I'll provide you with actionable insights and next steps.",
        "Thank you for that input. I'm calculating the best strategy to address your requirements."
      ];

      setMessages(prev => [...prev, {
        id: (Date.now() + 1).toString(),
        text: responses[Math.floor(Math.random() * responses.length)],
        sender: 'yoko',
        time: new Date().toLocaleTimeString('nl-NL', { hour: '2-digit', minute: '2-digit' })
      }]);
      setTyping(false);
    }, 2000);
  };

  if (!isClient) {
    return null;
  }

  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: '#0a0a0a',
      color: '#ffffff',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", sans-serif'
    }}>
      {/* Header Bar */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '16px 24px',
        backgroundColor: '#1a1a1a',
        borderBottom: '1px solid #333'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <button
            onClick={() => router.push('/')}
            style={{
              padding: '8px 16px',
              backgroundColor: 'transparent',
              border: '1px solid #444',
              borderRadius: '6px',
              color: '#fff',
              cursor: 'pointer',
              fontSize: '14px',
              transition: 'all 0.2s'
            }}
            onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#333'}
            onMouseLeave={(e) => e.currentTarget.style.backgroundColor = 'transparent'}
          >
            ← Back
          </button>
          
          <div>
            <h1 style={{
              fontSize: '20px',
              fontWeight: '600',
              margin: 0,
              background: 'linear-gradient(45deg, #ffffff, #ff8c00)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              backgroundClip: 'text'
            }}>
              YokoAI
            </h1>
            <p style={{
              fontSize: '12px',
              color: '#888',
              margin: 0,
              fontWeight: '400'
            }}>
              Your Virtual Employee That Delivers
            </p>
          </div>
        </div>

        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: '8px'
        }}>
          <div style={{
            width: '8px',
            height: '8px',
            backgroundColor: '#00ff88',
            borderRadius: '50%'
          }}></div>
          <span style={{ fontSize: '14px', color: '#888' }}>
            {typing ? 'Processing...' : 'Online'}
          </span>
        </div>
      </div>

      {/* Main Chat Area */}
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        height: 'calc(100vh - 73px)',
        maxWidth: '800px',
        margin: '0 auto'
      }}>
        {/* Messages */}
        <div style={{
          flex: 1,
          padding: '24px',
          overflowY: 'auto',
          display: 'flex',
          flexDirection: 'column',
          gap: '16px'
        }}>
          {messages.map(msg => (
            <div key={msg.id} style={{
              display: 'flex',
              justifyContent: msg.sender === 'user' ? 'flex-end' : 'flex-start'
            }}>
              <div style={{
                maxWidth: '70%',
                padding: '12px 16px',
                borderRadius: msg.sender === 'user' ? '16px 16px 4px 16px' : '16px 16px 16px 4px',
                backgroundColor: msg.sender === 'user' ? '#ff8c00' : '#1a1a1a',
                color: msg.sender === 'user' ? '#000' : '#fff',
                border: msg.sender === 'yoko' ? '1px solid #333' : 'none',
                boxShadow: '0 2px 8px rgba(0,0,0,0.3)'
              }}>
                {msg.sender === 'yoko' && (
                  <div style={{
                    fontSize: '11px',
                    color: '#ff8c00',
                    fontWeight: '500',
                    marginBottom: '4px',
                    textTransform: 'uppercase',
                    letterSpacing: '0.5px'
                  }}>
                    YokoAI
                  </div>
                )}
                <div style={{
                  fontSize: '14px',
                  lineHeight: '1.5',
                  fontWeight: '400'
                }}>
                  {msg.text}
                </div>
                <div style={{
                  fontSize: '11px',
                  marginTop: '6px',
                  opacity: 0.6,
                  color: msg.sender === 'user' ? '#000' : '#888'
                }}>
                  {msg.time}
                </div>
              </div>
            </div>
          ))}

          {/* Typing Indicator */}
          {typing && (
            <div style={{ display: 'flex', justifyContent: 'flex-start' }}>
              <div style={{
                padding: '12px 16px',
                borderRadius: '16px 16px 16px 4px',
                backgroundColor: '#1a1a1a',
                border: '1px solid #333',
                boxShadow: '0 2px 8px rgba(0,0,0,0.3)',
                display: 'flex',
                alignItems: 'center',
                gap: '12px'
              }}>
                <div style={{
                  fontSize: '11px',
                  color: '#ff8c00',
                  fontWeight: '500',
                  textTransform: 'uppercase',
                  letterSpacing: '0.5px'
                }}>
                  YokoAI
                </div>
                <div style={{ display: 'flex', gap: '4px' }}>
                  {[0, 1, 2].map(i => (
                    <div
                      key={i}
                      style={{
                        width: '6px',
                        height: '6px',
                        backgroundColor: '#ff8c00',
                        borderRadius: '50%',
                        animation: `pulse 1.4s infinite ${i * 0.2}s`
                      }}
                    />
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Input Area */}
        <div style={{
          padding: '24px',
          backgroundColor: '#111',
          borderTop: '1px solid #333'
        }}>
          {/* Quick Actions */}
          <div style={{
            display: 'flex',
            flexWrap: 'wrap',
            gap: '8px',
            marginBottom: '16px'
          }}>
            {[
              'How can you help me?',
              'What are your capabilities?',
              'Analyze this task',
              'Generate a report'
            ].map((action, index) => (
              <button
                key={index}
                onClick={() => {
                  setInput(action);
                  setTimeout(send, 100);
                }}
                style={{
                  padding: '6px 12px',
                  backgroundColor: 'transparent',
                  color: '#ff8c00',
                  border: '1px solid #ff8c00',
                  borderRadius: '20px',
                  fontSize: '12px',
                  cursor: 'pointer',
                  opacity: typing ? 0.5 : 1,
                  transition: 'all 0.2s',
                  fontWeight: '500'
                }}
                disabled={typing}
                onMouseEnter={(e) => {
                  if (!e.currentTarget.disabled) {
                    e.currentTarget.style.backgroundColor = '#ff8c00';
                    e.currentTarget.style.color = '#000';
                  }
                }}
                onMouseLeave={(e) => {
                  if (!e.currentTarget.disabled) {
                    e.currentTarget.style.backgroundColor = 'transparent';
                    e.currentTarget.style.color = '#ff8c00';
                  }
                }}
              >
                {action}
              </button>
            ))}
          </div>

          {/* Input */}
          <div style={{
            display: 'flex',
            gap: '12px',
            alignItems: 'flex-end'
          }}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && send()}
              placeholder="Type your message to YokoAI..."
              style={{
                flex: 1,
                padding: '14px 16px',
                backgroundColor: '#1a1a1a',
                border: '1px solid #333',
                borderRadius: '8px',
                color: '#fff',
                fontSize: '14px',
                outline: 'none',
                transition: 'border-color 0.2s'
              }}
              onFocus={(e) => e.currentTarget.style.borderColor = '#ff8c00'}
              onBlur={(e) => e.currentTarget.style.borderColor = '#333'}
              disabled={typing}
            />
            <button
              onClick={send}
              disabled={!input.trim() || typing}
              style={{
                padding: '14px 20px',
                backgroundColor: '#ff8c00',
                color: '#000',
                border: 'none',
                borderRadius: '8px',
                cursor: (!input.trim() || typing) ? 'not-allowed' : 'pointer',
                opacity: (!input.trim() || typing) ? 0.5 : 1,
                fontSize: '14px',
                fontWeight: '600',
                transition: 'all 0.2s'
              }}
              onMouseEnter={(e) => {
                if (!e.currentTarget.disabled) {
                  e.currentTarget.style.backgroundColor = '#e67e00';
                }
              }}
              onMouseLeave={(e) => {
                if (!e.currentTarget.disabled) {
                  e.currentTarget.style.backgroundColor = '#ff8c00';
                }
              }}
            >
              Send
            </button>
          </div>
        </div>
      </div>

      {/* CSS Animation */}
      <style jsx>{`
        @keyframes pulse {
          0%, 80%, 100% {
            opacity: 0.3;
            transform: scale(0.8);
          }
          40% {
            opacity: 1;
            transform: scale(1);
          }
        }
      `}</style>
    </div>
  );
}