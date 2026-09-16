# from fastapi import FastAPI
# from fastapi.responses import FileResponse
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel

# from graph import graph


# app = FastAPI(
#     title="ROBOAI - Agri AI Robot",
#     description="AI farming decision-making system",
#     version="1.0.0"
# )


# # ================================
# # FRONTEND
# # ================================

# app.mount(
#     "/static",
#     StaticFiles(directory="frontend"),
#     name="static"
# )


# @app.get("/")
# def home():
#     return FileResponse("frontend/index.html")


# # ================================
# # LATEST FARM STATE
# # ================================

# latest_farm_state = {
#     "connected": False,
#     "status": "waiting",
#     "tempreature": None,
#     "humidity": None,
#     "soil_moisture": None,
#     "crop": None,
#     "crop_stage": None,
#     "soil_type": None,
#     "area": None,
#     "observation": None,
#     "decision": None,
#     "reason": None,
#     "action_type": "NONE",
#     "hardware_command": 4,
#     "safety_status": None,
#     "safety_reason": None,
#     "executed_action": None,
#     "verification_status": None,
#     "verification_message": None,
#     "alert": None,
#     "response": None
# }


# # ================================
# # SENSOR DATA MODEL
# # ================================

# class SensorData(BaseModel):

#     tempreature: float
#     humidity: float
#     soil_moisture: float

#     crop: str = "Any"
#     crop_stage: str = "..."
#     soil_type: str = "Any"
#     area: str = "Area A"


# # ================================
# # RECEIVE SENSOR DATA
# # ================================

# @app.post("/sensor-data")
# def receive_sensor_data(data: SensorData):

#     print("\n" + "=" * 50)
#     print("SENSOR DATA RECEIVED")
#     print("=" * 50)

#     print(f"Temperature    : {data.tempreature} °C")
#     print(f"Humidity       : {data.humidity} %")
#     print(f"Soil Moisture  : {data.soil_moisture} %")
#     print(f"Crop           : {data.crop}")
#     print(f"Stage          : {data.crop_stage}")
#     print(f"Soil Type      : {data.soil_type}")
#     print(f"Area           : {data.area}")


#     # Data sent into LangGraph

#     initial_state = {

#         "tempreature": data.tempreature,
#         "humidity": data.humidity,
#         "soil_moisture": data.soil_moisture,

#         "crop": data.crop,
#         "crop_stage": data.crop_stage,
#         "soil_type": data.soil_type,
#         "area": data.area
#     }


#     # Run AI graph

#     result = graph.invoke(initial_state)


#     # Store latest result

#     latest_farm_state.update({

#         "connected": True,
#         "status": "success",

#         "tempreature":
#             data.tempreature,

#         "humidity":
#             data.humidity,

#         "soil_moisture":
#             data.soil_moisture,

#         "crop":
#             data.crop,

#         "crop_stage":
#             data.crop_stage,

#         "soil_type":
#             data.soil_type,

#         "area":
#             data.area,

#         "observation":
#             result.get("observation"),

#         "decision":
#             result.get("decision"),

#         "reason":
#             result.get("reason"),

#         "action_type":
#             result.get("action_type", "NONE"),

#         "hardware_command":
#             result.get("hardware_command", 4),

#         "safety_status":
#             result.get("safety_status"),

#         "safety_reason":
#             result.get("safety_reason"),

#         "executed_action":
#             result.get("executed_action"),

#         "verification_status":
#             result.get("verification_status"),

#         "verification_message":
#             result.get("verification_message"),

#         "alert":
#             result.get("alert"),

#         "response":
#             result.get("response")
#     })


#     print("\nLatest farm state updated.")


#     # Return result to the sender
#     # Later this will be NodeMCU

#     return latest_farm_state


# # ================================
# # FARM STATUS
# # ================================

# @app.get("/farm-status")
# def farm_status():

#     return latest_farm_state


# # ================================
# # HEALTH CHECK
# # ================================

# @app.get("/health")
# def health():

#     return {
#         "status": "online",
#         "service": "ROBOAI"
#     }








# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # from fastapi.staticfiles import StaticFiles
# # from fastapi.responses import FileResponse
# # from graph import graph

# # app=FastAPI(
# #     title="Agri AI Robot API",
# #     description="API for your Farm",
# #     version="1.0.0"
# # )

