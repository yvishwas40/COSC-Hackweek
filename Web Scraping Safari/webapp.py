import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send GET request to GitHub Trending page
url = 'https://github.com/trending'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
repo_list = soup.find_all('article', class_='Box-row')[:5]  # top 5

# Step 3: Extract repository names and links
repositories = []
for repo in repo_list:
    full_name = repo.h2.a.get('href').strip()  # e.g., /owner/repo-name
    name = full_name.lstrip('/')               # remove leading slash
    link = f'https://github.com{full_name}'    # full URL
    repositories.append((name, link))

# Step 4: Save to CSV
csv_file = 'trending_repos.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Repository Name', 'Link'])
    writer.writerows(repositories)

print(f"Top 5 trending repositories saved to {csv_file}")
