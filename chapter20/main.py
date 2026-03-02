import random
squares = [x**2 for x in range(6)]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flat = [x for row in matrix for x in row]
transpose = [[row[i] for row in matrix] for i in range(3)]
lst = [1,2,3,4]
random.shuffle(lst)
scrambled = random.sample(lst, len(lst))
print(lst)
print(scrambled)