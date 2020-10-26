from busca import Busca
from node import Node      


if __name__ == '__main__':

    state = [5, 1, 3, 
             0, 2, 6, 
             4, 7, 8]
    
    n = Node(state=state)

    n.printNo()

    b = Busca()

    # resp = b.buscaLargura(n)
    resp = b.buscaCustoUniforme(n)

    print('\n ----------------- Final ----------------------')

    resp.printNo()