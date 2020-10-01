from socket import *
serverPort = 22000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
RR ={
1: {"number":1,"name": "www.viasat.com","type": "A","value": "8.37.96.179","TTL": -1,"static": 1
},

}
print ('viasat server is ready to receive')

while True:
    name, clientAddress= serverSocket.recvfrom(2048)
    type, clientAddress= serverSocket.recvfrom(2048)
    name=name.decode()
    type=type.decode()
    flag = False
    print('viasat: Recieved ', type, ' request from client', clientAddress, 'for hostname', name)
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
