# Offline (Air-Gapped) Deployment Guide

This guide explains how to deploy the **License Generator Service** on a server that has **no internet access**.

## Prerequisites on the Online Machine

You need a machine with Docker and internet access to prepare the deployment package.

## Step 1: Save the Docker Image

On a machine **with internet access**, build and save the Docker image:

```bash
# Clone the repository
git clone https://github.com/Hossein558/LicenseGenerator.git
cd LicenseGenerator

# Build the Docker image
docker build -t license-service:v1.0.0 .

# Save the image to a tar file
docker save -o license-service-v1.0.0.tar license-service:v1.0.0
```

This creates a file `license-service-v1.0.0.tar` (~500MB-1GB depending on base images).

## Step 2: Transfer to Offline Server

Copy the following files to the offline server (via USB, SCP over local network, etc.):
- `license-service-v1.0.0.tar`
- `docker-compose.yml`
- `atlassian-agent.jar` (if not already included)

## Step 3: Load the Image on Offline Server

On the **offline server**:

```bash
# Load the Docker image from the tar file
docker load -i license-service-v1.0.0.tar

# Verify it's loaded
docker images | grep license-service
```

## Step 4: Run the Service

```bash
# Run using docker-compose (if available)
docker-compose up -d

# OR run directly
docker run -d -p 5000:5000 --restart always --name license-gen license-service:v1.0.0
```

## Step 5: Verify

Open a browser on the local network:
```
http://<server-ip>:5000
```

## Notes

- The image is self-contained with Python, Java, and all dependencies.
- No internet is required after loading the image.
- To update, repeat the process with a new image version.
