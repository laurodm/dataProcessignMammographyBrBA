import pandas as pd

from files import get_file


def getColumnByYear(year, columns):
    for equipColumn in columns:
        if year in equipColumn:
            return equipColumn


def prepair_equipment(year):
    try:
        file = get_file('equip')
        equip = pd.read_csv(file, sep=';', header=4, nrows=417)
        equip['Munic�pio'] = equip["Munic�pio"].str.slice(0, 6)
        equip = equip.rename(columns={'Munic�pio': "Mun.Cod."})
        yearColumn = getColumnByYear(year, equip.columns)
        equip = equip[["Mun.Cod.", yearColumn]]
        equip = equip.replace({'-': 0})
        equip[yearColumn] = pd.to_numeric(equip[yearColumn])
        equip = equip.rename(columns={yearColumn: "Mamógrafos existentes"})
        equip = equip.set_index('Mun.Cod.')
        print('-> The File '+file+' was prepared.')
        return equip
    except:
        input('-> csv could not be prepared.')
        exit()
