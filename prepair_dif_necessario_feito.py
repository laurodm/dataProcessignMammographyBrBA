import pandas as pd
from prepair_parametros_mamografia import prepair_parametros_mamografia
from prepair_mamo import prepair_mamo


def prepair_dif_necessario_feito(year):
    try:
        mamoDg = prepair_mamo(year, 'mamoDg')
        mamoBl = prepair_mamo(year, 'mamoBl')
        params = prepair_parametros_mamografia(year)
        dif = mamoBl
        dif = dif.drop(columns=['Mamografia Bilateral'])
        dif['Dif - Mamo Bilateral / ano'] = params['Mamog. Bilateral necessária / ano'] - \
            mamoBl['Mamografia Bilateral']
        dif['Dif - Mamo Diagnóstica / ano'] = params['Mamog. Diagnóstica necessária / ano'] - \
            mamoDg['Mamografia Diagnóstica']
        return dif
    except:
        input('-> csv could not be prepared.')
        exit()


prepair_dif_necessario_feito("2018")
