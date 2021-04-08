import numpy as np
import math as m


class Matriz:
  def __init__ (self, matriz):    
    self.matriz = np.array(matriz)
    self.printMatriz()
  
  def printMatriz(self):
    for m in self.matriz:
      print(m)
    print('')
  
  def translacao(self, x, y, matrizp=None):
    if matrizp is None:
      matrizp = self.matriz

    trans = np.array([
      [1, 0, 0],
      [0, 1, 0],
      [x, y, 1]
    ])

    return matrizp.dot(trans)
    
  def escalonamento(self, x, y, matrizp=None):
    if matrizp is None:
      matrizp = self.matriz

    esc = np.array([
      [x, 0, 0],
      [0, y, 0],
      [0, 0, 1]
    ])

    return matrizp.dot(esc)

  def rotacao(self, x, y, g, matrizp=None):
    if matrizp is None:
      matrizp = self.matriz

    rot = np.array([
      [m.cos(g), -m.sin(g), 0],
      [m.sin(g), m.cos(g), 0],
      [1, 1, 0]
    ])

    matrizp = self.translacao(-x, -y)
    matrizp = matrizp.dot(rot)
    matrizp = self.translacao(x, y, matrizp=matrizp)
    
    return matrizp       
      