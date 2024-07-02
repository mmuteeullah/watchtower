## watchtower

**Table of Contents**

* Prerequisites
* Steps to Run the App
* Notes

## Prerequisites

Before running the application, you'll need the following:

* [Docker]
* [Docker-compose]

## Steps to Run the App

1. **Running the Prometheus and Alertmanager Infra:**
    
    * First Create the docker network "watchtower-network":
    
     ```
     docker network create watchtower-network
     ```

     ```
     cd some_docker_stuff
     ```

     ```
     docker-compose up --build
     ```

2. **Running the App:**

    * Go back to the main directory 

     ```
     cd ..
     ```

     ```
     ./run.sh
     ```

     * The above run.sh script will build, test and deploy the project.

## Notes

- A custom app is created to mimic high cpu behaviour.
- Call the below api to mimic high cpu for 600 sec. (Metrics can be seen on localhost:8000/metrics)

    ```bash
    curl -X POST "http://localhost:8000/trigger/high-cpu/?duration=600"
    ```


