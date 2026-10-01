from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

    customer_id: str | None

    pending_order: dict | None

    order_total: float | None

    order_confirmed: bool