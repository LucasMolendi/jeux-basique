import random
from vinyles_list import *

def tirage():
    t = len(liste_vinyles)
    n = random.randint(0,t)
    return liste_vinyles[n]


print(tirage())