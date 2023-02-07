#Proposta do projeto individual 1
#Stephanie Ferreira Vale
#################################
#Deu Macht !!!!

def add_cand(): 

    sair = "sim" 

    while sair != "não": 

        print("Nome do candidato:") 

        cand = input() 

        print("Nota da entrevista:") 

        e = int(input()) 

        print("Nota da avaliação teórica:") 

        t = int(input()) 

        print("Nota da avaliação prática:") 

        p = int(input()) 

        print("Nota da avaliação de soft skills:") 

        s = int(input()) 

        selecao.append([cand, f"e{e}_t{t}_p{p}_s{s}"]) 

        print("Deseja incluir mais? sim ou não") 

        sair = input() 

 

selecao = [] 

add_cand() 

print(selecao) 