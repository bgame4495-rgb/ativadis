import os
os.system("cls")

preco_total= 0
while True:
    print("""
Codigo \t Prato \t \t valor
1      \t picanha\t 25,00
2      \t Lasanha\t 20,00
3      \t strogonoff\t 18,00
4      \t bife Acebolado\t 15,00
5      \t Pão com ovo \t 5,00 
""")

    codigo = int(input("DIGITEO CODIGO"))
    match codigo:
        case 1:
            print("Picanha")
            preco = 25
        case 2:
            print("Lasanha")
            preco = 20
        case 3: 
            print("Strogonoff")
            preco = 18
        case 4:
            print("Bife Acebolado")
            preco = 15
        case 5:
            print("Pão com ovo")
            preco = 5
        case _:
            print("INVALIDO")
            preco = 0

    preco_total = preco_total +   preco

    mais_pedidos = input("Deseja acrecentar mais? \nUse: S ou N  para responder: ")

    if mais_pedidos == "N":
        break
#Mostrando resultado
print("\n=== Restaurante ===")
print(f"Total a pagar: {preco_total}")

print("fim")
