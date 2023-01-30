
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from selenium import webdriver


# Get the absolute path to the script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the absolute file path by joining the script's directory with the relative file path
file_path = os.path.join(script_dir, 'files', 'CV_Jane_Smith.docx')


s = Service('/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

from selenium import webdriver
from urllib.parse import urlsplit

driver = webdriver.Chrome(service=s, options=options)

# Navigate to the website
driver.get("https://project-cad-sandpit.sandpit.itu.uts.edu.au/cad/eoi")

# Get the current URL
url = driver.current_url

# Parse the URL and get the port number
parsed_url = urlsplit(url)
port = parsed_url.port

# Print the port number
print(port)

# Close the browser
driver.quit()