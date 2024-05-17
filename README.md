# Gemini_Explorer
## Create Account and project
Create Google Cloud account by signing into https://console.cloud.google.com/
Create a project
Install Google Cloud SDK

## Install Required Packages:
pip install streamlit 
## Verify the Project ID:
Go to the Google Cloud Console.
Click on "IAM & Admin" > "Settings".
Note the "Project ID" (not the project name). This is the ID you need to use in your script.
## Enable Vertex AI API:
In the Google Cloud Console, go to "APIs & Services" > "Library".
Search for "Vertex AI" and ensure that the Vertex AI API is enabled for your project.
## Check IAM Permissions:
In the Google Cloud Console, Go to "IAM & Admin" > "IAM".
Ensure that your account has roles like Vertex AI User or Vertex AI Admin.

## Authenticate with Google Cloud:
open VSC and run: 
gcloud auth application-default login

## Set Your Google Cloud Project:
In the VSC run: 
gcloud config set project your-project-id

## Verify Authentication:
In the VSC run: 
gcloud auth application-default print-access-token

## Run Your Streamlit Application:
In the VSC run: 
streamlit run gemini_explorer.py
