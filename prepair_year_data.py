from numpy.core.numeric import NaN
import pandas as pd
import functools as ft
from prepair_diag import prepair_diag
from prepair_dif_necessario_feito import prepair_dif_necessario_feito
from prepair_ibge_cities import prepair_ibge_cities
from prepair_mamo import prepair_mamo
from prepair_parametros_mamografia import prepair_parametros_mamografia
from prepais_equip import prepair_equipment
from prepair_mulheres import prepair_mulheres


def prepair_year_data(year):
    ibge = prepair_ibge_cities()
    equip = prepair_equipment(year)
    mamoBl = prepair_mamo(year, 'mamoBl')
    mamoDg = prepair_mamo(year, 'mamoDg')
    diag = prepair_diag(year)
    mulhr5069 = prepair_mulheres(year, '5069')
    parametros = prepair_parametros_mamografia(year)
    dif = prepair_dif_necessario_feito(year)

    frames = [ibge, equip, mamoBl, mamoDg,
              diag, mulhr5069, parametros, dif]

    data = ft.reduce(lambda left, right: pd.merge(
        left, right, how="outer", on="Mun.Cod."), frames)

    data = data.rename(
        columns={"Código Município Completo": "ID IBGE"})

    data = data.reset_index()
    data = data.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
    data = data.set_index('Cidade')
    data = data.replace({NaN: 0})

    return data
