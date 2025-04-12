lista_fruta = ["banana","maça","laranja"]
lista_legumes= ["jilo","brocules","cemoura"]
n = input("digite um legume ou fruta:")
if n in lista_fruta:
    print(f"o {n} esta na lista fruta {lista_fruta}")
elif n in lista_legumes:
    print(f"o {n} esta na lista fruta {lista_legumes}")
else:
    print(f"o {n} não esta na lista ")