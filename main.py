from scraper import Scraper
from config import KHABAR_ONLINE_CONFIG,TASNIM_CONFIG

def main_loop():
    tasnim_scraper=Scraper(TASNIM_CONFIG)
    khabar_online_scraper=Scraper(KHABAR_ONLINE_CONFIG)

    tasnim_scraper.extract()
    khabar_online_scraper.extract()

if __name__=="__main__":
    main_loop()