import json
import uuid
import time
import os

from init import loadConfig

class TrainObj:
    def __init__(self, routeStart: str = None, routeEnd: str = None, routeEstimate: str = None, bordingTime: str = None, departureTime: str = None, arrivalTime: str = None):
        self.routeID: str = uuid.uuid4().hex[:getFromConfig("uuid_length")]
        self.routeStart: str = routeStart
        self.routeEnd: str = routeEnd
        self.routeEstimate: str = routeEstimate
        self.bordingTime: str = bordingTime
        self.departureTime: str = departureTime
        self.arrivalTime: str = arrivalTime

    def set_route_start(self, route_start: str):
        self.routeStart = route_start

    def get_route_start(self) -> str:
        return self.routeStart

    def set_route_end(self, route_end: str):
        self.routeEnd = route_end

    def get_route_end(self) -> str:
        return self.routeEnd

    def set_route_estimate(self, route_estimate: str):
        self.routeEstimate = route_estimate

    def get_route_estimate(self) -> str:
        return self.routeEstimate

    def set_bording_time(self, bording_time: str):
        self.bordingTime = bording_time

    def get_bording_time(self) -> str:
        return self.bordingTime

    def set_departure_time(self, departure_time: str):
        self.departureTime = departure_time

    def get_departure_time(self) -> str:
        return self.departureTime

    def set_arrival_time(self, arrival_time: str):
        self.arrivalTime = arrival_time

    def get_arrival_time(self) -> str:
        return self.arrivalTime

    def get_as_dict(self) -> dict:
        return {
            "routeID": self.routeID,
            "routeStart": self.routeStart,
            "routeEnd": self.routeEnd,
            "routeEstimate": self.routeEstimate,
            "bordingTime": self.bordingTime,
            "departureTime": self.departureTime,
            "arrivalTime": self.arrivalTime
        }
        
# Get a value from the configuration file
def getFromConfig(key: str) -> str:
    if not os.path.exists("./config.json"):
        loadConfig()
    
    with open("./config.json", "r") as f:
        return json.load(f)[key]
    
# Save the configuration file
def saveConfig(config: dict) -> None:
    with open("./config.json", "w") as f:
        json.dump(config, f, indent="\t")
        
# Get the current timestamp
def getTimestamp() -> int:
    return int(time.time())

# Clear the console
def clearConsole() -> None:
    os.system("cls" if os.name == "nt" else "clear")