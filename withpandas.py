import pandas as pd

class PandasFiltros:
    
    def __init__(self):
        self.path = input("Digite o caminho do arquivo: ")
        self.file = pd.read_csv(self.path, sep=";")

    def NumIndiv(self):  #Filtra o numero de indivíduos no estado indicado
        sigla = input("Digite a sigla do estado: ").upper()
        numero = self.file.loc[self.file['Estado/Provincia'] == sigla, 'Numero de individuos'].sum()
        print ("Número de indivíduos em", sigla, ":", numero)

    def NumOccor(self):  #Filtra o numero de ocorrências no estado indicado
        sigla = input("Digite a sigla do estado: ").upper()
        count = self.file[self.file['Estado/Provincia'] == sigla]
        print ("Número de ocorrências em", sigla, ":", len(count))
        
        
obj = PandasFiltros()
obj.NumIndiv()
obj.NumOccor()