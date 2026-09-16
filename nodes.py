from state import FarmState
import os
from dotenv import load_dotenv
from datetime import datetime
from pydantic import BaseModel
from typing import Literal
load_dotenv()
# What is farmstate?

#🚨🚨🚨Go through previous projects and tell me the output things and learn thoroughfully again 

# List Comprehension
# new_list = [expression for item in old_list if condition]
# for example
# want to do multiply with 2 so it will as expression means what function you wanna apply
# then for loop and if condition is common

# lambda x:x*2
# For each x multiply x with 2 but act as function 
# multipliers=[lambda x,i=1:x*i for i in range(4)]

# Alternative method of TypedDict and annotated is FarmState?⚠️
# TypedDict defines what data your state holds
# Annotated defines how that data updates over time
# TypedDict act as schema for a dictionary a blueprint
# It tells what keys are required and what data types must hold
# class profile(TypedDict):
    # username:str
    # age:int
    # is_active:bool
# user_one:Profile={
#     "username":"something",
#     "age":30,
#     "is_active":True
# }

# Annotated attaches meta data instructions to a specific data type
# priceTag=Annotated[str,"USD currency format should match"]
# Just to add more info
# item_price:priceTag="$20.99"
# BEHAVIOR A: Overwrite. No Annotated wrapper used. 
    # Any node returning 'current_status' completely replaces the old string.
    # current_status: str
    
    # BEHAVIOR B: Pre-built LangGraph Reducer.
    # Uses LangGraph's built-in 'add_messages' to append new LLM messages to the list.
    # (Imported via: from langgraph.graph.message import add_messages)
    # messages: Annotated[list, "add_messages"] 

    # BEHAVIOR C: Custom Reducer.
    # Uses our custom 'append_score' function to ensure scores accumulate.
    # score_history: Annotated[list[int], append_score]
# So that the annotated first use the in built langraph funtion,string information and our newly build functions too and not only it will add but also it will use them to calculate by ffunctions or read the information and automatically append to the list?
# "add_messages": Intelligently handles chatbot lists. (It automatically appends new messages, handles list extensions, and even updates existing messages if their unique IDs match).
# Tells an ORM database framework how to structure a SQL column
# ID = Annotated[int, "PRIMARY KEY AUTOINCREMENT"]
# LangGraph boards the ship and uses the metadata as a State Reducer.FastAPI boards the ship and uses the metadata for Dependency Injection.Pydantic boards the ship and uses the metadata for Data Validation.

from langchain_groq import ChatGroq


llm=ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b",
    temperature=0
)

def sensor_node(state: FarmState):

    return {
        "tempreature": state.get("tempreature", 0),
        "humidity": state.get("humidity", 0),
        "soil_moisture": state.get("soil_moisture", 0)
    }

def farm_context_node(state: FarmState):

    return {
        "crop": state.get("crop", "Any"),
        "crop_stage": state.get("crop_stage", "..."),
        "soil_type": state.get("soil_type", "Any"),
        "area": state.get("area", "Area A")
    }
# It always return dictionary in return that's why return {}
# Direct will return crop,stage and soil type?

def rag_node(state:FarmState):
    crop=state["crop"]
    crop_stage=state["crop_stage"]

    knowledge=f"""
    Crop:{crop}
    Growth Stage:{crop_stage}
    General Knowledge:It can be anything for suppose for particulary tomato what are the needs expecially during flowering and fruit developement.Irrigation should how?All env conditions should how?and about diseases"""

    return{
        "knowledge_context":knowledge
    }
    # If the rag will search according to crop and crop stage?

# def decision_node(state:FarmState):
#     prompt=f"""
#     You are an agricultural decision-making AI.

#     Farm information:
#     Crop:{state["crop"]}
#     Growth stage:{state["crop_stage"]}
#     Soil type:{state["soil_type"]}
#     Area:{state["area"]}

#     Current Sensor readings:
#     Tempreature:{state["tempreature"]}°C
#     Humidity:{state["humidity"]} %
#     Soil moisture:{state["soil_moisture"]} %

#     Agriculture knowledge:
#     {state["knowledge_context"]}

#     Analyze the farm condition.

#     Select exactly ONE action :

#     WATER:
#     Use the main irrigation pump when soil/root-zone watering is required.

#     SPRINKLER:
#     Use the sprinkler system when there is need of sprinkling of seeds or compost in distributed way and according to crop and crop season. 

#     ALERT:
#     Use when the situation needs attention but automatic watering should not happen.

