from busca import Busca
from node import Node      


if __name__ == '__main__':

    # state = [ 1,  2,  3,  4,
    #           5,  6,  7,  8,  
    #           9, 10,  11, 12,
    #           0, 15, 14, 13]
    
    # state = [ 1,  2,  3,  4,
    #           5,  6,  7,  0,  
    #           9, 10,  11, 8,
    #           13, 14, 15, 12]
    
    # state = [1, 2, 3, 4,
    #         5,6,7,8,
    #         9,10,11,12,
    #         13,0,14,15]
    
    state = [1,8,6,3,
            5,2,7,4,
            10,15,14,11,
            9,0,13,12]
    
    n = Node(state=state)

    n.printNo()

    b = Busca()

    resp = b.buscaAplus(n, 1)

    print('\n ----------------- Final ----------------------')

    resp.printResult()