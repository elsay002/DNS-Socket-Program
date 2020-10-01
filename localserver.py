from socket import *
import time
serverName = 'localhost'
serverPort = 15000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
clientPort = 0
RR = {
1: {"number":"1","name": "www.csusm.edu","type": "A","value": "144.37.5.45","TTL": -1,"static": 1
},

2:{"number":"2","name": "cc.csusm.edu","type": "A","value": "144.37.5.117","TTL":-1 ,"static": 1
},

3:{"number":"3","name": "cc1.csusm.edu","type": "CNAME","value": "cc.csusm.edu","TTL":-1 ,"static": 1
},

4:{"number": "4","name": "cc1.csusm.edu","type": "A","value": "144.37.5.118","TTL": -1,"static": 1
},

5:{"number":"5","name": "my.csusm.edu", "type": "A","value": "144.37.5.150","TTL": -1,"static": 1
},

6:{"number":"6","name": "qualcomm.com","type": "NS", "value": "dns.qualcomm.com","TTL": -1,"static": 1
},

7:
{"number":"7","name": "viasat.com","type": "NS","value": "dns.viasat.com","TTL": -1,"static": 1
}

}
name = "empty"
type = "empty"

print ('Local DNS server is ready to receive')
start_time = time.time()
while True:
    name, clientAddress= serverSocket.recvfrom(2048)
    type, clientAddress= serverSocket.recvfrom(2048)
    name=name.decode()
    type=type.decode()
    flag = False

    print('Local DNS: Recieved ', type, ' request from client', clientAddress, 'for hostname', name)
    tim = time.time()- start_time
    tim = int(tim)
    for x in RR:
        if RR[x]["static"] == 0:
            RR[x]["TTL"] = RR[x]["TTL"] - tim

    for x in list(RR):
        if RR[x]["TTL"] <=0 and RR[x]["static"]==0:
            del RR[x]

    for x in RR:
        if RR[x]["name"] == name and RR[x]["type"] == type:
            value = RR[x]["value"]
            name = RR[x]["name"]
            type = RR[x]["type"]
            flag = True
            break

    if flag == False:
        print('Local DNS: Not found. Sending request to other DNS')
        if name[4:] == "qualcomm.com":
            clientPort = 21000
        if name[4:] == "viasat.com":
            clientPort = 22000

        if clientPort == 0:
            value = "empty"
        else:
            serverSocket.sendto(name.encode(), (serverName,clientPort))
            serverSocket.sendto(type.encode(), (serverName,clientPort))
            value, serverAddress = serverSocket.recvfrom(2048)
            name, serverAddress = serverSocket.recvfrom(2048)
            type, serverAddress = serverSocket.recvfrom(2048)
            value = value.decode()
            name = name.decode()
            type = type.decode()

            RR[len(RR)+1] = { "name": name, "type": type, "value": value, "TTL": 60, "static" : 0}

    start_time = time.time()
    print(RR)
#--------------------------------------------------------#

    serverSocket.sendto(value.encode(), clientAddress)
    serverSocket.sendto(name.encode(), clientAddress)
    serverSocket.sendto(type.encode(), clientAddress)
