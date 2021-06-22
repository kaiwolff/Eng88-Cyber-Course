# Virtualisation

Virtualisation provides a layer between the software and the hardware, enabling us to take a configuration or set of packages and run them regardless of the underlying hardware.

Before virtualisation, it would be necessary to acquire compatible hardware to run a particular software or application For temporary purposes, this coudl lead to the acquisition of specialised hardware, which would then sit idle once demand for the service returned to normal levels. To make a machine work with a new application, or to set up a new server, it would be necessary to purchase the hardware, install the correct operating system, and then install and run the software.

Through virtualisation, we are able to run software or applications on a much wider variety of hardware, meaning that the process of providing a service can become much more scalable. Through virtualisations, it is also possible to have a virtual server that is not tied to a particular piece fo hardware, which protects the system against the failure of a physical node.

A good example of this is Java, which runs through the Java Virtual Machine. This makes Java much more portable than some other languages, which require compiling separately for each machine.

### Type 1 and Type 2 Virtualisation

There are two types of virtualisation, Type 1 and Type 2. Type 1, also known as bare-metal virtualisation, has the virtualisation layer interacting directly with the hardware being used. Type 2 virtualisation interacts with an operating system instead. Type 1 is preferable, as the lack of an OS provides fewer potential security flaws. However, Type 2 virtualisation has the advantage of convenience, as it enables users to quickly employ software on their machine.

## ISO Files

These are also termed disk images, and represent a virtual disk. For example, they can be used to simulate a disk by mounting them in a virtual disk drive, or be burned onto a CD or USB stick. The files contained on the disk image can also be extracted using dedicated software.
