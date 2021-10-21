import pandas as pd

from files import get_file


def prepair_equipment(year, lastMonth):
    try:
        yearMonth = year+"/"+lastMonth
        file = get_file('equip')
        equip = pd.read_csv(file, sep=';', header=4, nrows=417)
        equip['Munic�pio'] = equip["Munic�pio"].str.slice(0, 6)
        equip = equip.rename(columns={'Munic�pio': "Mun.Cod."})
        equip = equip[["Mun.Cod.", yearMonth]]
        equip = equip.replace({'-': 0})
        equip[yearMonth] = pd.to_numeric(equip[yearMonth])
        equip = equip.rename(
            columns={year+"/"+lastMonth: "Mamógrafos existentes"})
        equip = equip.set_index('Mun.Cod.')
        print('-> The File '+file+' was prepared.')
        return equip
    except:
        input('-> csv could not be prepared.')
        exit()
