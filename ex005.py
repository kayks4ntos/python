while True:
    n = input("digite um nome para cadastrar: ")
    s = input("digite um senha para cadastra: ")
    nome = []
    senha = []
    nome.append(n)
    senha.append(s)
    login = nome + senha
    nm=[]
    ss=[]
    nm= input("coloque seu nome ")
    ss = input("coloque sua senha ")
    nm=[]
    ss=[]
    k = nm + ss
    print(login)
    print(nm)
    print(k)
    if login == k:
        print("deu certo ")
    else:
        print("deu erraado")
    