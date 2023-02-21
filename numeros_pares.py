def pares(numeros):
    numeros_pares = []
    for n in numeros:
        if n % 2 ==0:
            numeros_pares.append(n)
            return numeros_pares
        numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        resultado = pares(numeros)
        print(resultado)