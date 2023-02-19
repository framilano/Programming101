
def decuplica(numero):
    return numero * 10

## Esercizio: Devi ciclare 10 volte un numero
def esercizio_uno():
    numero = 1
    index = 0
    while (index < 10):
        numero = decuplica(numero)
        index = index + 1

    print(numero)

def is_multiplo_di_sette(numero_da_controllare):
    if (numero_da_controllare % 7 == 0): 
        return True
    return False

## Esercizio due, Fare 100 cicli, stampare solamente gli indici multipli di 7
def esercizio_due():
    indice = 0

    while (indice < 100):
        if (is_multiplo_di_sette(indice) == False):
            indice += 1
            continue

        print(indice)
        indice += 1

def esercizio_tre():
    number = 100
    indice = 0

    while (indice < 100):
        print(number - indice)
        indice += 1

def main():
    #esercizio_uno()
    esercizio_due()
main()