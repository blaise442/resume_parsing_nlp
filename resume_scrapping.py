"""
In the above code, we are scraping resumes from Indeed.com for the keyword 'python' in the US location. 
We are using the requests library to send a request to the URL and BeautifulSoup to parse the HTML content.
We are then iterating over the resumes and extracting the name of the candidate, job title, location,
summary, and URL of the resume.
Note: Please make sure to read the terms and conditions of the job portal before scraping any data. Also,
please note that web scraping may be illegal in some countries or jurisdictions.
"""
import requests
import csv
import requests
from bs4 import BeautifulSoup

# URL of the job portal
url = 'https://www.indeed.com/resumes?q=python&co=US'

# Send a request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the resumes listed on the job portal
resumes = soup.find_all('div', class_='rezemp-ResumeSearchCard')

# Create a CSV file and write the header row
with open('resumes.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Job Title', 'Location', 'Summary', 'URL'])

    # Iterate over the resumes and extract the data
    for resume in resumes:
        # Extract the name of the candidate
        name = resume.find('span', class_='rezemp-ResumeSearchCard-name').text.strip()

        # Extract the job title
        job_title = resume.find('span', class_='rezemp-u-h4 rezemp-ResumeSearchCard-title').text.strip()

        # Extract the location
        location = resume.find('span', class_='rezemp-ResumeSearchCard-location').text.strip()

        # Extract the summary
        summary = resume.find('div', class_='rezemp-ResumeSearchCard-summary').text.strip()

        # Extract the URL of the resume
        url = resume.find('a', class_='rezemp-ResumeSearchCard-link')['href']

        # Write the extracted data to the CSV file
        writer.writerow([name, job_title, location, summary, url])
