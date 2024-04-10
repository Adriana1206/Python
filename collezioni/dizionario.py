#creare un dizionario in cui le chiavi sono stringhe e i valori sono numeri interi. Stampare solo le coppie chiave-valore in cui il valore è maggiore di 5.

dict = {"chiave1":10,"chiave2":7,"chiave3":5}

for chiave,valore in dict.items():
    if valore > 5:
        print(chiave,valore)

