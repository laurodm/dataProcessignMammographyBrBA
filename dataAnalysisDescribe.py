import pandas as pd
import functools as ft
import matplotlib.pyplot as plt
from pandas.plotting import radviz

from prepair_year_data import prepair_year_data


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
    frames = []
    for year in years:
        yearDf = getColumnDataByYear(year, columnName)
        frames.append(yearDf)

    data = ft.reduce(lambda left, right: pd.merge(
        left, right, how="outer", on="Cidade"), frames)

    return data


diagData = dfColumnDataByYear(years, 'Diagnósticos por local de moradia').sum()
diagBahia = pd.DataFrame(diagData).reset_index()

mamoDiagData = dfColumnDataByYear(years, 'Mamografia Diagnóstica').sum()
mamoDiagBahia = pd.DataFrame(mamoDiagData).reset_index()

mamoBilatData = dfColumnDataByYear(years, 'Mamografia Bilateral').sum()
mamoBilatBahia = pd.DataFrame(mamoBilatData).reset_index()

diagMamoDiag = diagBahia.merge(mamoDiagBahia, how="right", on='index')
diagMamoBilat = diagBahia.merge(mamoBilatBahia, how="right", on='index')

# print(diagBahia.describe())
# print(mamoDiagBahia.describe())

diagMamoDiag = diagMamoDiag.rename(columns={'0_x': "Diagnósticos Câncer"})
diagMamoBilat = diagMamoBilat.rename(columns={'0_x': "Diagnósticos Câncer"})

diagMamoDiag = diagMamoDiag.rename(columns={'0_y': "Mamografia Diagnóstica"})
diagMamoBilat = diagMamoBilat.rename(columns={'0_y': "Mamografia Bilateral"})

diagMamoDiag.plot.scatter(x='Diagnósticos Câncer', y='Mamografia Diagnóstica')
diagMamoBilat.plot.scatter(x='Diagnósticos Câncer', y='Mamografia Bilateral')
plt.show()
