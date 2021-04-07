class Matriz:
  def __init__ (self, matriz):    
    self.matriz = matriz
    self.printMatriz()
  
  def printMatriz(self):
    for m in self.matriz:
      print(m)
    print('')
  
  def rotacao(self):
    list_of_tuples = zip(*self.matriz[::-1])
    self.matriz = [list(elem) for elem in list_of_tuples]
    self.printMatriz()
       
  def translacao(self):
    print('Matriz translacionada')
    
  def escalonamento(self):
    print('Matriz escalonada')
      