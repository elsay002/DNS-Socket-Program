

# DNS-Socket-Program
A simulation of DNS-Client interaction 

##Client
Client sends DNS Requests to Local Server

##Local Server
Local server waits for request from client. Local server has presaved querys. If request cannot be found in local server, send request to other DNS servers. Local server saves
returned quertys locally for a limited time. 

##QualcommServer and Viasatserver
Servers both wait for requests, send back querys to local server.
