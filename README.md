# Backup Service using Docker and Kubernetes

## Project Overview
This project involves creating a backup service that periodically backs up a folder's contents to Google Drive using Docker and Kubernetes. The service is orchestrated using Kubernetes CronJobs and utilizes Docker containers for deployment.

## General Guidelines for the Project
- Create a GitHub Repository with a specific naming convention.
- Weekly progress updates must be pushed to the repository.
- Each team's weekly progress update must be shown to the teachers in class.

## Problem Statement Breakdown
### Week 1: Containerized Google Drive Client
1. Set up Google Drive API:
   - Obtain credentials for the Google Drive API.
   - Use the google-api-python-client library.
2. Create a Docker Container:
   - Write a Dockerfile.
   - Include all necessary dependencies and backup script.
   - Build the Docker image.
3. Write the Backup Script:
   - Develop a Python script that uses the Google Drive API.
   - Ensure the script can be triggered at regular intervals.

### Week 2: Kubernetes Deployment & Orchestration
- Kubernetes CronJob:
  - Define a CronJob resource to schedule the backup operation.
  - Run the Docker container at specified intervals.
- Persistent Volume Claims (PVC):
  - Use PVCs to ensure data accessibility to the container.
- Monitoring and Logging:
  - Implement logging to track the backup process.
  - Optionally, set up monitoring for failure alerts.
- Security Considerations:
  - Securely manage API credentials and sensitive data.
  - Use Kubernetes secrets for sensitive information.
- Testing and Validation:
  - Test the backup process thoroughly.
  - Validate the recovery process from the backups.

## Installation Instructions
### Pre-Requisites/Pre-Installation:
- Docker (Windows | Ubuntu | MacOS)
- Kubernetes (Windows | Ubuntu | MacOS)
- Google Drive API credentials

## Folder Structure
├── Dockerfile <br>
├── backup_script.py <br>
├── kubernetes <br>
│    ├── cronjob.yaml <br>
│    └── pvc.yaml <br>
├── README.md <br>
└── requirements.txt <br>


- **Dockerfile:** Contains instructions for building the Docker image.
- **backup_script.py:** Python script for interacting with the Google Drive API and performing backups.
- **kubernetes/cronjob.yaml:** Defines Kubernetes CronJob resources.
- **kubernetes/pvc.yaml:** Defines Kubernetes Persistent Volume Claim resources.
- **README.md:** Project documentation.
- **requirements.txt:** List of Python dependencies.


## Configuration
- **Dockerfile:** Contains instructions to build the Docker image.
- **backup_script.py:** Python script to interact with Google Drive API and perform backups.
- **kubernetes/cronjob.yaml:** Kubernetes CronJob definition file.
- **kubernetes/pvc.yaml:** Kubernetes Persistent Volume Claim definition file.
- **requirements.txt:** List of Python dependencies.

## Testing
- Run unit tests for the backup script.
- Manually trigger backups and verify data integrity.
- Validate the recovery process from the backups.

## Contributions
- Anirudh Sai Lanka (PES2UG21CS073)
- Armaan Mittal (PES2UG21CS092)
- Atif Shaik (PES2UG21CS105)
- B Karthik (PES2UG21CS111)
  
## License
This project is licensed under the [MIT License](LICENSE).
