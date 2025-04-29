import * as React from "react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"

interface Message {
  role: "user" | "assistant"
  content: string
}

interface ChatProps extends React.HTMLAttributes<HTMLDivElement> {
  messages: Message[]
  onSend: (message: string) => void
  onEdit: (index: number, newContent: string) => void
  isLoading?: boolean
}

export function Chat({ messages, onSend, onEdit, isLoading, className, ...props }: ChatProps) {
  const [input, setInput] = React.useState("")
  const [editIndex, setEditIndex] = React.useState<number | null>(null)
  const [editValue, setEditValue] = React.useState("")
  const scrollAreaRef = React.useRef<HTMLDivElement>(null)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (input.trim()) {
      onSend(input)
      setInput("")
    }
  }

  React.useEffect(() => {
    if (scrollAreaRef.current) {
      scrollAreaRef.current.scrollTop = scrollAreaRef.current.scrollHeight
    }
  }, [messages])

  return (
    <div className={cn("flex flex-col h-[70vh] min-h-[400px] w-full", className)} {...props}>
      <ScrollArea ref={scrollAreaRef} className="flex-1 p-4 min-h-[300px] max-h-[60vh] overflow-y-auto w-full">
        <div className="space-y-4 w-full">
          {messages.map((message, index) => (
            <div
              key={index}
              className={cn(
                "flex w-full max-w-full rounded-lg px-3 py-2 text-sm break-words whitespace-pre-wrap",
                message.role === "user"
                  ? "ml-auto bg-blue-600 text-white justify-end"
                  : "bg-gray-100 text-gray-900 border border-gray-200 justify-start"
              )}
            >
              {editIndex === index ? (
                <form
                  onSubmit={e => {
                    e.preventDefault()
                    onEdit(index, editValue)
                    setEditIndex(null)
                  }}
                  className="flex w-full"
                >
                  <input
                    className="flex-1 px-2 py-1 rounded text-black"
                    value={editValue}
                    onChange={e => setEditValue(e.target.value)}
                    autoFocus
                  />
                  <button type="submit" className="ml-2 text-blue-600">Save</button>
                  <button type="button" className="ml-2 text-gray-600" onClick={() => setEditIndex(null)}>Cancel</button>
                </form>
              ) : (
                <>
                  <p className="w-full break-words whitespace-pre-wrap">{message.content}</p>
                  {message.role === "user" && (
                    <button
                      className="ml-2 text-xs underline"
                      onClick={() => {
                        setEditIndex(index)
                        setEditValue(message.content)
                      }}
                    >
                      Edit
                    </button>
                  )}
                </>
              )}
            </div>
          ))}
          {isLoading && (
            <div className="flex items-center space-x-2">
              <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" />
              <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce [animation-delay:0.2s]" />
              <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce [animation-delay:0.4s]" />
            </div>
          )}
        </div>
      </ScrollArea>
      <form onSubmit={handleSubmit} className="flex items-center p-4 border-t bg-white w-full">
        <Input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          className="flex-1"
          disabled={isLoading}
        />
        <Button type="submit" className="ml-2" disabled={isLoading}>
          Send
        </Button>
      </form>
    </div>
  )
} 