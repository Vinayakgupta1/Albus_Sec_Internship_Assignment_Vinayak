import requests
from bs4 import BeautifulSoup
import re
import threading
import asyncio
import aiohttp
import random
import time

# Define common API key patterns
patterns = {
    "Google API Key": r"AIza[0-9A-Za-z-_]{35}",
    "AWS Access Key ID": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Access Key": r"(?<![A-Z0-9])[A-Za-z0-9/+=]{40}(?![A-Z0-9])",
    "Generic API Key": r"[a-zA-Z0-9]{32,45}",
    "Bearer Token": r"Bearer\s[0-9a-zA-Z\-_]{20,}",
}

# List of user agents for rotation
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
]

# Rate limiting control
semaphore = asyncio.Semaphore(5)

async def fetch_content(session, url):
    """
    Fetch the content of a URL using aiohttp library
    :param session: aiohttp session
    :param url: URL to fetch
    :return: HTML content of the URL
    """
    headers = {'User-Agent': random.choice(user_agents)}
    async with semaphore:
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()
            return await response.text()

def extract_js_files(soup):
    """
    Extract JavaScript file URLs from an HTML soup
    :param soup: BeautifulSoup object
    :return: List of JavaScript file URLs
    """
    scripts = soup.find_all('script', src=True)
    return [script['src'] for script in scripts]

def find_api_keys(content, patterns):
    """
    Find API keys in a given content using regular expressions
    :param content: Content to search for API keys
    :param patterns: Dictionary of API key patterns
    :return: Dictionary of found API keys
    """
    found_keys = {}
    for name, pattern in patterns.items():
        matches = re.findall(pattern, content)
        if matches:
            found_keys[name] = matches
    return found_keys

async def scan_js_file(session, js_file, url, patterns, found_keys):
    """
    Scan a JavaScript file for API keys
    :param session: aiohttp session
    :param js_file: JavaScript file URL
    :param url: Base URL
    :param patterns: Dictionary of API key patterns
    :param found_keys: Dictionary to store found API keys
    """
    if not js_file.startswith('http'):
        js_file = url.rstrip('/') + '/' + js_file.lstrip('/')
    try:
        js_content = await fetch_content(session, js_file)
        js_keys = find_api_keys(js_content, patterns)
        for key, values in js_keys.items():
            if key in found_keys:
                found_keys[key].extend(values)
            else:
                found_keys[key] = values
    except aiohttp.ClientError as e:
        print(f"Could not retrieve {js_file}: {e}")

async def scan_page(url):
    """
    Scan a webpage for API keys
    :param url: URL of the webpage to scan
    :return: Dictionary of found API keys
    """
    print(f"Scanning {url}...")
    async with aiohttp.ClientSession() as session:
        page_content = await fetch_content(session, url)
        soup = BeautifulSoup(page_content, 'html.parser')

        # Scan the HTML content
        found_keys = find_api_keys(page_content, patterns)

        # Extract and scan JavaScript files
        js_files = extract_js_files(soup)
        tasks = [scan_js_file(session, js_file, url, patterns, found_keys) for js_file in js_files]

        await asyncio.gather(*tasks)

    return found_keys

def main():
    """
    Main function to scan a webpage for API keys
    """
    url = input("Enter the URL to scan: ")
    found_keys = asyncio.run(scan_page(url))

    if found_keys:
        print("Found API keys:")
        for key_type, keys in found_keys.items():
            print(f"{key_type}:")
            for key in keys:
                print(f"  - {key}")
    else:
        print("No API keys found.")

if __name__ == "__main__":
    main()