# # app.mount(
# #     "/static",
# #     StaticFiles(directory="frontend"),
# #     name="static"
# # )
# # @app.get("/")
# # def home():
# #     return FileResponse("frontend/index.html")
# # class SensorData(BaseModel):
# #     tempreature:float
# #     humidity:float
# #     soil_moisture:float
# #     crop:str="Any"
# #     crop_stage:str="..."
# #     soil_type:str="Any"
# #     area:str="Area A"


# #     # return {
# #     #     # "status":"online",
# #     #     # "service":"Agri Smart Man",
# #     #     # "message":"Agri AI server is running"

# #     # }

# # @app.post("/sensor-data")
# # # ESP->Cloud(Like ESP save in database it will store in aws database or render database)
# # def receive_sensor_data(data:SensorData):

# #     print("\n======================")
# #     print("SENSOR DATA RECEIVED")
# #     print("\n======================")

# #     print(f"Tempreature   :{data.tempreature}°C")
# #     print(f"Humidity      :{data.humidity}%")
# #     print(f"Soil Moisture :{data.soil_moisture}%")
# #     print(f"Crop          :{data.crop}")
# #     print(f"Stage         :{data.crop_stage}")
# #     print(f"Soil Type     :{data.soil_type}")
# #     print(f"Area          :{data.area}")
# #     # Alt + 0176,0153 ™,0169 ‘,0174®,

# #     initial_state={
# #         "tempreature":data.tempreature,
# #         "humidity":data.humidity,
# #         "soil_moisture":data.soil_moisture,
# #         "crop":data.crop,
# #         "crop_stage":data.crop_stage,
# #         "soil_type":data.soil_type,
# #         "area":data.area
# #     }

# #     result=graph.invoke(initial_state)

# #     return {
# #         "status": "success",

# #         "observation": result.get("observation"),
# #         "decision": result.get("decision"),
# #         "reason": result.get("reason"),

# #         "action_type": result.get("action_type", "NONE"),
# #         "hardware_command": result.get("hardware_command", 4),

# #         "area": result.get("area"),

# #         "safety_status": result.get("safety_status"),
# #         "safety_reason": result.get("safety_reason"),

# #         "executed_action": result.get("executed_action"),

# #         "verification_status": result.get("verification_status"),

# #         "alert": result.get("alert"),

# #         "response": result.get("response")
# #     }
# # POST/command
# # For Cloud->ESP
# # {"action":"water"}

# # ESP->Fiber->Laptop->FastAPI
# # ESP->Fiber->Internet->Render->FastAPI->Langgraph

# # POST means I am sending data to a server and asking the server to do something with it
# # If FastAPI receives this 
# # {
# #   "temperature": 34,
# #   "humidity": 42,
# #   "soil_moisture": 18
# # }
# # can save it to AWS databse or can pass to langgraph or can run AI decision or control something or return a response or do all of these


# # 🚀Befotr>>
# # ESP8266
# #    │
# #    │ POST sensor data
# #    ↓
# # FastAPI
# #    │
# #    │ runs LangGraph
# #    ↓
# #   AI
# #    │
# #    │ decides WATER
# #    ↓
# # FastAPI
# #    │
# #    │ HTTP RESPONSE
# #    ↓
# # ESP8266

# # response-> action=water

# # 🚀After>>
# # ESP8266
# #    │
# # HTTPS POST
# #    ↓
# # Render
# #    │
# #    └── FastAPI
# #          │
# #          └── LangGraph
# #                │
# #                └── Groq

# # No database is required here ⚠️⚠️

# # State is a blue print , App Data is the place where data stored

# # Advance level>>>

# #                      INTERNET
# #                          │
# #                          │ HTTPS
# #                          ↓
# #                   ┌─────────────┐
# #                   │   Render    │
# #                   │             │
# #                   │  FastAPI    │
# #                   │      │      │
# #                   │  LangGraph  │
# #                   │      │      │
# #                   │     RAG     │
# #                   │      │      │
# #                   │    Groq     │
# #                   └──────┬──────┘
# #                          │
# #                ┌─────────┴─────────┐
# #                ↓                   ↓
# #           AWS Database        Knowledge/Data
# #                                 storage
               
