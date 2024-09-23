import os
os.system("cls || clear")

import random

for i in range (6):
    numero = random.randint(0,6)


print(f"Número sorteado: {numero}")


if numero == 5:
    print("Ola!")
else:
    print("Azarada")