import glob
import os
import pandas as pd
from source.importador import Transform

#estas duas funções servem para chamar todos os arquivos .csv que estão dentro da pasta input em archives
path_archives = "archives/input"
archives = glob.glob(os.path.join(path_archives, '*.csv'))
#pega a lista de arquivos gerada na função read_archive
arc_list = Transform.read_archive(archives)
#junta todos os arquivos que foram lidos
arc_concat = pd.concat(arc_list, ignore_index = True)
print(arc_concat.head())
