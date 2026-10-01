from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain_core.messages import HumanMessage
from langgraph.types import Command
from langsmith import traceable
from backend.agent.graph import graph
from backend.database.mongodb import test_connection


app = FastAPI(
    title="CallCart AI",
    description="Agentic Conversational Ordering System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    thread_id: str
    customer_id: str | None = None

@app.on_event("startup")
def startup():

    print("Starting CallCart AI...")

    test_connection()


@app.get("/")
def root():

    return {
        "message": "CallCart AI is running!",
        "status": "online"
    }

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

@app.post("/api/chat")

@traceable(
    name="CallCart Conversation",
    run_type="chain"
)

def chat(request: ChatRequest):

    config = {
        "configurable": {
            "thread_id": request.thread_id
        }
    }

    # Check whether this conversation is currently paused
    current_state = graph.get_state(config)

    if current_state.next:

        result = graph.invoke(
            Command(
                resume=request.message
            ),
            config
        )

    else:

        state = {
            "messages": [
                HumanMessage(
                    content=request.message
                )
            ],
            "customer_id": request.customer_id,
            "pending_order": None,
            "order_total": None
        }

        result = graph.invoke(
            state,
            config
        )

    updated_state = graph.get_state(config)

    if updated_state.next:

        interrupts = []

        for task in updated_state.tasks:

            if task.interrupts:

                for interrupt_item in task.interrupts:
                    interrupts.append(
                        interrupt_item.value
                    )

        if interrupts:

            interrupt_data = interrupts[0]

            return {
                "status": "waiting_for_confirmation",
                "thread_id": request.thread_id,
                "message": interrupt_data.get(
                    "message",
                    "Please confirm the order."
                ),
                "order": {
                    "items": interrupt_data.get(
                        "items",
                        []
                    ),
                    "total": interrupt_data.get(
                        "total",
                        0
                    )
                }
            }

    messages = result.get("messages", [])

    final_message = messages[-1]

    return {
        "status": "completed",
        "response": final_message.content,
        "thread_id": request.thread_id
    }

@app.get("/memory/{thread_id}")
def get_memory(thread_id: str):

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    state = graph.get_state(config)

    return {
        "thread_id": thread_id,
        "messages": [
            {
                "type": message.type,
                "content": message.content
            }
            for message in state.values.get(
                "messages",
                []
            )
        ]
    }