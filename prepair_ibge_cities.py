import pandas as pd


def prepair_ibge_cities():
    try:
        file = 'data/ibge_municipios.csv'
        ibge = pd.read_csv(file, sep=';')
        ibge = ibge.query('UF == 29')
        ibge['Mun.Cod.'] = pd.to_numeric(
            ibge["Código Município Completo"].astype(str).str[:-1])
        ibge = ibge.set_index("Mun.Cod.")
        ibge = ibge[["Nome_Município", "Código Município Completo"]]
        ibge = ibge.rename(columns={"Nome_Município": "Cidade"})
        print('-> The File '+file+' was prepared.')
        return ibge
    except:
        input('-> csv could not be prepared.')
        exit()
