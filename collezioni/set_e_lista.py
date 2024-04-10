#stampare i numeri che sono presenti sia nel set che nella lista

numeri_set = {1,2,3,4,5}
numeri_lista = [3,4,5,6,7]

for numero in numeri_set:
    if numero in numeri_lista:
        print(numero)