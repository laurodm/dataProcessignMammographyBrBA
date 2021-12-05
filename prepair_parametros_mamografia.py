import pandas as pd
from prepair_mulheres import prepair_mulheres


def prepair_parametros_mamografia(year):
    try:
        mulhr5069 = prepair_mulheres(year, '5069')
        mulhr5069['Mamog. Bilateral necessária / ano'] = mulhr5069['Mulheres 50 a 69'] * 0.5
        mulhr5069['Mamog. Diagnóstica necessária / ano'] = mulhr5069['Mulheres 50 a 69'] * 0.029
        mulhr5069 = mulhr5069.drop(columns=['Mulheres 50 a 69'])
        return mulhr5069
    except:
        input('-> csv could not be prepared.')
        exit()
