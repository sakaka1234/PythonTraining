from moduleB import *
import mymodule
from math import sqrt as s
import sys

print(sys.modules.keys())

for p in sys.path:
    print(p)
hello()
# bye()

print(mymodule.sa)
print(s(14))
code = """
a = 10
b = 20
print(a + b)
"""

exec(code)