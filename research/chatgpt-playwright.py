import asyncio
import nest_asyncio
nest_asyncio.apply()
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

def sync_get_page_content(url):
    with sync_playwright() as p:
        # Use the chromium browser, but you can also use 'firefox' or 'webkit'
        browser = p.chromium.launch()
        
        # Create a new browser context
        context = browser.new_context()
        
        # Create a new page in the context
        page = context.new_page()
        
        # Navigate to the given URL
        page.goto(url)
        
        # Get the page content
        content = page.content()
        
        # Close the browser
        # browser.close()

        return content

google_url = "https://www.google.com"
ashby_url = "https://jobs.ashbyhq.com/eightsleep/70a2ba22-04be-45b0-823a-8fc348035e0f/application?utm_source=Simplify"

content = sync_get_page_content(ashby_url)
print(content)