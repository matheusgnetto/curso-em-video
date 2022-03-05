from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram {num}')
print(f'O maior valor digitado foi {max(num)}')
print(f'O menor valor digitado foi {min(num)}')
