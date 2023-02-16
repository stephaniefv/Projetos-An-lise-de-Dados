#----------------------------------------------------
# Formação Analise de dados Resilia|Senac
# Autor: Stephanie Ferreira Vale
# Projeto Individual 2 do Módulo 2 : "Contratado!"
#----------------------------------------------------
#####python programação desenvolvimento

################################################################################

# Dicionários para armazenar as informações dos candidatos
candidatos = {}
candidatos_aprovados_vaga1 = {}
candidatos_aprovados_vaga2 = {}

# Função para cadastrar um novo candidato
def cadastrar_candidato():
    nome = input("Digite o nome do candidato: ")
    vaga = input("Digite o número da vaga para a qual deseja se candidatar (1 ou 2): ")
    resumo = input("Digite um breve resumo sobre suas habilidades e experiências: ")
    candidatos[nome] = {"vaga": vaga, "resumo": resumo}

# Função para avaliar os candidatos aprovados
def avaliar_candidatos():
    for nome, info in candidatos.items():
        if info["vaga"] == "1" and "Python" in info["resumo"] and "programação" in info["resumo"]:
            candidatos_aprovados_vaga1[nome] = info["resumo"]
        elif info["vaga"] == "2" and "Análise de dados" in info["resumo"] and "SQL" in info["resumo"]:
            candidatos_aprovados_vaga2[nome] = info["resumo"]

# Função para exibir os resultados
def exibir_resultados():
    print(f"Total de candidatos: {len(candidatos)}")
    print(f"Total de candidatos aprovados para a vaga 1: {len(candidatos_aprovados_vaga1)}")
    print(f"Total de candidatos aprovados para a vaga 2: {len(candidatos_aprovados_vaga2)}")
    print("Candidatos aprovados para a vaga 1:")
    for nome, resumo in candidatos_aprovados_vaga1.items():
        print(f"{nome}: {resumo}")
    print("Candidatos aprovados para a vaga 2:")
    for nome, resumo in candidatos_aprovados_vaga2.items():
        print(f"{nome}: {resumo}")

# Loop principal do programa
while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar candidato")
    print("2 - Avaliar candidatos aprovados")
    print("3 - Exibir resultados")
    print("0 - Sair")
    opcao = input()
    
    if opcao == "1":
        cadastrar_candidato()
    elif opcao == "2":
        avaliar_candidatos()
    elif opcao == "3":
        exibir_resultados()
    elif opcao == "0":
        break
    else:
        print("Opção inválida, tente novamente.")



