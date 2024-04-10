#creare una tupla di stringhe e stampare solo le stringhe di lunghezza pari

stringhe = ("anna","marco","luca","edoardo","attilio")

count = 0

for stringa in stringhe:
    if len(stringa) % 2 == 0:
        print(stringa)