from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import Remote, ChromeOptions
# from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
import time
import os

# ------------------------------------------------------------------------------
# Bright Data Scraping Browser WebDriver Key
# ------------------------------------------------------------------------------
# Replace `SBR_WEBDRIVER` with your actual WebDriver endpoint key from Bright Data.
# This key is required to authenticate and connect your script to the Bright Data
# Scraping Browser infrastructure.
#
# Example:
# SBR_WEBDRIVER = "https://brd.superproxy.io:9515"
#
# You can find your WebDriver key and endpoint in your Bright Data dashboard:
# https://brightdata.com
# ------------------------------------------------------------------------------

# SBR_WEBDRIVER = "SBR_WEBDRIVER"

# ------------------------------------------------------------------------------
# Alternative Method: Using Bright Data's Scraping Browser (SBR)
# ------------------------------------------------------------------------------
# The commented-out function below shows how to connect to Bright Data's 
# Scraping Browser to handle advanced automation scenarios like:
# - Solving captchas automatically
# - Bypassing IP bans and geo-restrictions
# - Accessing heavily protected websites
#
# To use this, you need:
# 1. An active Bright Data account with Scraping Browser access.
# 2. The SBR WebDriver endpoint (set in the `SBR_WEBDRIVER` variable).
# 3. The appropriate Bright Data browser driver and credentials.
#
# More details on setup and usage:
# https://brightdata.com/products/scraping-browser
#
# Uncomment and configure the code below to activate SBR support.
# ------------------------------------------------------------------------------

# def scrape_website(website):
#     print("Connecting to Scraping Browser...")
#     sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
#     with Remote(sbr_connection, options=ChromeOptions()) as driver:
#         driver.get(website)
#         print("Waiting captcha to solve...")
#         solve_res = driver.execute(
#             "executeCdpCommand",
#             {
#                 "cmd": "Captcha.waitForSolve",
#                 "params": {"detectTimeout": 10000},
#             },
#         )
#         print("Captcha solve status:", solve_res["value"]["status"])
#         print("Navigated! Scraping page content...")
#         html = driver.page_source
#         return html


def scrape_website(website):
    print("Starting Chrome browser...")
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background (remove this line to see browser)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Use the local chromedriver.exe
    chromedriver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        print(f"Navigating to {website}...")
        driver.get(website)
        print("Page loaded! Waiting for content...")
        
        # Wait for page to fully load
        time.sleep(3)
        
        print("Scraping page content...")
        html = driver.page_source
        return html
        
    except Exception as e:
        print(f"Error scraping website: {str(e)}")
        return ""
    finally:
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]