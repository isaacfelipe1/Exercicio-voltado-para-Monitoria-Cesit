#Tuplas são imutavel
#Listas podem ser trocados valores, mas adicionar só através
#do append()

num=[1,2,3,4]
num[2]=9 # eu só não posso em lista adicionar valores desta forma, utilizar-se o append()
num.append(3)
num.sort(reverse=True)
print(num)

valores=[]
valores.append(5)
valores.append(6)
valores.append(9)

for v in valores:
    print(f'{v}...')