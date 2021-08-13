from setup import *
import time
import random

t00 = time.time()
n = random.randint(0,6)
for id in [InspIds[n]]:
    t0 = time.time()
    pub = Publi(id)
    sub = pub.desc()
    tbls = pub.tabls()
    print(pub)
    t1 = time.time()
    print('made pub in {0} seconds'.format(t1-t0))
print('made all in {0} seconds'.format(t1-t00))
