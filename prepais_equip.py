import pandas as pd

from files import get_file


def prepair_equipment(year, lastMonth):
    try:
        file = get_file('eq'+year)
        equip = pd.read_csv(file, sep=';', header=4)
        equip = equip[["Mun.Cod.", year+"/"+lastMonth]]
        equip = equip.rename(
            columns={year+"/"+lastMonth: "Mamógrafos existentes"})
        equip = equip.set_index('Mun.Cod.')
        print('-> The File '+file+' was prepared.')
        return equip
    except:
        input('-> csv could not be prepared.')
        exit()
