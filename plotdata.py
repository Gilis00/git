import sys
sys.path.insert(1, '/home/juni/git')
from setup import *
import time
import random

a = 23

t00 = time.time()
n = random.randint(0,6)
for id in InspIds:
    t0 = time.time()
    pub = Publi(id)
    sub = pub.desc()
    tbls = pub.tabls()
    nestedextract(sub, 'comment')
    nestedextract(tbls[list(tbls.keys())[-1]], 'name', 'units', 'value', 'high', 'low')
    #nestedprint(sub[0])
    nestedprint(tbls[list(tbls.keys())[-1]])
    t1 = time.time()
    #print('made pub in {0} seconds'.format(t1-t0))
    #print('\n')
#print('made pub in {0} seconds'.format(t1-t00))