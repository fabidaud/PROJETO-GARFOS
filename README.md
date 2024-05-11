PROJETO DE GRAFOS
Prof. Ivan Carlos Alcantara de Oliveira

TRAFFIC SOLVER
Rota Alternativa

Autores:
BRUNO CASTRO TOMAZ - 10389988
GUSTAVO SAAD MALUHY ANDRADE - 10332747
LAURA FONTE ABI DAUD - 10395586

Sao Paulo - SP
2024
Relatorio do Projeto

Imagine que voce esta planejando um trajeto tranquilo pela cidade de Sao Paulo. De repente, se depara com uma rua interditada, um cruzamento bloqueado ou ate mesmo um acidente ou evento que impede a passagem. Nesse tipo de situacao, muito comum na capital paulista, e essencial que veiculos sejam capazes de realizar um contorno com o menor custo possivel e pelo melhor caminho viavel.

Pensando neste problema, nosso grupo resolveu desenvolver uma aplicacao que mapeia algumas regioes da capital paulista como um grafo direcionado; com ruas sendo representadas por arestas e cruzamentos por vertices. Esta nossa aplicacao abrange um dos 17 Objetivos de Desenvolvimento Sustentavel da ONU: a ODS 11 (Cidades e Comunidades Sustentaveis), haja vista que busca facilitar o transito de Sao Paulo, estando em conformidade com a meta "11.2.

Nosso codigo deve ser capaz de sugerir a melhor rota alternativa em situacoes excepcionais, onde o trajeto habitual e bloqueado por razoes distintas. Para isso podemos executar a remocao de vertices (cruzamentos) e/ou arestas (ruas) como uma simulacao de um bloqueio no trajeto. Nessa fase inicial da aplicacao, que sera elaborada neste semestre, construiremos um prototipo simples, que ira analisar as possibilidades em uma area no entorno da Universidade Presbiteriana Mackenzie (no campus Higienopolis). Vale considerar que estamos trabalhando com um cenario generico, desconsiderando fatores dinamicos como tempo de deslocamento, farois, tipo de transporte (a pe, de carro ou onibus, etc).

Apos pesquisar sobre o assunto, optamos por trabalhar em cima do bairro de Higienopolis. A relacao de ruas escolhidas para analise encontra-se no arquivo excel. Foram feitas duas planilhas, uma com suas identificacoes dos vertices (cruzamentos) por numero, e outra com os nomes das ruas e o peso das arestas (a distancia real do caminho entre dois cruzamentos, baseado no software Google Maps). As distancias entre as ruas foram calculadas em metros.

A partir da funcionalidade de remocao e insercao de vertices e arestas, o usuario pode remover ruas ou cruzamentos do algoritmo, para que ele possa calcular o caminho minimo, mesmo que haja alguma interdicao entre os dois pontos. O ponto interditado e removido do grafo e logo o algoritmo gera um novo caminho minimo a partir das modificacoes do usuario.
