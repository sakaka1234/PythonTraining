from person import Person,Manager
import shelve
bob = Person('Bob Smith') # Re-create objects to be stored
sue = Person('Sue Jones', job='dev', pay=100000)
pat = Manager('Pat Jones', 50000)

db = shelve.open('persondb')
for obj in (bob,sue,pat):
    db[obj.name] = obj
db.close()
