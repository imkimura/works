import math

x = verifyError = xo = 2
count = 0

def funcao(x):
    # return (2 * (x * x * x)) + (3 * (x * x)) - 2
    return math.exp(x) + (2 ** -x) + (2 * (math.cos(x))) - 6

def funcaoDerivada(x):
    # return (6 * (x * x)) + (6 * x)
    return math.exp(x) - (math.log(2) * (2 ** -x)) - (2 * (math.sin(x)))

while(verifyError > 0.00001):
  
    x = x - (funcao(x) / funcaoDerivada(x))    

    verifyError = abs(x - xo)

    count += 1

    xo = x

    print(f'Iteração {count} | X = {x} | verificador = {verifyError}')

print('')

print(f'Raiz é {x}')


