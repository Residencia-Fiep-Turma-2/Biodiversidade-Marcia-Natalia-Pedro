import pandas as pd
import numpy as np

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
    
    
    def nivel(self): # digita especie e volta categoria de ameaça
        self.file['Especie'] = self.file['Especie'].astype(str)
        especie1 = self.file["Especie"].str.split(" ", n = 1, expand = True)
        self.file["First Especie"] = especie1[0]
        self.file["Second Especie"] = especie1[1]
        #print(self.file['Especie'])

        especie = input("Digite a especie: ")
        #if especie == self.file['First Especie']:
         #   categoria = self.file.loc[self.file['First Especie'], 'Categoria de Ameaca']
          #  print(categoria)
        categoria = self.file.loc[(self.file['Especie'] == especie) | (self.file['First Especie'] == especie) | (self.file["Second Especie"] == especie), 'Categoria de Ameaca']
        #categoria = self.file.loc[np.logical_or(self.file['Especie'], self.file['First Especie'], self.file["Second Especie"]) == especie, 'Categoria de Ameaca']
        print(categoria)
     
        
        

obj = PandasFiltros()
obj.NumIndiv()
obj.NumOccor()
obj.nivel()

