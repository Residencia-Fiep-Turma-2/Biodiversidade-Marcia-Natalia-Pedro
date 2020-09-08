import pandas as pd

class PandasFiltros:
    
    def __init__(self):
        self.path = input("Digite o caminho do arquivo: ")
        self.file = pd.read_csv(self.path)

    def teste(self):
        sigla = input("Digite a sigla do estado: ")
        print (self.file[['Estado/Provincia']])

obj = PandasFiltros()
obj.teste()