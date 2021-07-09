Keep Project without SQL

Another branch for WITH SQL

Branch out to sql_integrate branch on Kali



SQL SELECT:

SELECT Count - total number of records returned.

E.g. SELECT Count FROM `user_table` WHERE `first_name` = ‘Adam’;

Does not return the record but rather some statistics on the record.

Example using SELEC Min command:

```SELECT Min(`user_id`) FROM `user_table`;```

The above returns the lowest values of a given field. SELECT MAX would work the same way, but return the highest value instead.

SELECT Avg - gives average value (might use on something like hours worked, salary, similar).

The outcomes of these look just like a table, where the only field is the requested value

Can also get several values into a table, for example

SELECT Max(`user_id`) as MAX_UID, Min(`user_id`) as MIN_UID FROM `user_table`;

Instead of using fetchall(), which fetches every record that complies with a test, you can return a count instead, which saves a lot of time, and gives back the result as a value.e

IMAGE: examples of code input to update a table and then order by column value




Processing Sequence:




When searching, always try to find a st6andard for what is being searched for re: capital or lowercase letter.


## Intro to DevOps

### What is DevOps good for?

Before DevOps, Development and Testing/QA were separate entities. This proved to have some problems as the isolated nature meant each of Dev, Testing, and Operations didn't get the "full picture" of what they were working on, Devops aims to address this problem by integrating the processes so that Development and Operations are combined (hence the name DevOps).

The Application Design Patterns have changed from "monolithic" approaches to a split between backend/devops and frontent, or a microservice based approach, where severals product services are aggregated and presented to the user via a frontend. This limits the effect of bugs (as the microservices exist in separate areas), and limit downtime. it also stops the "all-or-nothign" approach to a project, as each service can be added separately without affecting the other services' functionality.

### Microservices

Microservices are an organisational structure, where each microservice is designed to handle a specific process. They can interact with each other if needed.



While Agile methodology is well suited to being integrated into DevOps, the two are separate. it is also possible to work with DevOps principles and use, for example, the waterfall development method.

### Challenges for a DevOps Engineer

- Ease of use
- Flexibility
- Robustness
- Cost

Ease of use is vitla as other teams will be reusing software to work on later. When building somethign, it is important that it is easy to use by either a customer or by other developments. By putting effort into making parts easy to use, time is saved as code can more easily be reused.

Flexibility is similarly important as it aims to make the repurposing of parts of a developers code easier. As practices in the sector constantly evolve and new technologies are developed, it is important to attempt to make it possible to migrate to new technologies as they emerge, avoiding being "locked in" to a particular software, for example.

Robustness - it is important to eliminate single points of failure, so that osoftware is not broken by an error in an unrelated part of the program if possible. This is, for exampel, acheived by ringfencing microservices so that they can operate independently of each other if necessary

Cost -0 This is an often-overlooked aspect of development. For example, using machines that don't use more capacity than necessary. Making sure that the resources used are as close as possible to the resources required by the services.


### Relationship between Agile and DevOps

DevOps is broadly based on Agile principles. By breakign things down into smaller parts and deploying/delivering more frequently, risks are reduced and the process lends itself to, for example, repeated sprints as employed by the Scrum method, as a sprint might cover aspects relating to a particular microservice.

### DevOps

Hard to define specifically, as there is much discussion on how to define the concept. However, can agree on some practical definitions:

- A collaboration of Development and operations
- A culture promoting collaboration between Development and Operations tea to deploy code to production faster in automated and repeatable ways.
- A practice of development and operation engineers taking part in the whole service lifecycle together
- An approach that allows quicker and more reliable development of superior quality software

Academic deifnition

"A set of practices intended to reduce the time between committing a change to a system and the change being placed into normal production, while ensuring high quality."


 ## CAMS model
Core concept of devops:
- culture
    - Devops starts with learning how to work differently. Embracing cross-functional teams that interact with transparency, respect and openness, so that each team knows what hte other one is working on. This is similar to the Agile approaches previously discussed
- Automation
    - A very important part of DevOps, as having systems in place to replicate errors. In a nutshell, if there are more than three commands that are run on a very regular basis, it's better to have a bash script to do them for you. Reduces room for human error, as a working configuration, if put into automation, will mean the correct approach is being reliably taken at that point. Having polcieis and standards that can be automated using scripts and software is a useful part of this, for example automated testing with Jenkins
- Measurement
  - By monitoring and trackign performance throughout the cycle, the need to rework is limited. The goal is to expect errors, and ensure they are not repeated if possible. This lowers the cost of production significantly by lowering the number of reworks needed
- Sharing
    - Usually, people hide their problems because they think they will be punished or blamed for them. By sharing problems and mistakes, it is however possible for everyone to learn more quickly. The key is to have a blame-free environment as mistakes occur naturally and are more easily solved if they are quickly brought to everyone's attention
    

Key Aim of DevOps is to get the working product into the hands of customers as quickly as possible. This may take the shape of having, for example, monthly updates to software, which gives the customer a working product earlier and then adds features on. This leans on the above CAMS model.

### DevOps Principles

- Customer-Centric Action
    - customer should be taken into consideration in all steps. Need to focus on producing a product that can be sold to/used to by customers with a high degree of customer satisfaction. Steps taken should be done with teh aim of contributing to increased customer satisfaction.
    
- End-to-End Responsibility
    - Need to provide updates or product support until the software reaches end-of-life. Notice that end-of-life does not ncessarily mean end-of-use, and it may occasionally be necessary to release patches if a huge vulenrability is discovered after a product has ceased receiving official support. Important to this is gfood documentation so that past steps can be retraced if needed
    
