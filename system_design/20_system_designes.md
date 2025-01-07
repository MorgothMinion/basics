# 20 System Design Concepts Explained

## 1- vertical scaling:
- add more resource to a single node
- single point of failure

## 2- Holizontal Scaling:
- add more nodes. i.e replica
- this will add redundancy and fault tollerance 

## 3- load balancer
- work with horiznatl scalling to disribute the load
- revers proxy
- distrubute the load to the node, using different algorithms:
    - round robin
    - hashing the request id

## 4- Content Delivery Network - CDN
- loadblancer to distribute the load to the nearest location
- a network of servers located in different location
- used to serve static content
- they don't run any application logic, they just copy the files from the original server, they use either push or pull
- one of the caching techniques

## 5- caching
- making different copy from the file so it can be fetched faster
- like what happining in the computer it self, data cached from the desk to RAMs and yet it cached from RAM to CPU cache L1, L2, and L3

## 6- internet protocol address (IP) 
## 7- TCP/IP - includes UDP
- works using rules, aka Protocols that decide how to send data, protocols such http
- packets sent in numbers so once they arrived it can be re-assimpled
- if one packet is missing TCP will resend it again

## 8- Domain name System DNS

## 9- http 
- Application layer protocol unlike TCP which is a network layer protocol
- client send a request to the server which includes:
    - request header: where the package is going and who it is from and some other metadata about the package it self
    - request body: the package content
- with http there are api patterns we can follow

## 10- REST API:
- you make a single request for every response you are looking for
## 11- GraphQL
- is another API pattern
- unlike REST you make one request (query) only and chooses the resources that you want to fetch

## 12- gRPC
- RPC framework mainly used for server to server communication
- also there is gRPC web which allow client to server communication
- protocol buffers??

## 13- websocket
- use for chat and messaging. unlike http where it always needs to send request to server and get a response, websocket do bidirectional communication, so when you send a message it directly pushed to destination

## 14- SQL: relational DB
- arrange data into structured relational tables
- always ACID compliance

## 15- ACID
- Atomaciy
- Consisitancy
- Isolation
- Durability

## 16- No-Sql

## 17- Sharding
- devide our data and store it horizantally , using sharding key to know which data where
- sharding can get more complicated

## 18- Replication
- this is more simple than sharding and insure scalling holrizontally

## 19- CAP Therom




