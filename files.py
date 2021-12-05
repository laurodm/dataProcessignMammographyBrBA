files = {
    'equip': 'data/equip_mamografos_2017_a_2021.csv',
    'mamoBl': 'data/mamo_bilateral_2017_a_2021.csv',
    'mamoDg': 'data/mamo_diagnostica_2017_a_2021.csv',
    'diag': 'data/diag_lesao_cancer_2017_a_2021.csv',
    'mu4049': 'data/mulheres_40_49.csv',
    'mu5059': 'data/mulheres_50_59.csv',
    'mu5069': 'data/mulheres_50_69.csv'
}


def get_file(name):
    return files[name]
