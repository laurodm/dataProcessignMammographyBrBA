files = {
    'eq2018': 'data/equipamentos_mamografos_2018.csv',
    'eq2019': 'data/equipamentos_mamografos_2019.csv',
    'eq2020': 'data/equipamentos_mamografos_2020.csv',
    'eq2021': 'data/equipamentos_mamografos_2021.csv',
    'mamo': 'data/mamografias_2018-2021.csv',
    'diag': 'data/mamografias_diagnostico_cancer_2018-2021.csv'
}


def get_file(name):
    return files[name]
