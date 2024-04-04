# TEORIA DOS GRAFOS - ATIVIDADE PROJETO 1 - ARQUIVO FONTE PARA MATRIZ DE ADJACÊNCIAS
# BRUNO CASTRO TOMAZ - RA: 10389988
# GUSTAVO SAAD MALUHY ANDRADE - RA: 10332747
# LAURA FONTE ABI DAUD - RA: 10395586

TAM_MAX_DEFAULT = 100  # qtde de vértices máxima default

class TGrafo:
  # grafo direcionado ponderado
  def __init__(self, n=TAM_MAX_DEFAULT):
    self.n = n  # número de vértices
    self.m = 0  # número de arestas
    self.adj = [[-1 for i in range(n)] for j in range(n)] # -1 indica a inexistencia de aresta
    self.rua = [['' for i in range(n)] for j in range(n)] # nome da rua

  # Insere uma aresta no Grafo tal que v é adjacente a w
  def insereA(self, v, w, peso, nome):
    if (v in range(self.n)) and (w in range(self.n)):
      self.adj[v][w] = peso # aresta atualizada com peso
      self.rua[v][w] = nome # nome da rua que conecta os vértices
      self.m += 1  # atualiza qtd de arestas
      return True
    else:
      return False

  def insereV(self):
    # insere vertice no grafo e retorna seu indice
    for i in range(self.n):
      self.adj[i].append(-1)
      self.rua[i].append('')

    self.n += 1
    adj_line = [-1 for i in range(self.n)]
    rua_line = ['' for i in range(self.n)]
    self.adj.append(adj_line)
    self.rua.append(rua_line)
    return self.n
  
  def removeA(self, v, w):
    # remove a aresta v->w do Grafo, caso exista
    if self.adj[v][w] != -1: # verifica se existe a aresta
      self.adj[v][w] = -1
      self.rua[v][w] = ''
      self.m -= 1
      return True
    else:
      return False

  def removeV(self, v):
    if self.n == 0:
      print("Grafo vazio.")
      return False
    elif v >= self.n or v < 0: 
      print("Vértice não encontrado no grafo.")
      return False
    elif self.n == 1:
      print("Grafo vazio.")
      del self.adj[v]
      self.n -= 1
      return True
    else:
      #remover arestas
      for i in range(self.n):
        if (self.adj[v][i] != -1):
          self.removeA(v, i)
      for i in range(self.n):
        if (self.adj[i][v] != -1):
          self.removeA(i, v)
      #remover vértice
      #remover linha e coluna onde o vértice está na matriz
      del self.adj[v]
      del self.rua[v]

      for row in self.adj:
        del row[v]
      for row in self.rua:
        del row[v]

      self.n -= 1
      return True

  def show_list(self,vertices):
    # Imprime grafo como uma lista de adjacência
    for i in range(len(vertices)):
      print(f"\n{vertices[i]} : ", end="")
      for j in range(len(vertices)):
        if self.adj[i][j] != -1:
          print(f"{vertices[j]} -> {self.adj[i][j]} ", end="| ")
      print()

  def show_list_rotulos(self,vertices):
    # Imprime grafo como uma lista de adjacência com pesos
    for i in range(len(vertices)):
      print(f"\n{vertices[i]} : ", end="")
      for j in range(len(vertices)):
        if self.adj[i][j] != -1:
          print(f"{vertices[j]} {self.rua[i][j]} -> {self.adj[i][j]} ", end="| ")
      print()

  # def C3(self):

  #   def dfs_T(v):
  #     fechoTransitivo.append(v)
  #     for u in range(self.n):
  #       if self.adj[v][u] == 1 and u not in fechoTransitivo:
  #         dfs_T(u)

  #   def dfs_I(v):
  #     fechoInverso.append(v)
  #     for u in range(self.n):
  #       if self.adj[u][v] == 1 and u not in fechoInverso:
  #         dfs_I(u)

  #   fechoTransitivo = []
  #   fechoInverso = []
  #   v = -1
  #   for i in range(self.n):
  #     for j in range(self.n):
  #       if self.adj[i][j] == 1:
  #         v = i
  #         break
  #     if v != -1:
  #       break
  #   dfs_T(v)
  #   dfs_I(v)
  #   fechoTransitivo.sort()
  #   fechoInverso.sort()
  #   if fechoTransitivo == fechoInverso:
  #     return 1
  #   else:
  #     return 0

  # def C2(self):

  #   def dfs_T(v):
  #     fechoTransitivo.append(v)
  #     for u in range(self.n):
  #       if self.adj[v][u] == 1 and u not in fechoTransitivo:
  #         dfs_T(u)

  #   def dfs_I(v):
  #     fechoInverso.append(v)
  #     for u in range(self.n):
  #       if self.adj[u][v] == 1 and u not in fechoInverso:
  #         dfs_I(u)

  #   fechoTransitivo = []
  #   fechoInverso = []
  #   v = -1
  #   for i in range(self.n):
  #     for j in range(self.n):
  #       if self.adj[i][j] == 1:
  #         v = i
  #         break
  #     if v != -1:
  #       break
  #   dfs_T(v)
  #   dfs_I(v)
  #   uniao = list(set(fechoTransitivo + fechoInverso))
  #   if len(uniao) == self.n:
  #     return 1
  #   else:
  #     return 0

  # def C1(self, copia):
  #   #Implementação do algoritmo de Warshall para verificar acessibilidades
  #   for k in range(self.n):
  #     for i in range(self.n):
  #       for j in range(self.n):
  #         copia[i][j] = copia[i][j] or (copia[i][k] and copia[k][j])
  #   for i in range(self.n):
  #     for j in range(self.n):
  #       if copia[i][j] != 1:
  #         return 0
  #   return 1

  # def C0(self, copia):
  #   for k in range(self.n):
  #     for i in range(self.n):
  #       for j in range(self.n):
  #         copia[i][j] = copia[i][j] or (copia[i][k] and copia[k][j])
  #   for i in range(self.n):
  #     for j in range(self.n):
  #       if copia[i][j] != 1:
  #         return 1
  #   return 0

  # def categoriaConexidade(self):
  #   copia = [linha[:] for linha in self.adj]
  #   copia = converteDirecionados(copia)
  #   if self.C0(copia) == 1:
  #     return 0
  #   elif self.C3() == 1:
  #     return 3
  #   elif self.C2() == 1:
  #     return 2
  #   elif self.C1(copia) == 1:
  #     return 1
  def dfs(self,v, visitados):
    if v not in visitados:
      visitados.append(v)

    for i in range(len(self.adj)):
      if self.adj[v][i] != -1 and i not in visitados:
        self.dfs(i,visitados)
    return visitados
    
  def f_conexo(self):
    resp = True
    visitados = []
    for i in range(self.n):
      visitados = self.dfs(i,[])
      if len(visitados) < self.n:
        resp = False
    return resp

  def sf_conexo(self):
    resp = True
    for i in range(len(self.adj)):
      for j in range(len(self.adj)):
        visitados_i = self.dfs(i,[])
        if j not in visitados_i:
          visitados_j = self.dfs(j,[])
          if i not in visitados_j:
            resp = False
    return resp
    
  def desconexo(self):
    def converteSimetrico(copia):
      for i in range(len(copia)):
        for w in range(len(copia)):
          if i == w:
            continue
          else:
            if (copia[i][w] == -1) and (copia[w][i] != -1):
              copia[i][w] = copia[w][i]
            elif (copia[w][i] == -1) and (copia[i][w] != -1):
              copia[w][i] = copia[i][w]
      return copia


    def percurso_semClasse(matriz,v, visitados): 
      if v not in visitados:
        visitados.append(v)
  
      for i in range(len(matriz)):
        if matriz[v][i] != -1 and i not in visitados:
          percurso_semClasse(matriz,i,visitados)
      return visitados
      
    resp = True
    copia = self.adj
    copia = converteSimetrico(copia)
    visitados = percurso_semClasse(copia,0,[])
    if len(visitados) == self.n:
      resp = False
    return resp

  def conexidade(self):
    categoria = 3
    if not self.f_conexo():
      categoria = 2
      if not self.sf_conexo():
        categoria = 0
        if not self.desconexo():
          categoria = 1
    return categoria

     
  def grafoReduzido(self):
    
    def achar_r_negativo(matriz, vertice):
      lista = [vertice]

      adicionado = True

      while adicionado:
        adicionado = False
        for i in range(len(matriz)):
          for y in lista:
            if matriz[i][y] == 1 and i not in lista:
              lista.append(i)
              adicionado = True
      return lista

    def achar_r_positivo(matriz, vertice):
      lista = [vertice]
  
      adicionado = True
  
      while adicionado:
        adicionado = False
        for i in range(len(matriz)):
          for y in lista:  
            if matriz[y][i] == 1 and i not in lista:
              lista.append(i)
              adicionado = True
      return lista

    def achar_conexoes(matriz, lista):
      conexoes_positivo = []
      conexoes_negativo = []
      for i in lista:
        for y in range(len(matriz)):
          if y in lista:
            continue
          if matriz[i][y] == 1 and y not in conexoes_positivo:
            conexoes_positivo.append(y)
  
      for i in lista:
        for y in range(len(matriz)):
          if y in lista:
            continue
          if matriz[y][i] == 1 and y not in conexoes_negativo:
            conexoes_negativo.append(y)
      return conexoes_positivo, conexoes_negativo

    def uniao_grafo(matriz, intersecao, lista_positivo, lista_negativo):
      #primeiro une os vertices

      intersecao.sort()
      # print(intersecao)
      # print('\n')
      # for i in matriz:
      #   for y in i:
      #     print(y, end=' ')
      #   print()
      
      for i in lista_positivo:
        matriz[intersecao[0]][i] = 1

      for i in lista_negativo:
        matriz[i][intersecao[0]] = 1

      for i in range(len(intersecao)-1, 0, -1):
        del matriz[intersecao[i]]

      for i in range(len(matriz)):
        for j in range(len(intersecao)-1, 0, -1):
          del matriz[i][j]

      return matriz
    
    novo_grafo = [row[:] for row in self.adj]
    for i in range(len(novo_grafo)):
      for y in range(len(novo_grafo)):
        if novo_grafo[i][y] == -1:
          novo_grafo[i][y] = 0
        else:
          novo_grafo[i][y] = 1

    iteracoes = self.n
    
    i = 0
    while i < iteracoes:

      # for a in range(len(novo_grafo)):
      #   for b in range(len(novo_grafo[0])):
      #     print(novo_grafo[a][b], end=" ")
      #   print()
      
      intersecao = []
      r_negativo = achar_r_negativo(novo_grafo, i)
      r_positivo = achar_r_positivo(novo_grafo, i)

      for y in r_negativo:
        if y in r_positivo:
          intersecao.append(y) # intersecção de r- com r+

      if len(intersecao) > 1:
        conex_positivo, conex_negativo = achar_conexoes(novo_grafo, intersecao)
        novo_grafo = uniao_grafo(novo_grafo, intersecao, conex_positivo, conex_negativo)
        iteracoes -= len(intersecao)
        #unir vértices achados
      i += 1
  
    for i in range(len(novo_grafo)):
      for j in range(len(novo_grafo[0])):
        print(novo_grafo[i][j], end=" ")
      print()

  def dijkstra(self,origem):
    # -1 é custo infinito
    distancias = [-1]*self.n
    distancias[origem] = 0
    relacoes = [[0,[],[],origem]]
    h = HeapMin()
    h.adiciona_no(0,[],[],origem)
    
    while h.tamanho() > 0:
      dist_vertice, pesos, ruas, vertice = h.remove_no()
      for vizinho, peso in enumerate(self.adj[vertice]):
        if peso != -1:  # se existe aresta para o vizinho
          novaDistancia = distancias[vertice] + peso
          if distancias[vizinho] == -1 or novaDistancia < distancias[vizinho]:
            distancias[vizinho] = novaDistancia
            #atualiza o vetor de pesos e ruas visitados
            pesos_vizinho = pesos + [peso]
            ruas_vizinho = ruas + [self.rua[vertice][vizinho]]
            h.adiciona_no(novaDistancia, pesos_vizinho, ruas_vizinho, vizinho)
            # Verifica se o vértice já está na lista de relações
            encontrado = False
            for i, r in enumerate(relacoes):
              if r[3] == vizinho:
                relacoes[i] = [novaDistancia, pesos_vizinho, ruas_vizinho, vizinho]  # Atualiza a relação
                encontrado = True
                break
            if not encontrado:
               relacoes.append([novaDistancia, pesos_vizinho, ruas_vizinho, vizinho])  # Adiciona nova relação

    
    # Ordena a lista de relações com base no indice
    relacoes.sort(key=lambda x: x[3])
    return relacoes

