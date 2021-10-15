from numpy.core.numeric import NaN
import pandas as pd
import functools as ft
from prepair_diag import prepair_diag
from prepair_ibge_cities import prepair_ibge_cities
from prepair_mamo import prepair_mamo
from prepais_equip import prepair_equipment


def prepair_year_data(year, lastMonth):
    ibge = prepair_ibge_cities()
    equip = prepair_equipment(year, lastMonth)
    mamo = prepair_mamo(year)
    diag = prepair_diag(year)
    frames = [ibge, equip, mamo, diag]
    data = ft.reduce(lambda left, right: pd.merge(
        left, right, how="outer", on="Mun.Cod."), frames)
    data = data.rename(
        columns={"Código Município Completo": "ID IBGE"})
    data = data.reset_index()
    data = data.iloc[:, [1, 2, 3, 4, 5]]
    data = data.set_index('Cidade')
    data = data.replace({NaN: 0})
    return data
