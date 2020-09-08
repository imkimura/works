import sys
import math
import numpy as np

class Seidel:
    def __init__(self, exercise, error):
        self.exercise = exercise
        self.error = error
        self.start()

    def start(self):
        if self.verifyLines(self.exercise):
            self.seidel(self.exercise)
        else:     
            if self.verifyColumns(self.exercise):
                self.seidel(self.exercise)
            else:
                if self.verifySassenfield(self.exercise):
                    self.seidel(self.exercise)
                else:
                    print('Não da Convergência')

    def verifyLines(self, matrix):
        
        for line, countLines in zip(matrix, range(len(matrix))):
            for number, countColums in zip(line, range(len(line))):
                sums = 0
                if countLines == countColums:
                    for countColumsLine in range(len(line)-1):                 

                        if countColums != countColumsLine:
                            sums += line[countColumsLine]
                                    
                    if (sums / number) >= 1:
                        return False                
                    break                
        return True

    def verifyColumns(self, matrix):    
        for countColumns in range(len(matrix[0]) -1):
            sums = 0
            for countLines in range(len(matrix)):
                if countLines != countColumns:
                    sums += matrix[countLines][countColumns]
                else:
                    div = matrix[countLines][countLines]
            
            if (sums / div) >= 1:
                return False
        
        return True
        

    def verifySassenfield(self, matrix):
        newValueOfMultiplier = []
        countMultiplier = 0
        
        for countLines in range(len(matrix)):
            newValueOfMultiplier.append(1)

        for countLines in range(len(self.exercise)):
            sums = 0

            for countColumns in range(len(self.exercise[0])-1):
            
                if countLines != countColumns:        
                    sums += (self.exercise[countLines][countColumns] * newValueOfMultiplier[countColumns])
                    
                else:
                    divisor = self.exercise[countLines][countColumns]
            
            division = sums/divisor
            
            if division >= 1:
                return False
            else:        
                if countLines != (len(self.exercise)-1):
                    newValueOfMultiplier[countMultiplier] = division

                countMultiplier+=1
        
        return True

    def verifyStop(self, tableErrorVerify):
        
        for count in range(len(tableErrorVerify)):                
            if tableErrorVerify[count] > self.error:
                return False

        return True           


    def seidel(self, matrix):
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
                    
            tableValues, tableErrorVerify = self.seidelEquation(tableValues, equacao)    
        
            if(self.verifyStop(tableErrorVerify)):
                validator = False       

        print(f' Tabela Final - {tableValues}') 

        return True


    def seidelEquation(self, tableValues, equation):
        oldTableValues = tableValues[:]
        tableErrorVerify = []        

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