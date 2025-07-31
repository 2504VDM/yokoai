'use client'

import { useState } from 'react'
import Link from 'next/link'
import YokoLogo from '@/components/ui/YokoLogo'

export default function ContactPage() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    company: '',
    phone: '',
    message: '',
    demoRequest: false
  })

  const [isSubmitting, setIsSubmitting] = useState(false)
  const [isSubmitted, setIsSubmitted] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsSubmitting(true)
    
    // Simulate form submission
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    setIsSubmitting(false)
    setIsSubmitted(true)
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value, type } = e.target
    const checked = type === 'checkbox' ? (e.target as HTMLInputElement).checked : undefined
    
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }))
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Navigation */}
      <nav className="border-b border-white/10 bg-white/5 backdrop-blur-xl">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center">
              <Link href="/" className="flex items-center">
                <YokoLogo className="h-8 w-auto" />
                <span className="ml-2 text-xl font-bold text-white">VDM Nexus</span>
              </Link>
            </div>
            <div className="hidden md:flex items-center space-x-8">
              <Link href="/#features" className="text-white/80 hover:text-white transition-colors">
                Features
              </Link>
              <Link href="/#pricing" className="text-white/80 hover:text-white transition-colors">
                Pricing
              </Link>
              <Link href="/#demo" className="text-white/80 hover:text-white transition-colors">
                Demo
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Contact Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-16">
            <h1 className="text-5xl font-bold text-white mb-6">
              Neem Contact Op
            </h1>
            <p className="text-xl text-white/80">
              Klaar om je business te transformeren? Boek een gratis demo of stel je vraag.
            </p>
          </div>

          {!isSubmitted ? (
            <div className="grid lg:grid-cols-2 gap-12">
              {/* Contact Form */}
              <div className="bg-white/10 backdrop-blur-xl rounded-xl p-8 border border-white/20">
                <h2 className="text-2xl font-semibold text-white mb-6">Demo Aanvragen</h2>
                <form onSubmit={handleSubmit} className="space-y-6">
                  <div className="grid md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-white/80 mb-2">Naam *</label>
                      <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        required
                        className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-white/50 focus:outline-none focus:border-purple-500 transition-colors"
                        placeholder="Jouw naam"
                      />
                    </div>
                    <div>
                      <label className="block text-white/80 mb-2">Email *</label>
                      <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                        className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-white/50 focus:outline-none focus:border-purple-500 transition-colors"
                        placeholder="jouw@email.com"
                      />
                    </div>
                  </div>
                  
                  <div className="grid md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-white/80 mb-2">Bedrijf</label>
                      <input
                        type="text"
                        name="company"
                        value={formData.company}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-white/50 focus:outline-none focus:border-purple-500 transition-colors"
                        placeholder="Bedrijfsnaam"
                      />
                    </div>
                    <div>
                      <label className="block text-white/80 mb-2">Telefoon</label>
                      <input
                        type="tel"
                        name="phone"
                        value={formData.phone}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-white/50 focus:outline-none focus:border-purple-500 transition-colors"
                        placeholder="+31 6 12345678"
                      />
                    </div>
                  </div>

                  <div>
                    <label className="block text-white/80 mb-2">Bericht</label>
                    <textarea
                      name="message"
                      value={formData.message}
                      onChange={handleChange}
                      rows={4}
                      className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-white/50 focus:outline-none focus:border-purple-500 transition-colors resize-none"
                      placeholder="Vertel ons over jouw business en hoe we kunnen helpen..."
                    />
                  </div>

                  <div className="flex items-center">
                    <input
                      type="checkbox"
                      name="demoRequest"
                      checked={formData.demoRequest}
                      onChange={handleChange}
                      className="w-4 h-4 text-purple-600 bg-white/10 border-white/20 rounded focus:ring-purple-500 focus:ring-2"
                    />
                    <label className="ml-2 text-white/80">
                      Ik wil een gratis demo van VDM Nexus
                    </label>
                  </div>

                  <button
                    type="submit"
                    disabled={isSubmitting}
                    className="w-full bg-purple-600 hover:bg-purple-700 disabled:bg-purple-800 text-white py-4 rounded-lg font-semibold transition-colors"
                  >
                    {isSubmitting ? 'Versturen...' : 'Verstuur Bericht'}
                  </button>
                </form>
              </div>

              {/* Contact Info */}
              <div className="space-y-8">
                <div className="bg-white/10 backdrop-blur-xl rounded-xl p-8 border border-white/20">
                  <h3 className="text-xl font-semibold text-white mb-6">Direct Contact</h3>
                  <div className="space-y-4">
                    <div className="flex items-center text-white/80">
                      <svg className="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                      </svg>
                      <span>info@vdmnexus.com</span>
                    </div>
                    <div className="flex items-center text-white/80">
                      <svg className="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                      </svg>
                      <span>+31 6 12345678</span>
                    </div>
                    <div className="flex items-center text-white/80">
                      <svg className="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                      </svg>
                      <span>Amsterdam, Nederland</span>
                    </div>
                  </div>
                </div>

                <div className="bg-white/10 backdrop-blur-xl rounded-xl p-8 border border-white/20">
                  <h3 className="text-xl font-semibold text-white mb-6">Demo Aanvragen</h3>
                  <p className="text-white/70 mb-4">
                    Boek een gratis 15-minuten demo en zie hoe VDM Nexus jouw business kan transformeren.
                  </p>
                  <ul className="space-y-2 text-white/70">
                    <li>• Persoonlijke demo met jouw data</li>
                    <li>• Industry-specifieke use cases</li>
                    <li>• ROI berekening voor jouw business</li>
                    <li>• Geen verplichtingen</li>
                  </ul>
                </div>

                <div className="bg-white/10 backdrop-blur-xl rounded-xl p-8 border border-white/20">
                  <h3 className="text-xl font-semibold text-white mb-6">Bekijk Live Demo</h3>
                  <p className="text-white/70 mb-4">
                    Bekijk hoe Van der Meulen Vastgoed VDM Nexus gebruikt voor hun portfolio management.
                  </p>
                  <Link 
                    href="/vdmvastgoed.vdmnexus.com" 
                    className="inline-block bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg font-semibold transition-colors"
                  >
                    Bekijk Demo Platform
                  </Link>
                </div>
              </div>
            </div>
          ) : (
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-12 border border-white/20 text-center">
              <div className="text-6xl mb-6">✅</div>
              <h2 className="text-3xl font-bold text-white mb-4">Bericht Verstuurd!</h2>
              <p className="text-xl text-white/80 mb-8">
                Bedankt voor je bericht. We nemen binnen 24 uur contact met je op.
              </p>
              <Link 
                href="/" 
                className="bg-purple-600 hover:bg-purple-700 text-white px-8 py-3 rounded-lg font-semibold transition-colors"
              >
                Terug naar Homepage
              </Link>
            </div>
          )}
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-white/10 bg-white/5 py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto text-center text-white/70">
          <p>&copy; 2024 VDM Nexus. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
} 