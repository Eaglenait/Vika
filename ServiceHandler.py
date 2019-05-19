import VikaSyntax
import socket
import sys
from typing import cast
import requests
import json

from zeroconf import ServiceBrowser, Zeroconf

'''Represent a configured action on a device'''
class VikaAction:
    def __init__(self, url: str, verbs : list(), localisation: str, objects: list()):
        self.Url = url
        self.Verbs = verbs
        self.Localisation = localisation
        self.Objects = objects

    def PrintAction(self):
        print()
        print("url:", self.Url)

        print("verbs")
        print(*self.Verbs)

        print("loc")
        print(*self.Localisation)
        
        print("obj")
        print(*self.Objects)
        print()

    '''returns the matching percentage between a syntax and this action'''
    def Match(self, syntax: VikaSyntax) -> int:
        print("passed syntax")
        syntax.PrintSyntax()

        score = 0
        maxScore = len(syntax.verbs) + len(syntax.localisation) + len(syntax.objects)
        print("maxScore:", maxScore)
        self.PrintAction()

        for verb in syntax.verbs:
            for actionVerb in self.Verbs:
                if(verb["r"] in actionVerb):
                    score += 1

        for loc in syntax.localisation:
            for actionLoc in self.Localisation:
                if(loc["n"] in actionLoc):
                    score += 1

        for obj in syntax.objects:
            for actionObj in self.Objects:
                if(obj["n"] in actionObj):
                    score += 1

        print("match score:", score)
        return (score*100)/maxScore

'''represent a device that has actions and a config'''
class VikaDevice:
    def __init__(self, addr):
        self.address = addr
        self.actions = list()
        self.HasBeenInit = False
    
    '''Copies a devices config'''
    def GetConfig(self):
        ipstr = str(self.address[0]) + "." + str(self.address[1]) + "." + str(self.address[2]) + "." + str(self.address[3])
        self.address = ipstr
        configUrl = "http://" + ipstr + "/getConfig"

        config = requests.get(configUrl)

        strconfig = json.dumps(config.json())
        jsonConfig = json.loads(strconfig)
        for action in jsonConfig["a"]:
            self.actions.append(VikaAction(action["url"], 
                                           action["verbs"], 
                                           action["loc"], 
                                           action["obj"]))

        self.HasBeenInit = True
        print("config has been read")

'''Handles the devices on the network'''
class DeviceHandler:
    def __init__(self):
        self.devices = list()
        self.zeroconf = Zeroconf()
        self.serviceBrowser = ServiceBrowser(self.zeroconf, "_vika._tcp.local.", self)

    def InitDevices(self):
        for d in self.devices:
            if(not d.HasBeenInit):
                d.GetConfig()

    '''Tries to match the given syntax to a devices config'''
    def MatchSyntax(self, syntax: VikaSyntax) -> str:
        for d in self.devices:
            for action in d.actions:
                if(action.Match(syntax) >= 50):
                    deviceUrl = "http://" + d.address + action.Url
                    print("match found with url :", deviceUrl)
                    return deviceUrl 
                else:
                    print("no match found")

    '''called when a device disconnects'''
    def remove_service(self, zeroconf, type, name):
        print("service removed")
        for d in self.devices:
            if(d.name == name):
                self.devices.remove(d)

    '''called when a device connects, adds the device to the deviceHandler'''
    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type,name)
        addr = info.address
        intaddr = list()

        for i in addr:
            intaddr.append(i)

        addresses = [device for device in self.devices]
        if(intaddr not in addresses):
            self.devices.append(VikaDevice(intaddr))
        else:
            print("duplicate device")

        self.InitDevices()
