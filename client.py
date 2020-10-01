import time
from socket import *
serverName = 'localhost'
serverPort = 15000
clientSocket = socket(AF_INET, SOCK_DGRAM)
class Query:
    name=""
    type =""

RR = {

}

start_time = time.time()
while True:
    name= input("Enter Host name: ")
    type= input("Enter Query type: ")


    print('Client: searching for', name)
    flag = False
    tim = time.time()- start_time
    tim = int(tim)
    for x in RR:
        RR[x]["TTL"] = RR[x]["TTL"] - tim

    for x in list(RR):
        if RR[x]["TTL"] <=0 and RR[x]["static"]==0:
            del RR[x]

    for x in RR:
        if RR[x]["name"] == name and RR[x]["type"] == type:
            value = RR[x]["value"]
            flag = True
            print('CLient:' , name, 'found in RR')
            break

    if flag == False:
        print('Client: sending DNS Request')
        clientSocket.sendto(name.encode(),(serverName,serverPort))
        clientSocket.sendto(type.encode(),(serverName,serverPort))
#-----------------------------------------------------------------------#
        value, serverAddress = clientSocket.recvfrom(2048)
        name, serverAddress = clientSocket.recvfrom(2048)
        type, serverAddress = clientSocket.recvfrom(2048)
        value = value.decode()
        name = name.decode()
        type = type.decode()
        if value == "empty":
            print("Unable to recieve address")
        else:
            RR[len(RR)+1] = { "name": name, "type": type, "value": value, "TTL": 60, "static" : 0}
            print(value)

    start_time = time.time()
    print(RR)


clientSocket.close()
