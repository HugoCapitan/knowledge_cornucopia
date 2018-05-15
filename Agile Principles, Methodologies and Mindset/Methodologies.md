# Agile Methodologies

## Scrum

> *Sprint:* A fixed length development period with a specific goal. Usually one or two weeks long.  
> *Product backlog:* Any set of work items that need to be completed to finish the release.

Scrum is a framework which consists of **3 main roles, 5 events and 3 artifacts**. Utilizes an iterative, incremental approach in which each sprint builds on the ones before.

Scrum is a framework and not a methodology, in the sense that it does not prescribes how to implement certain things such as reporting, source control, implementation of code, etc...

#### Roles

| Product Owner | Scrum master | Scrum team |
| ------------- | ------------ | ---------- |  
| Responsible for mantaining the product backlog and prioritizing tasks. They should know the product and capacity of the team. In charge of communicating changes. | Ensures the right processes happen at the right time, they is like a master of ceremonies. Often called *"The remover of impediments"*. | Anyone working to deliver the end product. &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |

---

Scrum has 4 events that provide opportunities to inspect and adapt.

- Sprint planning

    Initial meeting, the product owner provides feedback based on previous sprint and the goals for the current sprint get defined.

- Daily scrum

    Quick meeting (15min), team answers the following questions and their whys when necessary.

    - What I did yesterday?
    - What will I do today?
    - Do I have any obstacles?

- Sprint review
    
    Meeting with stakeholders to review results of sprint.

- Sprint retrospective
    
    Team meeting to inspect the last sprint to know what went ok and what didn't and decide on what to do about it.



## XP

XP or Xtreme Programing was one of the first agile methodologies, Is a software centric methodology based on quick iterations that result in production-ready code. XP's objective is to improve team interactions.

XP's core values are

| Communication | Simplicity | Feedback | Courage |
| ------------- | ---------- | -------- | ------- |

XP is also centered around a number of engineering practices:

- ***Planning game:*** a method to bring together stake holders, costumers and the developer team to plan  releases and the delivery of software. 
- ***Whole team:*** Everyone involved in decition making.
- ***Coding standards.***
- ***Collective code ownerships:*** No one owns any piece of code, then everyone is responsible for all the code.
- ***Sustainable pace.***
- ***Pair programming.***
- ***Simple design:*** Every line of code is a potential line of errors. Keep design as simple as possible.
- ***Test-driven development.***
- ***Continuous integration:*** Everybody working with the latest version of code and merging multiple times a day.
- ***Code refactoring.***
- ***Small releases.***
- ***System metaphor:*** Think about the way the system works at a high level. What important things should the team keep in mind while working on the system.



## Lean

Lean is a set of principles derived from the Lean production processes of companies like Toyota. This principles doesn't prescribe specific development methods but instead, they provide guidelines for streamlining the development process. Focusing on empirical process and learning in a complex environment.

#### 7 Key principles

1. ***Eliminate Waste:*** What parts of the process are wastefull and don't contribute to the end value for the costumer.
2. ***Build quality in.***
3. ***Create knowledge:*** Work together, all parts of the system should understand what the others are doing, collaborate to create knowledge amongst the different team members and parts of the organization.
4. ***Defer commitment:*** Don't make important design desitions until you have the necessary information.
5. ***Deliver fast.***
6. ***Respect people:*** Respect individuality and creativity independence.
7. ***Optimize the whole.***



## Kanban

Kanban evolved from Lean principles. It's a method that helps 

- Visualze workflof
- Limit work in process
- Focus on flow
- Continuous improvement

kanban uses a presentation board divided into columns to visually manage the flow of work items through a process

| To Do | In Process | Done |
| ----- | ---------- | ---- |



## Scrum-ban

- Short work iterations.
- Items added to the board based on highes priority.
- Bucket size planning: understanding working capacity of a team and don't overload the bucket of work.
- Feature freeze: Which features wouldn't be completed for the end of the sprint.
- Triage them.



## Crystal Methodologies

Agile methodologies named after the colors of crystals of different hardness. These methodologies are people centric, adaptable and fit for your necessities.

As the project gets bigger this methodologies need more roles, artifacts and processes to suit your project and team size.

Clear -> Yellow -> Orange -> Orange Web -> Red -> Maroon



## Feature Driven Development

Client centric, Architecture centric. Clients are the project's stakeholders. All aspects of the software are planned, managed and tracked at the level of individual features.

> Members of the development team are assigned to be owners of each class and feature set.

#### FDD Actions

1. Develop an overall model
2. Build a features list
3. Plan by feature - Select class and feature owners.
4. Design by feature
5. Build by feature

System reqs are organized at three levels:

1. Features
2. Feature sets
3. Subject areas



## Dynamic System Development Method

> Business focused

It's philosophy is that any project must be aligned to clearly defined strategic goals and the project must focus in the early delivery of real value to the business.

It requires a large number of roles and artifacts however it has flexibility in the way activities are incorporated.

- System requirements must be prioritized.
- Low priority items can be eliminated to keep within budget.
- Prioritization is made using MoSCoW.h

#### Principles
- Active user involvement.
- Empowering teams to make decisions.
- Frequent delivery of products.
- Fitness for business purpouse as the main acceptance criterion.
- Iterative and incremental development.
- All changes during development should be reversible
- Testing throughout all project.
- Stakeholders collaboration is essentials.h

#### 3 project phases

1. Pre-project activities
2. Project lifecycle
    - Functional model iteration
    - Design and build iteration
    - Implementation
3. Post-project activities



## Agile Modeling

> Chaordic!

Agile modeling is an approach to developing software where extensive models are required before any development is done.

The team develops a high level model of the project scope and then iterates over developments of more low leve models.

- #### Iteration 0

    - Initial requirements envisioning
    - Initial architecture envisioning

- #### Iterations 1 - n

    - Iteration modeling
    - Model storming
    - Test driven development



## Disciplined Agile Delivery

This framework extends on other framework such as Scrum. A people-first, learning-oriented, hybrid agile model.

DAD takes proven strategies from other frameworks and methodologies, it's flexible in the way that it only provides guidelines and advice about technical practices and other strategies.

Keeps teams focused on a goal.

#### Primary Roles

These must exist on every DAD project.

- Team Lead
- Team member
- Product owner
- Architecture owner
- Stakeholder

##### Secondary roles

- Independent tester
- Specialist
- Domain expert
- Integrator
- Technical expert

#### 4 vesions of delivery lifecycle

- Basic version, extends Scrum.
- Advanced lean
- Lean continuous delivery
- Exploratory lean startup



## Test Driven Development

Writing tests before writing code

1. Write test for the next bit of functionality to add.
2. Write code till test passes.
3. Refactor code to improve it.
    - Remove bugs.
    - Improve performance.
    - Improve readability.



## Behavior driven development

An agile process for development software that incorporates concepts from test driven development. Is considered an evolution in the thinking of TDD.

- Where to start testing?
- What to test and what not to test?
- How much to test?
- Why a test should fail?
- What to call the tests?

BDD uses stories to express business value and desired behaviour. 

> **As a** ....role.... **I want to** ....feature.... **So that** ....benefit.... 

Tests of any unit of software should be specified of the desired behaviour of the unit and should look at the very specific business value.

