culturas = []

def calcular_area(tipo: str, base: float, altura: float):
    return base * altura

#Fontes: https://www.embrapa.br/agencia-de-informacao-tecnologica/cultivos/milho/producao/manejo-do-solo-e-adubacao/adubacao-e-fertilidade-do-solo/adubacao-mineral
# https://www.embrapa.br/agencia-de-informacao-tecnologica/cultivos/cana/producao/correcao-e-adubacao/diagnose-das-necessidades-nutricionais/recomendacao-de-correcao-e-adubacao/adubacao-mineral
def calcular_insumos(tipo, area: float):
    area_hectares = area / 10000

    if tipo == "Cana-de-açúcar":
        fosforo = 120 * area_hectares
        potassio = 200 * area_hectares
    elif tipo == "Milho":
        potassio = 120 * area_hectares
        fosforo = 100 * area_hectares
    else:
        return 'Tipo de cultura inválido'

    return {
        "Fosforo (kg)": fosforo,
        "Potassio (kg)": potassio
    }

def adicionar_cultura():
    print("\nCadastro de nova cultura:")
    tipo = input("Digite o tipo de cultura (Cana-de-açúcar ou Milho): ")

    if tipo not in ["Cana-de-açúcar", "Milho"]:
        print("Cultura inválida! Tente novamente.")
        return

    base = float(input("Digite a largura do terreno (em metros): "))
    altura = float(input("Digite o comprimento do terreno (em metros): "))
    area = calcular_area(tipo, base, altura)

    insumos_necessarios = calcular_insumos(tipo, area)

    culturas.append({
        "Tipo": tipo,
        "Area (m²)": area,
        "Fosforo (kg)": insumos_necessarios["Fosforo (kg)"],
        "Potassio (kg)": insumos_necessarios["Potassio (kg)"]
    })
    print("\nCultura adicionada com sucesso!\n")

def exibir_culturas():
    if not culturas:
        print("\nNenhuma cultura cadastrada ainda!\n")
        return

    print("\nCulturas cadastradas:")
    for i, cultura in enumerate(culturas):
        print(f"{i + 1}. Tipo: {cultura['Tipo']} - Area: {cultura['Area (m²)']} m² - Fosforo: {cultura['Fosforo (kg)']} kg - Potassio: {cultura['Potassio (kg)']} kg")

def menu():
    while True:
        print("\nSistema de Gerenciamento Agrícola")
        print("1 - Adicionar Cultura")
        print("2 - Exibir Culturas")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_cultura()
        elif opcao == "2":
            exibir_culturas()
        elif opcao == "3":
            print("\nSaindo do sistema... Até mais!\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()