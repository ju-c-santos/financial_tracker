import pandas as pd

class Transform:
    def read_archive(arq):
        '''O sistema irá informar todos os arquivos inseridos na pasta input, eles serão lidos e inseridos em uma lista'''
        readed_archives = []
        for a in arq:
            archive = pd.read_csv(a, sep=";")
            readed_archives.append(archive)
        return readed_archives