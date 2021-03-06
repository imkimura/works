from node import Node 
from helper import Helper as hp


class Busca:
    def __init__(self):
        self.fila = []
        self.objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        self.limite = 0
        self.filaOrd = [[] for y in range(100)]        
    
    def testeObjetivo(self, base):
        if base.state == self.objetivo:
            return True
        else:
            return False

    def addOrd(self, nodeAdd):        
        self.filaOrd[nodeAdd.getCusto()].append(nodeAdd)
    
    def addOrdbyHeuristic(self, nodeAdd, typeH):        
        self.filaOrd[nodeAdd.getHeuristic(typeH)].append(nodeAdd)
        
    def addOrdbyHeuristicCusto(self, nodeAdd, typeH):
        self.filaOrd[nodeAdd.getHeuristicCusto(typeH)].append(nodeAdd)

    def pegarPrimeiroNoOrd(self):
        i = 0
        while(i<100):
            if(len(self.filaOrd[i])!=0):
                firstNo = self.filaOrd[i][0]
                self.filaOrd[i].remove(firstNo)
                return firstNo
            i+=1
        return None

    def pegarPrimeiroNo(self):
        
        firstNo = self.fila[0]
        
        self.fila.remove(firstNo)
        
        return firstNo
    
    def pegarUltimoNo(self):
        
        lastNo = self.fila[len(self.fila)-1]
        
        self.fila.pop()        

        return lastNo

    def sucessor(self, base, typeAdd, typeH=None):
        nosGerados = 0
        limiteLadoEsquerdo = [0, 4, 8, 12]
        limiteLadoDireito  = [3, 7, 11, 15]

        posicaoNulo = base.state.index(0)
     
        # Cima P - 4
        if (posicaoNulo-4) >= 0:
            andaPraCima = Node(base=base, acao='Cima')

            andaPraCima.state = hp.move(andaPraCima.state, posicaoNulo, (posicaoNulo-4))
            nosGerados += 1
            if typeAdd == 1:                
                self.fila.append(andaPraCima)
            elif typeAdd == 2:                    
                self.addOrd(andaPraCima)
            elif typeAdd == 3:
                self.addOrdbyHeuristic(andaPraCima, typeH)
            else:
                self.addOrdbyHeuristicCusto(andaPraCima, typeH)

        # Baixo P + 4
        if (posicaoNulo+4) < len(base.state):
            andaPraBaixo = Node(base=base, acao='Baixo')

            andaPraBaixo.state = hp.move(andaPraBaixo.state, posicaoNulo, (posicaoNulo+4))
            nosGerados += 1
            if typeAdd == 1:                
                self.fila.append(andaPraBaixo)
            elif typeAdd == 2:                    
                self.addOrd(andaPraBaixo)
            elif typeAdd == 3:
                self.addOrdbyHeuristic(andaPraBaixo, typeH)
            else:
                self.addOrdbyHeuristicCusto(andaPraBaixo, typeH)

        # Left P - 1
        if posicaoNulo not in limiteLadoEsquerdo and (posicaoNulo-1) > 0:
            andaPraEsquerda = Node(base=base, acao='Esquerda')               

            andaPraEsquerda.state = hp.move(andaPraEsquerda.state, posicaoNulo, (posicaoNulo-1))
            nosGerados += 1
            if typeAdd == 1:                
                self.fila.append(andaPraEsquerda)
            elif typeAdd == 2:                    
                self.addOrd(andaPraEsquerda)
            elif typeAdd == 3:
                self.addOrdbyHeuristic(andaPraEsquerda, typeH)
            else:
                self.addOrdbyHeuristicCusto(andaPraEsquerda, typeH)
        
        # Right P + 1
        if posicaoNulo not in limiteLadoDireito and (posicaoNulo+1) < len(base.state):
            andaPraDireita = Node(base=base, acao='Direita')            

            andaPraDireita.state = hp.move(andaPraDireita.state, posicaoNulo, (posicaoNulo+1))
            nosGerados += 1
            if typeAdd == 1:                
                self.fila.append(andaPraDireita)
            elif typeAdd == 2:                    
                self.addOrd(andaPraDireita)
            elif typeAdd == 3:
                self.addOrdbyHeuristic(andaPraDireita, typeH)
            else:
                self.addOrdbyHeuristicCusto(andaPraDireita, typeH)
        
        return nosGerados
          
    def buscaLargura(self, base):
        self.fila.append(base)        

        count = 0
        # em test -> count != 10 // certo -> len(self.fila) > 0
        while(len(self.fila) > 0):
            
            no = self.pegarPrimeiroNo()
            # no.printNo()
            
            if self.testeObjetivo(no):
                # no.printNo()
                return no
            else:
                self.sucessor(no, 1)                            
            count += 1
    
    def buscaProfundidade(self, base):
        self.fila.append(base)        

        count = 0
        
        while(len(self.fila) > 0):
            
            no = self.pegarUltimoNo()
            
            no.printNo()
            
            if self.testeObjetivo(no):
                # no.printNo()
                return no
            else:            
                self.sucessor(no, 1)                            
            count += 1

    def buscaProfundidadeLimitada(self, base):        
        nosGerados = 0
        self.fila.append(base)        

        count = 0
        
        while(len(self.fila) > 0):
            
            no = self.pegarUltimoNo()            
            
            if self.testeObjetivo(no):
                return no, nosGerados
            else:                
                if (no.profundidade + 1) < self.limite:
                    nosGerados += self.sucessor(no, 1)                            
            count += 1
        
        print('\n ----------------- Sem Solução ----------------- \n') 

        return None, nosGerados 
    
    def buscaAprofIterativo(self, base):
        r = None
        
        self.limite = 0
        while(True):
            r, nosGerados = self.buscaProfundidadeLimitada(base)
            if r is None:
                self.limite += 1
                print(f'\n\n Limite = {self.limite}')
            else:
                return r, nosGerados
    
    def buscaCustoUniforme(self, base):
        self.addOrd(base)        

        count = 0
        # em test -> count != 10 // certo -> len(self.filaOrd) > 0
        while(len(self.filaOrd) > 0):

            no = self.pegarPrimeiroNoOrd()
            no.printNo()
            
            if self.testeObjetivo(no):
                return no
            else:
                self.sucessor(no, 2)                            
            count += 1
    
    def buscaGulosaME(self, base, typeH):
        if typeH: h = 'H2' 
        else: h = 'H1'
        print('Busca GME %s ...  \n\n' % h)
        self.addOrdbyHeuristic(base,typeH)        
        nosGerados = 0
        count = 0
        
        while(len(self.filaOrd) > 0):

            no = self.pegarPrimeiroNoOrd()
            
            no.printNo()
            if self.testeObjetivo(no):
                return no, nosGerados
            else:
                nosGerados += self.sucessor(no, 3, typeH)                            
            count += 1
    
    def buscaAplus(self, base, typeH):
        if typeH: h = 'H2' 
        else: h = 'H1'
        print('Busca A* %s ...  \n\n' % h)
        self.addOrdbyHeuristicCusto(base, typeH)        
        nosGerados = 0
        count = 0
        
        while(len(self.filaOrd) > 0):

            no = self.pegarPrimeiroNoOrd()
            if self.testeObjetivo(no):
                return no, nosGerados
            else:
                nosGerados += self.sucessor(no, 4, typeH)                            
            count += 1
                

#  Busca em profundidade - ok
#  Busca em profundidade limitada - ok
#  Busca em aprofundidamento iterativo - ok
#  Busca de custo uniforme - ok