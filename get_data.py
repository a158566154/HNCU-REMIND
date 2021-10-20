import json
from requests import get



def get_data():
    power = 'http://58.47.143.2:8080/stuWeixinfService/fwp/stuWeixinCharge.fwp?nodeId=1606702042&type=getCurrentdataByNode'
    water = 'http://58.47.143.2:8080/stuWeixinfServices/fwp/stuWeixinCharge.fwp?nodeId=1607311266&type=getCurrentdataByNode&callback'
    power_data = get(power).json()
    water_data = get(water).json()
    #print(power_data)
    #print(water_data)
    return power_data["result"][0]["SurplusData"],eval(water_data["result"][0]["SurplusData"])







