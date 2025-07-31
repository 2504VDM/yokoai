import Link from 'next/link'
import YokoLogo from '@/components/ui/YokoLogo'

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Navigation */}
      <nav className="border-b border-white/10 bg-white/5 backdrop-blur-xl">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center">
              <YokoLogo className="h-8 w-auto" />
              <span className="ml-2 text-xl font-bold text-white">VDM Nexus</span>
            </div>
            <div className="hidden md:flex items-center space-x-8">
              <Link href="#features" className="text-white/80 hover:text-white transition-colors">
                Features
              </Link>
              <Link href="#pricing" className="text-white/80 hover:text-white transition-colors">
                Pricing
              </Link>
              <Link href="#demo" className="text-white/80 hover:text-white transition-colors">
                Demo
              </Link>
              <Link href="/contact" className="bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-lg transition-colors">
                Contact
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto text-center">
          <h1 className="text-5xl md:text-7xl font-bold text-white mb-6">
            Upload je data.
            <br />
            <span className="bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
              Krijg je eigen AI platform.
            </span>
          </h1>
          <p className="text-xl text-white/80 mb-8 max-w-3xl mx-auto">
            VDM Nexus geeft Nederlandse bedrijven hun eigen business intelligence platform. 
            Upload CSV files en krijg automatisch database + AI analysis tools op je eigen subdomain.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link 
              href="#demo" 
              className="bg-purple-600 hover:bg-purple-700 text-white px-8 py-4 rounded-lg text-lg font-semibold transition-colors"
            >
              Vraag Demo Aan
            </Link>
            <Link 
              href="/vdmvastgoed.vdmnexus.com" 
              className="border border-white/20 hover:border-white/40 text-white px-8 py-4 rounded-lg text-lg font-semibold transition-colors"
            >
              Bekijk Live Demo
            </Link>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 px-4 sm:px-6 lg:px-8 bg-white/5">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-4xl font-bold text-white text-center mb-16">
            Waarom VDM Nexus?
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-8 border border-white/20">
              <div className="w-12 h-12 bg-purple-600 rounded-lg flex items-center justify-center mb-6">
                <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
              </div>
              <h3 className="text-xl font-semibold text-white mb-4">Geen Technische Kennis Nodig</h3>
              <p className="text-white/70">
                Upload je CSV files en krijg automatisch een complete database met AI analysis tools. 
                Geen code, geen complexe setup.
              </p>
            </div>
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-8 border border-white/20">
              <div className="w-12 h-12 bg-purple-600 rounded-lg flex items-center justify-center mb-6">
                <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <h3 className="text-xl font-semibold text-white mb-4">Eigen Subdomain Platform</h3>
              <p className="text-white/70">
                Krijg je eigen platform op [bedrijfnaam].vdmnexus.com met custom branding 
                en industry-specifieke templates.
              </p>
            </div>
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-8 border border-white/20">
              <div className="w-12 h-12 bg-purple-600 rounded-lg flex items-center justify-center mb-6">
                <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
              </div>
              <h3 className="text-xl font-semibold text-white mb-4">AI-Powered Insights</h3>
              <p className="text-white/70">
                Automatische business insights, predictive analytics en custom AI agents 
                die jouw specifieke business kennen.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Live Demo Section */}
      <section id="demo" className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-4xl font-bold text-white text-center mb-16">
            Bekijk het in Actie
          </h2>
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <h3 className="text-2xl font-semibold text-white mb-6">
                Van der Meulen Vastgoed - Live Demo
              </h3>
              <p className="text-white/70 mb-8">
                Bekijk hoe Van der Meulen Vastgoed hun vastgoed portfolio beheert met VDM Nexus. 
                Real-time dashboards, AI-powered insights en automatische data analysis.
              </p>
              <div className="space-y-4">
                <div className="flex items-center text-white/80">
                  <div className="w-2 h-2 bg-purple-400 rounded-full mr-3"></div>
                  <span>Property portfolio management</span>
                </div>
                <div className="flex items-center text-white/80">
                  <div className="w-2 h-2 bg-purple-400 rounded-full mr-3"></div>
                  <span>ROI analysis & predictions</span>
                </div>
                <div className="flex items-center text-white/80">
                  <div className="w-2 h-2 bg-purple-400 rounded-full mr-3"></div>
                  <span>Tenant payment tracking</span>
                </div>
                <div className="flex items-center text-white/80">
                  <div className="w-2 h-2 bg-purple-400 rounded-full mr-3"></div>
                  <span>AI-powered business insights</span>
                </div>
              </div>
              <Link 
                href="/vdmvastgoed.vdmnexus.com" 
                className="inline-block bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg font-semibold mt-8 transition-colors"
              >
                Bekijk Live Demo
              </Link>
            </div>
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-8 border border-white/20">
              <div className="aspect-video bg-gradient-to-br from-purple-600 to-pink-600 rounded-lg flex items-center justify-center">
                <div className="text-center text-white">
                  <div className="text-4xl mb-4">🏠</div>
                  <div className="text-lg font-semibold">Van der Meulen Vastgoed</div>
                  <div className="text-sm opacity-80">Live Dashboard Demo</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section id="pricing" className="py-20 px-4 sm:px-6 lg:px-8 bg-white/5">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-4xl font-bold text-white text-center mb-16">
            Pricing
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-8 border border-white/20">
              <h3 className="text-2xl font-semibold text-white mb-4">Starter</h3>
              <div className="text-4xl font-bold text-white mb-6">€199<span className="text-lg font-normal text-white/70">/maand</span></div>
              <ul className="space-y-3 text-white/70 mb-8">
                <li>• 1 subdomain platform</li>
                <li>• 5 CSV uploads (max 10MB)</li>
                <li>• 1 custom AI agent</li>
                <li>• 3 dashboard widgets</li>
                <li>• 1.000 AI queries/maand</li>
                <li>• Email support</li>
              </ul>
              <Link 
                href="#demo" 
                className="w-full bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-lg font-semibold block text-center transition-colors"
              >
                Start Trial
              </Link>
            </div>
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-8 border border-purple-500 relative">
              <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 bg-purple-600 text-white px-4 py-2 rounded-full text-sm font-semibold">
                Meest Populair
              </div>
              <h3 className="text-2xl font-semibold text-white mb-4">Business</h3>
              <div className="text-4xl font-bold text-white mb-6">€499<span className="text-lg font-normal text-white/70">/maand</span></div>
              <ul className="space-y-3 text-white/70 mb-8">
                <li>• 1 subdomain met custom branding</li>
                <li>• Unlimited CSV uploads (max 100MB)</li>
                <li>• 3 AI agents met specialisaties</li>
                <li>• 10 dashboard widgets</li>
                <li>• 5.000 AI queries/maand</li>
                <li>• Priority support</li>
                <li>• API access</li>
              </ul>
              <Link 
                href="#demo" 
                className="w-full bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-lg font-semibold block text-center transition-colors"
              >
                Start Trial
              </Link>
            </div>
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-8 border border-white/20">
              <h3 className="text-2xl font-semibold text-white mb-4">Enterprise</h3>
              <div className="text-4xl font-bold text-white mb-6">€1.299<span className="text-lg font-normal text-white/70">/maand</span></div>
              <ul className="space-y-3 text-white/70 mb-8">
                <li>• Multiple subdomains</li>
                <li>• Enterprise data limits (1GB+)</li>
                <li>• Unlimited AI agents</li>
                <li>• Unlimited dashboard customization</li>
                <li>• 25.000 AI queries/maand</li>
                <li>• Dedicated support manager</li>
                <li>• SSO integration</li>
                <li>• Advanced API access</li>
              </ul>
              <Link 
                href="/contact" 
                className="w-full bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-lg font-semibold block text-center transition-colors"
              >
                Contact Sales
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl font-bold text-white mb-6">
            Klaar om te Beginnen?
          </h2>
          <p className="text-xl text-white/80 mb-8">
            Boek een gratis demo en zie hoe VDM Nexus jouw business kan transformeren.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link 
              href="#demo" 
              className="bg-purple-600 hover:bg-purple-700 text-white px-8 py-4 rounded-lg text-lg font-semibold transition-colors"
            >
              Vraag Demo Aan
            </Link>
            <Link 
              href="/contact" 
              className="border border-white/20 hover:border-white/40 text-white px-8 py-4 rounded-lg text-lg font-semibold transition-colors"
            >
              Contact
            </Link>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-white/10 bg-white/5 py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center mb-4">
                <YokoLogo className="h-6 w-auto" />
                <span className="ml-2 text-lg font-bold text-white">VDM Nexus</span>
              </div>
              <p className="text-white/70">
                Business intelligence platform voor Nederlandse bedrijven.
              </p>
            </div>
            <div>
              <h4 className="text-white font-semibold mb-4">Product</h4>
              <ul className="space-y-2 text-white/70">
                <li><Link href="#features" className="hover:text-white transition-colors">Features</Link></li>
                <li><Link href="#pricing" className="hover:text-white transition-colors">Pricing</Link></li>
                <li><Link href="#demo" className="hover:text-white transition-colors">Demo</Link></li>
              </ul>
            </div>
            <div>
              <h4 className="text-white font-semibold mb-4">Support</h4>
              <ul className="space-y-2 text-white/70">
                <li><Link href="/contact" className="hover:text-white transition-colors">Contact</Link></li>
                <li><Link href="/docs" className="hover:text-white transition-colors">Documentation</Link></li>
                <li><Link href="/help" className="hover:text-white transition-colors">Help Center</Link></li>
              </ul>
            </div>
            <div>
              <h4 className="text-white font-semibold mb-4">Company</h4>
              <ul className="space-y-2 text-white/70">
                <li><Link href="/about" className="hover:text-white transition-colors">About</Link></li>
                <li><Link href="/privacy" className="hover:text-white transition-colors">Privacy</Link></li>
                <li><Link href="/terms" className="hover:text-white transition-colors">Terms</Link></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-white/10 mt-8 pt-8 text-center text-white/70">
            <p>&copy; 2024 VDM Nexus. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}