class Helper:

    @staticmethod
    def move(lista, original, final):
        aux = lista[final]

        lista[final] = lista[original]

        lista[original] = aux

        return lista
         
    @staticmethod
    def getDistanceFromRightPart(indexWrong, indexRight):
        
        lineWrong = indexWrong//4
        columnWrong = indexWrong%4
        
        lineRight = indexRight//4
        columnRight = indexRight%4
        
        line = abs(lineRight - lineWrong)
        column = abs(columnRight - columnWrong)
        
        distanceFromRight = line + column                        
        
        return distanceFromRight
        