#listas

lista1=['huevos','leche','carne','jugo']
print(lista1)
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[3])

lista1[0]='cereal'
print(lista1)
print(len(lista1))

for elemento in lista1:
    print('elemento:',elemento)

lista1.append('caguama')
print(lista1)
lista1.insert(1,'chettos')
print(lista1)

lista1.remove('leche')
print(lista1)

elemento=lista1.pop(0)
print('saque:',elemento)

lista1.reverse()
print(lista1)

lista1.sort()
print(lista1)