import requests
import time
from bs4 import BeautifulSoup

# URL of the login page
login_url = "https://example.com/login"

# URL of the website to check for grades
grades_url = "https://example.com/grades"

# Login credentials
payload = {
    "username": "your_username",
    "password": "your_password"
}

# Create a session to persist login information
session = requests.Session()

# Make a POST request to the login page with the login credentials
response = session.post(login_url, data=payload)

# Previous content of the website
prev_content = ""

while True:
    # Make a GET request to the website to check grades
    response = session.get(grades_url)

    # Get the current content of the website
    current_content = response.text

    # Check if the content has changed
    if current_content != prev_content:
        print("New grades have been announced!")
        # Update the previous content
        prev_content = current_content
    else:
        print("No new grades have been announced.")

    # Wait for 5 minutes before checking again
    time.sleep(3600)
