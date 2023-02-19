def fattoriale_due(numero):
    index = 2
    risultato = 1
    
    while (index <= numero):
        risultato = risultato * index
        index += 1
    
    return risultato


def fattoriale_uno(numero):
    index = numero
    risultato = 1
    while (index > 1):
        risultato *= index
        index -= 1
    
    return risultato

def main():
    print(fattoriale_uno(0))

main()