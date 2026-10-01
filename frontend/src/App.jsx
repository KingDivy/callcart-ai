import { useEffect, useRef, useState } from "react";
import {
  Bot,
  Send,
  ShoppingCart,
  Check,
  X,
  RotateCcw,
  Sparkles,
  Package,
  Circle,
  User,
  Loader2,
} from "lucide-react";

const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

function App() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hey! 👋 I'm CallCart AI. I can help you find products, build your order, calculate the total, and place it for you.",
    },
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [confirmation, setConfirmation] = useState(null);
  const [backendOnline, setBackendOnline] = useState(false);

  const messagesEndRef = useRef(null);

  const [threadId, setThreadId] = useState(() => {
    const existing = localStorage.getItem("callcart_thread_id");

    if (existing) {
      return existing;
    }

    const newId = "web-" + crypto.randomUUID();
    localStorage.setItem("callcart_thread_id", newId);

    return newId;
  });

  // Scroll to latest message
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading, confirmation]);

  // Check backend
  useEffect(() => {
    checkBackend();
  }, []);

  const checkBackend = async () => {
    try {
      const response = await fetch(`${API_URL}/health`);

      if (response.ok) {
        setBackendOnline(true);
      } else {
        setBackendOnline(false);
      }
    } catch {
      setBackendOnline(false);
    }
  };

  // Send message
  const sendMessage = async (messageText = input) => {
    const text = messageText.trim();

    if (!text || loading) {
      return;
    }

    setInput("");

    // Add user message
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: text,
      },
    ]);

    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/api/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: text,
          thread_id: threadId,
        }),
      });

      if (!response.ok) {
        throw new Error(`Backend error: ${response.status}`);
      }

      const data = await response.json();

      // Confirmation required
      if (data.status === "waiting_for_confirmation") {
        setConfirmation({
          message: data.message,
          items: data.order?.items || [],
          total: data.order?.total || 0,
        });

        return;
      }

      // Normal assistant response
      if (data.response) {
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            content: data.response,
          },
        ]);
      }
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "⚠️ I couldn't connect to the CallCart backend. Please make sure the FastAPI server is running.",
        },
      ]);

      setBackendOnline(false);
    } finally {
      setLoading(false);
    }
  };

  // Confirm / cancel order
  const handleConfirmation = async (confirmed) => {
    setConfirmation(null);

    if (confirmed) {
      await sendMessage("yes");
    } else {
      await sendMessage("no");
    }
  };

  // New conversation
  const newChat = () => {
    const newId = "web-" + crypto.randomUUID();

    localStorage.setItem("callcart_thread_id", newId);
    setThreadId(newId);

    setMessages([
      {
        role: "assistant",
        content:
          "New conversation started. 👋 What would you like to order today?",
      },
    ]);

    setConfirmation(null);
    setInput("");
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="app">

      {/* SIDEBAR */}
      <aside className="sidebar">

        <div className="brand">
          <div className="brand-icon">
            <ShoppingCart size={21} />
          </div>

          <div>
            <h1>CallCart</h1>
            <span>AI Ordering Agent</span>
          </div>
        </div>

        <button className="new-chat" onClick={newChat}>
          <RotateCcw size={17} />
          New conversation
        </button>

        <div className="sidebar-section">
          <p className="section-title">CAPABILITIES</p>

          <div className="capability">
            <Package size={17} />
            <span>Product search</span>
          </div>

          <div className="capability">
            <ShoppingCart size={17} />
            <span>Smart ordering</span>
          </div>

          <div className="capability">
            <Sparkles size={17} />
            <span>AI conversations</span>
          </div>

          <div className="capability">
            <Check size={17} />
            <span>Order confirmation</span>
          </div>
        </div>

        <div className="sidebar-bottom">
          <div className="system-status">
            <Circle
              size={9}
              fill={backendOnline ? "currentColor" : "none"}
            />

            <span>
              {backendOnline
                ? "Backend online"
                : "Backend offline"}
            </span>
          </div>

          <div className="powered">
            Made By Divy Desai
          </div>
        </div>

      </aside>

      {/* MAIN */}
      <main className="main">

        {/* HEADER */}
        <header className="header">

          <div className="header-info">
            <div className="bot-avatar">
              <Bot size={21} />
            </div>

            <div>
              <h2>CallCart AI</h2>

              <div className="online-status">
                <span className="online-dot"></span>
                AI agent online
              </div>
            </div>
          </div>

          <div className="header-badge">
            <Sparkles size={15} />
            Agentic AI
          </div>

        </header>

        {/* CHAT */}
        <div className="chat-container">

          <div className="welcome">

            <div className="welcome-icon">
              <Bot size={28} />
            </div>

            <h2>What can I get for you?</h2>

            <p>
              Search products, build your cart, and place your
              order using natural language.
            </p>

            <div className="quick-actions">

              <button
                onClick={() =>
                  sendMessage("Show me all available products")
                }
              >
                <Package size={16} />
                Browse products
              </button>

              <button
                onClick={() =>
                  sendMessage("What pizzas do you have?")
                }
              >
                🍕 Pizzas
              </button>

              <button
                onClick={() =>
                  sendMessage("Show me burgers")
                }
              >
                🍔 Burgers
              </button>

            </div>

          </div>

          {/* MESSAGES */}
          <div className="messages">

            {messages.map((message, index) => (
              <div
                key={index}
                className={`message-row ${message.role}`}
              >

                <div className="message-avatar">
                  {message.role === "assistant" ? (
                    <Bot size={16} />
                  ) : (
                    <User size={16} />
                  )}
                </div>

                <div className="message-bubble">
                  {message.content}
                </div>

              </div>
            ))}

            {/* TYPING */}
            {loading && (
              <div className="message-row assistant">

                <div className="message-avatar">
                  <Bot size={16} />
                </div>

                <div className="message-bubble typing">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>

              </div>
            )}

            <div ref={messagesEndRef} />

          </div>

          {/* CONFIRMATION CARD */}
          {confirmation && (
            <div className="confirmation-wrapper">

              <div className="confirmation-card">

                <div className="confirmation-header">

                  <div className="confirmation-icon">
                    <ShoppingCart size={20} />
                  </div>

                  <div>
                    <h3>Confirm your order</h3>
                    <p>Please review your order before placing it.</p>
                  </div>

                </div>

                <div className="order-items">

                  {confirmation.items.map((item, index) => (
                    <div className="order-item" key={index}>

                      <div>
                        <strong>{item.name}</strong>
                        <span>
                          Qty: {item.quantity}
                        </span>
                      </div>

                      <span>
                        {item.item_total !== undefined
                          ? `₹${item.item_total}`
                          : ""}
                      </span>

                    </div>
                  ))}

                </div>

                <div className="order-total">
                  <span>Total</span>
                  <strong>₹{confirmation.total}</strong>
                </div>

                <div className="confirmation-actions">

                  <button
                    className="cancel-btn"
                    onClick={() => handleConfirmation(false)}
                    disabled={loading}
                  >
                    <X size={17} />
                    Cancel
                  </button>

                  <button
                    className="confirm-btn"
                    onClick={() => handleConfirmation(true)}
                    disabled={loading}
                  >
                    {loading ? (
                      <>
                        <Loader2 size={17} className="spin" />
                        Processing...
                      </>
                    ) : (
                      <>
                        <Check size={17} />
                        Confirm Order
                      </>
                    )}
                  </button>

                </div>

              </div>

            </div>
          )}

        </div>

        {/* INPUT */}
        <div className="input-area">

          <div className="input-wrapper">

            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Ask me to find something or place an order..."
              rows={1}
              disabled={loading}
            />

            <button
              className="send-button"
              onClick={() => sendMessage()}
              disabled={!input.trim() || loading}
            >
              {loading ? (
                <Loader2 size={19} className="spin" />
              ) : (
                <Send size={19} />
              )}
            </button>

          </div>

          <p className="input-hint">
            CallCart AI can search products, calculate totals,
            and place orders with your confirmation.
          </p>

        </div>

      </main>

    </div>
  );
}

export default App;