#optamos por utilizar uma estrutura de dados HeapMin para auxiliar no codigo que implementa algoritmo de Dijkstra
class HeapMin:
  def __init__(self):
    self.nos = 0
    self.heap = []

  def adiciona_no(self, custo, pesos, ruas, indice):
    # Adiciona quatro elementos: custo, pesos, ruas e índice
    self.heap.append([custo, pesos, ruas, indice])
    self.nos +=1
    f = self.nos
    while True: 
      if f==1:
        break
      p = f // 2
      if self.heap[p-1][0] <= self.heap[f-1][0]:
        break
      else:
        self.heap[p-1] , self.heap[f-1] = self.heap[f-1] , self.heap[p-1]
        f = p
  def remove_no(self):
    x = self.heap[0]
    self.nos -= 1
    self.heap[0] = self.heap[self.nos]
    self.heap.pop()
    p = 1
    while True:
      f = 2*p
      if f > self.nos:
        break
      if f +1 <= self.nos:
        if self.heap[f][0] < self.heap[f-1][0]:
          f+=1
      if self.heap[p-1][0] <= self.heap[f-1][0]:
          break
      else:
        self.heap[p-1] , self.heap[f-1] = self.heap[f-1] , self.heap[p-1]
        p = f
    return x

  def tamanho(self):
    return self.nos
