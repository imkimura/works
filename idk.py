class Node:
    def __init__(self, base=None):

        if base is not None:
            self.pai = base    
            self.custo = base.custo + 1
            self.profundidade = base.profundidade + 1
            self.state = [None] * 9
            for i in range(9):
                self.state[i] = base.state[i]
        else:
            self.pai = self    
            self.custo = 0
            self.profundidade = 0
            self.state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    def __str__(self):
        
        print(f'{self.pai.state} {self.custo} {self.profundidade}')
        
        
        print('------------')
        
        for i in range(0, 9):
            print(self.state[i])

            if ((i+1)%3 == 0):
                print('\n')
            
            print('------------')

    
    def printNode(self):
        
        if self.pai is not None:
            print(self.pai)

        for i in range(0, 9):
            print(self.state[i])

            if ((i+1)%3 == 0):
                print('\n')
            
            print('------------')

class Busca:
    def testeObjetivo(self, base):
        return False
    
    def sucessor(self, base, lista):
        print('Logica aq')


if __name__ == '__main__':

    n = Node()

    n.printNode()

    j = Node(n)

    j.printNode()





    
