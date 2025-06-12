'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import YokoLogo from '@/components/ui/YokoLogo';

interface Agent {
  name: string;
  role: string;
  description: string;
  tasks: string[];
  price: string;
  icon: string;
}

interface PricingTier {
  name: string;
  subtitle: string;
  price: string;
  period: string;
  features: string[];
  cta: string;
  popular: boolean;
}

export default function YokoAILanding() {
  const router = useRouter();
  const [isClient, setIsClient] = useState(false);
  const [selectedAgent, setSelectedAgent] = useState<Agent | null>(null);
  const [expandedFAQ, setExpandedFAQ] = useState<number | null>(null);

  useEffect(() => {
    setIsClient(true);
  }, []);

  const agents: Agent[] = [
    {
      name: 'Emma',
      role: 'Data Analist',
      description: 'Rapporten genereren, trends analyseren, dashboards maken',
      tasks: ['Weekly KPI reports', 'Competitor analysis', 'Sales forecasting'],
      price: '€79',
      icon: '📊'
    },
    {
      name: 'Max',
      role: 'Sales Agent',
      description: 'Lead opvolging, deal management, proposal writing',
      tasks: ['Lead scoring', 'Follow-up emails', 'Meeting scheduling'],
      price: '€99',
      icon: '📈'
    },
    {
      name: 'Julia',
      role: 'Marketing Specialist',
      description: 'Content creatie, social media, SEO optimalisatie',
      tasks: ['Blog posts', 'Social posts', 'Email campaigns'],
      price: '€89',
      icon: '🎨'
    },
    {
      name: 'Sophie',
      role: 'HR Coordinator',
      description: 'Recruitment, onboarding, employee engagement',
      tasks: ['CV screening', 'Interview scheduling', 'Employee surveys'],
      price: '€69',
      icon: '👥'
    },
    {
      name: 'David',
      role: 'Customer Support',
      description: 'Ticket afhandeling, FAQ management, escalatie',
      tasks: ['Support tickets', 'Knowledge base updates', 'Chat support'],
      price: '€59',
      icon: '🛠️'
    },
    {
      name: 'Lisa',
      role: 'Operations Manager',
      description: 'Process optimization, task coordination, reporting',
      tasks: ['Workflow management', 'Status updates', 'Efficiency reports'],
      price: '€109',
      icon: '⚙️'
    }
  ];

  const pricingTiers: PricingTier[] = [
    {
      name: 'Starter',
      subtitle: 'Je Eerste AI Medewerker',
      price: '€29',
      period: '/maand',
      features: [
        '1 AI Specialist naar keuze',
        '1.000 taken/maand',
        'Basis dashboard',
        'Email support',
        'Gratis proefperiode'
      ],
      cta: 'Start Gratis',
      popular: false
    },
    {
      name: 'Professional',
      subtitle: 'Je AI Team',
      price: '€79',
      period: '/maand',
      features: [
        'Tot 3 AI Specialisten',
        '5.000 taken/maand',
        'Geavanceerd dashboard',
        'Live chat support',
        'Custom rules engine',
        'API toegang'
      ],
      cta: 'Meest Populair',
      popular: true
    },
    {
      name: 'Business',
      subtitle: 'Complete AI Afdeling',
      price: '€199',
      period: '/maand',
      features: [
        'Onbeperkte AI Specialisten',
        '25.000 taken/maand',
        'Team collaboration',
        'Prioriteit support',
        'White-label opties',
        'Dedicated account manager'
      ],
      cta: 'Schaal Je Business',
      popular: false
    }
  ];

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
      {/* Header */}
      <header style={{
        padding: '16px 24px',
        backgroundColor: '#1a1a1a',
        borderBottom: '1px solid #333',
        position: 'sticky',
        top: 0,
        zIndex: 50
      }}>
        <div style={{
          maxWidth: '1200px',
          margin: '0 auto',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
            <YokoLogo size={40} variant="compact" />
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
                margin: 0
              }}>
                Jouw AI Team. Altijd Actief.
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '16px', alignItems: 'center' }}>
            <button
              onClick={() => router.push('/chat')}
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
              Demo Proberen
            </button>
            <button
              style={{
                padding: '8px 16px',
                backgroundColor: '#ff8c00',
                border: 'none',
                borderRadius: '6px',
                color: '#000',
                cursor: 'pointer',
                fontSize: '14px',
                fontWeight: '600',
                transition: 'all 0.2s'
              }}
              onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#e67e00'}
              onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#ff8c00'}
            >
              Start Gratis
            </button>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section style={{
        padding: '80px 24px',
        textAlign: 'center',
        background: 'linear-gradient(180deg, #0a0a0a 0%, #111111 100%)'
      }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
          <YokoLogo size={200} variant="full" />
          
          <h2 style={{
            fontSize: '48px',
            fontWeight: '700',
            marginBottom: '24px',
            marginTop: '40px',
            background: 'linear-gradient(45deg, #ffffff, #ff8c00)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
            lineHeight: '1.2'
          }}>
            Bouw Je Perfecte AI Werkteam
            <br />24/7 Beschikbaar
          </h2>

          <p style={{
            fontSize: '20px',
            color: '#888',
            marginBottom: '48px',
            maxWidth: '600px',
            margin: '0 auto 48px auto',
            lineHeight: '1.6'
          }}>
            Vanaf €29/maand heb je je eigen AI specialist. Geen chatbot, maar een echte virtuele medewerker die autonoom werkt.
          </p>

          <div style={{ display: 'flex', gap: '16px', justifyContent: 'center', flexWrap: 'wrap' }}>
            <button
              style={{
                padding: '16px 32px',
                backgroundColor: '#ff8c00',
                border: 'none',
                borderRadius: '8px',
                color: '#000',
                cursor: 'pointer',
                fontSize: '16px',
                fontWeight: '600',
                transition: 'all 0.2s',
                boxShadow: '0 4px 16px rgba(255, 140, 0, 0.3)'
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.backgroundColor = '#e67e00';
                e.currentTarget.style.transform = 'translateY(-2px)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.backgroundColor = '#ff8c00';
                e.currentTarget.style.transform = 'translateY(0px)';
              }}
            >
              Start Gratis Proefperiode
            </button>
            
            <button
              style={{
                padding: '16px 32px',
                backgroundColor: 'transparent',
                border: '1px solid #444',
                borderRadius: '8px',
                color: '#fff',
                cursor: 'pointer',
                fontSize: '16px',
                transition: 'all 0.2s'
              }}
              onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#333'}
              onMouseLeave={(e) => e.currentTarget.style.backgroundColor = 'transparent'}
            >
              Bekijk AI Specialisten
            </button>
          </div>

          <p style={{
            marginTop: '32px',
            fontSize: '14px',
            color: '#666'
          }}>
            Sluit je aan bij de nieuwe generatie bedrijven die hun werk automatiseren met YokoAI
          </p>
        </div>
      </section>
{/* Statistics Section */}
<section style={{
        padding: '60px 24px',
        backgroundColor: '#111111',
        borderBottom: '1px solid #333'
      }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
            gap: '40px',
            textAlign: 'center'
          }}>
            <div style={{
              padding: '24px',
              backgroundColor: '#1a1a1a',
              borderRadius: '12px',
              border: '1px solid #333',
              transition: 'transform 0.2s ease'
            }}
            onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-4px)'}
            onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0px)'}
            >
              <div style={{
                fontSize: '36px',
                fontWeight: '700',
                color: '#ff8c00',
                marginBottom: '8px'
              }}>
                10+
              </div>
              <div style={{
                fontSize: '16px',
                color: '#888',
                lineHeight: '1.4'
              }}>
                Early adopters testen<br />YokoAI dagelijks
              </div>
            </div>

            <div style={{
              padding: '24px',
              backgroundColor: '#1a1a1a',
              borderRadius: '12px',
              border: '1px solid #333',
              transition: 'transform 0.2s ease'
            }}
            onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-4px)'}
            onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0px)'}
            >
              <div style={{
                fontSize: '36px',
                fontWeight: '700',
                color: '#ff8c00',
                marginBottom: '8px'
              }}>
                24/7
              </div>
              <div style={{
                fontSize: '16px',
                color: '#888',
                lineHeight: '1.4'
              }}>
                Beschikbare AI<br />specialisten
              </div>
            </div>

            <div style={{
              padding: '24px',
              backgroundColor: '#1a1a1a',
              borderRadius: '12px',
              border: '1px solid #333',
              transition: 'transform 0.2s ease'
            }}
            onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-4px)'}
            onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0px)'}
            >
              <div style={{
                fontSize: '36px',
                fontWeight: '700',
                color: '#ff8c00',
                marginBottom: '8px'
              }}>
                95%
              </div>
              <div style={{
                fontSize: '16px',
                color: '#888',
                lineHeight: '1.4'
              }}>
                Kostenbesparing vs<br />traditionele medewerkers
              </div>
            </div>
          </div>

          <div style={{
            textAlign: 'center',
            marginTop: '40px',
            padding: '20px',
            backgroundColor: '#0a0a0a',
            borderRadius: '8px',
            border: '1px solid #444'
          }}>
            <p style={{
              fontSize: '16px',
              color: '#888',
              margin: 0
            }}>
              🚀 <strong style={{ color: '#ff8c00' }}>Beta fase</strong> - Sluit je aan bij pioniers die de toekomst van werk vormgeven
            </p>
          </div>
        </div>
      </section>
{/* Problem Section - Traditioneel vs Virtueel */}
      <section style={{
        padding: '80px 24px',
        backgroundColor: '#0a0a0a'
      }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
          <h3 style={{
            fontSize: '36px',
            fontWeight: '700',
            textAlign: 'center',
            marginBottom: '16px',
            background: 'linear-gradient(45deg, #ffffff, #ff8c00)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text'
          }}>
            Traditioneel vs Virtueel
          </h3>
          
          <p style={{
            fontSize: '18px',
            color: '#888',
            textAlign: 'center',
            marginBottom: '48px',
            maxWidth: '600px',
            margin: '0 auto 48px auto'
          }}>
            Waarom betalen voor dure traditionele medewerkers als je dezelfde resultaten kunt krijgen voor een fractie van de kosten?
          </p>

          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))',
            gap: '32px',
            alignItems: 'start'
          }}>
            {/* Traditional Workers */}
            <div style={{
              padding: '32px',
              backgroundColor: '#1a1a1a',
              borderRadius: '12px',
              border: '1px solid #444'
            }}>
              <h4 style={{
                fontSize: '24px',
                fontWeight: '600',
                marginBottom: '24px',
                color: '#ff6b6b',
                display: 'flex',
                alignItems: 'center',
                gap: '12px'
              }}>
                ❌ Traditionele Medewerkers
              </h4>
              <ul style={{
                listStyle: 'none',
                padding: 0,
                margin: 0
              }}>
                {[
                  { text: 'Salaris €3.500-€8.000 per maand', cost: '€42K-€96K/jaar' },
                  { text: 'Vakantiedagen & ziekteverlof', cost: '+€8K/jaar' },
                  { text: 'Werkt alleen kantooruren', cost: '40 uur/week' },
                  { text: 'Training & onboarding periode', cost: '3-6 maanden' },
                  { text: 'Menselijke fouten & emoties', cost: 'Variabele kwaliteit' },
                  { text: 'Opzegperiodes & contracten', cost: 'Juridische risico\'s' }
                ].map((item, index) => (
                  <li key={index} style={{
                    padding: '12px 0',
                    fontSize: '16px',
                    color: '#ccc',
                    borderBottom: index < 5 ? '1px solid #333' : 'none',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center'
                  }}>
                    <span>{item.text}</span>
                    <span style={{ fontSize: '14px', color: '#ff6b6b', fontWeight: '600' }}>
                      {item.cost}
                    </span>
                  </li>
                ))}
              </ul>
              
              <div style={{
                marginTop: '24px',
                padding: '16px',
                backgroundColor: '#2a1a1a',
                borderRadius: '8px',
                textAlign: 'center'
              }}>
                <div style={{ fontSize: '20px', fontWeight: '700', color: '#ff6b6b' }}>
                  Totaal: €60.000+ per jaar
                </div>
                <div style={{ fontSize: '14px', color: '#888', marginTop: '4px' }}>
                  Per medewerker, exclusief overhead
                </div>
              </div>
            </div>

            {/* Virtual Workers */}
            <div style={{
              padding: '32px',
              backgroundColor: '#1a1a1a',
              borderRadius: '12px',
              border: '2px solid #ff8c00',
              position: 'relative'
            }}>
              {/* Popular badge */}
              <div style={{
                position: 'absolute',
                top: '-12px',
                left: '50%',
                transform: 'translateX(-50%)',
                backgroundColor: '#ff8c00',
                color: '#000',
                padding: '4px 16px',
                borderRadius: '20px',
                fontSize: '12px',
                fontWeight: '600'
              }}>
                AANBEVOLEN
              </div>
              
              <h4 style={{
                fontSize: '24px',
                fontWeight: '600',
                marginBottom: '24px',
                color: '#00ff88',
                display: 'flex',
                alignItems: 'center',
                gap: '12px'
              }}>
                ✅ YokoAI Virtuele Medewerkers
              </h4>
              <ul style={{
                listStyle: 'none',
                padding: 0,
                margin: 0
              }}>
                {[
                  { text: 'Vanaf €29 per maand', cost: '€348/jaar' },
                  { text: 'Nooit ziek, nooit vakantie', cost: '0 downtime' },
                  { text: 'Werkt 24/7, 365 dagen per jaar', cost: '8.760 uur/jaar' },
                  { text: 'Direct productief, geen training', cost: 'Instant ROI' },
                  { text: 'Consistent & betrouwbaar', cost: '99.9% uptime' },
                  { text: 'Flexibel opschalen of afschalen', cost: 'Geen contracten' }
                ].map((item, index) => (
                  <li key={index} style={{
                    padding: '12px 0',
                    fontSize: '16px',
                    color: '#ccc',
                    borderBottom: index < 5 ? '1px solid #333' : 'none',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center'
                  }}>
                    <span>{item.text}</span>
                    <span style={{ fontSize: '14px', color: '#00ff88', fontWeight: '600' }}>
                      {item.cost}
                    </span>
                  </li>
                ))}
              </ul>
              
              <div style={{
                marginTop: '24px',
                padding: '16px',
                backgroundColor: '#1a2a1a',
                borderRadius: '8px',
                textAlign: 'center'
              }}>
                <div style={{ fontSize: '20px', fontWeight: '700', color: '#00ff88' }}>
                  Totaal: €348-€2.388 per jaar
                </div>
                <div style={{ fontSize: '14px', color: '#888', marginTop: '4px' }}>
                  Per specialist, inclusief alles
                </div>
              </div>
            </div>
          </div>

          {/* Cost Savings Highlight */}
          <div style={{
            textAlign: 'center',
            marginTop: '48px',
            padding: '32px',
            backgroundColor: '#1a1a1a',
            borderRadius: '12px',
            border: '2px solid #ff8c00',
            background: 'linear-gradient(135deg, #1a1a1a 0%, #2a1a0a 100%)'
          }}>
            <h4 style={{
              fontSize: '28px',
              fontWeight: '700',
              marginBottom: '16px',
              color: '#ff8c00'
            }}>
              💰 Kostenbesparing van 95%
            </h4>
            <p style={{
              fontSize: '18px',
              color: '#ccc',
              margin: 0,
              lineHeight: '1.6'
            }}>
              Een traditionele medewerker kost je <strong style={{ color: '#ff6b6b' }}>€60.000+ per jaar</strong>. 
              <br />Met YokoAI betaal je slechts <strong style={{ color: '#00ff88' }}>€348-€2.388 per jaar</strong> per specialist.
            </p>
            
            <div style={{
              marginTop: '24px',
              display: 'flex',
              justifyContent: 'center',
              gap: '16px',
              flexWrap: 'wrap'
            }}>
              <button style={{
                padding: '12px 24px',
                backgroundColor: '#ff8c00',
                border: 'none',
                borderRadius: '8px',
                color: '#000',
                cursor: 'pointer',
                fontSize: '16px',
                fontWeight: '600',
                transition: 'all 0.2s'
              }}
              onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#e67e00'}
              onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#ff8c00'}
              >
                Bereken Je Besparing
              </button>
              <button style={{
                padding: '12px 24px',
                backgroundColor: 'transparent',
                border: '1px solid #ff8c00',
                borderRadius: '8px',
                color: '#ff8c00',
                cursor: 'pointer',
                fontSize: '16px',
                transition: 'all 0.2s'
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.backgroundColor = '#ff8c00';
                e.currentTarget.style.color = '#000';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.backgroundColor = 'transparent';
                e.currentTarget.style.color = '#ff8c00';
              }}
              >
                Bekijk Voorbeelden
              </button>
            </div>
          </div>
        </div>
      </section>      
{/* AI Agents Showcase */}
<section style={{
        padding: '80px 24px',
        backgroundColor: '#111111'
      }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
          <h3 style={{
            fontSize: '36px',
            fontWeight: '700',
            textAlign: 'center',
            marginBottom: '16px',
            background: 'linear-gradient(45deg, #ffffff, #ff8c00)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text'
          }}>
            Ontmoet Je AI Specialisten
          </h3>
          
          <p style={{
            fontSize: '18px',
            color: '#888',
            textAlign: 'center',
            marginBottom: '48px',
            maxWidth: '700px',
            margin: '0 auto 48px auto'
          }}>
            Elke specialist is getraind voor specifieke taken en werkt volledig autonoom. 
            Kies wat je nodig hebt en schaal op wanneer je wilt.
          </p>

          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))',
            gap: '24px'
          }}>
            {agents.map((agent, index) => (
              <div
                key={index}
                style={{
                  padding: '24px',
                  backgroundColor: selectedAgent?.name === agent.name ? '#2a1a0a' : '#1a1a1a',
                  borderRadius: '12px',
                  border: selectedAgent?.name === agent.name ? '2px solid #ff8c00' : '1px solid #333',
                  cursor: 'pointer',
                  transition: 'all 0.3s ease',
                  transform: selectedAgent?.name === agent.name ? 'translateY(-4px)' : 'none',
                  boxShadow: selectedAgent?.name === agent.name ? '0 8px 32px rgba(255, 140, 0, 0.2)' : 'none'
                }}
                onClick={() => setSelectedAgent(selectedAgent?.name === agent.name ? null : agent)}
                onMouseEnter={(e) => {
                  if (selectedAgent?.name !== agent.name) {
                    e.currentTarget.style.backgroundColor = '#222';
                    e.currentTarget.style.transform = 'translateY(-2px)';
                  }
                }}
                onMouseLeave={(e) => {
                  if (selectedAgent?.name !== agent.name) {
                    e.currentTarget.style.backgroundColor = '#1a1a1a';
                    e.currentTarget.style.transform = 'translateY(0px)';
                  }
                }}
              >
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  marginBottom: '16px'
                }}>
                  <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '12px'
                  }}>
                    <div style={{
                      fontSize: '32px',
                      width: '48px',
                      height: '48px',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      backgroundColor: '#333',
                      borderRadius: '8px'
                    }}>
                      {agent.icon}
                    </div>
                    <div>
                      <h4 style={{
                        fontSize: '20px',
                        fontWeight: '600',
                        margin: 0,
                        color: '#fff'
                      }}>
                        {agent.name}
                      </h4>
                      <p style={{
                        fontSize: '14px',
                        color: '#ff8c00',
                        margin: 0,
                        fontWeight: '600'
                      }}>
                        {agent.role}
                      </p>
                    </div>
                  </div>
                  
                  <div style={{
                    textAlign: 'right'
                  }}>
                    <div style={{
                      fontSize: '24px',
                      fontWeight: '700',
                      color: '#ff8c00'
                    }}>
                      {agent.price}
                    </div>
                    <div style={{
                      fontSize: '12px',
                      color: '#888'
                    }}>
                      per maand
                    </div>
                  </div>
                </div>

                <p style={{
                  fontSize: '16px',
                  color: '#ccc',
                  marginBottom: '16px',
                  lineHeight: '1.5'
                }}>
                  {agent.description}
                </p>

                {/* Expandable Tasks */}
                {selectedAgent?.name === agent.name && (
                  <div style={{
                    marginTop: '16px',
                    padding: '16px',
                    backgroundColor: '#0a0a0a',
                    borderRadius: '8px',
                    border: '1px solid #ff8c00'
                  }}>
                    <h5 style={{
                      fontSize: '16px',
                      fontWeight: '600',
                      marginBottom: '12px',
                      color: '#ff8c00'
                    }}>
                      Typische Taken:
                    </h5>
                    <ul style={{
                      margin: 0,
                      paddingLeft: '16px',
                      color: '#ccc'
                    }}>
                      {agent.tasks.map((task, taskIndex) => (
                        <li key={taskIndex} style={{
                          marginBottom: '8px',
                          fontSize: '14px'
                        }}>
                          {task}
                        </li>
                      ))}
                    </ul>
                    
                    <div style={{
                      marginTop: '16px',
                      display: 'flex',
                      gap: '12px'
                    }}>
                      <button style={{
                        padding: '8px 16px',
                        backgroundColor: '#ff8c00',
                        border: 'none',
                        borderRadius: '6px',
                        color: '#000',
                        cursor: 'pointer',
                        fontSize: '14px',
                        fontWeight: '600',
                        flex: 1,
                        transition: 'all 0.2s'
                      }}
                      onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#e67e00'}
                      onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#ff8c00'}
                      >
                        Kies {agent.name}
                      </button>
                      <button style={{
                        padding: '8px 16px',
                        backgroundColor: 'transparent',
                        border: '1px solid #444',
                        borderRadius: '6px',
                        color: '#ccc',
                        cursor: 'pointer',
                        fontSize: '14px',
                        flex: 1,
                        transition: 'all 0.2s'
                      }}
                      onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#333'}
                      onMouseLeave={(e) => e.currentTarget.style.backgroundColor = 'transparent'}
                      >
                        Meer Info
                      </button>
                    </div>
                  </div>
                )}

                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  marginTop: '16px',
                  fontSize: '14px',
                  color: '#888'
                }}>
                  <span>
                    {selectedAgent?.name === agent.name ? 'Klik om te sluiten' : 'Klik voor details'}
                  </span>
                  <span style={{
                    transform: selectedAgent?.name === agent.name ? 'rotate(180deg)' : 'rotate(0deg)',
                    transition: 'transform 0.3s ease'
                  }}>
                    ↓
                  </span>
                </div>
              </div>
            ))}
          </div>

          {/* CTA beneath agents */}
          <div style={{
            textAlign: 'center',
            marginTop: '48px',
            padding: '32px',
            backgroundColor: '#0a0a0a',
            borderRadius: '12px',
            border: '1px solid #333'
          }}>
            <h4 style={{
              fontSize: '24px',
              fontWeight: '600',
              marginBottom: '16px',
              color: '#fff'
            }}>
              Klaar om je AI team samen te stellen?
            </h4>
            <p style={{
              fontSize: '16px',
              color: '#888',
              marginBottom: '24px'
            }}>
              Start met één specialist en bouw je perfecte team op basis van je behoeften.
            </p>
            
            <div style={{
              display: 'flex',
              justifyContent: 'center',
              gap: '16px',
              flexWrap: 'wrap'
            }}>
              <button style={{
                padding: '14px 28px',
                backgroundColor: '#ff8c00',
                border: 'none',
                borderRadius: '8px',
                color: '#000',
                cursor: 'pointer',
                fontSize: '16px',
                fontWeight: '600',
                transition: 'all 0.2s'
              }}
              onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#e67e00'}
              onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#ff8c00'}
              >
                Start Met 1 Specialist
              </button>
              <button style={{
                padding: '14px 28px',
                backgroundColor: 'transparent',
                border: '1px solid #ff8c00',
                borderRadius: '8px',
                color: '#ff8c00',
                cursor: 'pointer',
                fontSize: '16px',
                transition: 'all 0.2s'
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.backgroundColor = '#ff8c00';
                e.currentTarget.style.color = '#000';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.backgroundColor = 'transparent';
                e.currentTarget.style.color = '#ff8c00';
              }}
              >
                Bekijk Alle Prijzen
              </button>
            </div>
            
            <p style={{
              fontSize: '14px',
              color: '#666',
              marginTop: '16px',
              margin: '16px 0 0 0'
            }}>
              💡 Tip: Combineer Emma (Data) + Max (Sales) voor optimale resultaten
            </p>
          </div>
        </div>
      </section>      
{/* Pricing Section */}
<section style={{
        padding: '80px 24px',
        backgroundColor: '#0a0a0a'
      }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
          <h3 style={{
            fontSize: '36px',
            fontWeight: '700',
            textAlign: 'center',
            marginBottom: '16px',
            background: 'linear-gradient(45deg, #ffffff, #ff8c00)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text'
          }}>
            Kies Je Plan
          </h3>
          
          <p style={{
            fontSize: '18px',
            color: '#888',
            textAlign: 'center',
            marginBottom: '48px',
            maxWidth: '600px',
            margin: '0 auto 48px auto'
          }}>
            Transparante prijzen zonder verborgen kosten. Start klein en schaal op wanneer je groeit.
          </p>

          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))',
            gap: '24px',
            alignItems: 'stretch'
          }}>
            {pricingTiers.map((tier, index) => (
              <div
                key={index}
                style={{
                  padding: tier.popular ? '32px 24px' : '24px',
                  backgroundColor: tier.popular ? '#1a1a1a' : '#111111',
                  borderRadius: '12px',
                  border: tier.popular ? '2px solid #ff8c00' : '1px solid #333',
                  position: 'relative',
                  transform: tier.popular ? 'scale(1.05)' : 'scale(1)',
                  transition: 'all 0.3s ease'
                }}
                onMouseEnter={(e) => {
                  if (!tier.popular) {
                    e.currentTarget.style.transform = 'scale(1.02)';
                    e.currentTarget.style.backgroundColor = '#1a1a1a';
                  }
                }}
                onMouseLeave={(e) => {
                  if (!tier.popular) {
                    e.currentTarget.style.transform = 'scale(1)';
                    e.currentTarget.style.backgroundColor = '#111111';
                  }
                }}
              >
                {/* Popular Badge */}
                {tier.popular && (
                  <div style={{
                    position: 'absolute',
                    top: '-12px',
                    left: '50%',
                    transform: 'translateX(-50%)',
                    backgroundColor: '#ff8c00',
                    color: '#000',
                    padding: '6px 20px',
                    borderRadius: '20px',
                    fontSize: '12px',
                    fontWeight: '700',
                    textTransform: 'uppercase',
                    letterSpacing: '0.5px'
                  }}>
                    Meest Populair
                  </div>
                )}

                {/* Header */}
                <div style={{
                  textAlign: 'center',
                  marginBottom: '24px'
                }}>
                  <h4 style={{
                    fontSize: '24px',
                    fontWeight: '700',
                    marginBottom: '8px',
                    color: tier.popular ? '#ff8c00' : '#fff'
                  }}>
                    {tier.name}
                  </h4>
                  <p style={{
                    fontSize: '16px',
                    color: '#888',
                    marginBottom: '16px'
                  }}>
                    {tier.subtitle}
                  </p>
                  
                  <div style={{
                    display: 'flex',
                    alignItems: 'baseline',
                    justifyContent: 'center',
                    gap: '4px'
                  }}>
                    <span style={{
                      fontSize: '40px',
                      fontWeight: '700',
                      color: '#ff8c00'
                    }}>
                      {tier.price}
                    </span>
                    <span style={{
                      fontSize: '16px',
                      color: '#888'
                    }}>
                      {tier.period}
                    </span>
                  </div>
                  
                  {tier.name === 'Starter' && (
                    <p style={{
                      fontSize: '14px',
                      color: '#00ff88',
                      margin: '8px 0 0 0',
                      fontWeight: '600'
                    }}>
                      Eerste maand gratis!
                    </p>
                  )}
                </div>

                {/* Features */}
                <ul style={{
                  listStyle: 'none',
                  padding: 0,
                  margin: '0 0 32px 0'
                }}>
                  {tier.features.map((feature, featureIndex) => (
                    <li key={featureIndex} style={{
                      padding: '12px 0',
                      fontSize: '16px',
                      color: '#ccc',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '12px',
                      borderBottom: featureIndex < tier.features.length - 1 ? '1px solid #333' : 'none'
                    }}>
                      <div style={{
                        width: '20px',
                        height: '20px',
                        backgroundColor: tier.popular ? '#ff8c00' : '#00ff88',
                        borderRadius: '50%',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: '12px',
                        color: '#000',
                        fontWeight: '700',
                        flexShrink: 0
                      }}>
                        ✓
                      </div>
                      <span>{feature}</span>
                    </li>
                  ))}
                </ul>

                {/* CTA Button */}
                <button style={{
                  width: '100%',
                  padding: '16px',
                  backgroundColor: tier.popular ? '#ff8c00' : 'transparent',
                  border: tier.popular ? 'none' : '2px solid #ff8c00',
                  borderRadius: '8px',
                  color: tier.popular ? '#000' : '#ff8c00',
                  cursor: 'pointer',
                  fontSize: '16px',
                  fontWeight: '700',
                  transition: 'all 0.2s',
                  textTransform: 'uppercase',
                  letterSpacing: '0.5px'
                }}
                onMouseEnter={(e) => {
                  if (tier.popular) {
                    e.currentTarget.style.backgroundColor = '#e67e00';
                  } else {
                    e.currentTarget.style.backgroundColor = '#ff8c00';
                    e.currentTarget.style.color = '#000';
                  }
                }}
                onMouseLeave={(e) => {
                  if (tier.popular) {
                    e.currentTarget.style.backgroundColor = '#ff8c00';
                  } else {
                    e.currentTarget.style.backgroundColor = 'transparent';
                    e.currentTarget.style.color = '#ff8c00';
                  }
                }}
              >
                {tier.cta}
              </button>

              {/* Additional Info */}
              <p style={{
                fontSize: '12px',
                color: '#666',
                textAlign: 'center',
                marginTop: '12px',
                margin: '12px 0 0 0'
              }}>
                {tier.name === 'Starter' && 'Geen verborgen kosten'}
                {tier.name === 'Professional' && 'Ideaal voor groeiende teams'}
                {tier.name === 'Business' && 'Voor enterprise organisaties'}
              </p>
              </div>
            ))}
          </div>

          {/* Bottom Section */}
          <div style={{
            marginTop: '48px',
            textAlign: 'center',
            padding: '32px',
            backgroundColor: '#111111',
            borderRadius: '12px',
            border: '1px solid #333'
          }}>
            <h4 style={{
              fontSize: '20px',
              fontWeight: '600',
              marginBottom: '16px',
              color: '#fff'
            }}>
              🤔 Niet zeker welk plan je nodig hebt?
            </h4>
            <p style={{
              fontSize: '16px',
              color: '#888',
              marginBottom: '24px'
            }}>
              Start met de gratis proefperiode en ontdek welke AI specialisten het beste bij je passen.
            </p>
            
            <div style={{
              display: 'flex',
              justifyContent: 'center',
              gap: '16px',
              flexWrap: 'wrap'
            }}>
              <button style={{
                padding: '12px 24px',
                backgroundColor: '#ff8c00',
                border: 'none',
                borderRadius: '8px',
                color: '#000',
                cursor: 'pointer',
                fontSize: '16px',
                fontWeight: '600',
                transition: 'all 0.2s'
              }}
              onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#e67e00'}
              onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#ff8c00'}
              >
                Plan een Demo
              </button>
              <button style={{
                padding: '12px 24px',
                backgroundColor: 'transparent',
                border: '1px solid #444',
                borderRadius: '8px',
                color: '#ccc',
                cursor: 'pointer',
                fontSize: '16px',
                transition: 'all 0.2s'
              }}
              onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#333'}
              onMouseLeave={(e) => e.currentTarget.style.backgroundColor = 'transparent'}
              >
                Vergelijk Plannen
              </button>
            </div>
            
            <div style={{
              display: 'flex',
              justifyContent: 'center',
              gap: '32px',
              marginTop: '24px',
              flexWrap: 'wrap'
            }}>
              <div style={{ fontSize: '14px', color: '#888' }}>
                ✓ Geen setup kosten
              </div>
              <div style={{ fontSize: '14px', color: '#888' }}>
                ✓ Maandelijks opzegbaar
              </div>
              <div style={{ fontSize: '14px', color: '#888' }}>
                ✓ 24/7 support
              </div>
            </div>
          </div>
        </div>
      </section>
{/* FAQ Section */}
<section style={{
        padding: '80px 24px',
        backgroundColor: '#111111'
      }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <h3 style={{
            fontSize: '36px',
            fontWeight: '700',
            textAlign: 'center',
            marginBottom: '16px',
            background: 'linear-gradient(45deg, #ffffff, #ff8c00)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text'
          }}>
            Veelgestelde Vragen
          </h3>
          
          <p style={{
            fontSize: '18px',
            color: '#888',
            textAlign: 'center',
            marginBottom: '48px'
          }}>
            Alles wat je wilt weten over YokoAI en onze AI specialisten.
          </p>

          <div style={{
            display: 'flex',
            flexDirection: 'column',
            gap: '16px'
          }}>
            {[
              {
                question: "Hoe werkt YokoAI precies?",
                answer: "YokoAI levert volledig autonome AI specialisten die specifieke taken voor je uitvoeren. In tegenstelling tot chatbots die alleen antwoorden geven, voeren onze AI agents daadwerkelijk werk uit: ze schrijven rapporten, verwerken data, beheren leads, creëren content en veel meer. Je geeft ze toegang tot je tools en systemen, en zij doen de rest."
              },
              {
                question: "Is er een gratis proefperiode?",
                answer: "Ja! Je krijgt een volledige maand gratis om YokoAI uit te proberen. Geen creditcard nodig tijdens de proefperiode. Je kunt een AI specialist kiezen en alle functies testen. Na de proefperiode kun je kiezen welk plan het beste bij je past."
              },
              {
                question: "Kan ik opzeggen wanneer ik wil?",
                answer: "Absoluut. Alle onze plannen zijn maandelijks opzegbaar zonder opzegtermijn. Je betaalt alleen voor de maanden dat je onze service gebruikt. Er zijn geen verborgen kosten of boetes voor vroegtijdige opzegging."
              },
              {
                question: "Welke taken kunnen AI specialisten uitvoeren?",
                answer: "Onze AI specialisten kunnen vrijwel elke digitale taak uitvoeren: data-analyse, lead management, content creatie, customer support, HR taken, operationele rapportages, social media management, email marketing, en veel meer. Ze integreren met je bestaande tools zoals Gmail, Slack, CRM-systemen, en databases."
              },
              {
                question: "Is mijn bedrijfsdata veilig?",
                answer: "Ja, data veiligheid staat bij ons voorop. We zijn GDPR-compliant, gebruiken enterprise-grade encryptie, en je data wordt nooit gedeeld met derden. Onze AI specialisten werken alleen met de data die je expliciet toegankelijk maakt en binnen de grenzen die je instelt."
              },
              {
                question: "Kan ik meerdere AI specialisten hebben?",
                answer: "Ja! Afhankelijk van je plan kun je meerdere specialisten hebben. Met het Professional plan krijg je tot 3 specialisten, en met het Business plan zijn er geen limieten. Je kunt specialisten combineren voor optimale resultaten, zoals Emma (Data) + Max (Sales) voor complete sales intelligence."
              },
              {
                question: "Hoe verschillen jullie van gewone chatbots?",
                answer: "Chatbots geven alleen antwoorden op vragen. Onze AI specialisten voeren daadwerkelijk werk uit en leveren concrete resultaten. Ze kunnen zelfstandig taken uitvoeren, beslissingen nemen binnen vooraf ingestelde parameters, en complete workflows beheren zonder constante supervisie."
              },
              {
                question: "Welke support krijg ik?",
                answer: "Alle plannen include support. Starter krijgt email support, Professional heeft live chat, en Business klanten krijgen een dedicated account manager. Daarnaast hebben we uitgebreide documentatie, video tutorials, en een actieve community waar je terecht kunt voor tips en best practices."
              }
            ].map((faq, index) => (
              <div
                key={index}
                style={{
                  backgroundColor: '#1a1a1a',
                  borderRadius: '12px',
                  border: expandedFAQ === index ? '1px solid #ff8c00' : '1px solid #333',
                  overflow: 'hidden',
                  transition: 'all 0.3s ease'
                }}
              >
                <button
                  style={{
                    width: '100%',
                    padding: '20px 24px',
                    backgroundColor: 'transparent',
                    border: 'none',
                    textAlign: 'left',
                    cursor: 'pointer',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    fontSize: '18px',
                    fontWeight: '600',
                    color: expandedFAQ === index ? '#ff8c00' : '#fff',
                    transition: 'all 0.2s ease'
                  }}
                  onClick={() => setExpandedFAQ(expandedFAQ === index ? null : index)}
                  onMouseEnter={(e) => {
                    if (expandedFAQ !== index) {
                      e.currentTarget.style.color = '#ff8c00';
                    }
                  }}
                  onMouseLeave={(e) => {
                    if (expandedFAQ !== index) {
                      e.currentTarget.style.color = '#fff';
                    }
                  }}
                >
                  <span style={{ flex: 1, paddingRight: '16px' }}>
                    {faq.question}
                  </span>
                  <div style={{
                    width: '24px',
                    height: '24px',
                    borderRadius: '50%',
                    backgroundColor: expandedFAQ === index ? '#ff8c00' : '#333',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontSize: '14px',
                    color: expandedFAQ === index ? '#000' : '#888',
                    transform: expandedFAQ === index ? 'rotate(180deg)' : 'rotate(0deg)',
                    transition: 'all 0.3s ease'
                  }}>
                    ↓
                  </div>
                </button>

                <div style={{
                  maxHeight: expandedFAQ === index ? '500px' : '0px',
                  overflow: 'hidden',
                  transition: 'max-height 0.3s ease'
                }}>
                  <div style={{
                    padding: '0 24px 24px 24px',
                    fontSize: '16px',
                    color: '#ccc',
                    lineHeight: '1.6',
                    borderTop: '1px solid #333'
                  }}>
                    <div style={{ paddingTop: '20px' }}>
                      {faq.answer}
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Bottom CTA */}
          <div style={{
            marginTop: '48px',
            textAlign: 'center',
            padding: '32px',
            backgroundColor: '#0a0a0a',
            borderRadius: '12px',
            border: '1px solid #333'
          }}>
            <h4 style={{
              fontSize: '24px',
              fontWeight: '600',
              marginBottom: '16px',
              color: '#fff'
            }}>
              Nog meer vragen?
            </h4>
            <p style={{
              fontSize: '16px',
              color: '#888',
              marginBottom: '24px'
            }}>
              Ons team staat klaar om al je vragen over YokoAI te beantwoorden.
            </p>
            
            <div style={{
              display: 'flex',
              justifyContent: 'center',
              gap: '16px',
              flexWrap: 'wrap'
            }}>
              <button style={{
                padding: '12px 24px',
                backgroundColor: '#ff8c00',
                border: 'none',
                borderRadius: '8px',
                color: '#000',
                cursor: 'pointer',
                fontSize: '16px',
                fontWeight: '600',
                transition: 'all 0.2s'
              }}
              onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#e67e00'}
              onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#ff8c00'}
              >
                📧 Contact Opnemen
              </button>
              <button style={{
                padding: '12px 24px',
                backgroundColor: 'transparent',
                border: '1px solid #444',
                borderRadius: '8px',
                color: '#ccc',
                cursor: 'pointer',
                fontSize: '16px',
                transition: 'all 0.2s'
              }}
              onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#333'}
              onMouseLeave={(e) => e.currentTarget.style.backgroundColor = 'transparent'}
              >
                💬 Live Chat
              </button>
            </div>

            <div style={{
              marginTop: '24px',
              fontSize: '14px',
              color: '#666',
              display: 'flex',
              justifyContent: 'center',
              gap: '24px',
              flexWrap: 'wrap'
            }}>
              <span>📞 +31 20 123 4567</span>
              <span>✉️ hello@yokoai.nl</span>
              <span>⏰ Ma-Vr 9:00-18:00</span>
            </div>
          </div>
        </div>
      </section>
{/* Final CTA Section */}
<section style={{
        padding: '80px 24px',
        background: 'linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0a0a0a 100%)',
        position: 'relative',
        overflow: 'hidden'
      }}>
        {/* Background Pattern */}
        <div style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundImage: `radial-gradient(circle at 20% 20%, rgba(255, 140, 0, 0.1) 0%, transparent 50%),
                           radial-gradient(circle at 80% 80%, rgba(255, 140, 0, 0.1) 0%, transparent 50%)`,
          pointerEvents: 'none'
        }}></div>

        <div style={{ maxWidth: '1000px', margin: '0 auto', textAlign: 'center', position: 'relative' }}>
          <h3 style={{
            fontSize: '42px',
            fontWeight: '700',
            marginBottom: '24px',
            background: 'linear-gradient(45deg, #ffffff, #ff8c00)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
            lineHeight: '1.2'
          }}>
            Klaar om je eerste AI medewerker<br />aan het werk te zetten?
          </h3>
          
          <p style={{
            fontSize: '20px',
            color: '#888',
            marginBottom: '32px',
            maxWidth: '700px',
            margin: '0 auto 32px auto',
            lineHeight: '1.6'
          }}>
            Sluit je aan bij de pioniers die hun bedrijf transformeren met autonome AI specialisten. 
            Start vandaag nog en ervaar het verschil.
          </p>

          {/* Trust Indicators */}
          <div style={{
            display: 'flex',
            justifyContent: 'center',
            gap: '32px',
            marginBottom: '48px',
            flexWrap: 'wrap'
          }}>
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              padding: '8px 16px',
              backgroundColor: '#1a1a1a',
              borderRadius: '20px',
              border: '1px solid #333'
            }}>
              <div style={{
                width: '8px',
                height: '8px',
                backgroundColor: '#00ff88',
                borderRadius: '50%'
              }}></div>
              <span style={{ fontSize: '14px', color: '#888' }}>99.9% Uptime</span>
            </div>
            
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              padding: '8px 16px',
              backgroundColor: '#1a1a1a',
              borderRadius: '20px',
              border: '1px solid #333'
            }}>
              <span style={{ fontSize: '14px', color: '#888' }}>🔒 GDPR Compliant</span>
            </div>
            
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              padding: '8px 16px',
              backgroundColor: '#1a1a1a',
              borderRadius: '20px',
              border: '1px solid #333'
            }}>
              <span style={{ fontSize: '14px', color: '#888' }}>⚡ Enterprise Ready</span>
            </div>
          </div>

          {/* Main CTA Buttons */}
          <div style={{
            display: 'flex',
            justifyContent: 'center',
            gap: '20px',
            marginBottom: '32px',
            flexWrap: 'wrap'
          }}>
            <button style={{
              padding: '18px 36px',
              backgroundColor: '#ff8c00',
              border: 'none',
              borderRadius: '12px',
              color: '#000',
              cursor: 'pointer',
              fontSize: '18px',
              fontWeight: '700',
              transition: 'all 0.3s ease',
              boxShadow: '0 8px 32px rgba(255, 140, 0, 0.3)',
              textTransform: 'uppercase',
              letterSpacing: '0.5px'
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.backgroundColor = '#e67e00';
              e.currentTarget.style.transform = 'translateY(-3px)';
              e.currentTarget.style.boxShadow = '0 12px 40px rgba(255, 140, 0, 0.4)';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.backgroundColor = '#ff8c00';
              e.currentTarget.style.transform = 'translateY(0px)';
              e.currentTarget.style.boxShadow = '0 8px 32px rgba(255, 140, 0, 0.3)';
            }}
            >
              🚀 Start Gratis Proefperiode
            </button>
            
            <button style={{
              padding: '18px 36px',
              backgroundColor: 'transparent',
              border: '2px solid #ff8c00',
              borderRadius: '12px',
              color: '#ff8c00',
              cursor: 'pointer',
              fontSize: '18px',
              fontWeight: '600',
              transition: 'all 0.3s ease'
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.backgroundColor = 'rgba(255, 140, 0, 0.1)';
              e.currentTarget.style.transform = 'translateY(-3px)';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.backgroundColor = 'transparent';
              e.currentTarget.style.transform = 'translateY(0px)';
            }}
            >
              📅 Plan een Demo
            </button>
          </div>

          {/* Urgency Element */}
          <div style={{
            padding: '20px',
            backgroundColor: '#1a1a1a',
            borderRadius: '12px',
            border: '1px solid #ff8c00',
            marginBottom: '32px',
            background: 'linear-gradient(135deg, #1a1a1a 0%, #2a1a0a 100%)'
          }}>
            <p style={{
              fontSize: '16px',
              color: '#ff8c00',
              margin: 0,
              fontWeight: '600'
            }}>
              🔥 <strong>Beta Launch Aanbieding:</strong> Eerste 100 klanten krijgen 50% korting de eerste 3 maanden
            </p>
          </div>
          {/* Bottom Stats */}
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
            gap: '24px',
            maxWidth: '600px',
            margin: '0 auto'
          }}>
            <div style={{ textAlign: 'center' }}>
              <div style={{
                fontSize: '24px',
                fontWeight: '700',
                color: '#ff8c00',
                marginBottom: '4px'
              }}>
                5 min
              </div>
              <div style={{ fontSize: '14px', color: '#888' }}>
                Setup tijd
              </div>
            </div>
            
            <div style={{ textAlign: 'center' }}>
              <div style={{
                fontSize: '24px',
                fontWeight: '700',
                color: '#ff8c00',
                marginBottom: '4px'
              }}>
                0€
              </div>
              <div style={{ fontSize: '14px', color: '#888' }}>
                Setup kosten
              </div>
            </div>
            
            <div style={{ textAlign: 'center' }}>
              <div style={{
                fontSize: '24px',
                fontWeight: '700',
                color: '#ff8c00',
                marginBottom: '4px'
              }}>
                Altijd
              </div>
              <div style={{ fontSize: '14px', color: '#888' }}>
                Opzegbaar
              </div>
            </div>
          </div>

          {/* Final Note */}
          <p style={{
            fontSize: '14px',
            color: '#666',
            marginTop: '32px',
            lineHeight: '1.5'
          }}>
            Geen creditcard vereist voor de proefperiode • 30 dagen geld-terug-garantie
          </p>
        </div>
      </section>      
      {/* Footer */}
      <footer style={{
        padding: '40px 24px',
        backgroundColor: '#111111',
        borderTop: '1px solid #333'
      }}>
        <div style={{
          maxWidth: '1200px',
          margin: '0 auto',
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
          gap: '32px'
        }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px' }}>
              <YokoLogo size={32} variant="compact" />
              <span style={{
                fontSize: '18px',
                fontWeight: '600',
                background: 'linear-gradient(45deg, #ffffff, #ff8c00)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                backgroundClip: 'text'
              }}>
                YokoAI
              </span>
            </div>
            <p style={{
              fontSize: '14px',
              color: '#888',
              lineHeight: '1.6'
            }}>
              De toekomst van werk is hier. Bouw je perfecte AI team en automatiseer je bedrijfsprocessen met YokoAI.
            </p>
          </div>

          <div>
            <h4 style={{
              fontSize: '16px',
              fontWeight: '600',
              marginBottom: '16px',
              color: '#fff'
            }}>
              Product
            </h4>
            <ul style={{
              margin: 0,
              padding: 0,
              listStyle: 'none'
            }}>
              {['AI Specialisten', 'Pricing', 'Demo', 'Documentatie'].map((item, index) => (
                <li key={index} style={{ marginBottom: '8px' }}>
                  <a href="#" style={{
                    fontSize: '14px',
                    color: '#888',
                    textDecoration: 'none',
                    transition: 'color 0.2s'
                  }}
                  onMouseEnter={(e) => e.currentTarget.style.color = '#ff8c00'}
                  onMouseLeave={(e) => e.currentTarget.style.color = '#888'}
                  >
                    {item}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h4 style={{
              fontSize: '16px',
              fontWeight: '600',
              marginBottom: '16px',
              color: '#fff'
            }}>
              Bedrijf
            </h4>
            <ul style={{
              margin: 0,
              padding: 0,
              listStyle: 'none'
            }}>
              {['Over Ons', 'Careers', 'Contact', 'Privacy'].map((item, index) => (
                <li key={index} style={{ marginBottom: '8px' }}>
                  <a href="#" style={{
                    fontSize: '14px',
                    color: '#888',
                    textDecoration: 'none',
                    transition: 'color 0.2s'
                  }}
                  onMouseEnter={(e) => e.currentTarget.style.color = '#ff8c00'}
                  onMouseLeave={(e) => e.currentTarget.style.color = '#888'}
                  >
                    {item}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h4 style={{
              fontSize: '16px',
              fontWeight: '600',
              marginBottom: '16px',
              color: '#fff'
            }}>
              Support
            </h4>
            <ul style={{
              margin: 0,
              padding: 0,
              listStyle: 'none'
            }}>
              {['Help Center', 'API Docs', 'Status', 'Community'].map((item, index) => (
                <li key={index} style={{ marginBottom: '8px' }}>
                  <a href="#" style={{
                    fontSize: '14px',
                    color: '#888',
                    textDecoration: 'none',
                    transition: 'color 0.2s'
                  }}
                  onMouseEnter={(e) => e.currentTarget.style.color = '#ff8c00'}
                  onMouseLeave={(e) => e.currentTarget.style.color = '#888'}
                  >
                    {item}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div style={{
          borderTop: '1px solid #333',
          marginTop: '32px',
          paddingTop: '24px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '16px'
        }}>
          <p style={{
            fontSize: '14px',
            color: '#666',
            margin: 0
          }}>
            © 2025 YokoAI by VDM Nexus. Alle rechten voorbehouden.
          </p>
          
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
            <span style={{
              fontSize: '14px',
              color: '#888'
            }}>
              Alle systemen operationeel
            </span>
          </div>
        </div>
      </footer>
    </div>
  );
}