# Week 5 Networking

Week 5 - Networking 2: Electric Boogaloo

A network is several devices that are connected to each other. The main purpose is to exchange data.

When we say that we have a network, we have networked components. These can be categorised in several ways.


The Host

The main network component is the host. The host is the central point of the network. All computers that are connected to the network and participate directly in network communications are classified as a host.The term host refers to devices that are assigned an address for communication purposes.The other term for host is “end device”.

Server

Computer or software that provides a service to other end devices on the network. “A host that provides a service”

Client
A host that requests a service.


Architecture types

This is collectively termed server-client architecture. In this, the server cannot ask the client for a service.


Other option is peer-to-peer architecture. In a peer-to-peer network, hosts can work as both a client and a server. Examples of this might be device sharing, file sharing, etc. See below:





To connect the host and client, we use intermediary device. The purpose of intermediary devices is to connect other devices on t he network. Types include:



Their primary purpose is to connect devices or to provide a function for these end devices to be connected.


Network Media;

The medium that we use to interconnect the devices. Network media include:

Metal Wires (aka cabling)
Fibres
Wireless

Network Type
Canc ategorise network based on:

Size of area covered
Number of connected users.
Types of Services
Area of Responsibility


Network Infrastructure

LAN: Local Area Network
WAN Wide Area Network

Lan is for small geographical area. Eg A house, an office, a building…

WAN is designed to provide access to other networks over wide geographical area. Generally managed by larger corporation or a telecom provider. The Internet is a collection of WANs. WANS usually used to connect several LANs together.





Also have MAN: Metropolitan Area Network. This term exists but is not widely used. Can generally be considered as a WAN. WAN is more generic and more ocmmonly used.

The Internet is a collection fo interconnected networks



Intranet; a private connection of LANs or WANs, usually belonging to an organisation (or group). Classic examples are company-internal networks.

Extranet: Another concept, not particularly well defined so will avoid talking about this.

Designed to provide secure access to people between two different organisations. Closed, private, but not as simple as an intranet. Example would be the NHS. Government agency, but needs to communicate between different trusts that may not be on the NHS intranet.



Area of Responsibility. In LAN, the network is managed on a smaller scale (e.g. the homeowner). When connected to a WAN, you are responsible for your LAN, but not the WAN itself. WAN responsibility is the provider’s (e.g. BT)


3 Elements of Communication


Source, Destination, Channel

Goal of communication is to transmit a message (from source to destination)


Message Delivery options

As Unicast
Multicast
Broadcast

Choice depends on number of users, and whether the message is meant to be targeted or not.

Unicast targets only one destination. Multicast targets a set of destinations. A broadcast is available to all destinations.


Protocols

Protocol Suite - ISO Suite

Protocol suite, or standard, are a group of protocols required for communication. For example, we have a protocol to manage the network media, or a protocol to show that a message has been delivered to the destination.

ISO

TCP



63+25.

ISO is a family of protocols, developed by International Standardisation Organisation in 1977. The ISO suit, is open 

OSI - Open Systems Interconnections

When developing a physical object, you also need to take care of the protocol for the Data Link portion

#### Physical - Network media
The physical level is stuff like the frequency used for wireless, what is sent down which channel in cables..


#### Data Link - Physical Addressing, Data Exchange over common media
The data link is about how to send and receive the data.Describes the means for exchanging the data over the medium. How the two shots should communicate directly. Data link provides the functionality to isolate the physical layer from the network layers and above.

#### Network Layer  - Addressing, Routing, Data Exchange across Networks
Provides service to allow end devices to exchange data across networks. While Data Link only takes care of hosts on the same network with common media. The network layer tackles communication across larger networks or one across several devices. Network addressing is more general than data link.

The network layer provides addressing to be used for cross-network communication. The classic example is the IP address. The key function is to give an address for each end device on the network. It will also give us routing.

In order to know which route we should take when several networks are connected, the network layer solves this. This and addressing are the main two thin562.s provided by the network layer.

#### Transport

