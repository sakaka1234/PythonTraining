from employees import PizzaRobot, Server    
class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, 'orders from', server)
    def pay(self, server):
        print(self.name, 'pays for item to', server)
class Oven:
    def bake(self):
        print('oven bakes')
class PizzaShop:
    def __init__(self):
        self.server = Server('Jan')         
        self.chef   = PizzaRobot('Pat')     
        self.oven   = Oven()
    def order(self, name):
        customer = Customer(name)           
        customer.order(self.server)         
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)
if __name__ == '__main__':
    scene = PizzaShop()                     
    scene.order('Sue')                      
    print('...')
    scene.order('Bob')                      
# Embed other objects
# A robot named Pat
# Activate other objects
# Customer orders from server
# Make the composite
# Simulate Sue's order
# Simulate Bob's order