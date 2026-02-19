import random

def get_input():
    while True:
        try:
            numero_usuario= int(input("Entre com um número: "))

        except ValueError as err:
            print("Valor inválido")
            continue

        if 1 <= numero_usuario <=15:
            return numero_usuario

        print("Valor Inválido! O valor deve ser entrega 1 e 15")

def check_number(sorteio, usuario):
    if sorteio == usuario:
        print("Parabéns! Você se tornou um milionário de experiência a nada")
        return True

    elif usuario > sorteio:
        print("Numero muito alto. tente um numero menor")
        return False

    else:
        print("Numero muito baixo. Tente um número maior")
        return False

numero_sorteio = random.randint(1,15)

for i in range(3):
        
    numero_usuario = get_input()
    if check_number(sorteio=numero_sorteio, usuario=numero_usuario):
        break

else:
    print("Suas tentativas acabaram!")