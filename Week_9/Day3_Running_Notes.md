# Cryptanalysis

Used to break ciphers

Cryptanalysis may be used by criminals, but also used by governments and to analyse weaknesses in ciphers.

Several methods may be employed.

### Brute-Force
The simplest attempt at breaking a cipher is brute force methods, where every possible key is tried until one works. If every possible key is tried, one of them will work. However, the risk can be minimised by usign longer keys as the difficulty of breakign the key increased 

## Ciphertext Methods

Ciphertext methods mean tryign certain plaintexts and monitorign the output of the ciphertext

### Chosen-PLaintext Method

have a chosen plaintext and monitor the ciphertext

### Chosen-ciphertext method

Chose a ciphertext to be cedrypted

### Meet-in-the-middle method

Have a portion of the plaintext, and a portion of the ciphertext.


All algorithms are breakable given enough time and resources (as eventually, brute force will work). However, the timeframe required to brute-force a key can be tens of thousands of years.

## Access Control

#### Access Control Models

Even if not used in daily operation, it is important to know these access control models

#### DAC - Discretionary AC

The least restrictive model. Allows the users to control access to their data as owners of this data. Example of this is some operating systems, which let theuser be in control of access to their own data

#### Mandatory AC (MAC)

Apply strict access control. Usually used to control and protect important assets in military applications or critical company information. Assign security level to an asset, and allows users to access based on their security clearance.

####Role-based AC (RBAC)

Assign different role different privileges based on the role they take in the environment. In this case, individuals are assigned to a profile of their role, and granted appropriate access.

#### Attribute-based AC (ABAC)

Some set of attributes governs whether access is granted. For example, "the server can be accessed by User X between 9 and 5"

#### Rule-based Access Control (RBAC)

Specify set of rules regarding access to a system. This may include permitted or denied IP addresses, or access via a particular protocol

#### Time-based AC

Allow access based on time or date. E.g no access durign weekend

#### Principle of least privilege

The user should be granted the minimum amount of access required to complete their work.

related is Privilege escalation: giving a user more access through a program, rather than giving the user extra access. For example, a user might send some data to be analysed, but the analysis requries more access than the user has. This can be abused by hackers to gain extra access, for example through injecting SQL statements


## AAA framework

Authentication, Authorisation, Accounting

- User and administrators must prove who they are
- Authorisation services determine which resources the user can access and which operations they are allowed to perform
- Record what the user does, including what was accessed and for how long, and what changes were made.

In an example organisation:
Authentication may be applied via a token, a username and password, or similar. Authorisation is usually controlled by the server. Accounting might be a limit on how many pages someone can print, how much they can download or similar.

Another example might be a debit card; authentication is the PIN, withdrawal (accounting) is limited to a certain amount per day, authorisation is to the user account.


Typews of authentication:

Local AAA authetnication; sometimes known as self-contained. Authenticate against locally stored usernames and passwords.

Server-based AAA Authentication. Authenticate against a central AAA server containing user and password details for all users.

AAA Protocols

RADIUS (remote authentication dial in user service): Old protocol that supports centralised authentication, authorication and accounting management for clients that establish connection with a network and intend to use any of the provided services.

TACACS Terminal Access Controller Access Control System - also old protocol uised on unix netowrks to allow a remote server to forward logon requests to authentication servers for access control purposes

TACACS+ was later released by Cisco as a response to RADIUS.



## Authentication

The process of identifying users or identity when they require access to a resource. 

The verification of identity can come about in three ways:

- Something you know, e.g. a passphrase or PIN
- Something you have/carry, such as an ID card, or a flash drive
- Something you are, for example fingerprints, facial ID

Conventional protocols e.g. passwords alone, are too weak, as it has become too easy to crack a password. therefore, it is good practice to ahve 2-factor authentication.


### Passwords

The most common method of authentication. On their own, insufficient as users will peak weak ones, dictionaries ofhundreds of thousands of common passwords are available (a lot of which are still in use), and only about half of users use a different password for each of their accounts.

#### Good practice for passwords

- Combo of numbers, letters, and special characters
- The longer the better
- don't use the same password for several sites
- Avoid patterns that make passwords guessable (usage of personal details, site name,)

#### Common Weaknesses

- using a dictionary word
- Personal Information
- Using patters
- Common character substitutions
- numbers of specials only at the end

Ideally, usign a fully randmoised password is the best choice.


#### Attacks & Defence

Attack Types include:

- Brute Force: simply try all possibilities
- Rainbow Table attack: have list of hashes and original passwords, try to lookup matching hash.


Defence Types Include:

- Salting hashes: add a unique bit of data to make the hash unrecognisable
- Key stretching: Add the salt, the password and some intermediate hash values. Run all of them through a hash function multiple times to further obfucscate the hash.


## Token Authentication

Can be eithe rhardware or software. Considered to be a device we use to access a secure system. Examples include cards, dongles, RFID chips. In this section, we will consider hardware mainly

## Biometric Authentication

Covers the "something you are" aspect of the authentication framework. Huge advantage is that they can be easily compared to authorised features, Can control physical access when isntalled. Can be added ot multi-factor authentication process. Options include voice recognition, eye scanners, fingerprint scanners, 


## Certificate-based Authentication

Identify with signatures

analogousa to driver licence or passport.

Digital identity using keys

## Multi-factor Authentication

Requires 2 or more independent ways to identify a user. Classic is a phone number linked to a username and password. This way, you can prove the user is in possession of their phone.

mutliple layers, but weakness is that people lose sim cards which can limit availability. 


## Authentication protocols

- NTLM - Windows-based security protocol. prvides authentication confidentiality and integrity


- KERBEROS

- PAP Password Authentication Protocol. provides password-based authentication. usually used to carry user validation from point to point. considered vulnerable to cyber attaciks now, but formerly very popular.

- CHAP

- SSL/TLS - client and server certificates available. This means that connection can be verrified as secure both ways. Traffic si also encrypted so that plaintext is as secure as possible. If choice between ssl and tls, prefer tls as it is considered more secure.


