<div align="center">

# 🛒 CallCart AI

### The Next Generation of Conversational Commerce

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=00D9FF&center=true&vCenter=true&width=700&lines=Agentic+AI+Ordering+System;Powered+by+LangGraph+%2B+Groq;Persistent+Memory+with+MongoDB;Human-in-the-Loop+Order+Confirmation;Built+for+Real-World+AI+Agents" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_Workflow-1C3C3C?style=for-the-badge)](https://www.langchain.com/langgraph)
[![Groq](https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge)](https://groq.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![LangSmith](https://img.shields.io/badge/LangSmith-Observability-000000?style=for-the-badge)](https://smith.langchain.com/)

<br/>

**An AI agent that doesn't just chat — it understands, remembers, calculates, confirms, and executes.**

</div>

---

## ⚡ What is CallCart AI?

**CallCart AI** is an agentic conversational ordering platform designed to simulate a real-world AI sales and ordering assistant.

Instead of building a traditional chatbot with hardcoded flows, CallCart uses an **LLM-powered agentic workflow** that can dynamically decide when to:

- 🔎 Search products
- 💰 Check prices
- 📦 Check availability
- 🧮 Calculate order totals
- 🧠 Maintain conversation context
- 👤 Retrieve customer information
- 🛑 Pause for human confirmation
- 🛒 Create orders
- 📋 Track order status
- 🕐 Retrieve order history

The system combines **LangGraph + Groq + MongoDB + FastAPI + React** into one end-to-end AI application.

---

## 🌐 Live Application

<p align="center">

<a href="https://callcart-ai.vercel.app/">
  <img src="https://img.shields.io/badge/🚀_LIVE_DEMO-CallCart_AI-00D9FF?style=for-the-badge" />
</a>

</p>

---

# 🧠 Why is this different from a chatbot?

A traditional chatbot:

```text
User
 ↓
LLM
 ↓
Response
```

CallCart AI:

```text
                    ┌──────────────────┐
                    │     User Chat    │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │    FastAPI API   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │    LangGraph     │
                    │   Agent Engine   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │   Groq LLM       │
                    └────────┬─────────┘
                             ↓
              ┌──────────────┴──────────────┐
              ↓                             ↓
      ┌───────────────┐             ┌───────────────┐
      │ Agent Tools   │             │ MongoDB       │
      │               │             │               │
      │ Search        │             │ Products      │
      │ Calculate     │             │ Customers     │
      │ Confirm       │             │ Orders        │
      │ Create Order  │             │ Memory        │
      └───────┬───────┘             └───────────────┘
              ↓
       ┌───────────────┐
       │ Human Approval│
       └───────┬───────┘
               ↓
       ┌───────────────┐
       │ Create Order  │
       └───────────────┘
```

The key idea is **agentic execution**.

The LLM decides which tools it needs instead of following a fixed conversational script.

---

# 🚀 Core Features

| Feature | Description |
|---|---|
| 🤖 Agentic AI | LLM dynamically decides which tools to use |
| 🧠 Persistent Memory | Conversations persist across requests |
| 🔧 Tool Calling | Product, customer and order operations |
| 🛑 Human-in-the-Loop | Order creation requires explicit confirmation |
| 🛒 Order Management | Create and track orders |
| 💰 Dynamic Pricing | Prices are retrieved from MongoDB |
| 🔎 Product Search | Search products using natural language |
| 📋 Order History | Retrieve previous orders |
| ⚡ Fast Inference | Powered by Groq |
| 🔍 Observability | LangSmith tracing |
| 🌐 REST API | FastAPI backend |
| 💻 Modern UI | React + Vite frontend |

---

# 🔥 Example Conversation

### User

> I want 2 Paneer Pizzas and a Coke.

### CallCart AI

```text
🔎 Searching products...

Paneer Pizza × 2
Coke × 1

Total: ₹550
```

### AI Agent

```text
Your order total is ₹550.
Would you like me to place the order?
```

### User

> Yes

### Agent

```text
✅ Order confirmed!

Order ID: ORD-A81F92C4
Total: ₹550
Status: confirmed
```

> **The AI cannot create the order until the customer explicitly confirms it.**

---

# 🧩 Agent Architecture

CallCart uses **LangGraph** to model the agent workflow as a stateful graph.

```text
                    START
                      │
                      ▼
              ┌──────────────┐
              │    Chatbot   │
              │   Groq LLM   │
              └──────┬───────┘
                     │
               Tool required?
                 /       \
               YES        NO
                │          │
                ▼          ▼
        ┌────────────┐    END
        │  ToolNode  │
        └─────┬──────┘
              │
              ▼
        ┌──────────────┐
        │ MongoDB Tools│
        └──────┬───────┘
               │
               ▼
          Chatbot Again
               │
               ▼
        Confirmation Tool
               │
               ▼
          ⏸ INTERRUPT
               │
        ┌──────┴──────┐
        │             │
       YES            NO
        │             │
        ▼             ▼
 Create Order        STOP
        │
        ▼
       END
```

---

# 🧠 Human-in-the-Loop

One of the main features of CallCart AI is **explicit human approval before an irreversible action**.

The workflow uses LangGraph's interrupt mechanism:

```python
confirmation = interrupt({
    "type": "order_confirmation",
    "message": "Would you like me to place the order?",
    "items": items,
    "total": total
})
```

The graph pauses.

The customer responds.

Then the same conversation thread resumes.

```text
Agent
 ↓
Calculate Order
 ↓
Ask Confirmation
 ↓
⏸ PAUSED
 ↓
Customer
 ↓
"Yes"
 ↓
RESUME SAME THREAD
 ↓
Create Order
```

This pattern can be extended to many real-world agent workflows:

```text
AI Agent
   ↓
Potentially irreversible action
   ↓
Human approval
   ↓
Execution
```

---

# 🧠 Persistent Conversation Memory

CallCart doesn't treat every request as a new conversation.

Each conversation receives a unique:

```text
thread_id
```

LangGraph checkpoints the conversation state using MongoDB.

```text
User
 ↓
Thread ID
 ↓
LangGraph
 ↓
MongoDB Checkpoints
 ↓
Previous Context
```

Example:

```text
User:
"My name is Divy."

AI:
"Nice to meet you, Divy!"

---

Later...

User:
"What is my name?"

AI:
"Your name is Divy."
```

The conversation state survives across API requests.

---

# 🗄️ MongoDB Architecture

CallCart uses MongoDB Atlas for application data and LangGraph persistence.

```text
MongoDB Atlas
│
├── callcart
│   │
│   ├── products
│   │
│   ├── customers
│   │
│   └── orders
│
└── callcart_memory
    │
    ├── checkpoints
    │
    └── checkpoint_writes
```

### Products

```json
{
  "name": "Paneer Pizza",
  "category": "Pizza",
  "price": 250,
  "available": true
}
```

### Orders

```json
{
  "order_id": "ORD-A81F92C4",
  "customer_id": "guest",
  "items": [],
  "total": 550,
  "status": "confirmed",
  "created_at": "UTC timestamp"
}
```

---

# 🛠️ Tech Stack

### Backend

```text
Python
FastAPI
LangChain
LangGraph
Groq
MongoDB
PyMongo
```

### Frontend

```text
React
Vite
JavaScript
CSS
Lucide Icons
```

### AI / Agent Infrastructure

```text
LangGraph
Groq
Tool Calling
Human-in-the-Loop
Persistent State
LangSmith
```

### Database

```text
MongoDB Atlas
```

---

# 📁 Project Structure

```text
callcart-ai/
│
├── backend/
│   │
│   ├── agent/
│   │   ├── graph.py
│   │   ├── prompts.py
│   │   └── state.py
│   │
│   ├── database/
│   │   └── mongodb.py
│   │
│   ├── tools/
│   │   ├── product_tools.py
│   │   ├── customer_tools.py
│   │   └── order_tools.py
│   │
│   ├── config.py
│   └── main.py
│
├── frontend/
│   │
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── package.json
│   └── .env
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Local Setup

## 1. Clone

```bash
git clone https://github.com/YOUR_USERNAME/callcart-ai.git
cd callcart-ai
```

## 2. Backend Setup

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 3. Environment Variables

Create:

```text
.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key
MONGODB_URI=your_mongodb_connection_string

LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=callcart-ai
```

## 4. Start Backend

```bash
uvicorn backend.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## 5. Start Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🔐 Security

Secrets are intentionally excluded from Git:

```gitignore
.env
.env.*
node_modules/
.venv/
```

Use:

```text
.env.example
```

for documenting required environment variables.

**Never commit API keys, MongoDB credentials or LangSmith credentials.**

---

# 🔭 Observability

CallCart integrates with **LangSmith** to trace agent execution.

```text
User Message
      ↓
LLM Call
      ↓
Tool Selection
      ↓
Tool Execution
      ↓
MongoDB Operation
      ↓
Agent Response
```

Useful for debugging:

- LLM decisions
- Tool calls
- latency
- failures
- agent execution flow

---

# 🧪 Current Capabilities

```text
[✓] React frontend
[✓] FastAPI backend
[✓] Groq LLM
[✓] LangGraph agent
[✓] MongoDB Atlas
[✓] Product search
[✓] Order calculation
[✓] Tool calling
[✓] Persistent memory
[✓] Human-in-the-loop confirmation
[✓] Order creation
[✓] Order status
[✓] Order history
[✓] LangSmith tracing
[✓] REST API
[ ] SMS notifications
[ ] Voice ordering
```

---

# 🗺️ Roadmap

### Phase 1 — Core Agent

```text
✓ Conversational ordering
✓ Product tools
✓ Order calculation
✓ MongoDB
✓ Persistent memory
```

### Phase 2 — Agent Safety

```text
✓ Human confirmation
✓ Interrupt / Resume workflow
✓ Explicit order confirmation
```

### Phase 3 — Production

```text
→ Deploy backend
→ Deploy frontend
→ Production CORS
→ Environment configuration
```

### Phase 4 — Communication

```text
→ SMS order confirmation
→ Twilio integration
→ Voice ordering
```

### Future

```text
→ Multi-channel ordering
→ Customer profiles
→ Recommendation engine
→ Analytics dashboard
→ Inventory management
→ Payment integration
```

---

# 🎯 Real-World Use Cases

The architecture isn't limited to food ordering.

The same agentic pattern can power:

```text
🛍️ E-commerce
📦 Order Management
🏨 Hotel Booking
✈️ Travel Booking
💳 Financial Operations
🩺 Healthcare Scheduling
🎫 Ticket Booking
🚚 Logistics
📞 Customer Support
```

Core pattern:

```text
Natural Language
      ↓
Agent Reasoning
      ↓
Tool Selection
      ↓
Database / API
      ↓
Human Approval
      ↓
Action
```

---

# 💡 What I Learned Building This

Building CallCart AI involved working with several important concepts in modern AI engineering:

- Agentic workflows
- LangGraph state management
- LLM tool calling
- Human-in-the-loop systems
- Persistent agent memory
- MongoDB integration
- FastAPI API design
- React frontend integration
- LLM observability
- Stateful conversations
- Production-oriented environment management

---

# 👨‍💻 Author

<div align="center">

### Divy Desai

B.Tech CSE — AI/ML  
Adani University

[![GitHub](https://img.shields.io/badge/GitHub-KingDivy-181717?style=for-the-badge&logo=github)](https://github.com/KingDivy)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Divy_Desai-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/divy-desai)

</div>

---

<div align="center">

## ⚡ CallCart AI

**Don't just build chatbots. Build agents that can act.**

```text
Think → Decide → Tool → Verify → Confirm → Execute
```

⭐ If you find this project interesting, consider starring the repository.

</div>
