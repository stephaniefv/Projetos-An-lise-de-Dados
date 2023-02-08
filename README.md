# Projetos-An-lise-de-Dados

SENAC/RESILIA - Formação em Análise de Dados (FAD)            
Projeto Individual 1 - Módulo 2 - Deu Match!         


#Explicando meu Código

Esta é uma função que permite adicionar candidatos a uma lista de seleção.

A função add_cand() inicia com a variável sair com o valor "sim".

O laço while é executado enquanto o valor de sair for diferente de "não".

Dentro do laço, o usuário é solicitado a inserir o nome do candidato, as notas da entrevista, avaliação teórica, prática e soft skills. 

Esses valores são lidos com input() e armazenados nas variáveis cand, e, t, p e s. Em seguida, os valores são adicionados à lista selecao usando append().

Por fim, o usuário é perguntado se deseja incluir mais candidatos e a resposta é armazenada na variável sair. 

Quando o usuário responde "não", o laço é encerrado e a lista selecao é exibida na tela.

###################################################

Ao executar o código:

---- Nome do canditado: Ana Cristina
-----Nota da entrevista: 5
-----Nota da avaliação teórica: 8
-----Nota da avaliação prática:7
-----Nota da avaliação de soft skills: 9
----- Deseja incluir mais? sim ou não
se Sim ( irá repetir novamente as perguntas. )
se Não ( irá mostrar o resustado.)

Resultado:

[['Ana Cristina','e5t6_p7_s8']]



