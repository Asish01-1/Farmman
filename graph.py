from langgraph.graph import StateGraph,START,END

from state import FarmState

from nodes import(
    sensor_node,
    farm_context_node,
    rag_node,
    decision_node,
    response_node,
    router_node,
    safety_validator_node,
    action_executor_node,
    verification_node,
    alert_node,
    display_node,
    memory_node
)

graph_builder=StateGraph(FarmState)

graph_builder.add_node("sensor",sensor_node)
graph_builder.add_node("farm_context",farm_context_node)
graph_builder.add_node("rag",rag_node)
graph_builder.add_node("decision",decision_node)
graph_builder.add_node("safety_validator",safety_validator_node)
graph_builder.add_node("router",router_node)
graph_builder.add_node("action_executor",action_executor_node)
graph_builder.add_node("verification",verification_node)
graph_builder.add_node("alert",alert_node)
graph_builder.add_node("display",display_node)
graph_builder.add_node("memory",memory_node)
graph_builder.add_node("response",response_node)

graph_builder.add_edge(START,"sensor")
graph_builder.add_edge("sensor","farm_context")
graph_builder.add_edge("farm_context","rag")
graph_builder.add_edge("rag","decision")
graph_builder.add_edge("decision","safety_validator")
graph_builder.add_edge("safety_validator","router")

def route_decision(state:FarmState):
    next_action=state.get("next_action","none")

    safety_status=state.get("safety_status","REJECTED")

    if safety_status != "APPROVED":
        return "alert"
    if next_action == "water":
        return"action_executor"
    elif next_action == "sprinkler":
        return"action_executor"
    elif next_action == "alert":
        return "alert"
    else:
        return "display"


graph_builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "action_executor":"action_executor",
        "alert":"alert",
        "display":"display"
    }
)

graph_builder.add_edge(
    "action_executor",
    "verification"
)

graph_builder.add_edge(
    "verification",
    "memory"
)

graph_builder.add_edge(
    "memory",
    "display"
)

# graph_builder.add_edge("display",END)
graph_builder.add_edge("display","response")
# END is correct?
graph_builder.add_edge("response",END)

graph=graph_builder.compile()

if __name__=="__main__":
    result=graph.invoke({})

    print("\n"+"="*50)
    print("FINAL RESPONSE")
    print("="*50)

    print(result.get("response"))

    print("\n"+"="*50)
    print("FULL STATE")
    print("="*50)

    print(result)