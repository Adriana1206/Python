#set di tuple
#Stampare le tuple in cui la somma dei numeri è pari

set_di_tuple = {(2,2),(3,4),(5,6),(6,8)}

for tupla in set_di_tuple:
    if (tupla[0] + tupla[1]) % 2 == 0:
        print(tupla)
    