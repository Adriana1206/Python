#Legge la stringa all'interno di un loop 
#se la stringa è uguale a stop il programma si interrompe
#in caso contrario verifica se la stringa è palindroma

print("Inserisci una stringa per verificare se è palindroma")
w = input()

while w!="stop":
    is_palindrome = True

    w_len = len(w)
    for i in range(w_len):
        j = w_len-1-i
        if w[i]!=w[j]:
            is_palindrome = False
            break

    if is_palindrome:
        print("la stringa",w ,"è palindorma")
    else:
        print("la stringa",w ,"non è palindorma")


    w = input()