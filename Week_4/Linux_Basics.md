#Linux Basics

LInux is an operating system first

It comes in a wide variety of distributions (aka distros), which range in featureset and specialisation from graphical, user-friendly to deliberately lightweight and barebones. Some distributions are specialised for particular purposes, such as Kali Linux. Linux is particularly popular in server applications, with the vast majority of servers running on Linux.

A few key distributions and their derivatives  are:

- Debian:
    - Non-Commercial
    - Many popular derivatives, including Ubuntu and Kali
  
- Fedora
    - RedHat, a commercial distributionwith support, a popular distro stemming from this one
    
- Arch Linux
    - Generally for more advanced users
    - While less user-friendly, has powerful features

## Linux Architecture

Linux distributions follow a key architecture:

- The applications interact with the shell
- The Shell interacts with the kernel
- The Kernel interacts with the hardware

This differs from the approach taken in  the Windows OS. The kernel interacts with and "covers" the hardware, and enables the commands coming from the shell to be executed. Several different shells exist, such as bash and zsh. Regardless of whether applications have a graphical or command-line interface, the application will always interact with the shell.

Linux treats everything as a file, which has the advantage of standardising interactions. While in Windows, a new drive would be assigned a letter (eg C:, E: F: etc), in Linux everything starts from one root directory. Similarly, interacting with external devices becomes more standardised. For example, a device with a sensor would have the output read by Linux as if it was being read from a file.

#### Some key differences to Windows

- Logs and user information are much easier to access, being stored in the filesystem.