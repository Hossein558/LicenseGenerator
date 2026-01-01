# Atlassian License Generator Service

A Dockerized service allowing you to generate licenses for Atlassian products and plugins via a simple Web UI or REST API. This project wraps the `atlassian-agent.jar` in a Python Flask application.

## Features

- **Web Interface**: Modern, responsive UI to easily generate keys.
- **REST API**: Simple endpoint for programmatic access.
- **Dockerized**: Easy to deploy anywhere (Linux, Windows, Cloud).
- **Auto-Restart**: configured for high availability.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine or server.

## Installation & Running

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Hossein558/LicenseGenerator.git
    cd LicenseGenerator
    ```

2.  **Place the Agent JAR:**
    Make sure you have `atlassian-agent.jar` in the root directory. *Note: This file is not included in the repo for copyright reasons.*

3.  **Build the Docker Image:**
    ```bash
    docker build -t license-service .
    ```

4.  **Run the Container:**
    ```bash
    docker run -d -p 5000:5000 --restart always --name license-gen license-service
    ```

## Quick Start with Docker Hub

You can also pull the pre-built image directly from Docker Hub:

```bash
docker pull hossein558/license-generator:v1.0.0
docker run -d -p 5000:5000 --restart always --name license-gen hossein558/license-generator:v1.0.0
```

## Usage

### Web Interface
Open your browser and navigate to:
http://localhost:5000

Enter the Organization Name and Plugin Key, then click **Generate**.

### REST API
You can generate a license by making a GET request:

```
GET /generate?o=<Organization_Name>&p=<Plugin_Key>
```

**Example:**
```bash
curl "http://localhost:5000/generate?o=MyCompany&p=com.atlassian.jira.plugin.example"
```

## Project Structure

- `app.py`: Flask application logic.
- `Dockerfile`: Configuration for building the Docker image (Python 3.9 + Java 11).
- `templates/index.html`: Frontend UI.
- `requirements.txt`: Python dependencies.

## Disclaimer
This project is for **educational purposes only**. Please support software developers by purchasing valid licenses.
