from random import randint
from time import time

def find():
  workingcombos = []

  start = time()

  while time() - start < 60:
    a = randint(-200,200)
    b = randint(-200,200)

    rancombo = [a,b]

    rancombo.sort()

    if a**2 + b**2 == 10**2 and rancombo not in workingcombos:
      workingcombos.append(rancombo)
      print(rancombo, len(workingcombos))

find()