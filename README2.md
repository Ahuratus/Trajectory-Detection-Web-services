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
5. 
## Running
run  following command
``` python run.py```

## Glossary
### TBA 

## Stakeholders
### Ethan Shagaei https://github.com/Ahuratus
Project Manager, Computer Vision, QA Engineer, Developer

### Denis Kalachev https://github.com/Mr-Barry
Documentation manager, Full-Stack Developer, QA Engineer, DevOps

## User stories
### User type: Web user
**Registration/Login/Logout:** User registers through the API providing his email and password and receives a VERIFICATION EMAIL.

**Reports Sessions:** A logged in user gets the reports of previous sessions using the provided API; providing his/her session TOKEN.

**Trajectory Estimation Session:** Logged in user uploads an .mp4 video to the server through the provided API; providing his/her session TOKEN.

**REST API**: The web service has a well-defined REST API


### User type: Server
**Database recovery**: In case of server failure/relocation, respectively failed/new server pulls the newest version of the software from the repository and deploys it. Server runs server initialization script and downloads and extracts the database back up.

**Database backup**: After every 10 requests, server creates a new backup from database and uploads it to Google Drive and files.fm

## Non-functional requirements:
**Simplicity**: Service provides a well defined REST API for the well defined user use case scenarios.

**Accessibility**: We want this service to have 99% uptime and be accessible from any device. We will achieve that using Amazon Cloud Web Service. 

**Stability**: After every 10 requests, server creates a backup and uploads it to Google drive and file.fm . In case of server failure/relocation, respectively failed/new server pulls the newest version of the software from the repository and deploys it. Server runs server initialization script and downloads and extracts the database back up.

**Authentication**: Service provides the sign up feature with email verification requirement for user, provides a session TOKEN for user login, provides logout

**Session safety**: Service will log off the user automatically after 10 minutes after last activity. Service supports HTTPS protocol for safer communication

**Login Tracking**: Service tracks the user login activities

## Design and architecture
### Class Diagram
![Class_Diagram](https://user-images.githubusercontent.com/54430660/136540402-32f2373d-4234-4009-89d6-c5ffc12c15f3.png)

### Sequence diagram
![Sequence Diagram Updated drawio](https://user-images.githubusercontent.com/54430660/136540624-f9d4a8c5-897d-4506-8cb0-77255b728273.png)

### Use case diagram
![Use case diagram](https://user-images.githubusercontent.com/54430660/136540666-9e454a59-7e45-49ab-af40-1e182abc6abc.png)

### Static analyzers TBA

## Sample Output
[![Sample Output](https://img.youtube.com/vi/TB-TUCAf1mk/default.jpg)](https://youtu.be/TB-TUCAf1mk)
