m = 0
while m <6:
    lista = [1,2,3,4,5]
    print(lista)
    n = int(input("digite um numero para vc remover: "))
    if n < 6:
        r = n -1
        lista.pop(r)
        print(lista)
    else:
        print("digite o numero certo")