# #                          ↑
# #                          │
# #                     HTTPS POST
# #                          │
# #                          │
# #                     ┌────┴────┐
# #                     │ ESP8266 │
# #                     ├─────────┤
# #                     │ DHT     │
# #                     │ Soil    │
# #                     │ Pump    │
# #                     │ Relay   │
# #                     │ Buzzer  │
# #                     │ Sprinkler
# #                     └─────────┘

# # Render does not initiate a connection to your ESP8266. The ESP8266 initiates an HTTPS request to Render.























# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
# from pydantic import BaseModel

# from graph import graph

# app = FastAPI()

# app.mount("/static", StaticFiles(directory="frontend"), name="static")


# class SensorData(BaseModel):
#     tempreature: float
#     humidity: float
#     soil_moisture: float


# latest_farm_state = {}


# @app.get("/")
# def home():
#     return FileResponse("frontend/index.html")


# @app.get("/health")
# def health():
#     return {"status": "ROBOAI is running"}


# @app.post("/sensor-data")
# def receive_sensor_data(data: SensorData):

#     global latest_farm_state

#     initial_state = {
#         "tempreature": data.tempreature,
#         "humidity": data.humidity,
#         "soil_moisture": data.soil_moisture,
#         "crop": "Rice",
#         "crop_stage": "Vegetative",
#         "soil_type": "Loamy",
#         "area": "Area A"
#     }

#     result = graph.invoke(initial_state)

#     # Convert LangGraph result into a normal Python dictionary
#     latest_farm_state = dict(result)

#     print("LATEST FARM STATE:")
#     print(latest_farm_state)

#     return {
#         "status": "success",
#         "message": "Sensor data received",
#         "hardware_command": latest_farm_state.get("hardware_command", 4)
#     }


# @app.get("/farm-status")
# def farm_status():

#     print("FARM STATUS REQUEST:")
#     print(latest_farm_state)

#     return dict(latest_farm_state)


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from graph import graph

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")


# =========================================================
# MODELS
# =========================================================

class SensorData(BaseModel):
    tempreature: float
    humidity: float
    soil_moisture: float


class FarmSetup(BaseModel):
    crop: str
    crop_stage: str
    soil_type: str
    area: str


# =========================================================
# MEMORY
# =========================================================

latest_farm_state = {}

farm_profile = {
    "crop": "Rice",
    "crop_stage": "Vegetative",
    "soil_type": "Loamy",
    "area": "Area A"
}


# =========================================================
# FRONTEND
# =========================================================

@app.get("/")
def home():
    return FileResponse("frontend/index.html")


# =========================================================
# HEALTH
# =========================================================

@app.get("/health")
def health():
    return {
        "status": "ROBOAI is running"
    }


# =========================================================
# FARM SETUP
# =========================================================

@app.post("/farm-setup")
def update_farm_setup(data: FarmSetup):

    global farm_profile

    farm_profile = {
        "crop": data.crop,
        "crop_stage": data.crop_stage,
        "soil_type": data.soil_type,
        "area": data.area
    }

    print("FARM PROFILE UPDATED:")
    print(farm_profile)

    return {
        "status": "success",
        "message": "Farm profile saved",
        "farm_profile": farm_profile
    }


@app.get("/farm-setup")
def get_farm_setup():

    return farm_profile


# =========================================================
# SENSOR DATA
# =========================================================

@app.post("/sensor-data")
def receive_sensor_data(data: SensorData):

    global latest_farm_state

    initial_state = {
        # Real sensor values
        "tempreature": data.tempreature,
        "humidity": data.humidity,
        "soil_moisture": data.soil_moisture,

        # Farm profile
        "crop": farm_profile["crop"],
        "crop_stage": farm_profile["crop_stage"],
        "soil_type": farm_profile["soil_type"],
        "area": farm_profile["area"]
    }

    # Run LangGraph
    result = graph.invoke(initial_state)

    # Save latest complete state
    latest_farm_state = dict(result)

    print("LATEST FARM STATE:")
    print(latest_farm_state)

    return {
        "status": "success",
        "message": "Sensor data received",
        "hardware_command": latest_farm_state.get(
            "hardware_command",
            4
        )
    }


# =========================================================
# FARM STATUS
# =========================================================

@app.get("/farm-status")
def farm_status():

    return dict(latest_farm_state)