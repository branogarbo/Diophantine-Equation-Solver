from random import randint
from time import time

def find():
  workingcombos = []

  start = time()

  while time() - start < 60:
    a = randint(-200,200)
    b = randint(-200,200)
    c = randint(-200,200)

    rancombo = [a,b,c]
    rancombo.sort()

    equation = a**3 + b**3 +c**3 == 2

    if equation and rancombo not in workingcombos:
      workingcombos.append(rancombo)
      print(rancombo, len(workingcombos))

find()
