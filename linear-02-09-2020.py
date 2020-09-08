import sys
import math
import numpy as np


'''
10 * x1 + 2 * x2 + 1 * x3 = 7
1 * x1 + 5 * x2 + 1 * x3 = 6
2 * x1 + 3 * x2 + 10 * x3 = 0

[[10, 2, 1, 7],
[1, 5, 1, 6],
[2, 3, 10, None]]

5 * x1 + 1 * x2 + 1 * x3 = 5
3 * x1 + 4 * x2 + 1 * x3 = 6
3 * x1 + 3 * x2 + 6 * x3 = 0
   
   0 1 2
0 [0 0 0]
1 [0 0 0]
2 [0 0 0]

'''
       
def verifyLines(matrix):
    
    for i, y in zip(matrix, range(len(matrix))):
        for j, z in zip(i, range(len(i))):
            soma = 0
            if y == z:
                for n in range(len(i)-1):                 

                    if z != n:
                        soma += i[n]
                                
                if (soma / j) >= 1:
                    return False
                
                break
                
    return True

def verifyColumns(matrix):    
    for i in range(len(matrix[0]) -1):
        soma = 0

        for j in range(len(matrix)):
            if j != i:
                soma += matrix[j][i]
            else:
                div = matrix[j][j]
        
        if (soma / div) >= 1:
            return False
    
    return True
    

def verifySassenfield(matrix):
    aux = []
    count = 0
    
    for x in range(len(matrix)):
        aux.append(1)

    for i in range(len(exercise)):
        soma = 0

        for j in range(len(exercise[0])-1):
          
            if i != j:        
                soma += (exercise[i][j] * aux[j])
                
            else:
                div = exercise[i][j]
        
        divisao = soma/div
        
        if divisao >= 1:
            return False
        else:        
            if i != (len(exercise)-1):
                aux[count] = divisao

            count+=1
    
    return True

def verifyStop(tableErrorVerify):
    error = 0.0001

    for count in range(len(tableErrorVerify)):                
        if tableErrorVerify[count] > error:
            return False

    return True           


def seidel(matrix):
    equacao = []
    
    for linha, count in zip(matrix, range(len(matrix))):
        soma = []
        for countColunaLinha in range(len(linha)):
            if linha[countColunaLinha] is not None:
                if (countColunaLinha == (len(linha) - 1)):
                    soma.append(linha[countColunaLinha])
                else:                                        
                    
                    if count != countColunaLinha:
                        soma.append(linha[countColunaLinha] * -1)
            else:
                soma.append(None)

        for countSoma in range(len(soma)):
            if soma[countSoma] is not None:
                soma[countSoma] = (1/linha[count]) * soma[countSoma]

        equacao.append(soma)
    
    tableValues = [0 for i in range(len(equacao))]
    tableErrorVerify = [0 for i in range(len(equacao))]

    validator = True
    
    while(validator):
                
        tableValues, tableErrorVerify = seidelEquation(tableValues, equacao)    
    
        if(verifyStop(tableErrorVerify)):
            validator = False       

    print(f' Tabela Final - {tableValues}') 

    return True


def seidelEquation(tableValues, equation):
    oldTableValues = tableValues[:]
    tableErrorVerify = []
    
    print(f'{tableValues} old')

    for i in range(len(equation)):
        linha = 0
        values = tableValues[:]
        values.pop(i)
        
        for j in range(len(equation[0])-1):            
            linha += (equation[i][j] * values[j])
        
        if equation[i][len(equation[0])-1] is not None:
            linha += equation[i][len(equation[0])-1]
        
        tableValues[i] = linha

    for i in range(len(tableValues)):
        tableErrorVerify.append(abs(round(tableValues[i] - oldTableValues[i], 5)))
    
    print(f'{tableValues} new')
    print(f'{tableErrorVerify} - Tabela de Verificação')

    return tableValues, tableErrorVerify


count = 0

exercise = [[10, 2, 1, 7],
            [1, 5, 1, -8],
            [2, 3, 10, 6]]

if verifyLines(exercise):
    seidel(exercise)
else:     
    if verifyColumns(exercise):
        seidel(exercise)
    else:
        if verifySassenfield(exercise):
            seidel(exercise)
        else:
            print('Não da Convergência')