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

## Glossary
### TBA 

## Stakeholders
### Ehsan Shaghaei https://github.com/Ahuratus
Project Manager, Computer Vision, QA Engineer, Developer

### Denis Kalachev https://github.com/Mr-Barry
Documentation manager, Full-Stack Developer, QA Engineer, DevOps

## User stories
### User type: Web user
**Registration/Login/Logout:** User registers through the API providing his email and password and receives a VERIFICATION EMAIL.

**Reports Sessions:** A logged in user gets the reports of previous sessions using the provided API; providing his/her session TOKEN.

**Trajectory Estimation Session:** Logged in user uploads an .mp4 video to the server through the provided API; providing his/her session TOKEN.

### User type: Server
**Database recovery**: In case of server failure/relocation, respectively failed/new server pulls the newest version of the software from the repository and deploys it. Server runs server initialization script and downloads and extracts the database back up.

**Database backup**: After every 10 requests, server creates a new backup from database and uploads it to Google Drive and files.fm

## Non-functional requirements
**Simplicity**: Service provides a well defined REST API for the well defined user use case scenarios.

**Accessibility**: We want this service to have 99% uptime and be accessible from any device. We will achieve that using Amazon Cloud Web Service. 

**Stability**: After every 10 requests, server creates a backup and uploads it to Google drive and file.fm . In case of server failure/relocation, respectively failed/new server pulls the newest version of the software from the repository and deploys it. Server runs server initialization script and downloads and extracts the database back up.

**Authentication**: Service provides the sign up feature with email verification requirement for user, provides a session TOKEN for user login, provides logout

**Session safety**: Service will log off the user automatically after 10 minutes after last activity. Service supports HTTPS protocol for safer communication

**Login Tracking**: Service tracks the user login activities

## Design and architecture
### Database Diagram
<img src="https://user-images.githubusercontent.com/54430660/136548204-a8ba3b46-ac43-4220-806a-f9ee37bc2b5d.png" height="350px" />

### Sequence diagram
<img src="https://user-images.githubusercontent.com/54430660/136548240-82bf033d-01a3-4206-89c1-fa1efe8642eb.png" height="350px" />

### Use case diagram
<img src="https://user-images.githubusercontent.com/54430660/136557133-ac610709-40b8-4757-bc93-ae5ec7e0b4ef.png" height="350px" />

### Architecture
Application consist of trajectory detecton service, web service, avaliable for users, and database. Trajectory detection service is a script, whitten on Python, database is PostgreSQL relational database management system, and web service works with REST API standart. During development we followed ISO 29148:2011 standart, which contains provisions for the processes and products related to the engineering of requirements for systems and software products and services throughout the life cycle.
### Examples of REST API requests:
<a href="https://youtu.be/zTwUmZ-vaso">
JWT Authentication test
<img src="https://user-images.githubusercontent.com/54430660/136561841-c86d70ba-8c62-4a4e-b32a-5da5edb402cd.jpg" height="450px" alt="Link" />
</a>

## Code quality
There is no major issues in the code. All the issues are about format of this README file and one unused import.
<img src="https://user-images.githubusercontent.com/54430660/136563200-acbe9767-5be2-4ddc-8344-cbc7c6107dc0.jpg" height="450px" alt="Issue file" />


## Sample Output
<a href="https://youtu.be/TB-TUCAf1mk"> 
<img src="https://img.youtube.com/vi/TB-TUCAf1mk/default.jpg" height="150px" alt="Link"/>
</a>
