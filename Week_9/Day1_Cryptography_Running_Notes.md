# Cryptography

Stems from Cryptology - the science of making and breaking secret codes.

Cryptanalyis - the breaking of codes. finding exploits or weaknesses in cryptography techniques.

Cryptography - development and use of codes used for communicating privately.


The module will focus on cryptography and briefly cover a little cryptanalysis

Cryptography has tow main areas: encryption and decryption.

Encryption: transform the original information into an unrecognizable form.

Decryption: convert encoded/encrypted data in a form that is readable and understood by the recipient

Ciphers

Algorithms that encrypt or decrypt messages.

2 main types

Substitution cipher:

Most famous is Caesar cypher. Take text, add key of how many places letters are shifted by, use to encrypt or decrypt a message. Complexity7 fo this is limited - measured by the fact that hte maximum number of runs needed would be 26 (1 run for each letter in the alphabet)

Transposition cypher. 

Don't replace letter, rearrange letters. Exampel might be rail fence cypher. See itexamanswers.net for an example of this, but separate letters by a key and then shift lines about.

### Encryption Classes

Two main classes of encryption used to provide data confidentiality

Symmetric encryption algorithms: use the same key to encrypt and decrypt data.

Asymmetric encryption algorithms. Use different keys to encrypt and decrypt data

Generally asymmetric are more complex and need mroe resources to be done. therefore they are usually slower. However, the use of separate keys can lead to better information security

Symmetric Encryption Ciphers:
Subclasses
Block ciphers: We take a fixed length block of plain text and encrypt these blocks (hence, block cipher). if the remaining part of a message is too small for a full block, padding is added.


Stream ciphers don't wait for a full block, isntead encrypting one bit at a time.

Block ciphers are best used for messages, while stream ciphers might be better for continuous messages.


For symmetric encryption, generally use AES (advanced encryption standard), which ahs been the official standard since 2001. AES is based on another algorithm called the Rijndael cipher.


### Asymmetrical Encryption

Two keys, public and private. Public key available to everyone, used for encryption. Private key used for decryption. This way, only people with access to the private key are able to decrypt data. can go up to 4096 bits for longest keys.

\Algorithms include Diffie-Hellman, Digital Signature Standard and DS-Algorithm.

RSA encryption algorithm
ElGamal
Elliptical curve techniques. 


To communicate, each entity needs a public and private key. using alice and bob as an example, tney would have each other's public keys and each have hteir own private key to decrypt the messages.

However, to authenticate the SOURCE of a public message, we would encrypt with the private key. Note that this message can be read by anyone with the public key.


### Diffie-Hellman

An asymmetric mathematical algorithm

Allows two comptuers to generate an identical shared secret without havign communicated before.
The new shared key is never actually exchanged between the sender and receiver

Commonly used in:

IPsec VPN
SSL or TLS
SSH data exchange


### Encryption Classes

Comapriing symmetric and asymmetric:

Symmetric uses same key to encrypt and decrypt
Asymmetrical has 512 to 4096 bit keys, symmetrical only 40 to 256
Synnetrucak us generally faster
Thus asymmetric is generally used for quick data transactions such as accessing bank data, while symmetrical is used for encrypting bulk data.

## Cryptographics Hash operation

