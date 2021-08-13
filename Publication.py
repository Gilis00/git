'''define a class wich corresponds to a publication of an especified inspire hep id'''

from urllib.request import Request, urlopen
import bibtexparser
import zipfile
from io import BytesIO
import yaml

def insptobib(InspId):
    """ Retrieve the BIBTEX of a INSPIREhep literature as a b string."""
    url = Request('https://inspirehep.net/api/literature/'+str(InspId)+
           '?format=bibtex')
    socket = urlopen(url)
    bibstr = socket.read().decode()
    socket.close()
    return bibstr

def propsfrombib(bibstr):
    """return year, collaboration, doi, title or author
    from a bibstring"""
    bibdata = bibtexparser.loads(bibstr)
    propdic = bibdata.entries_dict[list(bibdata.entries_dict.keys())[0]]
    return propdic
    #propdic['year]

def insptodata(InspId):
    url = Request('https://www.hepdata.net/download/submission/ins'+str(InspId)+'/1/original')
    http_resp = urlopen(url)
    zip = zipfile.ZipFile(BytesIO(http_resp.read()))
    subm, tbls = [],{}
    for name in zip.namelist():
        tb = zip.open(name)
        if name[-5:] == '.yaml':
            if name != 'submission.yaml':
                tbls[name] = yaml.load(tb, Loader=yaml.FullLoader)
            else:
                for arq in yaml.load_all(zip.open('submission.yaml'),
                                         Loader=yaml.FullLoader):
                    subm.append(arq)
    return subm, tbls

def nestedprint(it, count=0):
    size = '       '
    space = count*size
    if type(it) == type([]):
        for sub in it:
            nestedprint(sub, count)
    elif type(it) == type({}):
        for (k, v) in it.items():
            if (type(v)==type([]) and len(v) == 1 and type(v[0]) != type({})) or (type(v) != type([]) and type(v) != type({})):
                print(space+k+'-->'+str(v))
            else:
                print(space+k+':')
                nestedprint(v, count + 1)
    else:
        print(space+it)

def nestedextract(it, *prop):
    if type(it) == type([]):
        for sub in it:
            nestedextract(sub, *prop)
    elif type(it) == type({}):
        for (k, v) in it.items():
            if k in prop:
                print(k+'-->'+str(v))
            else:
                nestedextract(v, *prop)


class Publi:
    ''' Data class represents and manipulates
    a single dataset for multiplicity'''
    def __init__(self, id):
        '''create a data set'''
        self.bib = insptobib(id)
        self.props = propsfrombib(self.bib)
        self.subm, self.tbls = insptodata(id)

    def __str__(self):
        text = ''
        for prop in ['collaboration', 'year', 'title']:
            text += self.props[prop] + '\n'
        return text

    def desc(self):
        return self.subm
    def tabls(self):
        return self.tbls


