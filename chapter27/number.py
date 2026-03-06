class Number:

    def __init__(self,value):
        self.value = value
    def __add__(self, other):
        return Number(self.value + other.value) 
        