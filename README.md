# Trajectory Detection Web services
## Description
This project is a lightweight web-service providing [trajectory estimation](https://link.springer.com/chapter/10.1007/978-3-540-92957-4_28) *API* for users.
Nowadays, Trajectory estimation and detection as a fundamental means to robotics and  autonomus vehicles technology is in demand of the market of this industry. Thus we decided to develop a web service which can provide a lightweight, responsive web-service for [autonomous vehicles](https://en.wikipedia.org/wiki/Uncrewed_vehicle) and [IoT-devices](https://en.wikipedia.org/wiki/Internet_of_things). 




## Requirements

### **Glossary**

* **Token** - tokens are artifacts that allow application systems to perform the authorization and authentication process.

* **Access Token** - an access token contains the security credentials for a login session  
* **Refresh Token** - Once an ```access token``` expire, clients can use a refresh token to "refresh" the access token. That is, a refresh token is a credential artifact that lets a client application get new access tokens without having to ask the user to log in again.
* **Detection model** - class of machine learning models with a well
defined interface for detecting user desired class of entities  
* **Trajectory detection** - a sort of detection models which estimates
trajectory of the user desired class of entities

### **Stakeholder and Roles**
#### **Stakeholder**
[AHURATUS Tech](https://github.com/Ahuratus).
#### **Roles**
* [Ehsan Shaghaei](https://github.com/Ehsan2754)
  * Project Manager 
  * Back-End Developer
  * Computer Vision
  * DevOps 
  * QA

* [Denis Kalachev](https://github.com/Mr-Barry)
  * Documentation manager
  * Miscellaneous Roles

### **User stories**

#### Web client User:
* **Registration** User registers through the API providing his "email" and "password" and receives an access token and a refresh token.
```sh 
http://localhost:12345/api/registration
```

Example request:

Example Body
```JSON
{
    "email":"dummyuser@ahuratus.ir",
    "password":"dummypass"
}
```
Example Responses
``` JSON
{
    "message": "Logged in as dummyuser@ahuratus.ir",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMzg5MjQwNywianRpIjoiOTgxYjE3MDctMTBmZC00YjQ4LTg3ZWQtYzZlNzlmY2E5NzRjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImR1bW15dXNlckBhaHVyYXR1cy5pciIsIm5iZiI6MTYzMzg5MjQwNywiZXhwIjoxNjMzODkzMzA3fQ.GzyMkQb7b4fSGFsSLLKg853K-psydMtDBN47gGS50AM",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMzg5MjQwNywianRpIjoiMzM3ZTAyNjMtM2MxMS00MTk1LWI5NTctOTEzZDQ5Y2MyMDFjIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJkdW1teXVzZXJAYWh1cmF0dXMuaXIiLCJuYmYiOjE2MzM4OTI0MDcsImV4cCI6MTYzNjQ4NDQwN30.abwFLlwyfd3zQkLnuQNrIy2lRCWjhKUXyXgVzrudFVc"
}
```
``` JSON
{
    "message": "Email dummyuser@ahuratus.ir already exists"
}
```



* **login** Registered user logs in through the API providing his "email" and "password" and receives ```refresh token``` and ```access token```.
``` sh 
http://localhost:12345/api/login
```

Example request:

Example Body
```JSON
{
    "email":"dummyuser@ahuratus.ir",
    "password":"dummypass"
}
```
Example Responses
``` JSON
{
    "message": "User dummyuser@ahuratus.ir was created",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMzg5MjIyNywianRpIjoiZGE4MzQxY2EtMGJhNC00ZGNmLWJhYmUtZDRlMGIxNTFlOWUwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImR1bW15dXNlckBhaHVyYXR1cy5pciIsIm5iZiI6MTYzMzg5MjIyNywiZXhwIjoxNjMzODkzMTI3fQ.ZlUMHK1eWKOIsrzkt2En4zaIyY1rxkbvopmWBnFvZDc",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMzg5MjIyNywianRpIjoiN2JkN2RmZDMtYTkxYS00YjFhLWJiNDktOTgwYmRmNGIwNWVlIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJkdW1teXVzZXJAYWh1cmF0dXMuaXIiLCJuYmYiOjE2MzM4OTIyMjcsImV4cCI6MTYzNjQ4NDIyN30.Em6RwVhZY5ygKCJKajRC9Qo80-_feRLLBPMrrijJNQA"
}
```
Example Body
```JSON
{
    "email":"trickyuser@ahuratus.ir",
    "password":"dummypass"
}
```
Example Responses
``` JSON
{
    "message": "Email trickyuser@ahuratus.ir doesn't exist"
}
```


**Trajectory Estimation Session:** Logged in user send a ```BASE64 ``` frame and a ```buffer_size``` to the server through the provided API; providing his/her ACCESS TOKEN and receives the estimated trajectory vector,and ```base64``` output frame.
``` sh 
localhost:12345/api/process/trajectory
```

Example request:

Example Body
```JSON
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMzg5Mjc1MiwianRpIjoiYjhjOTgwMzMtYTc1OC00MWU4LWIwMTQtZGM1MzBlYTZhMDcyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImR1bW15dXNlckBhaHVyYXR1cy5pciIsIm5iZiI6MTYzMzg5Mjc1MiwiZXhwIjoxNjMzODkzNjUyfQ.Geahy1wgrbLd94RoOg7_g0Ip1R4JMJRTZ_uruSbX0bg",
    "buffer_size":"10",
    "frame":"B64 INPUT FRAME"
}
```
Example Responses
``` JSON
{
    "result": "[(693, 390)]",
    "trajectory": "b'/9j/4AAQSkZJRgABAQAAAQABAAD/
}
```
* **logout**
Logged in user requests for log out and his session will be terminaited, ```access token``` and ```refresh token``` will be revoked.
``` sh 
http://localhost:12345/api/logout/access
```
#### **Non-functional requirements**
* **Fast Expired Token Handling**
beside Postgres, we use Redis to keep track of the expiered tokens  because of its fast accessibility.

* **Database recovery**: In case of server failure/relocation, respectively failed/new server pulls the newest version of the software from the repository and deploys it. Server runs server initialization script and downloads and extracts the database backup.

* **Database backup**: After every 10 requests, server creates a new backup from database.

## Quality Standard

**Simplicity**: Service provides a well defined REST API for the well defined user use case scenarios.

**Accessibility**: We want this service to have 99% uptime and be accessible from any device. We will achieve that using Amazon Cloud Web Service. 

**Stability**: After every 10 requests, server creates a backup. In case of server failure/relocation, respectively failed/new server pulls the newest version of the software from the repository and deploys it. Server runs server initialization script and downloads and extracts the database back up.

**Authentication**: Service provides the sign up feature with email verification requirement for user, provides a session TOKEN for user login, provides logout

**Session safety**: Service will log off the user automatically after 10 minutes after last activity. Service supports HTTPS protocol for safer communication

**Login Tracking**: Service tracks the user login activities

## Design 
### Database Diagram
![Database Diagram](https://i.ibb.co/N9N95KH/DB-diagram-drawio.png)

### Sequence diagram

![sequence diagram](https://user-images.githubusercontent.com/54430660/136548240-82bf033d-01a3-4206-89c1-fa1efe8642eb.png)

### Use case diagram

![use case diagram](https://user-images.githubusercontent.com/54430660/136557133-ac610709-40b8-4757-bc93-ae5ec7e0b4ef.png)


### SOLID and Design Patterns

* **Single Responsibility:** The implemented classes in this project has their own responsibility. 
* **Open/Closed principle:** Classes are open for extection and does not require modifications . 
* **Liskov Substitution:** The hierarchy of the classes in program might be substituted by it's child and that will not lead to any change. **example**: [AImodel](web/ai_model.py) class and [TrajectoryEstimationModel](web/tracker_module.py) class
* **Interface Segregation:** There is no interfaces in the program, which are excessively big.
* **Dependency Inversion Principle:** in implemented classes high level modules depends on low level modules  

## Architecture
Application consist of trajectory detecton service, web service, avaliable for users, and database. Trajectory detection service is a script, written on Python, database is PostgreSQL relational database management system, and web service works with REST API standart. During development we followed ISO 29148:2011 standart, which contains provisions for the processes and products related to the engineering of requirements for systems and software products and services throughout the life cycle.
### ***Acceptance Criteria***
  * the program interface is RESTful API
  * the request body must be in JSON format 
  * the format of the frame in requests must be ```base64``` encoded '```JPG```'

### ***Technology Stack***
* Docker
* nginx
* gunicorn
* flask
* jwt
* Postgres
* redis (Used to store jwt token information)
* SQLalchemy
* OpenCV
* numpy

### ***Static view Diagram***
![Static view](https://user-images.githubusercontent.com/54430660/136585793-4f134ac8-3858-4426-a405-e2096df01600.png)  


### ***Dynamic view Diagram***
![Dynamic view](https://user-images.githubusercontent.com/54430660/136585878-c840cfb8-1cd2-47fe-b7c8-29c6b8b034a0.png)   

## Code
### **Usage**

#### **Pre-requesties**
Install [docker](https://www.docker.com/get-started)

#### **Installing and Running**

1. First clone the repo or download the repo as a zip and extract it.
```sh
 git clone https://github.com/Ahuratus/Trajectory-Detection-Web-services.git 
 ```

2. Change Directory
```sh
 cd Trajectory-Detection-Web-services 
 ```

3. Install application packages
```sh
docker-compose --file docker-compose.yml up --build
```

4. If you faced with issues, check the [issues](https://github.com/Ahuratus/Trajectory-Detection-Web-services/issues) page. if you can't find your problem. place your problem there. we would answer you ASAP!

5. You can use [Postman](https://www.postman.com/downloads/) to check our APIs. the ```nginx``` is running on the port ```12345```

### Running Example [Proof of concept]

* Full Test

[![Alt text](https://img.youtube.com/vi/I3LqgN1WdPU/0.jpg)](https://www.youtube.com/watch?v=I3LqgN1WdPU)

* JWT Auth. Test

[![Alt text](https://img.youtube.com/vi/I3LqgN1WdPU/1.jpg)](https://youtu.be/I3LqgN1WdPU?t=112)

* API Test

[![Alt text](https://img.youtube.com/vi/I3LqgN1WdPU/2.jpg)](https://youtu.be/I3LqgN1WdPU?t=203)

* Visual output of the trajectory model

[![Alt text](https://img.youtube.com/vi/I3LqgN1WdPU/3.jpg)](https://youtu.be/I3LqgN1WdPU?t=437)


### **Static analyzers (Lint)**
I used ```pyflake``` for static analyse. the results are pretty decent as we see in following images. And there are no criticial issues in the code.

![pyflake1](https://i.ibb.co/tH3DWNX/pyflake.png)
![pyflake2](https://i.ibb.co/tH3DWNX/pyflake1.png)

### **Code Quality**
I used codacy for checking my code quality.  and the results are as following.
![codacy](https://i.ibb.co/G70Q69k/test.png)


### Contributors

Feel free to contact me for contribution. The project is open source and I would like to invite anybody interested in feild of unmanned control to contribute.
<a href="https://github.com/Ahuratus/Trajectory-Detection-Web-services/graphs/contributors"><img src="]https://i.ibb.co/LJyTKZ4/Screenshot-2021-10-10-223456.png" /></a>


### License

[MIT](LICENSE) © Ahuratus