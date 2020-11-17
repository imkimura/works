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
    
    state = [1,  2,  3,  4,
 5,  0, 10,  7,
14, 11,  6,  8,
 9, 13, 15, 12]
    
    n = Node(state=state)

    n.printNo()

    b = Busca()

    # resp, nosGerados = b.buscaAprofIterativo(n)
    # resp, nosGerados = b.buscaGulosaME(n, 0)
    resp, nosGerados = b.buscaGulosaME(n, 1)
    # resp, nosGerados = b.buscaAplus(n, 0)
    # resp, nosGerados = b.buscaAplus(n,1)

    print('\n ----------------- Final ----------------------')

    resp.printResult()
    
    print(f'\n\nTotal de nós gerados igual a : {nosGerados}')