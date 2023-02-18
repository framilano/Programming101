def super_decuplicazione(numero):
    return numero * 10

def smezziamo(nuovo_numero):
    return nuovo_numero / 2


def main():

    x = 12

    risultato_parziale = super_decuplicazione(x)

    risultato_finale = smezziamo(risultato_parziale)

    print(risultato_finale)



    
main()