import os
import time

os.system("cls || clear")

opcao = int(input("2 reais ou um presente misterioso?: "))

match(opcao):
    case 1:
        print("2 reais")
        time.sleep(0.5)
        print("Pobre miserável")
    case 2: 
        print("Um presente misterioso")