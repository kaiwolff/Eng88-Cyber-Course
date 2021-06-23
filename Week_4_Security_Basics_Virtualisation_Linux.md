# Week 4: Computing, Security, Windows & Linux, Virtualisation Intro

## Introduction to Computer Components and Operating Systems

There are three basic types of computer components, that need to be considered from a security perspective:

- Hardware
- Software
- Humanware

For a long time, humanware was not considered sufficiently. This means considering how a user might actually be using a computer, which may be at odds with how it was designed to be used.

### Servers

Servers are computers which provide a service to other computers. This can be the data servers commonly associated with the term, but technically, if a user sets up their laptop to provide access to a printer for other users, that laptop is also running as a printing server.

A server will require different security protocols to a general purpose computer.

## Windows Security - Best Practices

This will be summarised as a "securing windows checklist".


### PowerShell

This is a windows designed multiplatform shell, that can be used in a way not dissimilar to bash

### PowerShell - Basic Commands

Get — To get something
Start — To run something
Out — To output something
Stop — To stop something that is running
Set — To define something
New — To create something


There are a lot of commands, data types, and comparative operators. generally, these are best explored with searching when needed. I may attach a few tables once I have formatted them.

##### Pipelines

These are used to send the output from one command to another command. this is shown using `|`. Extremely useful in scripting.

##### Windows Security - A few basic tips

First thing to check is whether Windows version is genuine or cracked. command for this is in powershell or command prompt and is ```slmgr /xpr```. This should return whether the windows version on the machine is activated or not.

Now tha twe have checked whether windows is genuine or not, the second thing is to deactivate Windows automatic login. When we create a new account on Windows, it is set to activate automatically, which is not particularly secure.

In order to do this use, win + r and then entering ```netplwiz```. If you have an account that doesn't need a username and password, it is advisable to force this. In the 'Advanced' tab, it is also possible to force the user to enter Ctrl + Alt + Del before the login screen appears, which ensures that the login screen isn't another program mimicking the login screen.

Clicking on the advanced options screen in the advanced tab will bring up even more options, such as making the suer change their password the next time they log in, or preventing a password from being changed.

So, having checked that hte windows version isn't a hacked or cracked version, and that there are no unexpected user accounts, we now check on automatic updates. Windows and most other operating systems have continuous updates to address bugs, security issues, etc. In Windows, it is important to have automatic updates on, so that any security weaknesses are fixed as quickly as possible. This can be checked and configured in Windows' "Update & Security" Settings.

##### Password Policy

Enforcing a strong password on a network can also be key. microsoft recommends:

- Password should not contain the username, or the user's actual name.
- Password should contain characters from 3 of the following
    -   Uppercase letters
    -   Lowercase letters
    -   Special Characters
    -   Numbers
    
If needed, passwords are changed through the control panel.

Group Policy Editor can be used to edit Password Policies.  You can enforce things such as the maximum age of the password, minimum length of the password, and so on.

Sign-in Options - these can be used tro change how signing in is allowed, including a PIN, fingerprint, a physical security key, etc.

It is also good practice to have several accounts. This compartmentalises data into.

Keeping a daily operation account as non-administrator is also good practice. If you are browsing the internet, for example, you may be tricked into clicking on a dangerous link. If you user account does not have administrator privileges, the damage this link can do is limited by the lack of permissions.

Disable guest account. This prevents unauthorised users from accessing your PC, even if a guest account has limited privileges.


#### Encrypting Data

If data needs to be particularly secure, it may be necessary to encrypt data. Windows Business/Pro has bitlocker for this. It encrypts using either 128bit or 256bit encryption.

### Basic Checklist for Securing a Windows Machine

Note, this list is non-exhaustive:

- Limit User privileges to the ones that are strictly necessary
- Don't have guest accounts
- Have several accounts with privileges tailored to their purpose
- Enforce strong passwords, and regularly make the users update their passwords

#### Checking a machine for suspicious activity

Starting Points:
- Check users, and their privileges. Malware often seeks to install a puppet user that it can use to manipulate the machine
- Check logs for suspicous events
- Check for new key markers regularly


