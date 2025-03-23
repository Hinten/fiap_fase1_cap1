from objetivo_a.culturas import CULTURA_1, CULTURA_2, Culturas
from objetivo_b.armazenamento_resultado_ruas import carregar_resultado_ruas

# Função para saída de dados
def saida_dados(culturas: Culturas):
    print("\nSaída de Dados:")
    cultura_nome = input(f"""
 0 - VOLTAR AO MENU
 1 - {CULTURA_1}
 2 - {CULTURA_2}
    """).strip().lower()
    
    if cultura_nome == '0' or cultura_nome == 'voltar ao menu':
        return
    if cultura_nome not in {'1', 'CULTURA_1', '2', 'CULTURA_2'}:
        print("Cultura não reconhecida. Retornando ao menu.")
        return
    if cultura_nome in {'1', 'CULTURA_1'}:
        cultura_nome = CULTURA_1
    elif cultura_nome in {'2', 'CULTURA_2'}:
        cultura_nome = CULTURA_2
    else:
        print("Cultura não reconhecida. Retornando ao menu.")
        return
    
    print(f"\nDados para {cultura_nome}:")
    
    if not culturas[cultura_nome]:
        print("Nenhum dado registrado.")
    else:
        # Carregar os resultados de ruas
        ruas_min, ruas_max = carregar_resultado_ruas()
        
        if ruas_min is None or ruas_max is None:
            print("Resultados de ruas não encontrados.")
        else:
            for i, dado in enumerate(culturas[cultura_nome], 1):
                print(f"  Registro {i}: Área = {dado}m², Ruas = {ruas_min} a {ruas_max}")