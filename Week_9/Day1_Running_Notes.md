CyberSecurity Essentials


Definitions:

NIST: Ability to protect or defend the use of cyberspace from cyber attacks

CNSS:>

Much longer

Prevention of danage to and the protection of and the restoration of computers, electronic communications services, wire communication, and electronic communication, including infomration contained therein, to ensure its availability, integrity, authetication, confidentiality, and non-repudiation.


CNSS entiosn the fiuve categories that should be achieved:

- Availability
- Integrity
- Authentication
- Confidentiality
- Non-Repudiation


## Cybersecurity Cube (aka McCumber Cube)

- A mdoel framework for establishing and evaluating information security programs
- piuctured as rubik's cube

###Desired goals 

(see previous five bullet points), Data states, Safeguards

Confidentiality means information is only accessible to authorised parties, and unatohorised parties do not have access to the data (whether intentionally or accidentally

Integrity - makign sure data has not been modified in a way that throws the reliability of the data into question

Availability - ensuring authorised individuals have reliable access to the data or resource.


### Data States

Storage - Data at Rest (DaR). Doesn't only mean that the data is stored on a hard disk. could also be in memory

Transmission - Transferring information betweeninformation systems(Data in transit DaT)

Processing - Performing operations on data to achieve a desired objective. even when processing, security must be assured.


### Safeguards

Policies and Practices

Human Factors - ensurign that hte users are aware of the practices. Everyone should be aware of their tasks and what practices or standards must be adhered to. Example is trainign users to avoid viruses in emails, social engineering tactics, etc.

Technology - Software and equipment


Many organisations make hte mistake of focusing too much on safeguards based on technology, but do not focus on the human factor. the idea of the cube is to cover all these topics and recognise that they are interlinked



1st Dimenions Desired goals (aka the CIA triad)

Confidentiality - Unauthorised access is prevented. This might be done via any technique sch as cryptography, access lists, etc.

Integrity - The data should not be moudified by any unauthorised entity.

Availability - Access should however, be available to authorised entities



## Alice, Bob and Trudy

Let's say alice wants to send a secret message to Bob. Trudy shoudl not be able to access the message. A secure system should be able to provide alice and bob with a secure system to exchange messages. The channel should be secure enough so that Trudy cannot access the messages. 
If Trudy manages to read the messages, we have lost confidentiality. If Trudy managed to intercept the message, modify it and send a modified message ot Bob, and Bob would be able to receive it without noticing the change, wqe have lost integrity. If Trudy is able to obstruct the message to Bob and it does not arrive, we have lost availability.

2nd Dimension - Data States

Quick note, the difference between data nad information. Data can be anything e.g the prhase England, London, Wales, Glasgow, Northern Ireland. These are pieces of data. Once they are classified (e.g. cities in the UK) then it has meaning and becomes information.

The 4th of July is data, but if you know what it means, it becomes information.

At Rest, In Transit, or Processing. See above for more in-depth explanation

3rd Dimension


Cybersecurity - Essential Terminology

Asset - what we are trying to protect. Things such as data, people, etc. Any tangible or intanglible items that can be assigned a value. Intangibles include things like a company's reputation.

Vulnerability - A weakness or gap in protection efforts. Common causes are mistakes made durign development process or human users not following practices. This is what an attacker would look for when attempting to compromise a system.
Not all bugs are vulnerabilities, but the ones that might be used by a hacker are known as CVE (common vulnerability and exposure) and will be covered in more depth later on.
Vulnerabilities are often alloted a score on a CVSS (common vulnerability scorign system), to make easier the assessment of how severe a vulnerability might be. PenTesting is part of assessing what bugs are present, and how serious the vulnerabilities are.


Exploit - How an attacker leverages a vulnerability to gain access.
 
Threat - What the outcome of a successful attack would be

Risk - basically assessment of how likely something is to happen, combined with how severe the impact might be. For example, a threat without vulnerabilities to carry out the threat would be considered a low risk.

### Causes of vulnerabilities

- Design and Development Errors
- System Configuration Problems
- Human Error
- Connectivity
- Complexity
- Passwords
- User Input
- Management
- Lack of Staff training
- Communication

## Cyber Attacks

Two primary types: targeted and untargeted. Untargeted sends out the attack to as many potential targets as possible.

Untargeted attacks are generally not concerned with a particular victim, but rather with easily obtaining a result (e.g. gaining bank account access) regardless of target

Targeted attacks are generally done with a specific objective in mind, such as attacking a particular company, or a particular piece of infrastrucutre (e.g. Stuxnet, which was targeted at a particular centrifuge). These attacks generally cover several stages, including for example what is going to happen once access is gained. Another example would be the Solar Winds attack, which, while it started as general fishing for vulnerabilities elsewhere, was then used to target a supply chain after the solar winds exploit was found.

## Threat Actors

Nation-States - generally geopolitical motivations

Cybercriminals - Profit

Hacktivists - ideological motivation

Terrorist groups - Ideological violence

Thrill-Seekers - Fun/Satisfaction

Insider Threats - Discontent/Profit

Not all threats or risks have motivations, for example a natural disaster can be a threat, as can an accidental action by a user.

## Cyber Threats

Malware: software that performs malicious tasks on a device or network

Spyware : a form of malware providing real-time information

Phishing attacks: An attacker attempting to lure individuals into giving out sensitive data

DDos (distributed Denial of Sevice) Attacks: Aiming to disrupt a computer network by flooding the network with requests, with the aim of overloading the system and preventing legitimate access to a network.

Ransomware: a type of malware that denies access to a computer system or data until a ransom is paid to the attacker.

Zero-day exploits: a flaw in software, hardware or firmware that is unknown to the party or parties responsible for patching the flaw. Known as zero-day because it was available from day zero.

Trojan: A backdoor in a system. Allows the hacker to gain control of a system or access confidential information.

Wiper attacks: a form of malware with the intention of wiping out the hard drive. Often ransoms are demanded by attackers as it is easier to wipe than to encrypt

IP theft: stealing intellectual property or using it without permission.

Theft of money: self-explanatory

Data manipulation: An attack with te aim of changing data rather than stealing it.

Data destruction: attacker attempts to destroy data

Advanced persistent Threats:An unauthorised user gains access to a system or netowrk and remains there undetected and for an extended period of time

Man-in-the-Middle (MITM) attack: relays and possibly alters or listens to communication between two parties who believe they are communicating with each other.

Driveby Downloads - downloading without user's knowledge

Rogue Software: Malware disguised as real software. For example an phone app collecting more ifnormation than is necessary.

Unpatched Software: Software with a known security weakness that has been fixed in a later update but not yet updated.

Data Center disruptions due to natural disaster

Water holing: setting up a fake website or compromising a legitimate one in order to exploit visitors

Spear-phishing: targeted finishing, aiming at particular individuals that could for example lure them to click on a malicious link

Deployment of a botnet: common emans for delivering a DDoS attacks. A network of devices that is used to for examepl send repeated requests

Subverting the supply chain: attack equipment or software beign delivered to an organisation.

## Cyber Threat Surface

The threat surface refers to all available endpoints that a threat actor might attempt to exploit within the cyber threat environment.

The (many) processes that produce, deliver, rely on info systems connected to the Internet are also potential threat vectors or targets

Services, devices and data can be targeted
Systems that connect physical entities with the internet

## Cyber Kill Chain

The chain of events leading to a successful cyberattack. Hackers usually go through these stages.

1. Reconnaisance -Harvesting email addresses, conference information, password lists, information on target system. basis for planning.

2. Weaponisation - Couple an exploit with a backdoor to get a deliverable payload.

3 delivery - get the weaponised bundle to the victim e.g. via email or USB.

4. Exploitation - making use of a bundle to perform action on the victim's system

5. Installation - installign malware on the asset

6. Command/control - Command channel for remote manipulation of target asset
   
7. Action on Objectives - with access established, perform actions to accomplish original goals.

Optional 8th stage Retreat - destroying your exploit to cover tracks, for example if an exploit must not be noticed or when trying to avoid prosecution.







