from utils_dados import CULTURA_1
from utils_dados import CULTURA_2

# Função para calcular o manejo de insumo com base na área
def calcular_manejo(cultura, area):
    if cultura in insumo_por_metro:
        insumo = insumo_por_metro[cultura] * area  # Cálculo do insumo necessário
        return insumo
    return 0

# Dicionário para armazenar os dados do manejo (insumo) por cultura
# Exemplo: cultura1 usa 500 mL/m², cultura2 usa 300 mL/m²
insumo_por_metro = {
    "cultura1": 500,  # Em mL/m²
    "cultura2": 300   # Em mL/m²
}
def input_float(chamada)
    texto = ''
    while not texto.insumeric():
        texto = input(chamada)

        if texto.isnumeric():
            numero = float(texto)
            return numero
        else:
            print('Digite um número válido.')      

def input_int(chamada)
    texto = ''
    while not texto.insumeric():
        texto = input(chamada)

        if texto.isnumeric():
            numero = int(texto)
            return numero
        else:
            print('Digite um número válido.')   