TCP - Transmission Control Protocol. 
UDP - User Datagram Protocol

TCP make sure all the data sent is received by the receiver.  UDP does not have this guarantee. This means that some data will be delivered, but if data has not been delivered, it does not matter to UDP.


TCP use case - email. All data needs to be delivered correctly to the receiver side.

Use case for UDP is continuous communication, where a continuous delivery of data , a classic would be livestreams. Maybe a quick wobble ina  picture, but the continuous transmission is more important and it would actually be harmful to try and enforce complete transmission of data. Cases where it is more important to continuously broadcast over sending everything perfectly.

#### Session

Communication between hosts

#### Presentation

Data representation, and excryption.

#### Application Layer

Data accesses by applications/users here, e.g. HTTP, Telnet


TCP/IP Layers




We have:

Network Access Layer - control hardware and media that make up the network. Here we specify what the best path through the network is and give IP addresses
Internet Layer - part of network layer in OSI. Similar purpose
Transport Layer - aforementioned TCP or UDP - Defines whether connection-oriented 
Application Layer - includes all the protocols such as HTTP - represent data, encoding and application protocol



OSI and TCP/IP model



OSI Model provides more abstracted description, but the concrete protocols stem from teh the TCP/IP protocol Suite.

How do the protocols work together?



This is called encapsulation. Each service adds its own data, which are called headers in the above diagram.

De-Encapsulation is the reverse of this. Each layer there takes away the data that was added by a different layer.


 TCP vs UDP



Both rely on IP, but the protocols that follow on are different. As can be seen from the options, IP focus on one-to-one connection where fidelity matters, while UDP is more tolerant of some data loss during transmission, while delays matter more to UDP than to TCP, where delays are comparably acceptable.

Port Numbers

When an application or process is attempting to work with a computer, they would normally listen to a port number. It is only possible for one app or process to listen to a port number at hte same time. The port numbers are thus used to manage multiple simultaneous ‘conversations’. 

IP sends to either TCP or UDP, then check destination port number and pass it to the next protocol or application. Notice that the source port and destination port are different.


SERVERS

In order to provide the service, the server needs just one port. The source port is different, but the destination port is just one..



Port numbers are a 16 bit integer, so range from 0 to 65535. IANA (Internat-Assigned Number Authority) will fix szome of these ports to certain services

0-1023: Well-known ports. Reserved for popular services, e.g. browsers
1024-49151 - Registered ports. These processes are primarily for applications that a user might commonly install.
49152-65535 - Private or Dynamic ports. For use and re-use by applications. Often used temporarily, whereas the previous numbers might more consistently use the same number.

Some more famous ports:

TCP 20: used by FTP (File transfer protocol): data
TCP 21: FTP - control
TCP 22: SSH - (Secure Shell)
TCP 23: Telnet (Non-secure compared to ssh)
TCP 25: SMTP (Simple Mail Transfer Protocol): Email.
TCP 80:HTTP (HyperText Transfer Protocol) - Web


Bandwidth

Defined as the capacity at which the medium can carry data. Generally in some form of bits/second (obviously in Megabits, gigabits or erven Terabits).

Addressing Standards

In order to understand networking, we need to understand the binary numeral system

Both binary and decimal (base 10) system are positional systems, meaning that each symbol changes it’s meaning depending on where it is situation (eg 11 shows 1 “1” and 1 “10” in decimal).  


Addressing in the data link is done using “Media access Control” (MAC). A MAC address is a global address that comes with the network interface card (NIC). This is hard-coded into the NIC.

A MAC address is 48 bits, expressed in 12 hex numbers.first six are “OUI” (organisationally unique identifiers), and second siz are NIC-specific. The actual MAC address cannot be changed on the NIC, but you can set this up via the network. 

To check in Windows: ipconfig /all

Can use this to find out vendor via various websites.

On linux and mac it becomes ifconfig -all


Network Layer Addressing:

IP (Internet Protocol) Address: Used to identify the host of any network. Several versions exist currently, IPv4 and IPv6. IPv4 still dominant, although migration towards IPv6 is ongoing.

IPv4:
Series of ones and zeroes. Composed of four octets (8 bits). Total of 32 bits. 

E.g 172.16.254.1 becomes 10101100.00010000.11111110.00000001




Can identify computer on network by following. All addresses starting with network ID octet (or octets) are from the same network. Can identify type of address by opening bits (see above picture).

So first number 0-127 is Class A, 128.0 to 191.255 is class B

This is useful as it lets us know if hosts are on the same network or not.

Find network ID by finding Ip class and then using correct number of octets for lookup.

Subnet Mask

This is a way of series of ones followed by series of zeroes. This allows the extension of the network address at the expense of the number of hosts. The format will be a series of 1s to designate the network portion. Using a logical AND (think if statement-style) the net address will be obtained when



The idea of the subnet mask is to liberate the IP address from the enforced octets.was a fix to the fact that network portion of address was static in old ip addresses. Allows dynamic network address size.

Recap again:

Series of ones, followed by series of zeroes. Defines which sections of the binary are network and which are host address. 1s represent network Id, zeroes represent host ID. ELIMINATES CLASSES




#### The Host

The main network component is the host. The host is the central point of the network. All computers that are connected to the network and participate directly in network communications are classified as a host.The term host refers to devices that are assigned an address for communication purposes.The other term for host is “end device”.

#### Server

Computer or software that provides a service to other end devices on the network. “A host that provides a service”

#### Client
A host that requests a service.


### Architecture types

This is collectively termed server-client architecture. In this, the server cannot ask the client for a service.


Other option is peer-to-peer architecture. In a peer-to-peer network, hosts can work as both a client and a server. Examples of this might be device sharing, file sharing, etc. See below:


To connect the host and client, we use intermediary device. The purpose of intermediary devices is to connect other devices on t he network. Types include:

Their primary purpose is to connect devices or to provide a function for these end devices to be connected.


### Network Media

The medium that we use to interconnect the devices. Network media include:
- Metal Wires (aka cabling)
- Fibres
- Wireless

### Network Type
Can categorise network based on:

- Size of area covered
- Number of connected users.
- Types of Services
- Area of Responsibility


### Network Infrastructure

- LAN: Local Area Network
- WAN Wide Area Network

Lan is for small geographical area, such as a house, an office, a building…

WAN is designed to provide access to other networks over wide geographical area. Generally managed by larger corporation or a telecom provider. The Internet is a collection of WANs. WANS usually used to connect several LANs together.

Today, working with IP addresses.

The whole process is built on binary. Therefore, quick revision of binary.


## Layer 3 Addressing

Every computer has an IP address on the internet. For human-readable form, we put this in dotted decimal form. E.g 216.24.61.137

This is expressed in binary by machines, as a 32 bit unsigned integer, in 4 octets separated by dots.

Layer 3 addressing is divided into classes, see previously shown table for how these are split up. The more of the 32 bits is dedicated to the network address, the more networks are available, and the fewer hosts (as they have to share 32 bits).

### Calculating Network ID
 Can be done in several ways. Generally looking at first octet and totalling. Number ranges determine type of address. Can also look at starting binary numbers.0


### Subnet Mask

Subnet mask is a 32-bit address used to block or “mask” a part of the IP address to separate the network ID front eh host id.

Each host on a TCP/IP network requires a subnet mask.

Default subnet mask is used on TCP/|IP networks that are not divided into subnets

Bits that are part of the network address are set to 1, bits that are host ID are 0.

Always in two blocks, left block is 1, right block is 0

The “Broadcast IP” is the last available IP in the network. It cannot be allocated to a host. All the host bits will be 1 (network ID will be the same as before). Broadcast IP is used to send specific data to all the machines on the same network. Usually abbreviated to bcast IP.


Two sets of addresses are reserved. Anything starting with 10 is private

Loopback is 127.0.0.0 Net etc