#     NONE:
#     Use when no action is required.

#     Return:
#     -Observation:What you observe from the data
#     -Decision:what should be done
#     -Reason:why
#     -action_type:WATER,SPRINKLER,ALERT, or  NONE

#     Keep the answer concise.
#     """
#     result=llm.invoke(prompt)
#     print("\n======AI RAW RESPONSE=======")
#     print(result.content)

#     import json

#     data=json.loads(result.content)

#     return{
#        "observation": data["observation"],
#         "decision": data["decision"],
#         "reason": data["reason"],
#         "action_type": data["action_type"]
#     }
# How can it possible if llm will separate these 3 things above in result.content?







def decision_node(state: FarmState):

    prompt = f"""
You are an agricultural decision-making AI.

Farm information:
Crop: {state["crop"]}
Growth stage: {state["crop_stage"]}
Soil type: {state["soil_type"]}
Area: {state["area"]}

Current sensor readings:
Temperature: {state["tempreature"]} C
Humidity: {state["humidity"]} %
Soil moisture: {state["soil_moisture"]} %

Agriculture knowledge:
{state["knowledge_context"]}

Analyze the farm condition.

Choose exactly ONE action:

WATER
SPRINKLER
ALERT
NONE

Explain:
1. Observation
2. Decision
3. Reason

At the very end write:
ACTION: WATER
or
ACTION: SPRINKLER
or
ACTION: ALERT
or
ACTION: NONE

FORMAT RULES:
- Do not use Markdown.
- Do not use * or **.
- Do not use # headings.
- Do not use bullet symbols.
- Write clean plain text.
- Keep the response short and readable.
- Use separate lines when presenting multiple pieces of information.
- Use bold and slight bigger font size for any headings
"""

    result = llm.invoke(prompt)

    content = result.content

    print("\n======AI RAW RESPONSE=======\n")
    print(content)

    # Find the action
    upper_content = content.upper()

    if "ACTION: WATER" in upper_content:
        action_type = "WATER"
    elif "ACTION: SPRINKLER" in upper_content:
        action_type = "SPRINKLER"
    elif "ACTION: ALERT" in upper_content:
        action_type = "ALERT"
    else:
        action_type = "NONE"

    return {
        "observation": content,
        "decision": content,
        "reason": content,
        "action_type": action_type
    }









def response_node(state:FarmState):

    # <<<<<<<<<<<<<<<<<<<<<<THE PRESENTATION LAYER>>>>>>>>>>>>>>>>>>>>>>>>>>
    response=f"""
    🌱 FARM AI DECISION

    Crop:{state["crop"]}
    Stage:{state["crop_stage"]}

    Tempreature:{state["tempreature"]}°C
    Humidity:{state["humidity"]} %
    Soil Moisture:{state["soil_moisture"]} %

    Observation:
    {state["observation"]}
    Decision:
    {state["decision"]}
    Reason:
    {state.get("reason")}
    Recommended Action:
    {state.get("action_type")}
    Safety:
    {state.get("safety_status")}
    Exexuted Action:
    {state.get("executed_action")}
    Alert:
    {state.get("alert","NONE")}
    """

    return{
        "response":response
    }
# The main decision will show to user? and the reason will what work?
def router_node(state:FarmState):
    # decision=state.get("decision","").upper()
    # Above line for what ⚠️ to extract decision from state
    action=state.get("action_type","NONE").upper()

    if action=="WATER":
        return{
            "next_action":"water"
        }
    elif action=="SPRINKLER":
        return{
            "next_action":"sprinkler"
        }
    elif action=="ALERT":
        return{
            "next_action":"alert"
        }
    else:
        return{"next_action":"none"}
    # if alert then none what does it mean?

def safety_validator_node(state:FarmState):
    decision=state.get("decision","").upper()
    # Just default settings it is
    safety_status="APPROVED"
    safety_reason="No unsafe condition detected."
    # Example safety rules
    tempreature=state.get("tempreature",0)
    soil_moisture=state.get("soil_moisture",0)
    # if this is already -   Soil Moisture:{state["soil_moisture"]} % then why this?
    # Cause-These are for display
    if tempreature<0 or tempreature>70:
        safety_status="REJECTED"
        safety_reason="Invalid soil moisture reading."
    elif soil_moisture<0 or soil_moisture>100:
        safety_status="REJECTED"
        safety_reason="Invalid soil moisture reading"
    return{
        "safety_status":safety_status,
        "safety_reason":safety_reason }

