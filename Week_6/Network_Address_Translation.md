# Nating (Nat- Network Address Translation)

Nat - short for network addressing. 

Nat is used to address the shortage of IPv4 addresses, which had led to there not being enough addresses to assign a unique one to each device connected to the internet.

The private addresses are used within an organisation or on a site to allow devices to communicate locally. Private IPv4 addresses cannot be routed over the internet.
These are IP addresses with the prefixes:

10.0.0.0/8 - Class A
172.16.0.0/12 - Class B
192.168.0.0/16 - Class C

These classes/ranges are private, cannot be routed over the internet, but can be used to connect machines within a local network.

How to use this with a public IP?

Example: have an office with 50 hosts, each being given a private IP address. In order to connect these to the internet, this would not work, since web sources cannot reply to the private IP.

Instead, the router will be given a public IP address that will be shared between the private network connected to the user. In the scenario given, all 50 hosts would have the same IP address to an observer in the public domain, as though there was only one host browsing the internet.

NAT provides the translation of private addresses into public addresses.

Basically: Internal network -> NAT Router -> Internet (Public IPv4 address space)



NAT functionality 





The NAT-enabled border router is concerned with the translation of the private address space into the public address space. It will change the source of the package from one fo the private host addresses to the public IPv4 address of the network.

R2 will then re-route a received packet to the address that was the original source.

If several devices wants to browse the same server, R2 would keep a table detailing the information of these connections. Known as NAT table. The server reply will be destined for the router R2, where it will be translated back into the original destination using the NAT table.



Static Natting - assign a public address to a particular local address. This does not save addresses, however it has the benefit of hiding the actual private address.
Dynamic NAT Will have a “global address pool” which it gives to a particular local address, and keep other ones as available

Difference to DHCP: In DHCP would take an IP address for a predefined timeframe. In dynamic NAT, it will not be leased, but assigned in the NAT table. The router will therefore translate traffic to a particular global address until there is no traffic from the private address for a certain amount of time. In a DHCP server, renewal is needed after a certain amount of time. However, there is a limit on the number of addressing due to the one-to-one mapping of private IP addresses to global ones.

TO have multiple private addresses as part of one global address, use PAT (Port Address Translation) aka NAT overload. Here, the IPs are bundled inside a global IP address. The protocol will also change the source port when travelling to the outside. This massively increases the capacity of IP addresses, as a lot of ports are available. Teh connection is recognised based on source address AND source port.

NAT IPS DON’T FORM A NETWORK, MEANING EVEN THE BROADCAST IP CAN BE USED


