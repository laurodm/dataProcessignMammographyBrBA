import pandas as pd

from files import get_file


def prepair_regioes():
    try:
        file = get_file('regioes')
        diag = pd.read_csv(file, sep=';', header=0, encoding='utf-8')
        diag['cod'] = diag['cod'].astype(str)
        diag = diag.rename(columns={'cod': "Mun.Cod."})
        diag = diag[["Mun.Cod.", "Regi?o de sa�de"]]
        diag = diag.set_index('Mun.Cod.')
        print(diag)
        print('-> The File '+file+' was prepared.')
        return diag
    except:
        input('-> csv could not be prepared.')
        exit()
