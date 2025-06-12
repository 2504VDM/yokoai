'use client';

import React from 'react';

interface YokoLogoProps {
  size?: number;
  variant?: 'compact' | 'full';
  className?: string;
}

// Compact logo voor chat headers en kleine ruimtes
const YokoCompactLogo: React.FC<{ size: number }> = ({ size }) => (
  <svg 
    width={size} 
    height={size} 
    viewBox="0 0 100 100" 
    style={{ flexShrink: 0 }}
  >
    <g strokeLinecap="round" strokeLinejoin="round">
      {/* Diagonale lijnen patroon */}
      <line x1="15" y1="15" x2="35" y2="35" stroke="#ffffff" strokeWidth="3"/>
      <line x1="20" y1="10" x2="40" y2="30" stroke="#ffffff" strokeWidth="3"/>
      <line x1="25" y1="15" x2="45" y2="35" stroke="#ff8c00" strokeWidth="4"/>
      <line x1="30" y1="20" x2="50" y2="40" stroke="#ffffff" strokeWidth="3"/>
      <line x1="35" y1="25" x2="55" y2="45" stroke="#ffffff" strokeWidth="3"/>
      
      {/* Counter diagonale lijnen */}
      <line x1="15" y1="85" x2="35" y2="65" stroke="#ffffff" strokeWidth="3"/>
      <line x1="20" y1="90" x2="40" y2="70" stroke="#ffffff" strokeWidth="3"/>
      <line x1="25" y1="85" x2="45" y2="65" stroke="#ff8c00" strokeWidth="4"/>
      <line x1="30" y1="80" x2="50" y2="60" stroke="#ffffff" strokeWidth="3"/>
      <line x1="35" y1="75" x2="55" y2="55" stroke="#ffffff" strokeWidth="3"/>
      
      {/* Accent elements */}
      <circle cx="70" cy="30" r="4" fill="#ff8c00"/>
      <circle cx="30" cy="70" r="4" fill="#333333"/>
      <circle cx="85" cy="15" r="2" fill="#ffffff"/>
      <circle cx="15" cy="85" r="2" fill="#ffffff"/>
    </g>
  </svg>
);

// Full logo voor landingspages
const YokoFullLogo: React.FC<{ size: number }> = ({ size }) => (
  <svg 
    width={size} 
    height={size * 0.4} 
    viewBox="0 0 500 200" 
    style={{ flexShrink: 0 }}
  >
    <g strokeLinecap="round" strokeLinejoin="round">
      {/* Icon deel */}
      <line x1="15" y1="30" x2="45" y2="60" stroke="#ffffff" strokeWidth="4"/>
      <line x1="25" y1="20" x2="55" y2="50" stroke="#ffffff" strokeWidth="4"/>
      <line x1="35" y1="30" x2="65" y2="60" stroke="#ff8c00" strokeWidth="5"/>
      <line x1="45" y1="40" x2="75" y2="70" stroke="#ffffff" strokeWidth="4"/>
      <line x1="55" y1="50" x2="85" y2="80" stroke="#ffffff" strokeWidth="4"/>
      
      <line x1="15" y1="110" x2="45" y2="80" stroke="#ffffff" strokeWidth="4"/>
      <line x1="25" y1="120" x2="55" y2="90" stroke="#ffffff" strokeWidth="4"/>
      <line x1="35" y1="130" x2="65" y2="100" stroke="#ff8c00" strokeWidth="5"/>
      <line x1="45" y1="140" x2="75" y2="110" stroke="#ffffff" strokeWidth="4"/>
      <line x1="55" y1="150" x2="85" y2="120" stroke="#ffffff" strokeWidth="4"/>
      
      <circle cx="100" cy="60" r="6" fill="#ff8c00"/>
      <circle cx="60" cy="120" r="6" fill="#333333"/>
    </g>
    
    {/* YokoAI tekst */}
    <text x="140" y="80" fill="#ffffff" fontSize="48" fontWeight="700" fontFamily="Arial, sans-serif">
      YokoAI
    </text>
    
    {/* Tagline */}
    <text x="140" y="110" fill="#999999" fontSize="14" fontFamily="Arial, sans-serif">
      YOUR VIRTUAL EMPLOYEE THAT DELIVERS.
    </text>
  </svg>
);

const YokoLogo: React.FC<YokoLogoProps> = ({ 
  size = 40, 
  variant = 'compact', 
  className = '' 
}) => {
  return (
    <div className={className}>
      {variant === 'compact' ? (
        <YokoCompactLogo size={size} />
      ) : (
        <YokoFullLogo size={size} />
      )}
    </div>
  );
};

export default YokoLogo;