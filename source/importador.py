import pandas as pd
from bank.nubank import Nubank

class Transform:
    def choose_bank(arq):
        #função para definir de qual banco se trata o arquivo e formatá-lo.
        pass
    
    def read_archive(arq): #recebe o arquivo formatado de choose_bank
        '''O sistema irá informar todos os arquivos inseridos na pasta input, eles serão lidos e inseridos em uma lista'''
        readed_archives = []
        for a in arq:
            archive = pd.read_csv(a, sep=";")
            readed_archives.append(archive)
        return readed_archives

    def number_formatt():
        pass