numeros = []
soma = 0
q= int(input("quantas provas deseja somar : "))
for i in range(q):
    numero = int(input(f"digite a nota de todas as {q} notas para fazer a media {i+1} : "))
    numeros.append(numero)
    soma += numeros[i] 
media = soma/q
print(media)