## Introduction to Virtualisation


Virtualisation provides a layer between the software and the hardware, enabling us to take a configuration or set of packages and run them regardless of the underlying hardware.

Before virtualisation, it would be necessary to acquire compatible hardware to run a particular software or application For temporary purposes, this coudl lead to the acquisition of specialised hardware, which would then sit idle once demand for the service returned to normal levels. To make a machine work with a new application, or to set up a new server, it would be necessary to purchase the hardware, install the correct operating system, and then install and run the software.

Through virtualisation, we are able to run software or applications on a much wider variety of hardware, meaning that the process of providing a service can become much more scalable. Through virtualisations, it is also possible to have a virtual server that is not tied to a particular piece fo hardware, which protects the system against the failure of a physical node.

A good example of this is Java, which runs through the Java Virtual Machine. This makes Java much more portable than some other languages, which require compiling separately for each machine.

### Type 1 and Type 2 Virtualisation

There are two types of virtualisation, Type 1 and Type 2. Type 1, also known as bare-metal virtualisation, has the virtualisation layer interacting directly with the hardware being used. Type 2 virtualisation interacts with an operating system instead. Type 1 is preferable, as the lack of an OS provides fewer potential security flaws. However, Type 2 virtualisation has the advantage of convenience, as it enables users to quickly employ software on their machine.

### ISO Files

These are also termed disk images, and represent a virtual disk. For example, they can be used to simulate a disk by mounting them in a virtual disk drive, or be burned onto a CD or USB stick. The files contained on the disk image can also be extracted using dedicated software.

## Virtualisation - Part 2

In part one, we looked at virtualisation that took the same structure as a computer, but made it portable. We used  a hypervisor, a virtualised version of the hardware that allows the software to run. Effectively, we were mimicking the hardware as a software. The result is having a machine running on 'pretend' hardware. The disadvantage of this is slower performance as the system is having to expend more effort to emulate the hardware, and some of the host system's capacity is reserved by the virtual machines.

More recently, there have been attempts to more easily employ virtualisation, to automate the process of virtualisation, and to employ virtualisation in the development phase.

One of the biggest challenges that developers face is the difference between the development and the user/production environment. 

In the past, the developer would write the code, send the code to the production environment. If there was a difference between the development and production environment, this could lead to conflicts. The cause was usually differences between the development and production environment, for example OS type, versions of particular software packages, etc.

Virtualisation can let developers recreate the production environment for the developers to use in their testing befor ethe code is sent to production.

For this, we use software such as Vagrant - a tool for managing virtual machine environments in a single workflow. You would pass a config file to the developers, and the virtual machines would then be created by vagrant. Vagrant is a building and management tool, nto a virtual machine or a hypervisor.


For example, if a developer was working on two projects with different requirements, the requirements are put into a vagrant file instead of needing the developer to install the requirements. By compartmentalising the testing into virtual machines, it is possible for the developer to avoid the need any potential conflicts.



### Using Vagrant - Running Notes

`vagrant init` will initialise a directory for vagrant

Then set the machine via a vagrantfile.

Finally, “up” will set up the virtual machine. After a pause, a new virtual machine will have been created.

The directory that was set up and initialised will be shared between the user PC and the virtual machine.

Use Case: could have a pycharm project directory targeted by vagrant, which allows the testing, then also git push it to a repo if possible.


### Docker

Docker offers a different concept of virtualisation to Vagrant, focusing on “containerisation”.

The guest operating system shares nothing with the host or each other in hypervisors.

In Docker, this is not the case. Containerisation creates abrstraction at the OS level, allowing functionality to run in an independent way. This means that instead of having to ensure various libraries are installed before another user could run an app, containerisation allows a “container” to be sent, which contains all the dependencies required to run the application. Unlike a full VM, the container is not a complete virtual OS. It is run on the host operating system with the aid of a container engine.This is different to a hypervisor, as there is no guest operating system or hypervisor, just a container engine running the container inside the host operating system. This reduces the footprint of the virtualisation significantly, and decreases the likelihood of performance issues, as the hardware does not effectively need to run two separate operating systems.


