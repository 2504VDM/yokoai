'use client';

import React, { useState, useEffect } from 'react';

export default function VDMNexusLanding() {
  const [isHovered, setIsHovered] = useState(false);
  const [backendData, setBackendData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8080/api/vandermeulen')
      .then(res => res.json())
      .then(data => {
        console.log('Backend data:', data);
        setBackendData(data);
      })
      .catch(err => console.log('Backend error:', err));
  }, []);

  return (
    <main style={{
      minHeight: '100vh',
      backgroundColor: '#0a0a0a',
      color: '#ffffff',
      padding: '0 20px'
    }}>
      <div style={{
        maxWidth: '1200px',
        margin: '0 auto',
        paddingTop: '80px'
      }}>
        
        {/* Navigation */}
        <nav style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          marginBottom: '80px'
        }}>
          <div style={{
            fontSize: '28px',
            fontWeight: 'bold',
            background: 'linear-gradient(135deg, #00ff88, #0066ff)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent'
          }}>
            VDM Nexus
          </div>
          
          <div style={{ display: 'flex', gap: '32px', alignItems: 'center' }}>
            <a href="#platform" style={{ color: '#9ca3af', textDecoration: 'none' }}>Platform</a>
            <a href="#pricing" style={{ color: '#9ca3af', textDecoration: 'none' }}>Pricing</a>
            <a href="#contact" style={{ color: '#9ca3af', textDecoration: 'none' }}>Contact</a>
            <button style={{
              backgroundColor: '#00ff88',
              color: '#000',
              padding: '12px 24px',
              borderRadius: '8px',
              border: 'none',
              fontWeight: '600',
              cursor: 'pointer'
            }}>
              Get Demo
            </button>
          </div>
        </nav>

        {/* Hero Section */}
        <div style={{ textAlign: 'center', marginBottom: '120px' }}>
          <div style={{
            fontSize: '64px',
            fontWeight: 'bold',
            lineHeight: '1.1',
            marginBottom: '24px',
            background: 'linear-gradient(135deg, #ffffff, #9ca3af)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent'
          }}>
            Transform Knowledge into
            <br />
            <span style={{
              background: 'linear-gradient(135deg, #00ff88, #0066ff)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent'
            }}>
              Competitive Intelligence
            </span>
          </div>
          
          <p style={{
            fontSize: '24px',
            color: '#9ca3af',
            marginBottom: '48px',
            maxWidth: '800px',
            margin: '0 auto 48px auto'
          }}>
            Business Intelligence Platform waar elke Nederlandse enterprise client 
            <br />een gepersonaliseerd subdomain krijgt met AI getraind op bedrijfskennis
          </p>

          <button
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            style={{
              backgroundColor: isHovered ? '#00ff88' : '#0066ff',
              padding: '20px 40px',
              color: isHovered ? '#000' : '#fff',
              borderRadius: '12px',
              fontWeight: '600',
              fontSize: '20px',
              border: 'none',
              cursor: 'pointer',
              transition: 'all 0.3s ease',
              transform: isHovered ? 'scale(1.05)' : 'scale(1)'
            }}
          >
            Schedule Enterprise Demo
          </button>
        </div>

        {/* Pricing Section */}
        <div id="pricing" style={{ marginBottom: '120px' }}>
          <h2 style={{
            fontSize: '48px',
            fontWeight: 'bold',
            textAlign: 'center',
            marginBottom: '64px'
          }}>
            Enterprise Pricing
          </h2>
          
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
            gap: '32px',
            maxWidth: '1000px',
            margin: '0 auto'
          }}>
            {/* Intelligence Starter */}
            <div style={{
              backgroundColor: '#1f2937',
              padding: '32px',
              borderRadius: '16px',
              textAlign: 'center'
            }}>
              <h3 style={{
                fontSize: '24px',
                fontWeight: '600',
                marginBottom: '16px'
              }}>
                Intelligence Starter
              </h3>
              <div style={{
                fontSize: '48px',
                fontWeight: 'bold',
                color: '#00ff88',
                marginBottom: '24px'
              }}>
                €499<span style={{ fontSize: '18px', color: '#9ca3af' }}>/maand</span>
              </div>
              <div style={{ textAlign: 'left', color: '#9ca3af' }}>
                <div style={{ marginBottom: '12px' }}>✅ Custom subdomain</div>
                <div style={{ marginBottom: '12px' }}>✅ 4 business functions</div>
                <div style={{ marginBottom: '12px' }}>✅ Basic knowledge training</div>
                <div style={{ marginBottom: '12px' }}>✅ Email support</div>
              </div>
            </div>

            {/* Business Intelligence */}
            <div style={{
              backgroundColor: '#1f2937',
              padding: '32px',
              borderRadius: '16px',
              textAlign: 'center',
              border: '2px solid #00ff88'
            }}>
              <div style={{
                backgroundColor: '#00ff88',
                color: '#000',
                padding: '8px 16px',
                borderRadius: '20px',
                fontSize: '14px',
                fontWeight: '600',
                display: 'inline-block',
                marginBottom: '16px'
              }}>
                MOST POPULAR
              </div>
              <h3 style={{
                fontSize: '24px',
                fontWeight: '600',
                marginBottom: '16px'
              }}>
                Business Intelligence
              </h3>
              <div style={{
                fontSize: '48px',
                fontWeight: 'bold',
                color: '#00ff88',
                marginBottom: '24px'
              }}>
                €1.299<span style={{ fontSize: '18px', color: '#9ca3af' }}>/maand</span>
              </div>
              <div style={{ textAlign: 'left', color: '#9ca3af' }}>
                <div style={{ marginBottom: '12px' }}>✅ All Starter features</div>
                <div style={{ marginBottom: '12px' }}>✅ 8 business functions</div>
                <div style={{ marginBottom: '12px' }}>✅ Advanced knowledge training</div>
                <div style={{ marginBottom: '12px' }}>✅ Priority support</div>
                <div style={{ marginBottom: '12px' }}>✅ Custom integrations</div>
              </div>
            </div>

            {/* Enterprise Intelligence */}
            <div style={{
              backgroundColor: '#1f2937',
              padding: '32px',
              borderRadius: '16px',
              textAlign: 'center'
            }}>
              <h3 style={{
                fontSize: '24px',
                fontWeight: '600',
                marginBottom: '16px'
              }}>
                Enterprise Intelligence
              </h3>
              <div style={{
                fontSize: '48px',
                fontWeight: 'bold',
                color: '#00ff88',
                marginBottom: '24px'
              }}>
                €3.999<span style={{ fontSize: '18px', color: '#9ca3af' }}>/maand</span>
              </div>
              <div style={{ textAlign: 'left', color: '#9ca3af' }}>
                <div style={{ marginBottom: '12px' }}>✅ All Business features</div>
                <div style={{ marginBottom: '12px' }}>✅ Unlimited functions</div>
                <div style={{ marginBottom: '12px' }}>✅ Deep knowledge training</div>
                <div style={{ marginBottom: '12px' }}>✅ 24/7 dedicated support</div>
                <div style={{ marginBottom: '12px' }}>✅ Multi-tenant management</div>
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div style={{
          textAlign: 'center',
          paddingTop: '40px',
          borderTop: '1px solid #374151',
          color: '#6b7280',
          fontSize: '14px'
        }}>
          <div>
            © 2025 VDM Nexus B.V. - Business Intelligence Platform
          </div>
        </div>
      </div>
    </main>
  );
}