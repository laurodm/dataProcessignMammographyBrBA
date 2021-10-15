import pandas as pd

from files import get_file


def prepair_mamo(year):
    try:
        file = get_file('mamo')
        mamo = pd.read_csv(file, sep=';')
        mamo = mamo[["Mun.Cod.", year]]
        mamo = mamo.rename(
            columns={year: "Mamografias por local de atendimento"})
        mamo = mamo.set_index('Mun.Cod.')
        print('-> The File '+file+' was prepared.')
        return mamo
    except:
        input('-> csv could not be prepared.')
        exit()
