# **Experimentos de otimização e algoritmos genéticos**

Quem bom ter você por aqui, colega!😄 Nessa pasta você vai encontrar as práticas que eu estou executando em Algoritmos Genéticos, a pasta funcoes.py que contém todas as funções em python usadas nos experimentos e logo abaixo você pode ler sobre quais experimentos foram trabalhados por aqui.

## Introdução sobre Algoritmos genéticos com problemas iniciais - Aula 1 

Na aula 1 do dia 09/03/23 estudamos sobre dois experimentos que introduziram a matéria de Algoritmos Géneticos, a busca aleatória e a busca em grade. Nesse caderno, ambas buscam soluções para um problema de otimização do experimento da caixa binária, não é o único que podemos fazer com esses algoritmos, mas foi usado para estudar a performace deles.

Na `busca aleatória` não temos a garantia que teremos um resultado ótimo, mas teremos um satisfatório.
Por outro lado, na `busca em grande`, o algoritmo testa todas (eu disse: TODAS!) as combinações possíveis dos conjuntos de parâmetros, e consequentemente, encontra os mínimos e máximos da função objetivo, o que pode ser bom e ruim. Quando digo que pode ser ruim, lembre-se da expressção "TODAS!", pelo fato de testar integralmente cada possibilidade, com um número grande de dados o teste pode demorar muito tempo e acabar sendo insastifatório para a pesquisa.

🧐 Está curioso(a) para entender como aconteceu esses dois tipos de busca? Aqui na pasta de Algortimos Genéticos você clica em "experimento A.01" para busca aleatória e "experimento A.02" para busca em grade.

## Agora que já passamos pelos primeiros experimentos, vamos ver como utilizar os algoritmos genéticos e explorar outros experimentos

➡️*Algoritmo genético - atravéz do problema das caixas binárias e Caixas não binárias (com cruzamento de mutação)*

No experimento A.03 fomos introduzidos ao algortimo genético e trabalhamos com contanstes como tamanho da população, número de genes, de gerações, chance de cruzamento e chance de mutações. Já no A.04, utilizamos as funções já criadas nas práticas anteriores, adicionamos novas e trabalhamos com caixas não binárias! Para entender melhor clique em "experimento A.03" e "experimento A.04".


➡️*Descobrindo a senha (com um tamanho definido)*

Esse experimento é o "experimento A.05" e ele é usado para minimizar o erro ao testar uma senha. Para cada geração, são selecionados os indivíduos para passar por ela e para isso ocorrer usamos a função de seleção por meio de um "torneio". 

➡️*Caixeiro viajante*

É um problema NP-difícil e utilizamos um algoritmo genético para que o viajante passasse por todas as cidades sem repetir a passagem de nenhuma. Esse é o "experimento A.06" e eu me inspirei no estado de Roraima, pois possui apenas quinze municípios, a menor quantidade dentre os estados brasileiros. Logo, o meu viajante é um aventureiro que quer conhecer toda essa região.

➡️*Realizando restrições - por mei do problema da mochila infinita*

É um problema onde queremos maximizar uma função, entretanto, ela possui restrições que devem ser seguidas. Clique no "experimento A.07" e descubra como colocamos limite de carga para os itens que iriam entrar em uma mochila com Algoritmos Genéticos!

➡️*Experimento G.01 - senha de tamanho variavel.ipynb*

Essa foi uma atividade para treinarmos o nosso aprendizado, cada aluno escolheu um desafio e eu escolhi o de senha com tamanho variável. Se parece com um problema já resolvido, no entanto, não se sabe o tamanho inicial da senha, assim, o algoritmo deve descobrir este tamanho.



## Agradeciementos 

Agradeço à todos os glias (guias nas aulas de computação) que me ajudaram de alguma forma na realização dos experimentos. Em especial, agradeço aos meu colegas Pedro Sophia ([@PedroSophiaaa](https://github.com/PedroSophiaaa)) e João Pedro Arroucha ([@jpab2004](https://github.com/jpab2004)) pela ajuda no desafio da senha com tamanho variável.
