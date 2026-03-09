class MixedName:
    data = 'text'
    def __init__(self, value):
        self.data = value
    def display(self):
        print(self.data,MixedName.data)

x = MixedName(1)
y = MixedName(2)
x.display()
y.display()