from bs4 import BeautifulSoup
import requests
from pprint import pprint as p


def find_jumia(search):
    n = ' '
    for n in search:
        word = search.replace(' ', '+')
    url = "https://www.jumia.com.ng/catalog/?q=" + word
    article = requests.get(url)
    jumia = BeautifulSoup(article.text, "html.parser")
    item_name = []
    item_price = []
    item_url = []
    item_url1 = []
    item_data = []
    all_h2 = jumia.find_all("h2")
    price = jumia.find_all("span", "price")
    all_urls = jumia.find_all("a", "link")
    for i in range(0, 15):
        item_name.append(all_h2[i].get_text("->"))
    for i in range(0, 30, 2):
        item_price.append(price[i].get_text())
    for i in range(0, len(all_urls)):
        item_url.append(all_urls[i].get_text())
        links = all_urls[i]['href']
        item_url1.append(links)
    for i in range(0, 15):
        item_data.append(item_name[i])
        item_data.append(item_price[i])
    #     print(item_name[i])
    #     print(item_price[i])
    #     print(item_url1[i])
    #p(item_data)
    return item_data, item_url1


#find_jumia('gowns')


def find_konga(search):
    n = ' '
    for n in search:
        word = search.replace(' ', '+')
    url = "https://www.konga.com/catalogsearch/result/?q=" + word
    article = requests.get(url)
    konga = BeautifulSoup(article.text, "html.parser")
    item_name = []
    item_price = []
    item_url = []
    all_span = konga.find_all("div", "product-name truncate")
    price = konga.find_all("div", "original-price")
    all_urls = konga.find_all("a", "product-block-link")
    url_prefix ="https://www.konga.com"
    for i in range(0, 9):
        item_name.append(all_span[i].get_text("|", strip=True))
    for i in range(0, 9):
        item_price.append(price[i].get_text())
    for i in range(0, len(all_urls)):
        links = all_urls[i]['href']
        item_url.append(url_prefix + links)
    for i in range(0, 9):
        print(item_name[i])
        print(item_price[i])
        print(item_url[i])


#find_konga('samsung')


def find_payporte(search):
    n = ' '
    for n in search:
        word = search.replace(' ', '+')
    url = "https://www.payporte.com/catalogsearch/result/?q=" + word
    article = requests.get(url)
    payporte = BeautifulSoup(article.text, "html.parser")
    item_name = []
    item_price = []
    item_url = []
    all_h3 = payporte.find_all("div", "product-name text-capitalize")
    price = payporte.find_all("span", "price")
    all_urls = payporte.find_all("a", "product-image")
    for i in range(0, 10):
        item_name.append(all_h3[i].get_text("|", strip=True))
    for i in range(0, 10):
        item_price.append(price[i].get_text())
    for i in range(0, len(all_urls)):
        links = all_urls[i]['href']
        item_url.append(links)
    for i in range(0, 10):
        print(item_name[i])
        print(item_price[i])
        print(item_url[i])


#find_payporte('shoes')
