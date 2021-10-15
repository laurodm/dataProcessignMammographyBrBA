import pandas as pd


def prepair_diag(file, year):
    try:
        diag = pd.read_csv(file, sep=';')
        diag = diag[["Mun.Cod.", year]]
        diag = diag.rename(columns={year: "Diagnósticos"})
        print('-> The File '+file+' was prepared.')
        return diag
    except:
        input('-> csv could not be prepared.')
        exit()
