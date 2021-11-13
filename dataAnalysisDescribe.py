import pandas as pd
import functools as ft

from prepair_year_data import prepair_year_data

frames = []
years = ['2017', '2018', '2019', '2020', '2021']


# Seleciona os dados de uma coluna de um ano específico
def getColumnDataByYear(year, columnName):
    try:
        data = prepair_year_data(year)
        diagData = pd.DataFrame(data[columnName])
        diagData = diagData.rename(columns={columnName: year})
        return diagData
    except:
        input('-> data could not be prepared.')
        exit()


# agrupa dados de uma coluna de vários anos definidos
def dfColumnDataByYear(years, columnName):
    for year in years:
        yearDf = getColumnDataByYear(year, columnName)
        frames.append(yearDf)

    data = ft.reduce(lambda left, right: pd.merge(
        left, right, how="outer", on="Cidade"), frames)

    return data


diagData = dfColumnDataByYear(years, 'Diagnósticos por local de moradia').sum()
diagBahia = pd.DataFrame(diagData)

print(diagBahia.describe())
