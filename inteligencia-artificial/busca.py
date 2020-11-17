from node import Node 
from helper import Helper as hp


class Busca:
    def __init__(self):
        self.fila = []
        self.objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        self.limite = 0
        self.filaOrd = []
    
    def testeObjetivo(self, base):
        if base.state == self.objetivo:
            return True
        else:
            return False

    def addOrd(self, nodeAdd):
        for chave, node in enumerate(self.filaOrd):
            if nodeAdd.getCusto() < node.getCusto():
                self.filaOrd.insert(chave, nodeAdd)
                break
        else:
            self.filaOrd.append(nodeAdd)
    
    def addOrdbyHeuristic(self, nodeAdd, typeH):
        for chave, node in enumerate(self.filaOrd):
            if nodeAdd.getHeuristic(typeH) < node.getHeuristic(typeH):
                self.filaOrd.insert(chave, nodeAdd)
                break
        else:
            self.filaOrd.append(nodeAdd)
   
    def addOrdbyHeuristicCusto(self, nodeAdd, typeH):
        for chave, node in enumerate(self.filaOrd):
            if nodeAdd.getHeuristicCusto(typeH) < node.getHeuristicCusto(typeH):
                self.filaOrd.insert(chave, nodeAdd)
                break
        else:
            self.filaOrd.append(nodeAdd)

    def pegarPrimeiroNo(self):
        
        firstNo = self.fila[0]
        
        self.fila.remove(firstNo)
        
        return firstNo
    
    def pegarPrimeiroNoOrd(self):
        
        firstNo = self.filaOrd[0]
        
        self.filaOrd.remove(firstNo)
        
        return firstNo

    def pegarUltimoNo(self):
        
        lastNo = self.fila[len(self.fila)-1]
        
        self.fila.pop()        

        return lastNo

    def sucessor(self, base):

        limiteLadoEsquerdo = [0, 4, 8, 12]
        limiteLadoDireito  = [3, 7, 11, 15]

        posicaoNulo = base.state.index(0)
     
        # Cima P - 4
        if (posicaoNulo-4) >= 0:
            andaPraCima = Node(base=base, acao='Cima')

            andaPraCima.state = hp.move(andaPraCima.state, posicaoNulo, (posicaoNulo-4))

            self.fila.append(andaPraCima)     
            self.addOrd(andaPraCima)

        # Baixo P + 4
        if (posicaoNulo+4) < len(base.state):
            andaPraBaixo = Node(base=base, acao='Baixo')

            andaPraBaixo.state = hp.move(andaPraBaixo.state, posicaoNulo, (posicaoNulo+4))
            
            self.fila.append(andaPraBaixo)     
            self.addOrd(andaPraBaixo)

        # Left P - 1
        if posicaoNulo not in limiteLadoEsquerdo and (posicaoNulo-1) > 0:
            andaPraEsquerda = Node(base=base, acao='Esquerda')               

            andaPraEsquerda.state = hp.move(andaPraEsquerda.state, posicaoNulo, (posicaoNulo-1))
            
            self.fila.append(andaPraEsquerda)       
            self.addOrd(andaPraEsquerda)
        
        # Right P + 1
        if posicaoNulo not in limiteLadoDireito and (posicaoNulo+1) < len(base.state):
            andaPraDireita = Node(base=base, acao='Direita')            

            andaPraDireita.state = hp.move(andaPraDireita.state, posicaoNulo, (posicaoNulo+1))
            
            self.fila.append(andaPraDireita)          
            self.addOrd(andaPraDireita)
          
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
                self.sucessor(no)                            
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
                self.sucessor(no)                            
            count += 1

    def buscaProfundidadeLimitada(self, base):        

        self.fila.append(base)        

        count = 0
        
        while(len(self.fila) > 0):
            
            no = self.pegarUltimoNo()            
            
            if self.testeObjetivo(no):
                return no
            else:                
                if (no.profundidade + 1) < self.limite:
                    self.sucessor(no)                            
            count += 1
        
        print('\n ----------------- Sem Solução ----------------- \n') 

        return None 
    
    def buscaAprofIterativo(self, base):
        r = None
        self.limite = 0
        while(True):
            r = self.buscaProfundidadeLimitada(base)
            if r is None:
                self.limite += 1
                print(f'\n\n Limite = {self.limite}')
            else:
                return r
    
    def buscaCustoUniforme(self, base):
        self.addOrd(base)        

        count = 0
        # em test -> count != 10 // certo -> len(self.filaOrd) > 0
        while(len(self.filaOrd) > 0):

            no = self.pegarPrimeiroNoOrd()
            no.printNo()
            
            if self.testeObjetivo(no):
                no.printNo()
                return no
            else:
                self.sucessor(no)                            
            count += 1
    
    def buscaGulosaME(self, base, typeH):
        self.addOrdbyHeuristic(base,typeH)        

        count = 0
        
        while(len(self.filaOrd) > 0):

            no = self.pegarPrimeiroNoOrd()
            no.printNo()
            
            if self.testeObjetivo(no):
                no.printNo()
                return no
            else:
                self.sucessor(no)                            
            count += 1
    
    def buscaAplus(self, base, typeH):
        self.addOrdbyHeuristicCusto(base, typeH)        

        count = 0
        
        while(len(self.filaOrd) > 0):

            no = self.pegarPrimeiroNoOrd()
            no.printNo()
            
            if self.testeObjetivo(no):
                no.printNo()
                return no
            else:
                self.sucessor(no)                            
            count += 1

#  Busca em profundidade - ok
#  Busca em profundidade limitada - ok
#  Busca em aprofundidamento iterativo - ok
#  Busca de custo uniforme - ok