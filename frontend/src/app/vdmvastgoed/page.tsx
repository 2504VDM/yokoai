'use client'

import { useState, useEffect } from 'react'
import Link from 'next/link'
import YokoLogo from '@/components/ui/YokoLogo'

interface Property {
  id: number
  name: string
  address: string
  purchasePrice: number
  currentValue: number
  monthlyRent: number
  status: string
  roi: number
}

interface Tenant {
  id: number
  name: string
  property: string
  monthlyRent: number
  status: string
  lastPayment: string
}

interface Payment {
  id: number
  tenant: string
  property: string
  amount: number
  date: string
  status: string
}

export default function VDMVastgoedPage() {
  const [activeTab, setActiveTab] = useState('dashboard')
  const [properties, setProperties] = useState<Property[]>([])
  const [tenants, setTenants] = useState<Tenant[]>([])
  const [payments, setPayments] = useState<Payment[]>([])
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    // Simulate loading data
    setTimeout(() => {
      setProperties([
        {
          id: 1,
          name: 'Villa Amsterdam',
          address: 'Herengracht 123, Amsterdam',
          purchasePrice: 450000,
          currentValue: 480000,
          monthlyRent: 2800,
          status: 'Rented',
          roi: 7.5
        },
        {
          id: 2,
          name: 'Appartement Rotterdam',
          address: 'Coolsingel 456, Rotterdam',
          purchasePrice: 320000,
          currentValue: 340000,
          monthlyRent: 2100,
          status: 'Available',
          roi: 7.9
        },
        {
          id: 3,
          name: 'Huis Utrecht',
          address: 'Domstraat 789, Utrecht',
          purchasePrice: 380000,
          currentValue: 400000,
          monthlyRent: 2400,
          status: 'Rented',
          roi: 7.6
        }
      ])

      setTenants([
        {
          id: 1,
          name: 'Jan Jansen',
          property: 'Villa Amsterdam',
          monthlyRent: 2800,
          status: 'Active',
          lastPayment: '2024-01-15'
        },
        {
          id: 2,
          name: 'Maria de Vries',
          property: 'Huis Utrecht',
          monthlyRent: 2400,
          status: 'Active',
          lastPayment: '2024-01-10'
        }
      ])

      setPayments([
        {
          id: 1,
          tenant: 'Jan Jansen',
          property: 'Villa Amsterdam',
          amount: 2800,
          date: '2024-01-15',
          status: 'Paid'
        },
        {
          id: 2,
          tenant: 'Maria de Vries',
          property: 'Huis Utrecht',
          amount: 2400,
          date: '2024-01-10',
          status: 'Paid'
        }
      ])

      setIsLoading(false)
    }, 1000)
  }, [])

  const totalValue = properties.reduce((sum, p) => sum + p.currentValue, 0)
  const totalRent = properties.reduce((sum, p) => sum + p.monthlyRent, 0)
  const averageROI = properties.reduce((sum, p) => sum + p.roi, 0) / properties.length

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 flex items-center justify-center">
        <div className="text-center text-white">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-purple-500 mx-auto mb-4"></div>
          <p>Loading Van der Meulen Vastgoed Dashboard...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Navigation */}
      <nav className="border-b border-white/10 bg-white/5 backdrop-blur-xl">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center">
              <YokoLogo className="h-8 w-auto" />
              <span className="ml-2 text-xl font-bold text-white">Van der Meulen Vastgoed</span>
              <span className="ml-2 text-sm text-white/60">Powered by VDM Nexus</span>
            </div>
            <div className="flex items-center space-x-4">
              <Link href="/" className="text-white/60 hover:text-white transition-colors text-sm">
                ← Terug naar VDM Nexus
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Dashboard Header */}
      <div className="py-8 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          <h1 className="text-3xl font-bold text-white mb-2">Vastgoed Portfolio Dashboard</h1>
          <p className="text-white/60">Real-time insights en AI-powered analysis</p>
        </div>
      </div>

      {/* Stats Cards */}
      <div className="px-4 sm:px-6 lg:px-8 mb-8">
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-4 gap-6">
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-6 border border-white/20">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white/60 text-sm">Total Portfolio Value</p>
                  <p className="text-2xl font-bold text-white">€{totalValue.toLocaleString()}</p>
                </div>
                <div className="w-12 h-12 bg-green-500/20 rounded-lg flex items-center justify-center">
                  <svg className="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
                  </svg>
                </div>
              </div>
            </div>
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-6 border border-white/20">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white/60 text-sm">Monthly Rental Income</p>
                  <p className="text-2xl font-bold text-white">€{totalRent.toLocaleString()}</p>
                </div>
                <div className="w-12 h-12 bg-blue-500/20 rounded-lg flex items-center justify-center">
                  <svg className="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                  </svg>
                </div>
              </div>
            </div>
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-6 border border-white/20">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white/60 text-sm">Average ROI</p>
                  <p className="text-2xl font-bold text-white">{averageROI.toFixed(1)}%</p>
                </div>
                <div className="w-12 h-12 bg-purple-500/20 rounded-lg flex items-center justify-center">
                  <svg className="w-6 h-6 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                  </svg>
                </div>
              </div>
            </div>
            <div className="bg-white/10 backdrop-blur-xl rounded-xl p-6 border border-white/20">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white/60 text-sm">Active Tenants</p>
                  <p className="text-2xl font-bold text-white">{tenants.length}</p>
                </div>
                <div className="w-12 h-12 bg-orange-500/20 rounded-lg flex items-center justify-center">
                  <svg className="w-6 h-6 text-orange-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="px-4 sm:px-6 lg:px-8 mb-8">
        <div className="max-w-7xl mx-auto">
          <div className="flex space-x-1 bg-white/10 rounded-lg p-1">
            <button
              onClick={() => setActiveTab('dashboard')}
              className={`flex-1 py-2 px-4 rounded-md text-sm font-medium transition-colors ${
                activeTab === 'dashboard'
                  ? 'bg-purple-600 text-white'
                  : 'text-white/60 hover:text-white'
              }`}
            >
              Dashboard
            </button>
            <button
              onClick={() => setActiveTab('properties')}
              className={`flex-1 py-2 px-4 rounded-md text-sm font-medium transition-colors ${
                activeTab === 'properties'
                  ? 'bg-purple-600 text-white'
                  : 'text-white/60 hover:text-white'
              }`}
            >
              Properties
            </button>
            <button
              onClick={() => setActiveTab('tenants')}
              className={`flex-1 py-2 px-4 rounded-md text-sm font-medium transition-colors ${
                activeTab === 'tenants'
                  ? 'bg-purple-600 text-white'
                  : 'text-white/60 hover:text-white'
              }`}
            >
              Tenants
            </button>
            <button
              onClick={() => setActiveTab('payments')}
              className={`flex-1 py-2 px-4 rounded-md text-sm font-medium transition-colors ${
                activeTab === 'payments'
                  ? 'bg-purple-600 text-white'
                  : 'text-white/60 hover:text-white'
              }`}
            >
              Payments
            </button>
          </div>
        </div>
      </div>

      {/* Content */}
      <div className="px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          {activeTab === 'dashboard' && (
            <div className="grid lg:grid-cols-2 gap-8">
              {/* AI Insights */}
              <div className="bg-white/10 backdrop-blur-xl rounded-xl p-6 border border-white/20">
                <h3 className="text-xl font-semibold text-white mb-4">🤖 AI Insights</h3>
                <div className="space-y-4">
                  <div className="bg-green-500/10 border border-green-500/20 rounded-lg p-4">
                    <p className="text-green-400 font-medium">Portfolio Performance</p>
                    <p className="text-white/80 text-sm">Your portfolio is performing 12% above market average. Consider expanding in Amsterdam area.</p>
                  </div>
                  <div className="bg-blue-500/10 border border-blue-500/20 rounded-lg p-4">
                    <p className="text-blue-400 font-medium">Rental Optimization</p>
                    <p className="text-white/80 text-sm">Appartement Rotterdam could generate €300 more monthly with minor renovations.</p>
                  </div>
                  <div className="bg-purple-500/10 border border-purple-500/20 rounded-lg p-4">
                    <p className="text-purple-400 font-medium">Market Trends</p>
                    <p className="text-white/80 text-sm">Utrecht market showing 8% growth potential. Consider additional investments.</p>
                  </div>
                </div>
              </div>

              {/* Recent Activity */}
              <div className="bg-white/10 backdrop-blur-xl rounded-xl p-6 border border-white/20">
                <h3 className="text-xl font-semibold text-white mb-4">📊 Recent Activity</h3>
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-white font-medium">Payment Received</p>
                      <p className="text-white/60 text-sm">Jan Jansen - Villa Amsterdam</p>
                    </div>
                    <span className="text-green-400 font-medium">€2.800</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-white font-medium">Property Valuation</p>
                      <p className="text-white/60 text-sm">Villa Amsterdam updated</p>
                    </div>
                    <span className="text-blue-400 font-medium">+€30.000</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-white font-medium">New Tenant</p>
                      <p className="text-white/60 text-sm">Maria de Vries - Huis Utrecht</p>
                    </div>
                    <span className="text-purple-400 font-medium">Active</span>
                  </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'properties' && (
            <div className="bg-white/10 backdrop-blur-xl rounded-xl border border-white/20 overflow-hidden">
              <div className="p-6">
                <h3 className="text-xl font-semibold text-white mb-4">🏠 Properties</h3>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead className="bg-white/5">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Property</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Address</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Purchase Price</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Current Value</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Monthly Rent</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">ROI</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Status</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-white/10">
                    {properties.map((property) => (
                      <tr key={property.id} className="hover:bg-white/5">
                        <td className="px-6 py-4 whitespace-nowrap text-white font-medium">{property.name}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-white/80">{property.address}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-white/80">€{property.purchasePrice.toLocaleString()}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-white/80">€{property.currentValue.toLocaleString()}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-white/80">€{property.monthlyRent.toLocaleString()}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-green-400 font-medium">{property.roi}%</td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                            property.status === 'Rented' 
                              ? 'bg-green-500/20 text-green-400' 
                              : 'bg-yellow-500/20 text-yellow-400'
                          }`}>
                            {property.status}
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {activeTab === 'tenants' && (
            <div className="bg-white/10 backdrop-blur-xl rounded-xl border border-white/20 overflow-hidden">
              <div className="p-6">
                <h3 className="text-xl font-semibold text-white mb-4">👥 Tenants</h3>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead className="bg-white/5">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Tenant</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Property</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Monthly Rent</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Status</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Last Payment</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-white/10">
                    {tenants.map((tenant) => (
                      <tr key={tenant.id} className="hover:bg-white/5">
                        <td className="px-6 py-4 whitespace-nowrap text-white font-medium">{tenant.name}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-white/80">{tenant.property}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-white/80">€{tenant.monthlyRent.toLocaleString()}</td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <span className="px-2 py-1 rounded-full text-xs font-medium bg-green-500/20 text-green-400">
                            {tenant.status}
                          </span>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-white/80">{tenant.lastPayment}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {activeTab === 'payments' && (
            <div className="bg-white/10 backdrop-blur-xl rounded-xl border border-white/20 overflow-hidden">
              <div className="p-6">
                <h3 className="text-xl font-semibold text-white mb-4">💰 Payments</h3>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead className="bg-white/5">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Tenant</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Property</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Amount</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Date</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-white/60 uppercase tracking-wider">Status</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-white/10">
                    {payments.map((payment) => (
                      <tr key={payment.id} className="hover:bg-white/5">
                        <td className="px-6 py-4 whitespace-nowrap text-white font-medium">{payment.tenant}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-white/80">{payment.property}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-white/80">€{payment.amount.toLocaleString()}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-white/80">{payment.date}</td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <span className="px-2 py-1 rounded-full text-xs font-medium bg-green-500/20 text-green-400">
                            {payment.status}
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Footer */}
      <footer className="border-t border-white/10 bg-white/5 py-8 px-4 sm:px-6 lg:px-8 mt-16">
        <div className="max-w-7xl mx-auto text-center text-white/60">
          <p>Van der Meulen Vastgoed - Powered by VDM Nexus</p>
          <p className="text-sm mt-2">Live demo van het VDM Nexus platform</p>
        </div>
      </footer>
    </div>
  )
} 