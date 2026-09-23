\# Jenkins CI/CD Pipeline with Docker



\## Project Overview



This project demonstrates a basic CI/CD pipeline using GitHub, Jenkins, Docker, and a Python Flask application.



Whenever code is pushed to GitHub, a GitHub webhook automatically triggers Jenkins. Jenkins then checks out the latest code, builds and tests the application, creates a Docker image, and deploys the application in a Docker container.



\## CI/CD Flow



GitHub → Jenkins → Build → Test → Docker Build → Docker Deploy → Application



\## Technologies Used



\* Git \& GitHub

\* Jenkins

\* Python

\* Flask

\* Docker

\* Dockerfile

\* Jenkins Pipeline



\## Pipeline Stages



\### 1. Checkout Code



Jenkins retrieves the latest source code from the GitHub repository.



\### 2. Build



A Python virtual environment is created and the application dependencies are installed.



\### 3. Test



The Flask application is tested using Python's built-in `unittest` framework.



\### 4. Docker Build



A Docker image is created using the Dockerfile.



\### 5. Docker Run/Deploy



Any existing application container is removed and a new container is started from the latest Docker image.



\## Automatic Trigger



A GitHub webhook is configured to trigger the Jenkins pipeline whenever code is pushed to the repository.



\## Application



The Flask application runs on:



`http://localhost:5000`



\## Project Files



```text

jenkins-docker-demo/

├── app.py

├── requirements.txt

├── Dockerfile

├── Jenkinsfile

├── test\_app.py

├── .dockerignore

└── README.md

```



\## Result



The project successfully demonstrates an automated CI/CD workflow where a code change pushed to GitHub triggers Jenkins, runs the build and tests, builds a Docker image, and deploys the updated application.



