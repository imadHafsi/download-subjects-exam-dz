import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import wget


def download_page(link,folder_name):
    driver.get(link)
    driver.implicitly_wait(2)
    ps = driver.page_source
    soup_download_page = BeautifulSoup(ps, 'html.parser')
    download_link = soup_download_page.find(id="actions-download").get('href')
    wget.download(download_link, folder_name)

# Get the absolute path of the script and its directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the target URL
driver.get('https://www.dzexams.com/ar/3ap/tamazight')

# Wait for the page to load
driver.implicitly_wait(2)

# Get the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find all divs with the specified class
divs = soup.find_all('div', class_='btn-group header bg-purple-700 item-tablist')

# Extract the level title from the page
level_title = soup.find('div', class_="item-title").find('a', class_='bg-1').find('h2').text.split(' - ')[0].replace('\n', '')

# Extract the subject title from the page
subject_title = soup.find('div', class_="item-title").find('h1', class_='bg-2').text.split(' - ')[0].replace('\n', '')

# Create a base directory for the level
base_dir_lvl = os.path.join(script_dir, level_title)
os.makedirs(base_dir_lvl, exist_ok=True)

# Create a base directory for the subject
base_dir = os.path.join(base_dir_lvl, subject_title)
os.makedirs(base_dir, exist_ok=True)

# Extract panel IDs from the onclick attributes
panel_ids = []
for div in divs:
    onclick_attr = div.get('onclick')
    if onclick_attr:
        match = re.search(r"\$\('#(panel-[^']+)'\)", onclick_attr)
        if match:
            panel_ids.append(match.group(1))

# Iterate over the divs and create folders for each button
for idx, div in enumerate(divs):
    button = div.find('button', class_='btn btn-group-content')
    to_delete = f"{subject_title} -  "
    button_text = button.text.replace(to_delete, "").strip()
    folder_name = os.path.join(base_dir, button_text)
    os.makedirs(folder_name, exist_ok=True)
    
    # Find the corresponding panel using the panel ID
    panel = soup.find('div', id=panel_ids[idx])
    to_links = panel.find_all('div')

    # Iterate over the links and download the files
    for to_link in to_links:
        href = to_link.find('a').get('href')
        link = f"https://www.dzexams.com{href}"
        download_page(link, folder_name)

# Close the WebDriver
driver.quit()
