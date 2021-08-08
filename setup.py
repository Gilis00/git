#!/usr/bin/env python3

from urllib.request import Request, urlopen
import bibtexparser
from bs4 import BeautifulSoup
import yaml

InspIds = ['879315', '1614477', '1426695', '1467230',
           '882098', '1680318', '1426695', '1419652']

def test(func, params):
    try:
        func(*params)
        print('function {0} works with params {1}'.format(func.__name__, *params))
    except: print("function {0} don't works with params {1}".format(func.__name__, *params))


def insptobib(InspId):
    """ Retrieve the contents of a INSPIREhep literature as a string.
    """
    url = Request('https://inspirehep.net/api/literature/'+str(InspId)+
           '?format=bibtex')
    socket = urlopen(url)
    bibstr = socket.read().decode()
    socket.close()
    return bibstr

def propsfrombib(bibstr, prop):
    """return year, collaboration, doi, title or author
    from a bibstring"""
    if prop not in ['year', 'collaboration', 'doi', 'title', 'author']:
        return None
    bibdata = bibtexparser.loads(bibstr)
    propdic = bibdata.entries_dict[list(bibdata.entries_dict.keys())[0]]
    return propdic[prop]

for id in InspIds:
    for prop in ['year', 'collaboration', 'doi', 'title', 'author']:
        print(propsfrombib(insptobib(id), prop))
    print('\n')

#data = yaml.load(my_socket, Loader=yaml.FullLoader)


#a = [,]
#req = Request''("https://www.hepdata.net/record/ins1680318")
#req = Request("https://inspirehep.net/literature/1467230")

#html_page = urlopen(req)
#soup = BeautifulSoup(html_page, 'html.parser')
#links = []
#coisas = []
#for link in soup.findAll('a'):
#    links.append(link.get('href'))
#for coisa in soup.findAll('div_class'):
#    coisas.append(coisa)
#for li in soup.findAll('li'):
#    try:
#        print(li['class'])
        #print(li)
        #print(li.get_text())
        #print(li.get_text().split('\n'))
#    except: pass
#print(soup)
#print(links)
#print(coisas)


