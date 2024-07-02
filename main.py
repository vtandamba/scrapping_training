import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://www.docstring.fr/api/books_to_scrape/index.html"
response = requests.get(url)

with open("index.html", "w") as f:
    f.write(response.text)
with open("index.html", 'r') as f:
    html = f.read()
    
# analyser la page d'accueil des livres du site books_to_scrape
soup = BeautifulSoup(html, "html.parser")
aside = soup.find('div', class_='side_categories')
# categories_div = aside.find('ul').find('li').find('ul')
# for category in categories.children:
#     if(category.name):
#         print(category.text.strip())
#     

categories_div = aside.find('ul').find('li').find('ul')
categories = [child.text.strip() for child in categories_div.children if child.name]
pprint (categories)


images = soup.find('section').find_all('img')
for img in images:
    print(img['src'])
    # ou
    print(img.get('src'))
    
# pprint('images')