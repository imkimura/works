class Helper:

    @staticmethod
    def move(lista, original, final):
        aux = lista[final]

        lista[final] = lista[original]

        lista[original] = aux

        return lista