- Continuous Improvement
    - Focus on continually doing things in a better way.
-Automate Everything
      - Automation is vital for the DevOps process. Not only for the software development side, but for the entire landscape. Ideally automate everything, from testing, to creating or destroying infrastructure, configuring firewalls, etc.The more can be automated, the more time developers can spend on adding value to the product rather than repeating themselves taking testing steps.
- Work as one team
    - In DevOps culture roles, there should be no isolated positions. While specialisation can be helpful, full collaboration should be the norm, and specialists shoudl be available of what the rest of the team are doign and vice versa
- Monitor and Test Everything
    - In order to improve, need to constantly monitor performance and requirements from the customer side.
    
### DevOps Lifecycle

- Continuous Development
- Continuous Testing
- Continuous Integration
- Continuous deployment
- Continuous Monitoring

Notice that all parts are continuous throughout the.

Testing - Once the initial code has been created, it will be continuously tested for bugs, either while unchanged and certainyl more rigorously before any new features are accepted. Can use automation for this e.g. Selenium.

Integration - Heart of processes. Requires developers to commit changes to the source code more frequently. Each commit is then built, unit-tested, integration-tested and packaged.

Deployment - Stage where tested and integrated new code is sent intot he production environment. It is important here to ensure that the code is correctly deployed to all servers in such a manner that any change made should not compromise the functionality of the application.

Monitoring - Once deployed, performance, customer feedback and use cases need to be gathered and reviewed so that the information cna beused to target improvements to future releases. The more information is gathered, the better. For example, by monitoring if performance degrades after a new release, it is possible to address this problem before app functionality is compromised.


## Tools

A lot available, mostly concerned with aiding the automation of stagesa of this cycle. For example, Jenkins helps to automate testing of committed code. Ties into setting up an evnironment, using several toolsets to create the architecture of the project



### Risk Register

List possible risk areas, including an estimate of how likely the even it to happen, and the severity of the impact of an event occuring.

In conclusion:
DevOps impacts the culture, affecting the entire development process. It has become the favoured approach for almost all IT departments, with demand far outstripping supply, especially in the DevSecOps area. This is especially true with the Covid-19 pandemic, which caused more needs for secure remote access to company infrastructures as employees had to work from home due to the quarantine.

CI/CD

Continuous Integration - Coding philosophy/ set of practices. Drive to implement small changes and check in code to version control more often. Aim is ot establish consistent, automated way of building, packaging and testing applications. With consistency in integration process, teams are likely to commit more frequently, leading to better colaboration and software quality

Continuous Deployment - automate the delivery of applications to production environment, or other selected ifnrastructure. 



The principles of CI/CD are part of the DevOps Lifecycle. 

Cannot always have continuous delivery. In some sectors, lengthy testing is required before deployment is permitted.

WHY CI/CD

 - Reduce cost
- Faster Release Rate
- Smaller Code Changes
- Fault Isolation
- Reliable testing
- Increased transparency & accountability
- Easy maintenance and updates


RESTful APIs

REST stands for REpresentational State Transfer.

Architectural style for applications

Ideally, a RESTful service is easy to implement, maintainable, extensible, and scalable.

RESTFUL service should have the following properties:
- Representaiton and data flow
- Messages
- URIs/Naming resources
- Statelessness


### Representation and Data Flow

First step in defining data sources. Taking an example of somethign like customer data, we might represent this as a JSON, or as an XML to contain the data to be used by a RESTful service.

### Messages

HTTP is protocol of internet communication. Works on simple methodology of request/response system. Whenever a request is sent, a response needs to be received back.

The Response Code section represents a status, e.g. the infamous 404 response code means that a resource cannot be found.


#### Requests

The "verb" part of the http request contains one of the following options:
- GET: Read a resource
- POST: Create a resource
- PUT: Update and replace a resource
- PATCH: Update and modify a resource
- DELETE: Delete a resource

URI's & Naming Resources

Key part of R (the representational part) of REST.

By entering a URL, eg `http://service.com/customer/id=1` would yield the customer details as a JSON, e.g:

```
{
"ID":"1",
"firstname:"Joe",
"surname":"Bloggs",
}
```
This will be covered in more detail later on via a practical exercise.



### Statelessness

Statelessness emans that a RESTful service does not maintain or hold the status of previously made requests. E.g. if sendign a request for customer 1 and then customer 2, the calls should be totally separate and the second call would be processed without regard for how the first request was handled.

"Stateful" services might have the ability to call customer 2 by calling customer 1 and then calling "next customer". In a stateless service this is not possible as there is no previous customer call saved. 

In a stateful design, it is necessary to connect to the same server every time. If the server was to go down for some reason, everything would need to be started from the beginning. Statelessness in RESTful APIs means several different servers can be used in the same session, as the need to maintain a record of state is removed.

The advantage of statelessness is that the server does not have to keep any session alive once a request has been received, simply to respond to each request. In a system where a load balancer might process requests, this means that the load balancer can more easily distribute the requests to connected servers, as each request needs only the one response and no session. it is also important as a secodn request might go to a different server, which in a stateful system would lead to problems with replying to requests depending on the state of a previous request.

Stateful systems are used only when it is acceptable or advantageous to have a session open on the service. the common problem associated with this is the aforementioned tendency to reset a session if the point of cotnact changes or a load alancer direts traffic to a different server.

 Authentication can still be handled in stateless systems. Once authenticated, the user receives a "token" that is sent with future requests, meaning that the request is authenticated without the need for a new session. 
 
n analogy would be having a keyfob or ID card instead of having to request access to a building each time the security guard changes.