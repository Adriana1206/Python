#lista di tuple 
#stampare le tuple in cui la prima stringa inizia con la lettera a

lista_di_tuple = [("anna","luca"),("marco","edoardo"),("leandro","attilio")]

for tupla in lista_di_tuple:
    if tupla[0][0] == "a":
        print(tupla)