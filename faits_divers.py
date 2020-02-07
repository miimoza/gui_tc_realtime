import display
import requests
from bs4 import BeautifulSoup

region="ile-de-france"
departement = "val-de-marne"
city = "vitry-sur-seine"


request = "https://faitsdivers365.fr/" + region + "/" + departement + "/" + city + "/"
html_doc = requests.get(request)



soup = BeautifulSoup(html_doc.text, "html.parser")

n = 30
width = 30
n_max = 59

n = display.print_49(n, "="*5 + "[" + ("FAITS DIVERS").center(20) +"]" + "="*4)

posts = soup.find_all('a', {'class': 'mh-thumb-icon'})
dates = soup.find_all('span', {'class': 'mh-meta-date updated'})

for i in range(0,10):
    n = display.print_49(n, '-'*10 + dates[i].text.center(10, '-') + '-'*10)
    n = display.breakline_49(n, width, n_max, posts[i]['title'])
    if n > n_max:
        break;

print(n)
