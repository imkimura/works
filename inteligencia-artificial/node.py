from queue import Queue 
from helper import Helper as hp


class Node:
    def __init__(self, state=None, base=None, acao=None):        
                                
        if base is not None:
            
            self.pai = base    
            self.custo = base.custo + 1
            self.profundidade = base.profundidade + 1            
            self.state = base.state[:]
            self.acao = acao

        else:
            self.acao = None
            self.pai = None    
            self.custo = 0
            self.profundidade = 0
            self.state = state[:] 
        
        self.h1, self.h2 = self.getHeuristics()

    def getHeuristics(self):
        objetive = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        
        partsOutPlace = 0
        distanceFromRight = 0
        
        for idx, part in enumerate(self.state):
            if (part != objetive[idx]) and (part != 0):
                partsOutPlace += 1
                distanceFromRight += hp.getDistanceFromRightPart(idx, objetive.index(part))                   
        
        return partsOutPlace, distanceFromRight
   
    def getCusto(self):
        return self.custo 

    def getHeuristic(self, typeH):
        if typeH:        
            return self.h2
        else:
            return self.h1
    
    def getHeuristicCusto(self, typeH):
        if typeH:        
            return (self.h2 + self.custo)
        else:
            return (self.h1 + self.custo)

    def printNo(self):

        print('')
        for i in range(0, 16):
            print('{:^3} |'.format(self.state[i]), end=" ")            

            if ((i+1)%4 == 0):
                print('\n______________________')

            if ((i+1)%16 == 0):

                if self.acao is not None:
                    print('\n\n\n ------------')
                    print('Custo - {} | Profundidade - {} | Ação - {} | H1 - {} | H2 - {}' .format(self.custo, self.profundidade, self.acao, self.h1, self.h2))
                    print('------------')
                else:
                    print('------------')
                    print('Custo - {} | Profundidade - {} |  H1 - {} | H2 - {}' .format(self.custo, self.profundidade, self.h1, self.h2))
                    print('------------')

    def printResult(self):        
        pai = self.pai
        self.printNo()
        while (pai):
            pai.printNo()
            pai = pai.pai
