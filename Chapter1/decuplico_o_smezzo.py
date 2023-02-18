# Scrivete una funzione che preso in ingresso un numero:
# Se pari, allora lo decuplica altrimenti lo smezza 

# Decuplica un numero e lo restituisce
def decuplica(numero_da_decuplicare):
    return numero_da_decuplicare * 10

# Smezza un numero e lo restituisce
def smezza(numero_da_smezzare):
    return numero_da_smezzare / 2

# Prende un numero, se pari lo decuplica altrimenti lo smezza, infine lo restituisce
def esercizio(numero):
    risultato = 0

    if (numero % 2 == 0):
        risultato = decuplica(numero)
    
    if(numero % 2 != 0):
        risultato = smezza(numero)

    return risultato

def main():
   x = 30
   risultato = esercizio(x)
   print(risultato)

    
main()