def is_pari(numero):
    if (numero % 2 == 0): return True
    
    return False

def esempio_continue():
    print("INIZIO ESEMPIO CONTINUE")

    frase = "Ciao capo!"
    index = 0

    while (index < 10):
        
        if (is_pari(index) == True): 
            index = index + 1
            continue

        print(f"{index}: {frase}")
        index = index+1
    
    print("FINE ESEMPIO CONTINUE")


def esempio_break():
    print("INIZIO ESEMPIO BREAK")
    frase = "Ciao capo!"
    index = 0

    while (True):
        
        if (index == 10): break
        print(f"{index}: {frase}")

        index = index+1
    
    print("FINE ESEMPIO BREAK")


def main():
    esempio_continue()
    esempio_break()



main()