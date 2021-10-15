import pandas as pd
import functools as ft
from prepair_diag import prepair_diag
from prepair_mamo import prepair_mamo
from prepais_equip import prepair_equipment


ibge = diag = pd.read_csv('data/ibge_municipios.csv', sep=';')
ibge = ibge.query('UF == 29')
ibge['Mun.Cod.'] = pd.to_numeric(
    ibge["Código Município Completo"].astype(str).str[:-1])
ibge = ibge.set_index("Mun.Cod.")
ibge = ibge[["Nome_Município", "Código Município Completo"]]

equipMamo2018 = prepair_equipment(
    'data/equipamentos_mamografos_2018.csv', '2018')
mamo2018 = prepair_mamo('data/mamografias_2018-2021.csv', '2018')
diag2018 = prepair_diag(
    'data/mamografias_diagnostico_cancer_2018-2021.csv', '2018')
frames2018 = [ibge, equipMamo2018, mamo2018, diag2018]

equipMamo2019 = prepair_equipment(
    'data/equipamentos_mamografos_2019.csv', '2019')
mamo2019 = prepair_mamo('data/mamografias_2018-2021.csv', '2019')
diag2019 = prepair_diag(
    'data/mamografias_diagnostico_cancer_2018-2021.csv', '2019')
frames2019 = [ibge, equipMamo2019, mamo2019, diag2019]

data2018 = ft.reduce(lambda left, right: pd.merge(
    left, right, how="outer", on="Mun.Cod."), frames2018)
data2018["Mun.Cod."] = data2018["Código Município Completo"]
data2018 = data2018.drop(columns="Código Município Completo")

data2019 = ft.reduce(lambda left, right: pd.merge(
    left, right, how="outer", on="Mun.Cod."), frames2019)


with pd.ExcelWriter("dataAnalysisMamoBrBA_VYR.xlsx") as writer:
    try:
        data2018.to_excel(writer, sheet_name="2018")
        data2019.to_excel(writer, sheet_name="2019")
        print('-> Data was written in file')
    except:
        input('-> data was not written in file')
        exit()
