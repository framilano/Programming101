def is_pari(numero):

    result = False

    if (numero % 2 == 0):
        result = True
    
    return result 

def main():
    x = 10
    result = is_pari(x)

    print(result)





main()