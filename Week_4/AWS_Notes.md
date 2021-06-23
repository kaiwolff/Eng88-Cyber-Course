AWS Notes




Instance ID: used to identify the instance internally.

Public IP address: access point for outside
Private IP address: used if creating small private cloud inside AWS network.

If not using IP address, can use DNS name.

	DNS = Domain Name System



Details Tab:


Mostly self-explanatory.

AMI ID - the image that you are using.
Key-pair name: name for the ssh key used to secure server. Make sure you have that as otherwise you cannot access the data.


Security Tab:

Inbound Rules, - rules for interacting with external input

Outbound rules: rules allowing communication from inside the network to the outside.


Networking TAB

Details for networking the instance.

Storage:
Self-explanatory

Status Checks


To connect to the server:

Click Connect: now have optiosna for ocnnection.


Add ssh key to identities on connecting machine
Ssh -i in - amazon provides this command
Fingerprinting - will discuss later


Keys, network, instances should be in the same region, otherwise can run into issues when launching.

Common Abrreviations in AWS

EC2 - Elastic Computing; the webservice that provides the cloud computing capacity. In another word, the virtual machines.


Security Groups

Volumes 

These can be checked 

Instances 

The set up virtual machines

Images (AMI - Amazon Machine Image)
The operating system that will be running on EC2

Network & Security Tab

Security Groups - we are currently leeting AWS create security groups by default. If configuring own cloud, would define these things ourselves.

Elastic IPs - we can allocate new IP addresses if we need to, for example if we are repeatedly starting new instances. This can be convenient, as a static IP would be useful if you repeatedly need the same point of contact

Key Pairs

The network keys stored in this group

Network Interfaces
Load Balancing - More on these later. Basically how to cope with a sudden influx of demand.

Launch Configurations - 

S3 - Simple Storage Service



ALWAYS REMEMBER TO TERMINATE INSTANCE ONCE DONE.
