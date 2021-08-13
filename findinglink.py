from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

InspIds = ['879315', '1614477', '1426695', '1467230',
           '882098', '1680318', '1426695', '1419652']

req = Request("https://www.hepdata.net/record/ins1680318")
#req = Request("https://inspirehep.net/literature/1467230")

html_page = urlopen(req)
soup = BeautifulSoup(html_page, 'html.parser')
links = []
coisas = []
for link in soup.findAll('a'):
    links.append(link.get('href'))
for coisa in soup.findAll('div_class'):
    coisas.append(coisa)
for li in soup.findAll('li'):
    try:
        print(li['class'])
        #print(li)
        #print(li.get_text())
        #print(li.get_text().split('\n'))
    except: pass
print(soup)
print(links)
print(coisas)