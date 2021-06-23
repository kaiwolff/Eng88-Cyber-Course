# Week 6

The first two days of this week were devoted to a project ot creat a password checker and generator in python. The project was forked to the repository https://github.com/kaiwolff/password_generator
and modified in branches to achieve integration of SQL and to get the functions to work as part of a Flask webapp.

The other days featured recaps and more in-depth exploration of some previously covered topics, and begins the introduction to SQL & databases.

## Virtualisation 3:

Recap: Hypervisor is used to interface between the virtual machine and the host, as opposed to a traditional compute where the operating system interacts with the hardware.

Type 1 hypervisor - “bare metal” on the hardware.
Type 2 - sits on a host OS.


Type 1 considered more secure, generally. This is because more systems mean more potential exploits.


### Vagrant

Tool for building and managing virtual machine environments in single workflow.

Allows the quick reproduction of the production environment, which makes testing much easier.

Workflow of Vagrant:

- Developer creates vagrant file
- Vagrant uses a virtualisation method (e.g. Virtualbox) to create the virtual machines that are requested
- Will include a common directory with the host OS
- The virtual machien can now be used by the developer

### Containerisation

Abstraction at OS level. NOT a full virtual machine, but a different form of virtualisation. Containers hold all the configurations and everything else related to a particular software. Contains only part of the operating system. Uses the host operating system, all containers share the same host operating system through a container engine

#### Docker

Docker is a container engine. It can also give us a network of containerised “systems” if needed. Docker commands are run from our host operating system using docker client. Dominant provider of containerisation.

##### List of useful docker commands

`Docker container ls` - lists running containers

`Docker images` - shows stored images.

`Stop` vs `kill`: stop will give a grace period to container to finish its work. Kill outright stops the process.

# Virtual Private Networks 2:

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


# Introduction to SQL

### What is a database?

A collection of information. A database is a structured set of data. In the case of SQL, the databases are stored digitally. A database system allows the 

Databases are crucial to most online interactions. E.g. logins, booking systems, contact lists.


We need to structure data in a way that allows the easy querying of informations. Making queries is an essential operation we need in a database. For example, we need to be able to search an address book for the address associated with a particular person.

Starts with deciding on the ‘Fields’ to use in a database. All fields will be in a table, with fields corresponding to a particular bit of information.

E.g. First Name, Last name, Birthday, etc.

Table is displayed in columns and rows.

A column represents a category of information.A row represents all the information about a single object inside the database, e.g all the information on a customer in an order database.

Other key terminology: Table - predefined format of rows and columns that define an entity. Aka File. Tables exist inside a database. A database can contain several tables. E.g. a supermarket database might have a database with tables of payments, of customers, of employees, and of stock levels. A field is a cell in a table.

DBMS - DataBase Management System. Allows computer to perform database functions of storing, retrieving, adding, deleting and modifying data. 

Relational Databases - these contain connected data. Tables should be related.

For example - have Reviews_DB, a database of reviews. Could contain a database called book_reviews of the reviews, listing the book name, author_id, date of release, publication status. Email addresses etc.

Then have the author_id refer to a table called author_details, where information on the author can be found. 

Could also have a table linking the publishers of reviewed books, and then a separate table again containing the contact details of various publishers.

A few standards. Use lowercase with underscores as spaces for naming tables. E.g table_customer_info, or table_library_staff

Types of Database

Flat-File
Everything in one Table. Good for small number of records related to single topic

Relational
Ability to separate masses of data into numerous tables
Linked through use of keys

Big Data
MongoDB, Vertica, etc
Used in Data Analytics and Business Intelligence
Also useful in IoT


### Relationship Types

One to One
Each row in A is linked to no more than one row in Table B Attribute of the relationship, not the tables. E.g. A student may have one row in the contact_info table

#### One to Many

Each row in the table can be related to many rows in the relating table
Allows frequently used information o eb saved once in a table and referenced many times in other tables. An employee might have several tasks to do, for example.

#### Many to Many

Oner or more rows in a table can be related to 0,1, or many rows in another table

A 3rd table called a mapping or link table is needed in order to implement this relationship. A customer could purchase many products for example.

#### Primary Key

Used to uniquely identify each record in the table

Most tables should have one. Each table can have more than one column which is part of its primary key (known as a composite key). Examples include order numbers or order line numbers.

The primary key can either be an attribute that is guaranteed to be unique (like an NI number) or can be generated by the management system.

The management system will enforce the uniqueness of the primary key, which means it will not allow repeated records to be part of the table.Constraints

Must be unique
Must always have an entry
Value must never change
Maximum of one primary key (although you can have a composite key)

Classic example of a compositie key would be order number and line number (like below)




Foreign Key

Foreign keys are used to create relationships between keys.

Foreign keys ensure that the rows in different tables correspond to each other correctly.
Constraint is used to stop actions that would destroy linking between tables.

No uniqueness constraint
Can have any number of foreign keys.
Row cannot be deleted from a reference table if used as a foreign key

Advantages of foreign keys are that we can change aspects of a particular thing for several dependents at once - such as updating a job description or a user groups privileges. We can also standardise input, compartmentalise information better, and overcome language barriers.



Designing a Database

Usually start with an entity relationship diagram, such as this one:



Decide on relationships, e.g. one-to-many when going author to books database.


	See presentation for an example of a timesheet database

Database Tools

Microsoft access - local database setup for small amount of data. Not as powerful as oracle or mysql
Microsoft SQL server. Designed to be accessed by more users and be internetaccessible, and so on

PostgreSQL (aka postgres) SQL-based relational database. Older, but widely used as it is open source database tool. Follows SQL standards.

SQLite - file-based embedded relational database.Popular choice for small databases.

MySQL Server - most widely used, cross platform. Works with SQL as most others do. By far most widely SQL database tool.

Redis - “key-value store”. More lax on standards compared to some other database tools. Past use cases include a set of keys with changeable values (such as a cloud computing project with hundreds of containers working in groups across different servers). The number of containers should be read by the apps working in the cloud. Run Redis database on the server where it can be queried to ask how many containers are working right now.


MongoDB - based on JSON . used for big data

Oracle - generally used for big projects - not free.

SQL stands for structured query language.


Notes from practical - mostly commands:


docker-compose up -d runs container as a daemon
docker exec -it mysql_dbms mysql -u root -p

