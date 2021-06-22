Virtual Private Networks 2:

Use public network as a carrier, but no one on the public network can read the information being used. Thus, we create a private network, or tunnel, with the information being hidden inside the tunnel.

Without a VPN, if we wanted to securely send information or permit access to a server, the servers would need reachable public IP addresses, which would have to allow traffic from the other sites. This is of course a security vulnerability, as the servers would be accessible from the internet, potentially allowing a hacker to attack the server.

So, in order to hide access to a server,  but to give access to users in another network, is to create a private network between the two sites, which encrypts the


Can use VPN clients, or connect a network’s router to the VPN, to have access to resources from another site in a secure and protected way. Anyone attempting to listen to the connection would be able to see that traffic is exchanged, but would be unable to see the actual information being exchanged.

VPN Protocols

PPTP - Point-to-Point Tunneling Protocol
GRE - Generic Route Encapsulation
L2TP - Layer 2 Tunneling Protocol
IPSec - IP Security
SSL - Secure Socket Layer




The idea of tunneling is just to use the same network ID as a target network, which is how in a business you would connect between sites. 

Host-to_host VPN

Before a VPN is established, we would have network 1 with the host and network 2 with the server, connected bya  router. Their IP addresses are on different networks. Any traffic between them would allow reading of the data.

However, with a VPN, the host will establish a connection between its IP and the server IP. After that, the new, virtual IP addresses are created. The tunnel has thus been created. Listening to the router will still show traffic, however with a VPN the data is not readable at the router point.

2.  Host-to-Site VPN

Example: a mobile worker using a vpn client to access material from the site.

VPN server running on what is known as a VPN gateway. Can use a router configured to be a VPN gateway, a firewall, or a dedicated VPN gateway device. Also known as a VPN concentrator.

Host is now connecting to the VPN gateway, and then accesses the network that is onsite. The advantage is that instead of being connected to only one server securely, it can access the entire network and the public part of the traffic route is secured.

Site-to-Site VPN

Hosts keep private IP addresses,c connect to routers which then connect ot another router’s network using  VPN.
