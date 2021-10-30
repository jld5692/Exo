#coding:utf-8

import random

ligne = 0
i = 1

while i < 200:
    randVal = random.randbytes(100) ##   randint(0, 9)    
    print(f"{ligne}")
    ligne = str(ligne) + str(randVal)
    i = i + 1    

print("Fin")
