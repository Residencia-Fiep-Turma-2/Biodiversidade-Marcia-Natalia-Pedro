import pandas as pd
import numpy as np

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
   
    def nivel(self):
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
#obj.teste()
#gitobj.nivel()