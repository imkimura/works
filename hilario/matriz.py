from random import randrange as rd

def getMaior(lista):
    numMaior = 0
    numMenor = float('inf')
    for i in range(len(lista)):
        if lista[i] > numMaior:
            numMaior = lista[i]
        if lista[i] < numMenor:
            numMenor = lista[i]

    return numMaior, numMenor

if __name__ == "__main__":

    x = 10
    y = 10

    matriz = [[rd(50) for n in range(y)] for n in range(x)]
    soma = 0

    print('%s %s\n|      JULIA KIMURA SILVA 585890         |%s\n%s\n\n' % (
        ('=' * 41),  
        ('\n|                                        |' * 1), 
        ('\n|                                        |' * 1), 
        ('=' * 41)
    ))

    for i in range(x):
        somaLinha = 0
        for j in range(y):
            print('[ {:^2} ] '.format(matriz[i][j]), end='')
            maior, menor = getMaior(matriz[i])
            somaLinha += matriz[i][j]    
        soma += somaLinha
        print(f'  -> maior: {maior} | menor: {menor} | soma linha: {somaLinha}', end='')
        print('')

    print(f'\nsoma: {soma}\nmedia: {round(soma/(x*y), 2)}')

