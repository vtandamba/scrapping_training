import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com")
# on peut faire des post aussi put ..
# print(response)
# retourne 200 donc c'est bon !
# print(response.raise_for_status()) quand il ya des erreures

# recuperer un fichier de google et le mettre dans index.html qui est créer automatiquement
with open("index.html", "w") as f:
    f.write(response.text)
    # .json si on tape sur une api

