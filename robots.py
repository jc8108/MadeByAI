## create a python script that takes a robots.txt file from a website and generates a list of all the directories in that file
## UNTESTED

import requests
from urllib.parse import urljoin

# Enter the URL of the website to fetch robots.txt from
website_url = input("Enter website URL: ")

# Fetch robots.txt file
robots_url = urljoin(website_url, "/robots.txt")
response = requests.get(robots_url)

# Parse robots.txt file and extract directories
if response.status_code == 200:
    disallowed_dirs = []
    for line in response.text.split("\n"):
        if "Disallow:" in line:
            disallowed_dir = line.split(" ")[1]
            if disallowed_dir != "/":
                disallowed_dirs.append(disallowed_dir)
    
    # Print list of disallowed directories
    print("Disallowed directories:")
    for dir in disallowed_dirs:
        print(dir)
else:
    print("Error fetching robots.txt file")
