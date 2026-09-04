import logging
# Creating a logger object and implementing its structure
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(lineno)d - %(message)s - ",encoding="utf-8",filename="news.log",level=logging.INFO)
logger=logging.getLogger(__name__)
