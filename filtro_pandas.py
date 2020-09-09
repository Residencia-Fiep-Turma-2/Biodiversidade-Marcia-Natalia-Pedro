import pandas as pd

class PandasFiltros:

    def __init__(self):

        self.path = input("Digite o caminho do arquivo: ")
        self.file = pd.read_csv(self.path, sep=";")

    #Filtro que retorna todas as Localidades em que a Categoria de Ameaça é Vulnerável: 
    def localidadesVulneraveis(self):
        
        self.file['localidadesVulneraveis'] = [self.file['Localidade'] for item in self.file['Categoria de Ameaca'] if item == "Vulnerável"]
        
        print("Localidades vulneráveis: \n" + str(self.file['localidadesVulneraveis'].explode().value_counts()))       
        print("Quantidade de localidades vulneráveis:" + str(len(self.file['localidadesVulneraveis'])))
   
obj = PandasFiltros()
obj.localidadesVulneraveis()
