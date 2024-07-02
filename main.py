import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://www.docstring.fr/api/books_to_scrape/index.html"
response = requests.get(url)

# recuperer des informations avec beautifulsoup
soup = BeautifulSoup(response.text, "html.parser")
# images = soup.find_all('img')
images = soup.find_all('article', class_="product_prod")
aside = soup.find('aside')
for child in aside.children:
    if child.name:
        print(child.name)
pprint(images)
pprint(aside)
side_categories = aside.find('div', class_ ='side_categories')
links = side_categories.find_all('a')
# Compter le nombre de liens avec un attribut href
if side_categories:  # Vérifiez que l'élément a été trouvé
    links = side_categories.find_all('a')
    pprint(links)

    # Compter le nombre de liens avec un attribut href
    href_count = len([link for link in links if link.get('href')])
    print(f"Nombre de liens avec un attribut href : {href_count}")
else:
    print("Div with class 'side_categories' not found")
    
print(aside.parent.parent)