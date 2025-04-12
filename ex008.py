import random
i = 0
lista = []
for i in range(1,6,1):
    n = input("digite 5 nomes para o sorteo: ")
    lista.append(n)
escolhido = random.choice(lista)
print(f" nome sorteado é {escolhido} parabéns ")