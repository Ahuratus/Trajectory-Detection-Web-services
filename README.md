# Trajectory Detection Web services
## Description
This project is a lightweight web-service providing [trajectory estimation](https://link.springer.com/chapter/10.1007/978-3-540-92957-4_28) *API* for users.
Nowadays, Trajectory estimation and detection as a fundamental means to robotics and  autonomus vehicles technology is in demand of the market of this industry. Thus we decided to develop a web service which can provide a lightweight, responsive web-service for [autonomous vehicles](https://en.wikipedia.org/wiki/Uncrewed_vehicle) and [IoT-devices](https://en.wikipedia.org/wiki/Internet_of_things). 


## Installing

1. First clone the repo or download the repo as a zip and extract it.
``` git clone https://github.com/Ahuratus/Trajectory-Detection-Web-services.git ```

2. Change Directory
``` cd Trajectory-Detection-Web-services```

3. Install application packages
```  pip install -r requirements.txt ```

4. If you are a windows user check the [issue 1](https://github.com/Ahuratus/Trajectory-Detection-Web-services/issues/1)

## Running
run  following command
``` python run.py```

## Requirements
### Glossary
**Token** - 256 bytes unique string for session id, which is responsible
for authentication and identification of a user session, which can
also be used for retrieving reports or responding to user requests  
**Detection model** - class of machine learning models with a well
defined interface for detecting user desired class of entities  
**Trajectory detection** - a sort of detection models which estimates
trajectory of the user desired class of entities

### Stakeholders
#### Ehsan Shaghaei https://github.com/Ahuratus
Project Manager, Computer Vision, QA Engineer, Developer

#### Denis Kalachev https://github.com/Mr-Barry
Documentation manager, Full-Stack Developer, QA Engineer, DevOps

### User stories
#### User type: Web user
**Registration/Login/Logout:** User registers through the API providing his email and password and receives a VERIFICATION EMAIL.

**Reports Sessions:** A logged in user gets the reports of previous sessions using the provided API; providing his/her session TOKEN.

**Trajectory Estimation Session:** Logged in user uploads an .mp4 video to the server through the provided API; providing his/her session TOKEN.

#### Non-functional requirements
**Database recovery**: In case of server failure/relocation, respectively failed/new server pulls the newest version of the software from the repository and deploys it. Server runs server initialization script and downloads and extracts the database back up.

**Database backup**: After every 10 requests, server creates a new backup from database and uploads it to Google Drive and files.fm

## Quality Standard

**Simplicity**: Service provides a well defined REST API for the well defined user use case scenarios.

**Accessibility**: We want this service to have 99% uptime and be accessible from any device. We will achieve that using Amazon Cloud Web Service. 

**Stability**: After every 10 requests, server creates a backup and uploads it to Google drive and file.fm . In case of server failure/relocation, respectively failed/new server pulls the newest version of the software from the repository and deploys it. Server runs server initialization script and downloads and extracts the database back up.

**Authentication**: Service provides the sign up feature with email verification requirement for user, provides a session TOKEN for user login, provides logout

**Session safety**: Service will log off the user automatically after 10 minutes after last activity. Service supports HTTPS protocol for safer communication

**Login Tracking**: Service tracks the user login activities

## Design 
### Database Diagram
<img src="https://user-images.githubusercontent.com/54430660/136548204-a8ba3b46-ac43-4220-806a-f9ee37bc2b5d.png" height="350px" />

### Sequence diagram
<img src="https://user-images.githubusercontent.com/54430660/136548240-82bf033d-01a3-4206-89c1-fa1efe8642eb.png" height="350px" />

### Use case diagram
<img src="https://user-images.githubusercontent.com/54430660/136557133-ac610709-40b8-4757-bc93-ae5ec7e0b4ef.png" height="350px" />
### SOLID and Design Patterns
**Single Responsibility:** Each class in this project have only one responsibility.  
**Open/Closed principle:** Classes are open for extection and does not require modifications  
**Liskov Substitution:** Each class in program might be substituted by it's child and that will not lead to any change  
**Interface Segregation:** There is no interfaces in the program, which are excessively big  
**Dependency Inversion Principle:** No high level modules depends on low level modules  

## Architecture
Application consist of trajectory detecton service, web service, avaliable for users, and database. Trajectory detection service is a script, written on Python, database is PostgreSQL relational database management system, and web service works with REST API standart. During development we followed ISO 29148:2011 standart, which contains provisions for the processes and products related to the engineering of requirements for systems and software products and services throughout the life cycle.
### Acceptance Criteria
  * RESTful API
  * 

### Static view Diagram
<img src="https://user-images.githubusercontent.com/54430660/136585793-4f134ac8-3858-4426-a405-e2096df01600.png" height="450px" alt="Static view" />  

### Dynamic view Diagram
<img src="https://user-images.githubusercontent.com/54430660/136585878-c840cfb8-1cd2-47fe-b7c8-29c6b8b034a0.png" height="450px" alt="Dynamic view" />  

## Code
### Examples of REST API requests:
<a href="https://youtu.be/zTwUmZ-vaso">
JWT Authentication test
<img src=https://img.youtube.com/vi/zTwUmZ-vaso/default.jpg height="450px" alt="Link" />
</a>

### Code quality
There is no major issues in the code. All the issues are about format of this README file and one unused import.
<img src="https://user-images.githubusercontent.com/54430660/136563200-acbe9767-5be2-4ddc-8344-cbc7c6107dc0.jpg" height="450px" alt="Issue file" />


### Sample Output
<a href="https://youtu.be/TB-TUCAf1mk"> 
<img src="https://img.youtube.com/vi/TB-TUCAf1mk/default.jpg" height="150px" alt="Link"/>
</a>
