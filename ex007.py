import random
i = 0
while i in range(4):
    nomes= ["kayk","henrique","arthu","mathues ","devid"]
    escolhido = random.choice(nomes)
    i += 1
    print("são esse o escolhido:")
    if escolhido in nomes:
        print(escolhido)
        nomes.remove(escolhido)


