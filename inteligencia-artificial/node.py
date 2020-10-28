from queue import Queue 


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

    def getCusto(self):
        return self.custo 

    def printNo(self):

        print('')
        for i in range(0, 16):
            print(self.state[i], end=" ")

            if ((i+1)%4 == 0):
                print('')

            if ((i+1)%16 == 0):

                if self.acao is not None:
                    print('\n\n------------')
                    print('Custo - {} | Profundidade - {} | Ação - {}' .format(self.custo, self.profundidade, self.acao))
                    print('------------')
                else:
                    print('------------')
                    print('Custo - {} | Profundidade - {}' .format(self.custo, self.profundidade))
                    print('------------')

    def printResult(self):        
        pai = self.pai
        while (pai):
            pai.printNo()
            pai = pai.pai
