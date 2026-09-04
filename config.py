HEADER_CONFIG = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
MAX_RETRIES=5
MAX_CRITICAL_ERRORS=10
REQUIRED_KEYS=[
    "web_name",
    "category",
    "web_url",
    "main_tag",
    "block",
    "url_tag",
    "title_tag"
]

TASNIM_CONFIG={
    "web_name":"tasnim",
    "category":"فضا-و-نجوم",
    "web_url":"https://www.tasnimnews.ir/fa/service/1486/%D9%81%D8%B6%D8%A7-%D9%88-%D9%86%D8%AC%D9%88%D9%85",
    "main_tag":"#Container",
    "block":"article",
    "url_tag":"a",
    "title_tag":"h2",
    "description_tag":"h4",
    "date_tag":"time",
    "image_tag":"img"

}

KHABAR_ONLINE_CONFIG={
    "web_name":"khabar_online",
    "category":"دانش-و-فناوری",
    "web_url":"https://www.khabaronline.ir/archive/pl/174/%D8%AF%D8%A7%D9%86%D8%B4-%D9%88-%D9%81%D9%86%D8%A7%D9%88%D8%B1%DB%8C?tp=7",
    "main_tag":"#box202 > div > ul",
    "block":"#box202 > div > ul > li",
    "url_tag":"a",
    "title_tag":"h3",
    "description_tag":"p",
    "date_tag":"time",
    "image_tag":"img"

}



