from busca import Busca
from node import Node      


if __name__ == '__main__':
    
    state = [1,  2,  0,  8,
            5,  6, 12,  3,
            9, 10,  4, 15,
            13, 14,  7, 11]
    
    n = Node(state=state)

    n.printNo()

    b = Busca()

    # resp, nosGerados = b.buscaAprofIterativo(n) # IDS
    # resp, nosGerados = b.buscaGulosaME(n, 0) # GME H1
    # resp, nosGerados = b.buscaGulosaME(n, 1) # GME H2
    # resp, nosGerados = b.buscaAplus(n, 0) # A* H1
    resp, nosGerados = b.buscaAplus(n,1) # A* H2

    print('\n ----------------- Final ----------------------')

    resp.printResult()
    
    print(f'\n\nTotal de nós gerados igual a : {nosGerados}')