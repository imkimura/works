from matriz import Matriz


if __name__ == "__main__":
  
  m = Matriz([[0, 2, 1], [4, 5, 1], [8, 9, 1]])
  
  print('---- Rotação -----')
  print(m.rotacao(1, 1, 60))
  print('')

  print('---- Translação -----')
  print(m.translacao(3, 4))
  print('')
  
  print('---- Escalonamento -----')
  print(m.escalonamento(3, 4))