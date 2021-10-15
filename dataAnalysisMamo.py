import pandas as pd
import functools as ft

from prepair_year_data import prepair_year_data

data2018 = prepair_year_data('2018', 'Dez')
data2019 = prepair_year_data('2019', 'Dez')
data2020 = prepair_year_data('2020', 'Dez')
data2021 = prepair_year_data('2021', 'Ago')

with pd.ExcelWriter("dataAnalysisMamoBrBA_VYR.xlsx") as writer:
    try:
        data2018.to_excel(writer, sheet_name="2018")
        data2019.to_excel(writer, sheet_name="2019")
        data2020.to_excel(writer, sheet_name="2020")
        data2021.to_excel(writer, sheet_name="2021")
        print('-> Data was written in file')
    except:
        input('-> data was not written in file')
        exit()
