import pandas as pd

from files import get_file


def prepair_diag(year):
    try:
        file = get_file('diag')
        diag = pd.read_csv(file, sep=';')
        diag = pd.read_csv(file, sep=';', header=0, encoding='utf8')
        diag['Munic.de residencia'] = diag["Munic.de residencia"].str.slice(
            0, 6)
        diag = diag.rename(columns={'Munic.de residencia': "Mun.Cod."})
        diag = diag[["Mun.Cod.", year]]
        diag = diag.rename(columns={year: "Diagnósticos por local de moradia"})
        diag = diag.set_index('Mun.Cod.')
        diag = diag.drop(index="Total")
        print('-> The File '+file+' was prepared.')
        return diag
    except:
        input('-> csv could not be prepared.')
        exit()
