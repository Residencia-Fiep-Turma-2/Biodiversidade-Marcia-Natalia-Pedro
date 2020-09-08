import pandas as pd

class PandasFiltros:
    
    def __init__(self):
        self.path = input("Digite o caminho do arquivo: ")
        self.file = pd.read_csv(self.path, sep=";")

    def teste(self):
        sigla = input("Digite a sigla do estado: ").upper()
        numero = self.file.loc[self.file['Estado/Provincia'] == sigla, 'Numero de individuos'].sum()
        print ("Número de indivíduos em", sigla, ":", numero)
        
        #for line in sigla_estados:
         #   print (self.file.sum('Numero de individuos'))
        #print(sigla_estados)
            #print (result)
        #print (self.file[['Estado/Provincia'] == 'SP'])
obj = PandasFiltros()
obj.teste()