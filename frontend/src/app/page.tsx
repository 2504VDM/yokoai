'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { motion } from 'framer-motion'

export default function Home() {
  const router = useRouter()
  const [isHovered, setIsHovered] = useState(false)

  return (
    <main className="min-h-screen bg-black text-white">
      <div className="container mx-auto px-4 py-16">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="max-w-4xl mx-auto text-center"
        >
          <h1 className="text-6xl font-bold mb-6 bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent">
            Yoko AI
          </h1>
          <p className="text-xl text-gray-300 mb-12">
            Your intelligent AI assistant for seamless conversations and task management
          </p>
          
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onHoverStart={() => setIsHovered(true)}
            onHoverEnd={() => setIsHovered(false)}
            onClick={() => router.push('/chat')}
            className="px-8 py-4 bg-white text-black rounded-lg font-semibold text-lg 
                     hover:bg-gray-100 transition-colors duration-300 relative overflow-hidden"
          >
            <span className="relative z-10">Start Chatting</span>
            <motion.div
              className="absolute inset-0 bg-gray-200"
              initial={{ x: '-100%' }}
              animate={{ x: isHovered ? '0%' : '-100%' }}
              transition={{ duration: 0.3 }}
            />
          </motion.button>
        </motion.div>

        <div className="mt-24 grid grid-cols-1 md:grid-cols-3 gap-8">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="bg-gray-900 p-6 rounded-xl"
          >
            <h3 className="text-xl font-semibold mb-4 text-white">Smart Conversations</h3>
            <p className="text-gray-400">Engage in natural, context-aware discussions with our advanced AI</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="bg-gray-900 p-6 rounded-xl"
          >
            <h3 className="text-xl font-semibold mb-4 text-white">Task Management</h3>
            <p className="text-gray-400">Efficiently organize and track your tasks with AI assistance</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.6 }}
            className="bg-gray-900 p-6 rounded-xl"
          >
            <h3 className="text-xl font-semibold mb-4 text-white">24/7 Availability</h3>
            <p className="text-gray-400">Get instant help whenever you need it, day or night</p>
          </motion.div>
        </div>
        <div className="mt-24 text-center text-gray-500 text-sm">
          v0.2.3 | Made by VDM Nexus
        </div>
      </div>
    </main>
  )
}
