from busca import Busca
from node import Node      


if __name__ == '__main__':

    state = [ 1,  2,  3,  4,
              5,  6,  7,  8,  
              9, 10,  0, 12,
              11, 13, 14, 15]
    
    n = Node(state=state)

    n.printNo()

    b = Busca()

    resp = b.buscaLargura(n)

    print('\n ----------------- Final ----------------------')

    resp.printResult()