Localhost is addressed as 127.0.0.1
This means that if you try to connect to 127.0.0.1, you will be immediately looped back to your own machine. This is the method for communication with your own machine.

Each machine considers itself to be 127.0.0.1

First UP all host as 0 except the last 1

Last IP all hsot id is 1 except last digit is 0

Broadcast - all host part is 1



The problem with classful allocation is that a lot of addresses are wasted for subnets with asmall number of hosts. We can either use IPv6 (which si a recent development, or use a subnet mask to render the entire setup “classless”


CISCO Packet Tracer - Running Notes

Cna be used to set up a simulation of a network, in preparation for setting up a virtualised network. Once we have got the hand of it, we will be given files and told to configure the network

Network Switch - A connection point. They understand mac addresses, but don’t work with IP addresses

Testing Connectivity, just ping via command prompt

Ping is a tool relying on a protocol called ICMP (Internet Control Message Protocol).

Whenever the switch has a packet to an address it doesn’t recognise, it will send to everybody and receive back the reply from the correct one. But, once received, it will learn the mac address, and remember it. Therefore, it will send a second ping only to the address it has identified as belonging to the correct MAC address.

ARP protocol

Stands for Address Resolution Protocol. ARP is used to find the mac address that belongs to an IP address. Basically asks device to answer with mac address if the IP address is correct. This allows the switch to identify the correct address. Other devices discard the received packet without replying. ARP cna also tell us if something has the same address on the network, in which case it stops the IP address from being assigned.

Notice that if two hosts are on different private networks by logic they will not be able to communicate, even if they are sharing a switch (as in, are physically connected)

IP Address Tools:

Ipconfig is a Microsoft utility which verifies network connections and settings. On linux, it is not available, and the tool is ifconfig.

The option /all will show all the information

PIng Options

Ping -t: pings until stopped

-n count - number of requests to send


Usually get either:

Reply from - received by target host and answered

Timed out - sent but no reply received

Destination Host Unreachable

Route to system cannot be found.


Broadcast Domain vs. Collision Domain

Broadcast Domain is the region that a broadcast is heard on. When we send a broadcast on a network, it doesn’t usually reach the entire network, and will stop at the router instead. A BROADCAST CAN NEVER GO BEYOND A ROUTER, or generally, any layer 3 device. Therefore, if a router was dividing up parts of a network, the broadcast domain would not be the entire network. A switch will pass a broadcast signal on the other hand. NOTICE THAT A BROADCAST DOMAIN INCLUDES MACHINES THAT DON’T SHARE A NETWORK, BUT ARE ON THE SAME SWITCH FOR EXAMPLE.

Once we reach layer 3, the devices should understand IP addresses. Any device that “understands” IP addresses will not pass on a broadcast signal.



A general sending procedure inside a network. PC1 knows it’s own MAc and IP address, and the target address. It will need the target MAC address to send, and gets this either from its cache if it has already sent, or will attempt to use ARP protocol to resolve this issue. If it gets the MAC address, it can then send the package.

Devices cannot exchange traffic using layer 2 protocol unless their IP addresses are from teh same subnet (that is, if they are on the same network by logic)

On different IP subnets, we would need to exchange data through a Layer 3 device, such as a router.


Routers

 Layer 3 device that can be used to route traffic between subnets. A computer with two network cards can be turned into a router.  The use of the router is that as a layer 3 device, it “understands” IP addresses, and can therefore be used to communicate with devices outside of the subnet.

The Default Gateway

Teh device that will be used by the host to contact other networks. This is normally the router. The router will need and IP address on the network to be contactable. WE also have to make sure that the PC we are sending the data from knows where the default gateway is using the router’s IP address.

CANNOT ACCESS THE SAME DEFAULT GATEWAY FROM DIFFERENT BROADCAST DOMAIN DIRECTLY. 

A router can only have one IP per subnet. If subnet is split across broadcast domains, either change subnet of pc, or move the pc to be in the correct broadcast domain. Need to be LOGICALLY AND PHYSICALLY CONNECTED TO THE SAME BROADCAST DOMAIN.

Advice, keep default gateway IP should not be standardised. If the address has a pattern, then an attacker has an easier time finding the gateway, and exploring the network from there.



So, when sending between networks.

PC1 knows it’s mac, mask and IP, target mask and IP and gateway IP (same mask as its own). Will get gateway mac using arp or the cache, and the same. The target mac address would be obtained by the router using either the router’s cache or the arp protocol.

Recap on default gateway

The device that weill handle traffic between different IP networks.Devices have to be physically and logically connected under the 3rd layer in order to communicate on the same subnet.

Connecting between routers.

This exists as it’s own network. So the routers need IP addresses on this network. The routers will know onl ythe networks they are directly connected to initially (includign the router), so we need to set up static routing between the routers so that they know to pass any traffic headed for a particular network ID onto the other router. The other router’s IP address should be the “next hop” for a target network ID.

### Quick Recap before the next section

Router is a host. Switch is not. Switch will take a packet and forward it to everybody.

Routers do not pass on ARP requests, as they are layer 3 devices. Only layer 2 passes on broadcasts, because they do not understand IP addresses. 

If you were pinging a device from another network separated by a router, the router would just return its MAC address. The router handles the requests to another network separately. With static routing, the router will check if it has a network ID associated with the target IP address in its database, and then pass the request that way if needed.

### DHCP - Dynamic Host Configuration Protocol

Helps to configure many hosts, where setting up hosts individually may not be practicable. If you then needed to change a config aspect, you would need to do it to each host individually. DHCP solves this by having hosts be issued with a configuration. An extension of Boot Protocol (BOOTP). Listens to Port number 67/udp for server side, 68/udp for client side.

Doesn’t really “give” the configuration to a host, but rather “leases” the configuration. Configuration is temporarily allocated. Changes are updated as the lease is renewed, and this can lead to downtime if for example a default gateway is changed.

These messages are used to set up or alter the configuration of a hostVarious message types - a few examples include:

- DHCPDECLINE is sent if an address is found to already be in use
- DHCPRELEASE - client telling the server that they no longer need the elase and relinquishing the IP address
- DHCPDISCOVER is a broadcast to locate available server 

DHCP also has other options to offer, e.g. Subnet Mask, the name server, Domain name, and so on. This is a convenient way of settign up a series of hosts which have the same networking details.



### Example Case.
New host, needs an IP address, sends DHCP DISCOVER. DHCP servers say what IP and for how long they can have it. It accepts a particular setup. ACK sent by DHCP (acknowledge) to confirm lease. The host now has that IP address for the length of the lease.


#### Ipconfig

This command has DHCP options. /renew to renew configs. /release to release current lease. Renew is particularly useful if more details have been added onto a DHCP server (such as a DNS server)

## Setup

Instead of assigning a static IP address to our PCs, we set them to look for the DHCP server instead.  The DHCP server will need a default gateway (if needing to use a router), IP address and subnet mask, as well as instructions as to what IPs to assign,w hat the default gateway should be and how many users can be assigned. Note that this can make direct pinging difficult, need a dns (domain name system/server?) for this.


Normally, server only operates within it’s own broadcast domain, but this can be circumvented.


**APIPA** - automatic private IP addressing. This is what we use to have private addresses set up.

Handy Tip, a Router can be set up to also act as a DHCP server. This means it automatically assigns IPs.

DSHCP is an APPLICATION LAYER PROTOCOL, NOT NETWORK LAYER.  Whenever you know that a protocol uses a port, that means it is an application layer protocol. Added a DHCP server to the packet tracer simulation.

### HTML/HTTP

Markup language. Not a part of the application layer. Data Layer, is concerned with data nad hwo data is written. Transferred via http (hyper text transfer protocol). Http was designed for the communication between a web server and a web browser (client-server protocol). Client is the browser, web server is the server.

By default the http protocol takes the tcp port number 80. Adding a http server to nbetwokr 1 in our packet tracer simulation 

#### HTTPS

More secure version of http. By default, works on port 443. 


### FTP

File Transfer Protocol. The standard protocol for file transfers on the internet. Uses port 20 and 21 by default. Also a client-server protocol. Usually, if downloading a file from browser, not using ftp, but rather http or https. However, if wantign something efficient and designed to transfer files, ftp is the wya to go.


### DNS
Short for domain name systems. The idea is that IPs are not easily human-readable, and that DHCP can further mess with the IP addresses. Hierarchical system. Each domain might have child domains, for example edu might have colorado, or uk might have ac , which might have shef, leading to shef.ac.uk. By default, uses Port 53/UDP

### Setting up DNS in packet tracer:

Instead of accessing the web server using an IP address, want to access using a URL. Need to add a DNS server. Once added, we can start adding names for IP addresses. Will need to make sure that the DHCP server is updated to include the DNS server. This way, any new devices will automatically receive the new DNS server address, and they can be reset using ”ipconfig  /renew”. 

Host then recognises name rather than IP, contacts DNS server, DNS server just returns the IP associated with the URL and the host then communicates with the target IP address.

Several of these processes can also be set up for several of these services. A lot of this can actually be done just through the router, for example.

It is possible to access the DNS server from another network, but the IP address needs to be set up correctly. You can set up a DHCP server that points to a DNS server etc outside of the network. ONLY THE PROTOCOLS THAT DEPEND ON BROADCASTS NEED TO BE CONTAINED IN THE SAME NETWORK

## Firewall

A device, system or software. Idea is to control access policy between networks. We will study

- How the firewall enforces a policy
- How to write these policies.

SSL filter the access to the network or network resources. When we want to protect, limit or grant access to network resources, we generally write an access list (ACL). Main options are either GRANT or DENY. An access list is a collection of the rules that grant or deny access to a certain resources. Could be anything: a file, a printer, etc. These take a different format depending on what the access list covers.

A firewall is a system or group of systems, that enforce these access lists.

All firewalls share some common properties:
- Should be resistant to network attacks
- Can filter traffic
- Can allow or deny access based on the rules they have
- They enforce their access list
- Can be either hardware or software


If software,can be installed on the host, server, etc.

If it is hardware, then it is a computer enforcing an access list/policy.


Firewalls can be used both to protect the users from accessing unsafe content, and to prevent unauthorised access from outside of the network.

Firewall Policies: Either allow something to pass, or not. Decision depends on variety of factors, e.g. destination or origin IP, port connected to (for example a web server might allow traffic but only via ports 80 and 443 for HTTP and HTTPs traffic)

### Packet Filtering Firewall

A firewall that controls the network access by analysing outgoing and incoming packets, based on information in the network and transport layers. Will check IP address, TCP or UDP and ports. Based on this information, will either allow or deny the traffic.

 Intercept packet -> Check network and transport layer info -> if in allow policy, let through.


## Application Gateway Firewall

 Will check the application data. Working on more than just layer 3 and layer 4 data. Can also check the application (e.g. whether working with http, etc etc) More capabilities than packet filtering firewall.

### Firewall Zones

Will always have an inside (private) zone, and a public (untrusted) zone. Usually, you would trust your own network, and connected public networks are untrusted. Also have DMZ (“demilitarised zone”) which can be accessed from the outside in order to use certain services (for example, a web server might be added to the DMZ), since we might want part of our network to be accessible from the outside. Would allow the DMZ to be accessed from the outside, and from the inside, however the network cannot be accessed from the DMZ. The idea is to isolate anything interacting with the outside world from the rest of the world. This wya, if there are any breaches, they are contained within the DMZ.You can have several DMZs, and it is good practice to do so. Generally, the more separation between the network and the public domain, the more secure and trusted the DMZ is considered. You should not allow access from a less trusted network onto a more trusted network normally.

#### Wildcard Mask

Can be considered as the opposite of a subnet mask. In a wildcard mask, blank is 255.255.255.255
