import pandas as pd


def prepair_mamo(file, year):
    try:
        mamo = pd.read_csv(file, sep=';')
        mamo = mamo[["Mun.Cod.", year]]
        mamo = mamo.rename(columns={year: "Mamografias"})
        print('-> The File '+file+' was prepared.')
        return mamo
    except:
        input('-> csv could not be prepared.')
        exit()
