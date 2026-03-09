import shelve
db = shelve.open('persondb')
print(len(db))
print(list(db.keys()))
pat = db['Pat Jones']
print(pat.lastName())
print(pat)

for key in sorted(db):
    print(key,'=>',db[key])