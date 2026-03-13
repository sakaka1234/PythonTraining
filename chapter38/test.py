class Test:

    def getX(self):
        print("getting")
        return self._x

    def setX(self, value):
        print("setting")
        self._x = value

    x = property(getX, setX)


t = Test()

t.x = 10
print(t.x)

