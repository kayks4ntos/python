reposta = 0
lista = []
while True:
    print("1-adicionar um item: ")
    print("2-ver lista: ")
    print("3-remova um item : ")
    print("4-sair: ")
    reposta = int(input("digite o numero: "))
    if reposta == 1:
        r = input("o que deseja add na lista: ")
        r.lower().split()
        lista.append(r)
        print(f"o {r} foi add na lista ")
    elif reposta == 2:
        print(lista)
    elif reposta == 3:
        r = input("digite o nome do item que deseja remover: ")
        r.lower().split()
        lista.remove(r)
        print(lista)
    elif reposta == 4:
        print("saindo.....")
        break
print("fechou")