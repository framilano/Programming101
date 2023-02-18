# Negativizza un numero
def negativizza(numero_da_negativizzare):
    if (numero_da_negativizzare < 0):
        print("Già negativo")
        return numero_da_negativizzare

    if (numero_da_negativizzare >= 0):
        return -numero_da_negativizzare

# Positivizza un numero
def positivizza(numero_da_positivizzare):
    if (numero_da_positivizzare < 0):
        return -numero_da_positivizzare

    if (numero_da_positivizzare >= 0):
        print("Già positivo")
        return numero_da_positivizzare

    

def main():

    numero = -10
    numero_di_prova = 15
    
    risultato_di_positivizza = positivizza(numero)
    risultato_di_negativizza = negativizza(numero_di_prova)


    print(f"Il numero originale era {numero}, ma è stato positivizzato in {risultato_di_positivizza}")
    print(f"Il numero originale era {numero_di_prova}, ma è stato negativizzato in {risultato_di_negativizza}")




main()