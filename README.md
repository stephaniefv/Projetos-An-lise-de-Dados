# 📊 Projetos - Análise de Dados  

**SENAC/RESILIA** - Formação em Análise de Dados (FAD)  
**Projeto Individual 1** - Módulo 2: **Deu Match!**

---

## 📖 Sobre o Projeto  

Este projeto tem como objetivo a criação de uma função para gerenciar uma lista de seleção de candidatos. Com base nas entradas fornecidas pelo usuário, a função coleta informações relevantes sobre os candidatos e organiza os dados para análise posterior.

---

## 🛠️ Explicando meu Código  

A função principal, `add_cand()`, é projetada para permitir que usuários adicionem candidatos a uma lista de seleção. Aqui está um resumo de como ela funciona:  
- A variável `sair` é inicializada com o valor `"sim"`.  
- Um laço `while` é executado enquanto o valor de `sair` for diferente de `"não"`.  
- Durante cada iteração:  
  - O usuário insere o **nome do candidato** e as **notas da entrevista**, **avaliação teórica**, **prática** e **soft skills**.  
  - Os dados são armazenados em variáveis correspondentes e adicionados à lista `selecao` por meio de `append()`.  
- Após cada entrada, o usuário é perguntado se deseja incluir mais candidatos:  
  - Se a resposta for `"sim"`, o laço recomeça.  
  - Se a resposta for `"não"`, o laço é encerrado e a lista final de candidatos é exibida.  

---

## 💻 Exemplo de Execução  

**Entradas do usuário**:  
```bash
---- Nome do candidato: Ana Cristina
----- Nota da entrevista: 5
----- Nota da avaliação teórica: 8
----- Nota da avaliação prática: 7
----- Nota da avaliação de soft skills: 9
----- Deseja incluir mais? (sim ou não)
```

- **Se `sim`**: O programa repete as perguntas para um novo candidato.  
- **Se `não`**: O programa exibe o resultado final.  

**Saída esperada**:  
```python
[['Ana Cristina', 'e5t8_p7_s9']]
```

---

## 🌟 Objetivo do Projeto  

Este projeto simula um sistema básico de seleção, integrando a coleta, organização e exibição de dados em Python. É uma ferramenta educativa que demonstra a aplicação prática de conceitos como:  
- Estruturas de repetição  
- Manipulação de listas  
- Interatividade via `input()`  

---

O que você achou dessa versão? Caso queira mais ajustes ou adicionar algo, é só me falar! 😊
