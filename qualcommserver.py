from socket import *
serverPort = 21000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

RR = {
1: {"number":1,"name": "www.qualcomm.com","type": "A","value": "104.86.224.205","TTL": -1,"static": 1
},

2:{"number":2,"name": "qtiack12.qti.qualcomm.com","type": "A","value": "129.46.100.21","TTL":-1 ,"static": 1
},

}
print ('Qualcomm server is ready to receive')


while True:
    name, clientAddress= serverSocket.recvfrom(2048)
    type, clientAddress= serverSocket.recvfrom(2048)
    name=name.decode()
    type=type.decode()
    flag = False
    print('Qualcomm: Recieved ', type, ' request from client', clientAddress, 'for hostname', name)
    for x in RR:
        if RR[x]["name"] == name and RR[x]["type"] == type:
            value = RR[x]["value"]
            name = RR[x]["name"]
            type = RR[x]["type"]
            flag = True
            break
#----------------------------------------------------------#
    serverSocket.sendto(value.encode(), clientAddress)
    serverSocket.sendto(name.encode(), clientAddress)
    serverSocket.sendto(type.encode(), clientAddress)
