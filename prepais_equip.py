import pandas as pd


def prepair_equipment(file, year):
    try:
        equip = pd.read_csv(file, sep=';', header=4)
        equip = equip[["Mun.Cod.", year+"/Dez"]]
        equip = equip.rename(columns={year+"/Dez": "Equipamentos"})
        equip = equip.set_index('Mun.Cod.')
        print('-> The File '+file+' was prepared.')
        return equip
    except:
        input('-> csv could not be prepared.')
        exit()
