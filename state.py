from typing import TypedDict

class FarmState(TypedDict,total=False):

    tempreature:float
    humidity:float
    soil_moisture:float


    crop:str
    crop_stage:str
    soil_type:str
    area:str

    knowledge_context:str

    observation:str
    decision:str
    reason:str
    next_action:str
    safety_status:str
    safety_reason:str
    executed_action:str
    verification_status:str
    verification_message:str
    alert:str
    display_text:str
    farm_memory:str
    response:str

    action_type:str
    hardware_command:int
    