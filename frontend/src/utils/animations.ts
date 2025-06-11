// src/lib/animations.ts
// Fix voor animation loading issues

import { useEffect, useRef } from 'react'

// Hook voor fade-in animaties
export const useFadeIn = (delay: number = 0) => {
  const ref = useRef<HTMLElement>(null)

  useEffect(() => {
    const element = ref.current
    if (!element) return

    // Reset initial state
    element.style.opacity = '0'
    element.style.transform = 'translateY(20px)'
    element.style.transition = 'opacity 0.6s ease, transform 0.6s ease'

    // Trigger animation na delay
    const timer = setTimeout(() => {
      element.style.opacity = '1'
      element.style.transform = 'translateY(0)'
    }, delay)

    return () => clearTimeout(timer)
  }, [delay])

  return ref
}

// Observer voor scroll-based animaties
export const useScrollAnimation = (threshold: number = 0.1) => {
  const ref = useRef<HTMLElement>(null)

  useEffect(() => {
    const element = ref.current
    if (!element) return

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animate-fade-in')
            observer.unobserve(entry.target)
          }
        })
      },
      { threshold }
    )

    observer.observe(element)

    return () => observer.disconnect()
  }, [threshold])

  return ref
}

// Performance optimized animation classes
export const animationClasses = {
  fadeIn: 'animate-fade-in',
  slideUp: 'animate-slide-up', 
  stagger: 'animate-stagger',
}

// CSS-in-JS animaties voor emergency fallback
export const fallbackAnimations = {
  fadeIn: {
    opacity: 1,
    transform: 'translateY(0)',
    transition: 'all 0.6s ease',
  },
  hidden: {
    opacity: 0,
    transform: 'translateY(20px)',
  }
}