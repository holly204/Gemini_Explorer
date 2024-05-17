# Gemini_Explorer
## Install Required Packages:
pip install streamlit vertexai
## Verify the Project ID:
Go to the Google Cloud Console.
Click on "IAM & Admin" > "Settings".
Note the "Project ID" (not the project name). This is the ID you need to use in your script.
## Enable Vertex AI API:
In the Google Cloud Console, go to "APIs & Services" > "Library".
Search for "Vertex AI" and ensure that the Vertex AI API is enabled for your project.
## Check IAM Permissions:
Go to "IAM & Admin" > "IAM".
Ensure that your account has roles like Vertex AI User or Vertex AI Admin.

## Authenticate with Google Cloud:
gcloud auth application-default login

