from node import Node 
from helper import Helper as hp


class Busca:
    def __init__(self):
        self.fila = []
        self.objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    def testeObjetivo(self, base):
        if base.state == self.objetivo:
            return True
        else:
            return False
    
    def pegarPrimeiroNo(self):
        
        firstNo = self.fila[0]
        self.fila.remove(firstNo)
        
        return firstNo

    def sucessor(self, base):

        limiteLadoEsquerdo = [0, 3, 6]
        limiteLadoDireito = [2, 5, 8]

        posicaoNulo = base.state.index(0)
     
        # Cima P - 3
        if (posicaoNulo-3) >= 0:
            andaPraCima = Node(base=base, acao='Cima')

            andaPraCima.state = hp.move(andaPraCima.state, posicaoNulo, (posicaoNulo-3))

            self.fila.append(andaPraCima)     

        # Baixo P + 3
        if (posicaoNulo+3) < len(base.state):
            andaPraBaixo = Node(base=base, acao='Baixo')

            andaPraBaixo.state = hp.move(andaPraBaixo.state, posicaoNulo, (posicaoNulo+3))
            
            self.fila.append(andaPraBaixo)     

        # Left P - 1
        if posicaoNulo not in limiteLadoEsquerdo:
            andaPraEsquerda = Node(base=base, acao='Esquerda')               

            andaPraEsquerda.state = hp.move(andaPraEsquerda.state, posicaoNulo, (posicaoNulo-1))
            
            self.fila.append(andaPraEsquerda)       
        
        # Right P + 1
        if posicaoNulo not in limiteLadoDireito and (posicaoNulo+1) < len(base.state):
            andaPraDireita = Node(base=base, acao='Direita')            

            andaPraDireita.state = hp.move(andaPraDireita.state, posicaoNulo, (posicaoNulo+1))
            
            self.fila.append(andaPraDireita)          
          
    def buscaLargura(self, base):
        self.fila.append(base)        

        count = 0
        # em test -> count != 10 // certo -> len(self.fila) > 0
        while(len(self.fila) > 0):
            
            no = self.pegarPrimeiroNo()
            no.printNo()
            
            if self.testeObjetivo(no):
                no.printNo()
                return no
            else:
                self.sucessor(no)                            
            count += 1