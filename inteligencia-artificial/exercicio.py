from queue import Queue 

class Node:
    def __init__(self, state=None, base=None):

        if base is not None:
            self.pai = base    
            self.custo = base.custo + 1
            self.profundidade = base.profundidade + 1
            self.state = [None] * 9
            for i in range(9):
                self.state[i] = base.state[i]
        else:
            self.pai = None    
            self.custo = 0
            self.profundidade = 0
            self.state = state[:]
    
    # def __str__(self):
        
    #     print(f'{self.custo} {self.profundidade}')

    
    
    def printNode(self):
        
        # if self.pai is not None:
        #     print(self.pai, end="")
        
        print('')
        for i in range(0, 9):
            print(self.state[i], end=" ")

            if ((i+1)%3 == 0):
                print('')
            
            if ((i+1)%9 == 0):
                print('------------')
                print('Custo - {} | Profundidade - {}' .format(self.custo, self.profundidade))
                print('------------')

def move(self, listOrd, original_index, final_index):
    listOrd.insert(final_index, listOrd.pop(original_index))
    return listOrd

class Busca:
    def __init__(self):
        self.fila = Queue() 
        self.file = []
        self.objetivo = [5, 1, 3, 
                         0, 2, 6, 
                         4, 7, 8]
    
    def testeObjetivo(self, base):
        if base.state == self.objetivo:
            return True
        else:
            return False
    
    def getFile(self):
        first = self.file[0]
        self.file.remove(first)
        return first

    def sucessor(self, base):
        print('Logica aq')

        
    
    def buscaLargura(self, raiz):
        self.file.append(raiz)        

        while(len(self.file) > 0):
            node = Node(base=self.getFile())
            print(node)
            if self.testeObjetivo(node):
                print(node)
                return node
            else:
                self.sucessor(node)



if __name__ == '__main__':

    state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    n = Node(state=state)

    n.printNode()

    b = Busca()

    resp = b.buscaLargura(n)





    
