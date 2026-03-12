class Combust(Exception): pass

def makePizza():
    raise Combust()

try:
    makePizza()
except Combust:
    print('got exception')