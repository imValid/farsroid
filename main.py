# imNotValid
from requests import get
from bs4 import BeautifulSoup
def get_data(q: str):
    req = get("https://www.farsroid.com/", {"s": q}).text
    soup = BeautifulSoup(req, "html.parser")
    links = soup.find_all("a", {"rel": "bookmark"})
    for link in links:
        link, text = link["href"], link.get_text()
        req = get(link).text
        soup = BeautifulSoup(req, "html.parser")
        downloadable_links =  soup.find_all("a", {"class": "download-btn"})
        yield {"url": link, "link_text": text, "download_links": [url["href"] for url in downloadable_links]}
if __name__ == "__main__":
    for data in  get_data("robbery bob"):
        print(data)
