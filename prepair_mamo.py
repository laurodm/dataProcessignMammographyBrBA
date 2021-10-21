import pandas as pd

from files import get_file


def prepair_mamo(year, type):
    try:
        typeParams = {
            'mamoBl': {'name': 'Bilateral', 'file': 'mamoBl'},
            'mamoDg': {'name': 'Diagnóstica', 'file': 'mamoDg'},
        }
        file = get_file(typeParams[type]['file'])
        mamo = pd.read_csv(file, sep=';', header=4, nrows=417, encoding='utf8')
        mamo['Munic�pio'] = mamo["Munic�pio"].str.slice(0, 6)
        mamo = mamo.rename(columns={'Munic�pio': "Mun.Cod."})
        mamo = mamo[["Mun.Cod.", year]]
        mamo = mamo.replace({'-': 0})
        mamo[year] = pd.to_numeric(mamo[year])
        mamo = mamo.rename(
            columns={year: "Mamografia "+typeParams[type]['name']})
        mamo = mamo.set_index('Mun.Cod.')
        print('-> The File '+file+' was prepared.')
        return mamo
    except:
        input('-> csv could not be prepared.')
        exit()
