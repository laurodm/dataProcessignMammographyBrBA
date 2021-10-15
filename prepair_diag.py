import pandas as pd

from files import get_file


def prepair_diag(year):
    try:
        file = get_file('diag')
        diag = pd.read_csv(file, sep=';')
        diag = diag[["Mun.Cod.", year]]
        diag = diag.rename(columns={year: "Diagnósticos por loca de moradia"})
        diag = diag.set_index('Mun.Cod.')
        print('-> The File '+file+' was prepared.')
        return diag
    except:
        input('-> csv could not be prepared.')
        exit()
