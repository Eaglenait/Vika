#! /usr/bin/python3

import Desyntaxer
import ServiceHandler
import requests
import ServiceHandler

desyntaxer = Desyntaxer.Desyntaxer()
deviceHandler = ServiceHandler.DeviceHandler()

if __name__ == '__main__':
    print("q - quit")
    print("desyn [text] - desyntax entered text")
    print("device print|init - Discovers devices on the network, or init a client side configuration of the devices")
    print("match [text] - desyn's a sentence and tries to match to a initialized config found")

    while(True):
        command = input()
        commands = command.split()

        if(commands[0] == "q"):
            break
        elif(commands[0] == "desyn"):
            commands.pop(0)
            syn = desyntaxer.GetSyntax(' '.join(word for word in commands))
            syn.PrintSyntax()
        elif(commands[0] == "device"):
            if(len(commands) > 1):
                if(len(commands) >= 2):
                    if(commands[1] == "print"):
                        for device in deviceHandler.device:
                            print(device.address,device.HasBeenInit)
                    if(commands[1] == "init"):
                        for device in deviceHandler.device:
                            device.GetConfig()
        elif(commands[0] == "match"):
            commands.pop(0)
            syn = desyntaxer.GetSyntax(' '.join(word for word in commands))
            deviceUrl = deviceHandler.MatchSyntax(syn)
            if(deviceUrl != None):
                response = requests.get(deviceUrl)
                print(response)
            else:
                print("no match found")
        else:
            print("not a valid command")
