import requests
from bs4 import BeautifulSoup

def search_articles(search_term, num_pages=1):
    article_urls = []
    for i in range(num_pages):
        url = f"https://www.google.com/search?q={search_term}&tbm=nws&start={i*10}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "lxml")
        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if "url?q=" in href and not "webcache" in href:
                article_urls.append(href.split("?q=")[1].split("&sa=U")[0])
    return article_urls
