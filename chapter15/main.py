import sys
# print(dir(sys))
# print(len(dir(sys)))
print(len([x for x in dir(sys) if not x.startswith('__')]))