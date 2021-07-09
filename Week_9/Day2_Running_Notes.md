# Hash Functions

Hash functions are "one-way" mathematical functions used to ensure data integrity. These are generally computationally ch4eap to compute, but hard to reverse. An analogy might be breaking a glass or grinding coffee, which is easy to do but hard to reverse.
A hashign function should output a value with an identical length each time, regardless of the input data's length

A hash function should output the same thing given the same input each time.

Collision-free hash functions is where we can be certain that two different inputs will produce different outputs.

To ensure that data has not been changed, the sending device inputs the message to a hashing algorithm and then sends the hash value attached to the message. The receiving device will take the message and will hash it again, then compare to attached hash value. If the hash values match, the message can be considered authenticated. This protects against accidental changes to the data, however encryption is needed to protect against a malicious party intercepting the message, rehashing it and sending the new message nad hash combination to the receiver.

Well known hash functions

MD5 - 128 bit hashed message. Out of use as moved to SHA-2

Secure Hash Algorithm (SHA-1)- developed by NIST in 94, similar to MD5

SHA-2 = Next generation of hashing algorithms, should be used wherever possible.


Ensuring authetnication

Hash Message Authentication

In orde rto add authetntication to a hashed message, an additional secret key is used as input to the hash function. This protects against man-in-the-middle attacks, as the attacker would nto have access to the key, only the hashed information.


## Password Salting

As we use hashing to store passwords in a database, if two people have the same password, the hashed value would be the same. This would also make attempting to obtain passwords against hashed values easier. Thus we add "salt" to a password, a unique value for each user that is added before the hashing operation to make the output of hte hashing function different. The salt might be unique to the user, or unique to the system storing the data, but either way this makes it hard for an attacker to compare their hash of a password to the hash of the target value

The salt should be kept secret, not brute-forceable, and 


## Public Key Infrastructure

Using digital signatures

Simple concept - verify authetnticity by havign a unique identifier that only one person can generate "sign the document"

Properties needed:

Authentic - cannot be forged and provides proof that hte signer, and no one else, signed the document.

Unalterable - after signature, the signature cannot be altered

Non-reusable - the signature cannot be transferrred to another document

Non-repudiated - considered the same as a physical document.

Three standards

DSA Digital Signature Algorithm - the original standard for generating public and private key pairs, and for generating and verifying digital signatures

Rivest-Shamir Adelman Algorithm (RSA) - assymmetric algorithm commonly used for generating and verifying digital signatures

Elliptic Curve Digital Signature Algorithm (ECDSA) - newer variant of DSA with added benefit of computational efficiency, small signature sizes and minimal bandwidth requirements.


## Code signing


Digital signatures are commonly used to provide assurance of the authetnticity and integrity of software code.

The signature assures that:

- the code is authentic and amde by the publisher
- the code has nto been modified since it left the publisher
- The publisher undeniably produced the code.


A digital certificate is equivalent to an electronic passport. It enables users, hosts and organisations to securely exchange information over the Internet.

Public Key management

An asymmetric conneciton: hosts exchange public key information so they cna send encrypted data or verify authenticity of messages. the problem is figurign out how the public key received is the public key of a particular user (as a MITM attack might attempt to send different keys to the covnersational partners, and decrypt and read messages in the middle).

The problem therefore is the secure exchange of public keys. for this,w e need a third, trusted source to give us this information. Analogous to getting a driving licence after approving ID, then using the dirving licence elsewhere to prove ID. This is basically what a digital certificate does via a trusted third party.

This trusted third party is termed the certificate authority, who also keep a database of certificates. Wehen two people are now communicating, they exchange certificates, which are then looked at and decrypted by the Certificate authority.

There are several ceretificate authority, as well as registration authorities that manage the requests for certificates.


X.509 and Application

Defines the format of a digital certificate.

used in:

SSL/TLS secure web servers

Web browsers use it to implement client certificates

S/MIME - user mail agents that support mail.


Certificate Manager as part of web browser lists acceptable Certificate Authorities, which lists some of the authorities that issue certificates. the certificates can eb verified as the public key for the certificate is issued and the can be verified via the CA.

CA Procedure

1. Certificate Retrieval; All systems that use the PKI must have the CA public key (called self-signed as the root CA signed it's own certificate) Onyl a root CA can issue a self-signed certificate.

2. Ceritficate Enrolment - requesting permission to be part of the PKI. The certificate is issued for the network. The PKI contacts the CA to obtain a digital certificate for itself and to get the CA certificate for the user.

Using Alice and bob as examples; They request a CA certificate containing the CA public key.
 When they receive the certificate, they woudl request the system to verify the validity of the certificate usign the public key that they already have.


With bob and alice havign certificates, they now exchange them. The CA has ceased to be 9involved directly. Each party decrypt the certificate using the CA public key.

They take the certificate, they hash teh certificate, they receive and decrypt the certificates. If values match their certificate, it means the certificate came from the CA (as encrypted with their private key).

Certificate Revocation:

may occasionally occur, for example if a key is compromised or the certificate is no longer needed, like if the server using the certificate is no longer active.

2 main methods

CRL (certificate revocation list)

Online Certificate Status Protocol

