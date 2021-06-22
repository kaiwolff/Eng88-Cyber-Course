# Virtualisation - Further Notes

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
