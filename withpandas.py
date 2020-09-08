import pandas as pd

class PandasFiltros:
    
    def __init__(self):
        self.path = input("Digite o caminho do arquivo: ")
        self.file = pd.read_csv(self.path, sep=";")

<<<<<<< HEAD
    def NumIndiv(self):  #Filtra o numero de indivíduos no estado indicado
        sigla = input("Digite a sigla do estado: ").upper()
        numero = self.file.loc[self.file['Estado/Provincia'] == sigla, 'Numero de individuos'].sum()
        print ("Número de indivíduos em", sigla, ":", numero)

    def NumOccor(self):  #Filtra o numero de ocorrências no estado indicado
        sigla = input("Digite a sigla do estado: ").upper()
        count = self.file[self.file['Estado/Provincia'] == sigla]
        print ("Número de ocorrências em", sigla, ":", len(count))
        
        
=======
    def teste(self):
        sigla = input("Digite a sigla do estado: ").upper()
        numero = self.file.loc[self.file['Estado/Provincia'] == sigla, 'Numero de individuos'].sum()
        print ("Número de indivíduos em", sigla, ":", numero)
        
        #for line in sigla_estados:
         #   print (self.file.sum('Numero de individuos'))
        #print(sigla_estados)
            #print (result)
        #print (self.file[['Estado/Provincia'] == 'SP'])
>>>>>>> 670f8f654aca6b704f781f9105120e1c09d99a4d
obj = PandasFiltros()
obj.NumIndiv()
obj.NumOccor()