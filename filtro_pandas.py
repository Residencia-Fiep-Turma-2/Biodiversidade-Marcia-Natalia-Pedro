import pandas as pd

class PandasFiltros:

    def __init__(self):

        self.path = input("Digite o caminho do arquivo: ")
        self.file = pd.read_csv(self.path, sep=";")

    def localidadesVulneraveis(self):

        self.file['localidadesVulneraveis'] = [self.file['Localidade'] for row in self.file['Categoria de Ameaca']]
        print(self.file['localidadesVulneraveis'])

        
obj = PandasFiltros()
obj.localidadesVulneraveis()
