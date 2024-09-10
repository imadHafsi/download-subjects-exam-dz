# download-subjects-exam-dz

This project automates the process of scraping web pages and downloading files using Selenium and BeautifulSoup. The script is designed to navigate through a specific exam-dz link, extract relevant information, and download files into organized directories.

## Features

- Uses Selenium to navigate web pages and handle dynamic content.
- Utilizes BeautifulSoup for parsing HTML content.
- Automatically creates directories based on extracted information.
- Downloads files using `wget`.

## Prerequisites

- Python 3.x
- Selenium
- BeautifulSoup
- `wget` module
- Chrome WebDriver

## Installation

1. **Clone the repository:**
    ```bash
    git clone [https://github.com/imadHafsi/download-subjects-exam-dz]
    cd your-repo-name
    ```

2. **Install the required Python packages:**
    ```bash
    pip install selenium beautifulsoup4 wget
    ```

3. **Download and install Chrome WebDriver:**
    - Download the WebDriver from ChromeDriver.
    - Ensure the WebDriver is in your system's PATH or place it in the project directory.

## Usage

1. **Update the target URL:**
    - Modify the URL in the script to the desired target page:
    ```python
    driver.get('https://www.dzexams.com/ar/3ap/tamazight')
    ```

2. **Run the script:**
    ```bash
    python exam-dz.py.py
    ```

3. **The script will:**
    - Navigate to the specified URL.
    - Extract level and subject titles.
    - Create directories based on the extracted titles.
    - Download files into the respective directories.

## Project Structure

