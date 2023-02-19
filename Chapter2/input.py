def main():
    
    x = input("Inserisci un numero minore di 20: ")
    x = int(x)

    while (x >= 20):
            print("NO! Devi inserire un numero minore di 20")
            x = input("Inserisci un numero minore di 20: ")
            x = int(x)
    
    print("Bravo!")

main()