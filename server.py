from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from graph import graph

app=FastAPI(
    title="Agri AI Robot API",
    description="API for your Farm",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="frontend"),
    name="static"
)
@app.get("/")
def home():
    return FileResponse("frontend/index.html")
class SensorData(BaseModel):
    tempreature:float
    humidity:float
    soil_moisture:float
    crop:str="Any"
    crop_stage:str="..."
    soil_type:str="Any"
    area:str="Area A"


    # return {
    #     # "status":"online",
    #     # "service":"Agri Smart Man",
    #     # "message":"Agri AI server is running"

    # }

@app.post("/sensor-data")
# ESP->Cloud(Like ESP save in database it will store in aws database or render database)
def receive_sensor_data(data:SensorData):

    print("\n======================")
    print("SENSOR DATA RECEIVED")
    print("\n======================")

    print(f"Tempreature   :{data.tempreature}°C")
    print(f"Humidity      :{data.humidity}%")
    print(f"Soil Moisture :{data.soil_moisture}%")
    print(f"Crop          :{data.crop}")
    print(f"Stage         :{data.crop_stage}")
    print(f"Soil Type     :{data.soil_type}")
    print(f"Area          :{data.area}")
    # Alt + 0176,0153 ™,0169 ‘,0174®,

    initial_state={
        "tempreature":data.tempreature,
        "humidity":data.humidity,
        "soil_moisture":data.soil_moisture,
        "crop":data.crop,
        "crop_stage":data.crop_stage,
        "soil_type":data.soil_type,
        "area":data.area
    }

    result=graph.invoke(initial_state)

    return {
        "status": "success",

        "observation": result.get("observation"),
        "decision": result.get("decision"),
        "reason": result.get("reason"),

        "action_type": result.get("action_type", "NONE"),
        "hardware_command": result.get("hardware_command", 4),

        "area": result.get("area"),

        "safety_status": result.get("safety_status"),
        "safety_reason": result.get("safety_reason"),

        "executed_action": result.get("executed_action"),

        "verification_status": result.get("verification_status"),

        "alert": result.get("alert"),

        "response": result.get("response")
    }
# POST/command
# For Cloud->ESP
# {"action":"water"}

# ESP->Fiber->Laptop->FastAPI
# ESP->Fiber->Internet->Render->FastAPI->Langgraph

# POST means I am sending data to a server and asking the server to do something with it
# If FastAPI receives this 
# {
#   "temperature": 34,
#   "humidity": 42,
#   "soil_moisture": 18
# }
# can save it to AWS databse or can pass to langgraph or can run AI decision or control something or return a response or do all of these


# 🚀Befotr>>
# ESP8266
#    │
#    │ POST sensor data
#    ↓
# FastAPI
#    │
#    │ runs LangGraph
#    ↓
#   AI
#    │
#    │ decides WATER
#    ↓
# FastAPI
#    │
#    │ HTTP RESPONSE
#    ↓
# ESP8266

# response-> action=water

# 🚀After>>
# ESP8266
#    │
# HTTPS POST
#    ↓
# Render
#    │
#    └── FastAPI
#          │
#          └── LangGraph
#                │
#                └── Groq

# No database is required here ⚠️⚠️

# State is a blue print , App Data is the place where data stored

# Advance level>>>

#                      INTERNET
#                          │
#                          │ HTTPS
#                          ↓
#                   ┌─────────────┐
#                   │   Render    │
#                   │             │
#                   │  FastAPI    │
#                   │      │      │
#                   │  LangGraph  │
#                   │      │      │
#                   │     RAG     │
#                   │      │      │
#                   │    Groq     │
#                   └──────┬──────┘
#                          │
#                ┌─────────┴─────────┐
#                ↓                   ↓
#           AWS Database        Knowledge/Data
#                                 storage
               
#                          ↑
#                          │
#                     HTTPS POST
#                          │
#                          │
#                     ┌────┴────┐
#                     │ ESP8266 │
#                     ├─────────┤
#                     │ DHT     │
#                     │ Soil    │
#                     │ Pump    │
#                     │ Relay   │
#                     │ Buzzer  │
#                     │ Sprinkler
#                     └─────────┘

# Render does not initiate a connection to your ESP8266. The ESP8266 initiates an HTTPS request to Render.