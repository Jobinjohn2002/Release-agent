import os
import requests
from dotenv import load_dotenv

# Load API token from .env
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")

# GitHub API URL
url = f"https://api.github.com/repos/{GITHUB_REPO}/pulls"

# Headers for authentication
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

# Function to fetch and check PR descriptions
def check_pr_descriptions():
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        prs = response.json()
        for pr in prs:
            pr_number = pr["number"]
            pr_title = pr["title"]
            pr_body = pr["body"]

            if not pr_body or pr_body.strip() == "":
                print(f"⚠️ PR #{pr_number} ('{pr_title}') has NO description!")
            else:
                print(f"✅ PR #{pr_number} ('{pr_title}') looks good.")
    else:
        print(f"Error: {response.status_code}, {response.json()}")

# Run the check
check_pr_descriptions()
