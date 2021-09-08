##5. Crie um programa que incrementa todos os números em uma frase.##

def split(word):
    return [char for char in word]

word = 'ABCDEFGHIJ'
lst1 = split(word)

lst2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(''.join([str(a) + b for a, b in zip(lst2, lst1)]))
# print(' '.join([str(a) + b for a, b in zip(lst2, lst1)]))