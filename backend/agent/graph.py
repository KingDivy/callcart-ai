from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage

from langgraph.checkpoint.mongodb import MongoDBSaver

from backend.agent.state import AgentState
from backend.agent.prompts import SYSTEM_PROMPT

from backend.tools.product_tools import search_products
from backend.tools.customer_tools import get_customer, create_customer

from backend.tools.order_tools import (
    calculate_order,
    confirm_order,
    create_order,
    get_order_status,
    get_order_history
)

from backend.config import GROQ_API_KEY
from backend.database.mongodb import client


tools = [
    search_products,
    get_customer,
    create_customer,
    calculate_order,
    confirm_order,
    create_order,
    get_order_status,
    get_order_history
]


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=GROQ_API_KEY
)

llm_with_tools = llm.bind_tools(tools)


def chatbot(state: AgentState):
    messages = state["messages"]

    response = llm_with_tools.invoke(
        [
            SystemMessage(content=SYSTEM_PROMPT),
            *messages
        ]
    )

    return {
        "messages": [response]
    }


builder = StateGraph(AgentState)

builder.add_node(
    "chatbot",
    chatbot
)

builder.add_node(
    "tools",
    ToolNode(tools)
)

builder.add_edge(
    START,
    "chatbot"
)

builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

builder.add_edge(
    "tools",
    "chatbot"
)

builder.add_edge(
    "chatbot",
    END
)


memory = MongoDBSaver(
    client,
    db_name="callcart_memory",
    checkpoint_collection_name="checkpoints",
    writes_collection_name="checkpoint_writes"
)


graph = builder.compile(
    checkpointer=memory
)