Another difference is that with a VM, the guest OS can be any OS. As there is no sharing at all between the virtualised environment and the guest OS, this doesn’t differ. For container engines, the host OS is shared, which needs to be accounted for.
Containers are much easier to run, since they require a much smaller download and doesn’t require as much installation. For most use cases, it isn’t necessary to emulate an entire machine, but rather it has a similar footprint to just running an app. While virtual machine reserve resources, containers only use what they need. Containers enable us to pass all dependencies and settings as one container. The advantage of containers still enables to avoid library conflicts (e.g. if there are different versions of an interpreter)

### Downsides 

Container do have a security downside, as the sharing of the host OS does increase the access code run through containers might have. There was, for example, a security issue specific to containers in 2018, affecting a large number of users/projects. As containers share the host, this can be a security issue if there are misconfigurations.


`Docker Daemon -> REST API -> Client (Docker CLI)`


(Quick definition - daemon - an app running a background without interacting with the user.)

Docker is a widely employed platform because of the ease of creating containers and deploy them

Most companies are moving to giving customers a container with an app rather than just the app, so that their applications are more generally applicable, and to reduce issues. Docker containers are supported on a wide variety of platforms.

### Quick notes on docker commands:

`ps` - shows all currently running containers. With -a flag, shows stopped and killed ones as well.

`kill [name]` - kills the named container (stops it)

Once stopped, a container will be deleted at some point. They are not permanently saved. However, you can recover the contents of a container of a closed container if it has not yet been deleted. The concept of the container was always to be disposable.

We can add a volume to containers, which would save data from a container even after the container was deleted if need be.

Going through how docker builds an image from a repository, step by step:

- Run command issued in shell
- Docker client receives command. Makes API call to Daemon
- Daemon implements the Docker Remote API
- Docker run starts a new container
- Docker Hub is default public registry
- Daemon will pull images it doesn’t have.

# Cloud Computing

Cloud Computing is the on-demand use of online computing services, such as data storage or program execution. Cloud Computing covers any on-demand delivery of computing resources, and is therefore a wide-ranging umbrella term.

The key advantage is that instead of being responsible for the maintenance of the hardware and needing to scale the process, it is possible to rent access to these services instead. This approach makes capacity highly scalable, which greatly saves on infrastructure costs. 

The pay-as-you-go model offered by many cloud providers also means that costs are more controllable during times of lower demand, as opposed to constant maintenance costs when running hardware.

Due to most cloud providers having backups, the reliability of a service is laso greatly increased.

### Disadvantages

There are, however, downsides to cloud services. As data is passed to a cloud provider, this could present a security issue. While security is likely to be a key concern for any cloud provider, the full extent of their security protocols is not known to the user.

Transparency is a big potential issue with using cloud computing, as the user may not know where your data is being stored (which can have an impact as different countries have different strengths of data protection laws), whether a breach has occurred, etc.

It can become problematic if data stored with one cloud provider is incompatible with another provider, leaving the user of cloud computing “locked in” to a particular provider. Similarly, if a provider stops providing the user with a particular service, it may be a problem if this is something a service is completely dependent on.

### Types of cloud deployment:

- On Premises/Internal, Off Premises/Third Party, Hybrid.

- On Premises/internal may be useful fo some services that require stricter security, such as banking or government data storage. Hybrids include a mixture of the two, where particularly sensitive data might be stored on an internal cloud, while some customer services may be suited for third party/external cloud services.

### Different Models of Cloud Services

Note that while the services are provided, the user still has to set up and configure them:


- On-Site - Everything managed by user, no cloud provider involved.

- Infrastructure as a service - Service provider manages Servers, Storage, Networking, and Virtualisation. Operating System, Runtime, Middleware, Data and applications are user responsibility. 

- Platform as a service - similar to previous, but OS, Middleware and Runtime also covered by Cloud Provider.

- Software as a Service - Everything covered by cloud Provider, only configuring and setup to be managed by the user.

 Cloud Computing is very different to virtualisation, and the two must not be confused. Virtualisation is the technology that led to cloud computing, as it enables a layer between hardware and software, but cloud computing is a service that employs this technology to provide scalable computing capacity.
