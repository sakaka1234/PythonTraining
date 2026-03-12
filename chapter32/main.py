class E:
    __slots__ = ['c', 'd']

    def __init__(self):
        print("E created")


class D(E):
    __slots__ = ['a', '__dict__']

    def __init__(self):
        super().__init__()
        print("D created")


# create instance
I = D()

print("\n--- Assign attributes ---")
I.a = 1
I.c = 3
I.b = 2   # stored in __dict__

print("I.a =", I.a)
print("I.c =", I.c)
print("I.b =", I.b)

print("\n--- Slots info ---")
print("E.__slots__:", E.__slots__)
print("D.__slots__:", D.__slots__)
print("I.__slots__:", I.__slots__)

print("\n--- __dict__ ---")
print(I.__dict__)

print("\n--- dir() output (all attributes) ---")
print([name for name in dir(I) if not name.startswith("_")])

print("\n--- Access via getattr ---")
print("a:", getattr(I, "a"))
print("b:", getattr(I, "b"))
print("c:", getattr(I, "c"))
