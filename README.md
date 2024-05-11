PROJETO DE GRAFOS
Prof. Ivan Carlos Alcântara de Oliveira

TRAFFIC SOLVER
Rota Alternativa

Autores:
BRUNO CASTRO TOMAZ - 10389988
GUSTAVO SAAD MALUHY ANDRADE - 10332747
LAURA FONTE ABI DAUD - 10395586

São Paulo - SP
2024
Relatório do Projeto

Imagine que você está planejando um trajeto tranquilo pela cidade de São Paulo. De repente, se depara com uma rua interditada, um cruzamento bloqueado ou até mesmo um acidente ou evento que impede a passagem. Nesse tipo de situação, muito comum na capital paulista, é essencial que veículos sejam capazes de realizar um contorno com o menor custo possível e pelo melhor caminho viável.

Pensando neste problema, nosso grupo resolveu desenvolver uma aplicação que mapeia algumas regiões da capital paulista como um grafo direcionado; com ruas sendo representadas por arestas e cruzamentos por vértices. Esta nossa aplicação abrange um dos 17 Objetivos de Desenvolvimento Sustentável da ONU: a ODS 11 (Cidades e Comunidades Sustentáveis), haja vista que busca facilitar o trânsito de São Paulo, estando em conformidade com a meta "11.2.

Nosso código deve ser capaz de sugerir a melhor rota alternativa em situações excepcionais, onde o trajeto habitual é bloqueado por razões distintas. Para isso podemos executar a remoção de vértices (cruzamentos) e/ou arestas (ruas) como uma simulação de um bloqueio no trajeto. Nessa fase inicial da aplicação, que será elaborada neste semestre, construiremos um protótipo simples, que irá analisar as possibilidades em uma área no entorno da Universidade Presbiteriana Mackenzie (no campus Higienópolis). Vale considerar que estamos trabalhando com um cenário genérico, desconsiderando fatores dinâmicos como tempo de deslocamento, faróis, tipo de transporte (a pé, de carro ou ônibus, etc).

Após pesquisar sobre o assunto, optamos por trabalhar em cima do bairro de Higienópolis. A relação de ruas escolhidas para análise encontra-se no arquivo excel. Foram feitas duas planilhas, uma com suas identificações dos vértices (cruzamentos) por número, e outra com os nomes das ruas e o peso das arestas (a distância real do caminho entre dois cruzamentos, baseado no software Google Maps). As distâncias entre as ruas foram calculadas em metros.

A partir da funcionalidade de remoção e inserção de vértices e arestas, o usuário pode remover ruas ou cruzamentos do algoritmo, para que ele possa calcular o caminho mínimo, mesmo que haja alguma interdição entre os dois pontos. O ponto interditado é removido do grafo e logo o algoritmo gera um novo caminho mínimo a partir das modificações do usuário.
