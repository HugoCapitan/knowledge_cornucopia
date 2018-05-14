## Process
There is Object Oriented:
- Analysis
- Design
- Programming

This course focuses on the two first.

The objective of this metodology is not to gather a perfect design before starting building like in a waterfall approach but instead get a good enough design to start iterating in a more *Agile* way. 

## What is an object?
Anything that has: identity, attributes (these describes the current stat of the object) and behavior 

## Aanalysis and design
This will be continuely revisited and polished in the development.

- Gather requirements
  What the app HAS TO DO, not what it could do.
- Describe the app
  In conversational language, what the app will do? This may change, this shouldn't be perfect
- Identify the main objects
  Use the descriptions and pick the most important ideas and concepts
- Describe interactions
  Formally describe this interactions, what does my objects have to do?
- Create a class diagram
  Yeah... that.

## Gather Requirements
What the app MUST do, what is required, not what it would be nice or cool. This will change, don't think you need to answer all the questions or think of all the possibiltities.

- Functional  
  Featurs / Capability  
  Often writen like "The app must do..." 
  
- Non-Functional  
  This are not features but something that is required, like the laws we need to comply with or uptimes, loading times, etc...
  - Help
  - Legal
  - Performance
  - Support
  - Security

 
> **FURPS**  
Functional  
Usability  
Reliability  
Performance  
Supportability  

## Describe app
Switch from feature focus requirement to user focus.
What does the user needs to be able to do with this app?

### 1. Use Case
- Tile: What is the goal? A short phrase with an active verb.
- Actor: Who desires the goal? It doesn't has to be a human being, its any external entity, even another computer system or so.
- Scenario: How its accomplished? Scenario as a paragraph or steps.

Goals of an actor might not succeed.  
User focused, for example login is not an objective of a login, instead the want to login to accomplish a goal, like purchasing an item, so login is just a step on the use case.  
Extensions of an use case are the possible things that can happen if something goes different than expected.  
Write use cases in active voice, "Who does what", avoid to much detail. focus on intention. no technicalities.  
Who performs system administration?
Who manages users and security?
What if the system fails?
Is anyone looking at performance metrics or logs?  
Diagrams are not replacements for written use cases

### 2. User story
Written in one or two sentences  
As a (type of user)  
I want (goal)  
So that (reason)  

Not a use case, a placeholder of a conversation that needs to happen, in comparison a user case is the record of a conversation

## Create a conceptual model of the app
Identifying the most important things in the application, what we need to be aware of.

1. Collect use cases and stories and start picking up nouns, just making a list. Check the list for duplicates, feel free to combine them or split them as you need to.

2. Diagram as in the note at lynda

3. Identify responsibilities, this time list the actions in the use cases and user stories, then go through each one and identify who's responsibiblity is and add that to de diagram.

## CRC cards
Physical index cards.

Classname, Responsibilities, Collaborators (Other classes it interacts with)

## Class diagrams
Classes are name on singular, not plural.  
For static vars or methods, represent underlined.  
Inheritance is shown with an open arrow pointing to the parent class.
Agregation: empty diamond, diamond part in the parent or container
Composition: filled diamond

## Behavior diagrams

## Some OOP concepts
- Constructors, initialize the object
- Destructors, logic before destroying the oject
- Static methods or variables are shared accross all the objects of that class, to access a static variable of method use classname.varname instead of instancename
- an Abstract class is a class that wont be instantiated.
- an Interface is a list of method signatures, is like a contract, you have to provide those methods in the class. you can ask in any part of your code if the object implements the interface to know if you can use those methods
- Agregation: One object is made from other , relationship "has a"
- Composition, is a form of agregation but implies ownership, this is the child depends on the parent, if the parent doesnt exist, neither the child

## OOD principles
### General Dev Principles
- Don't Repeat Yourself - DRY. not only in code, but diagrams, database, etc... 
- You Ain't Gonna Need It - YAGNI. Don't write speculative code, sole the problems that exists, today's problems.
- Pointless comments.
- Big methods.
- God objects. Objects that handles a lot of functionality

### SOLID (OOD principles)
- Single responsibility: An object should have only one reason to exist, encapsulated within one class.
- Open / Closed: Open for extension, closed to modification. If necessary to change behavior, add code, dont modify code that already works
- Liskov Substitution WHAAT??? Child classes should be able to be substitutable with parent class, this is it should be possible to use them as their parent class at any moment
- Interface segregation. Interfaces should be as small as possible so classes can have the possibility to use multiple and not forced to support a lot of methods.
- Dependency inversion. Depend on abstractions, not concretions. ABSTRACT, men tell me about this one...
be careful with the YAGNI principle.

### GRASP (General Responsibility Assignment Software Patterns)
Who creates this object, who is in charge of how this objects talk to each other, etc...
- Creator  
**Who is responsible for creating an object?**
Does one object contains another?
Does one object knows enough to make another object?

- Controller  
Intermediary between objects.

- Pure Factory  
When something doesn't belong anywhere else, use a factory, baby. HAHA this doesn't happen in js

- Information Expert  
A class should be responsible for itself, assign new responsibilities who has the most information needed to fulfill it.

- High Cohesion  
How focused the internal behavior of a class is, are their behaviors focused on the single responsibility of the class their in?

- Indirection  
Decrease coupling between objects by using an intermediary

- Low Coupling  
Reduce the ammount of required connections between objects.

- Polymorphism  
Yeah, that.

- Protected Variations  
Identify the most likely points of change to protect that, using encapsulation, interfaces, etc...