# Maximum pump duration
# Pump cooldown
# Water tank level
# Emergency stop
# Sensor failure
# Motor overheating
# Maximum daily irrigation  
# We are gonna add above sections soon....
#   😊 Stay UPdated
# ❤️❤️❤️🔥🔥🔥
# return
#   ↓
# LangGraph STATE

# print
#   ↓
# Terminal

def action_executor_node(state:FarmState):
    # just after safety check action and print
    
    if state.get("safety_status")!="APPROVED":
        action="NONE"
    else:
        action=state.get("action_type","NONE").upper()

    if action=="WATER":
        hardware_command=1
        print("💧MAIN WATER PUMP COMMAND")
    elif action=="SPRINKLER":
        hardware_command=2
        print("🚿 SPRINKLER COMMAND")
    elif action=="ALERT":
        hardware_command=3
        print("🚨 ALERT/BUZZER COMMAND")
    else:
        hardware_command=4
        print("NO PHYSICAL ACTION")

    return{
        "executed_action":action,
        "hardware_command":hardware_command
    }
# What to do after this? how to connect this with wifi ?

def verification_node(state:FarmState):
    before=state.get("soil_moisture",0)

    # if action in["WATER","SPRINKLER"]:

    #     before=state.get("soil_moisture",0)

    after=before+7
    # what is this? it's like sensor will read again tell that yes it is working now means the pump has been worked for 30 minutes

    if after>before:
        verification="SUCCESS"

        message=(
            f"Soil moisture increased from"
            f"{before}% to {after}%."
        )
    else:
        verification="FAILED"

        message=(
            "Soil moisture did not increase"
            "Possible pump or sensor problem"
        )

    return {
        "verification_status":verification,
        "verification_message":message
    }

def alert_node(state:FarmState):
    alerts=[]

    tempreature=state.get("tempreature",0)
    soil_moisture=state.get("soil_moisture",0)

    if tempreature>40:
        alerts.append(
            "⚠️Tempreature is extreamly high."
        )
    if soil_moisture<10:
        alerts.append(
            f"⚠️Soil Moisture is critically low."
        )
    if state.get("safety_status")=="REJECTED":
        alerts.append(
            f"⚠️Action Rejected:"
            f"{state.get('safety_reason')}"
        )
    if not alerts:
        alerts.append("NO CRITICAL ALERTS")
    return{
        "alert":"\n".join(alerts)
        # As it is a list? for this
    }


def display_node(state:FarmState):
    # It will only work if I want to show to farmer otherwise no use
    display_text=f"""
    
    Tempreature:{state.get("tempreature")}^C
    Humidity:{state.get("humidity")}%
    Soil Moisture:{state.get("soil_moisture")}%
    Crop:{state.get("crop")}
    Stage:{state.get("crop_stage")}
    Decision:{state.get("decision")}
    Action:{state.get("action_type")}
    Safety:{state.get("safety_status")}
    Executed:{state.get("executed_action")}
    """
    return{
        "display_text":display_text
    }
# It is for LED/OLED

def memory_node(state:FarmState):
    # Can we use this as memory and give decision according to that also can know the location
    memory={
        "timestamp":datetime.now().isoformat(),
        "tempreature":state.get("tempreature"),
        "humidity":state.get("humidity"),
        "soil_moisture":state.get("soil_moisture"),

        "crop":state.get("crop"),
        "crop_stage":state.get("crop_stage"),

        "decision":state.get("decision"),
        "safety_status":state.get("safety_status"),

        "executed_action":state.get("executed_action")

    }

    print("\n FARM MEMORY")
    print(memory)

    return{
        "farm_memory":memory
    }

# Last node hasn't written fully

# Data nodes are sensor node,farm_context_node,rag_node
# decision node and router node decides all
# Other are deterministic and action nodes

# So now the next part comes in how wifi will take instruction and will do action

# | Node            | Reads                        | Returns/updates                      |
# | --------------- | ---------------------------- | ------------------------------------ |
# | Sensor          | state                        | temperature, humidity, soil moisture |
# | Farm Context    | state                        | crop, stage, soil                    |
# | RAG             | crop/stage                   | knowledge                            |
# | Decision        | sensor + context + knowledge | observation, decision, reason        |
# | Safety          | sensor + decision            | safety status                        |
# | Router          | decision + safety            | next_action                          |
# | Action Executor | decision                     | executed_action                      |
# | Verification    | soil moisture                | verification                         |
# | Memory          | everything needed            | farm_memory                          |
# | Display         | state                        | display_text                         |
# | Response        | state                        | response                             |
