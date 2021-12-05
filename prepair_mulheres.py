import pandas as pd

from files import get_file


def prepair_mulheres(year, type):
    try:
        typeParams = {
            '4049': {'name': 'Mulheres 40 a 49', 'file': 'mu4049'},
            '5059': {'name': 'Mulheres 50 a 59', 'file': 'mu5059'},
            '5069': {'name': 'Mulheres 50 a 69', 'file': 'mu5069'},
        }
        file = get_file(typeParams[type]['file'])
        mulhr = pd.read_csv(file, sep=',', header=5,
                            nrows=417, encoding='utf8')
        mulhr['Munic�pio'] = mulhr["Munic�pio"].str.slice(0, 6)
        mulhr = mulhr.rename(columns={'Munic�pio': "Mun.Cod."})
        mulhr = mulhr[["Mun.Cod.", year]]
        mulhr = mulhr.replace({'-': 0})
        mulhr[year] = pd.to_numeric(mulhr[year])
        mulhr = mulhr.rename(
            columns={year: typeParams[type]['name']})
        mulhr = mulhr.set_index('Mun.Cod.')
        print('-> The File '+file+' was prepared.')
        return mulhr
    except:
        input('-> csv could not be prepared.')
        exit()
