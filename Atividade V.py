import os
import time

os.system("cls || clear")

opcao = int(input("Digite (1 para 2 reais) ou (2 para um presente misterioso): "))

match(opcao):
    case 1:
        print("\nVocê quer 2 reais?")
        time.sleep(0.5)
        print("\nPobre miserável...")
    case 2: 
        print("\nVocê quer um presente misterioso?")
        time.sleep(0.8)
        print("\nVai ficar sem nada :)")