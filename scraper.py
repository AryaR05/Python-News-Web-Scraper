from bs4 import BeautifulSoup
import requests
from function import logger
from config import HEADER_CONFIG, MAX_RETRIES, MAX_CRITICAL_ERRORS,REQUIRED_KEYS
import time
from urllib.parse import urljoin
from news_database import NewsDatabase


class Scraper:
    def __init__(self, web_config):

        self.web_config = web_config

# Checking the accuracy of important values inside configs
        for key in REQUIRED_KEYS:

            if not self.web_config.get(key):
                logger.critical(f"Missing required config: {key}")
                return None
        self.session = requests.Session()
        self.retries = 0
        self.critical_errors = 0

    def sleep(self):
        time.sleep(2)

# Request sending function
    def request(self, url, header):
        try:
            response = self.session.get(url, headers=header, timeout=3)
            return response.text if response.status_code == 200 else None

        except Exception as e:
            logger.error(f"The request was unsuccessful! error type : {e}")
            return None
        
# Get the page HTML content  from the site
    def fetch_html(self):
# Retry the request if it fails
        while self.retries < MAX_RETRIES:
            html = self.request(self.web_config["web_url"], HEADER_CONFIG)

            if html:
                logger.info("Request successful")
                return html

            self.retries += 1
            logger.error(
                f"The request was unsuccessful! , retry {self.retries}/{MAX_RETRIES}")
            self.sleep()

        logger.critical("The request failed after maximum retries")
        return None
    
# Convert raw BeautifulSoup to HTML
    def parser(self):
        html = self.fetch_html()
        if not html:
            return None
        soup = BeautifulSoup(html, "html.parser")
        return soup
    
# Extracting the text of an element using a CSS Selector
    def get_text(self,parent,selector):
        if not selector:
            return None
        tag=parent.select_one(selector)
        return tag.get_text(strip=True) if tag else None
# Extracting the value of an element using a CSS Selector
    def get_attr(self,parent,selector,attr):
        if not selector:
            return None
        tag=parent.select_one(selector)
        return tag.get(attr) if tag else None

# Extracting Texts and Links from HTML Content
    def extract(self):
        self.retries = 0
        self.critical_errors = 0
        soup = self.parser()
        if not soup:
            return None
        
# Finding the parent tag
        main_tag = soup.select_one(self.web_config["main_tag"])
        if not main_tag:
            logger.critical("The main tag not found!")
            return None
        
# Find all the news in the main section of the page
        block = main_tag.select(self.web_config["block"])
        if not block:
            logger.critical(f"The block not found!")
            return None
        
# Extracting tag contents for each news item
        for news_tag in block:

# Getting the news link
            path = self.get_attr(news_tag,self.web_config["url_tag"],"href")
            
# Checking if the news link has been extracted
            if not path:
                self.critical_errors += 1
                logger.error(
                    f"url missing for news item {self.critical_errors} / {MAX_CRITICAL_ERRORS}")
# Checking the number of errors
                if self.critical_errors >= MAX_CRITICAL_ERRORS:
                    logger.critical("No url found for any news")
                    return None
                continue

# Merging the news path with the site's base link
            news_url = urljoin(self.web_config["web_url"], path)

# Checking that the news is not already in the database
            with NewsDatabase() as db:
                if db.check_exists_news(news_url):
                    logger.info(f"already url in DB: {news_url}")
                    continue
            
# Extracting the news headline
            news_title = self.get_text(news_tag,self.web_config["title_tag"])

# Checking if the news headline was extracted
            if not news_title:
                self.critical_errors += 1
                logger.error(
                    f"Title missing for a news item {self.critical_errors} / {MAX_CRITICAL_ERRORS}")
# Checking the number of errors
                if self.critical_errors >= MAX_CRITICAL_ERRORS:
                    logger.critical("No title found for any news")
                    return None
                continue

# Extracting news descriptions
            description = self.get_text(news_tag,self.web_config.get("description_tag"))
            
# Extracting the news release date
            published_date = self.get_text(news_tag,self.web_config.get("date_tag"))

# Extract the news image link if it exists
            image_url = self.get_attr(news_tag,self.web_config.get("image_tag"),"src")


            if not description:

                logger.warning(f"Description missing for: {news_title}")

            if not published_date:

                logger.warning(f"Date missing for: {news_title}")

            if not image_url:
                logger.warning(f"Image url missing for{news_title}")

# Save the news in the database
            with NewsDatabase() as db:
                db.save_news(self.web_config["web_name"],self.web_config["category"],news_title, description, news_url, image_url, published_date)
                logger.info(f"Saved news with {news_title}")

