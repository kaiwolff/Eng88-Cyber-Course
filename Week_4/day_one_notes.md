# Introduction to Computer Components and Operating Systems

There are three basic types of computer components, that need to be considered from a security perspective:

- Hardware
- Software
- Humanware

For a long time, humanware was not considered sufficiently. This means considering how a user might actually be using a computer, which may be at odds with how it was designed to be used.

Hardware covers things such as the motherboard, CPU, etc. At this point, it is useful to point out that the motherboard has a "brain", BIOs (Basic Input/Output System), and more recently UEFI BIOS (Unified Extensible Firmware Interface) to interact with the hardware outside of the operating system
### Servers

Servers are computers which provide a service to other computers. This can be the data servers commonly associated with the term, but technically, if a user sets up their laptop to provide access to a printer for other users, that laptop is also running as a printing server.

A server will require different security protocols to a general purpose computer.


# Windows

Windows is the most popular personal computing operating system. It is an important security consideration as it is often a popular attack vector. As security was not a key concern in early iterations of windows, some vulnerabilities remain.

### The Windows Filesystem

Firstly, a filesystem describes how data is organised and managed for storage or retrieval on the hard disk. In windows, the original standards where FAT (File Allocation Table), followed by a number related to the maximum file size. Since then, the NTFS (New Technology File System) filesystem is commonly used in windows.



#### Environment Variables

#### Accessing Logs

This is done via EventViewer. Events are organised according to type

#### Managing Users and Groups


### PowerShell

This is a windows designed multiplatform shell, that can be used in a way not dissimilar to bash. 

##### PowerShell - Basic Commands

Get — To get something
Start — To run something
Out — To output something
Stop — To stop something that is running
Set — To define something
New — To create something


There are a lot of commands, data types, and comparative operators. generally, these are best explored with searching when needed. I may attach a few tables once I have formatted them.



##### Pipelines

These are used to send the output from one command to another command. this is shown using `|`. Extremely useful in scripting.

### Windows Security - A few basic tips

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

If data needs to be particularly secure, it may be necessary to encrypt data. Windows Business/Pro has bitlocker for this. It encrypts using either 128bit or 256bit encryption. There are also third party tools available for encryption.

## Windows Security - Best Practices

This will be summarised as a "securing windows checklist".


