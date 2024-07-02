import requests
from bs4 import BeautifulSoup

url = "https://www.docstring.fr/api/books_to_scrape/index.html"
response = requests.get(url)

# analyser ou parser le fichier à taper
# beautifulSoup dispose de 4 parsers dont lxml lxml-xml html.parser(pas tolerent si balises son formaté) et html5lib plus lent mais
# tolérents s' il y a des balises mal faites

soup = BeautifulSoup(response.text, "html.parser")
# prettiffy une methode de beautifulsoup qui permet de mettre en forme l'affichage le doc html
print(soup.prettify())

## Fonction de parcourir récursivement l'arbre DOM / afficher les noeuds du dom
def traverse_dom(element, level = 0):
    # Afficher l'element actuel
    if element.name:
        print(f"{'' * level }<{element.name}>")
        # Si l'element a des enfants, les parcourir egalement
        if hasattr(element, 'children'):
            for child in element.children:
                traverse_dom(child, level+1)
#commencer le parcours depuis la racine de l'arbre DOM
traverse_dom(soup)