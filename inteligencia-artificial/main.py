from busca import Busca
from node import Node      


if __name__ == '__main__':

    state = [ 1,  2,  3,  4,
              5,  6,  7,  8,  
              9, 10,  11, 12,
              0, 15, 14, 13]
    
    n = Node(state=state)

    n.printNo()

    b = Busca()

    resp = b.buscaAplus(n, 0)

    print('\n ----------------- Final ----------------------')

    resp.printResult()