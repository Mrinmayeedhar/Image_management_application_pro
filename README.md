# Image_management_application_pro
# Cloud-Based Image Management Application

## Overview
This web application allows users to upload, list, download, and optionally encrypt images. It is hosted on an AWS EC2 instance and interacts with an AWS S3 bucket. The application uses Flask as the web framework and Boto3 to interface with AWS services.

## Features
- *Image Upload:* Upload images directly to an AWS S3 bucket.
- *Image Listing:* List all images stored in the S3 bucket.
- *Image Download:* Download images stored in the bucket.
- *Encryption (Optional):* Encrypt images before uploading them.
- *Decryption:* Decrypt encrypted images before download.
- *User Authentication:* Sign up and login for secure access.

## Prerequisites
- AWS account (sign up [here](https://aws.amazon.com/free/)).
- EC2 instance and S3 bucket on AWS.
- Python 3.x installed.
- Flask, Boto3, and cryptography libraries installed.

## Setup Instructions

1. *AWS Setup:*
   - Launch an EC2 instance and create an S3 bucket in your AWS account.

2. *Install Required Dependencies:*
   ```bash
   pip install flask boto3 cryptography werkzeug
