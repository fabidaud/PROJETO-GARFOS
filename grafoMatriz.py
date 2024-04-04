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
    for i in range(self.n):
      print(f"\n{vertices[i]} : ", end="")
      for j in range(self.n):
        if self.adj[i][j] != -1:
          print(f"{vertices[j]} -> {self.adj[i][j]} ", end="| ")
      print()

  def show_list_rotulos(self,vertices):
    # Imprime grafo como uma lista de adjacência com pesos
    for i in range(self.n):
      print(f"\n{vertices[i]} : ", end="")
      for j in range(self.n):
        if self.adj[i][j] != -1:
          print(f"{vertices[j]} {self.rua[i][j]} -> {self.adj[i][j]} ", end="| ")
      print()

  def inDegree(self, v):
    entrada = 0
    for i in range(self.n):
      if self.adj[i][v] != -1: # verifica se existe a aresta
        entrada += 1
    print(f"\nO grau de entrada do vértice {v} é {entrada}.")

  def outDegree(self, v):
    saida = 0
    for i in range(self.n):
      if self.adj[v][i] != -1: # verifica se existe a aresta
        saida += 1
    print(f"\nO grau de saída do vértice {v} é {saida}.")

  def isFonte(self, v):
    for i in range(self.n):
      if self.adj[i][v] != -1: # verifica se existe a aresta
        return 0
    return 1

  def isSorvedouro(self, v):
    for i in range(self.n):
      if self.adj[v][i] != -1: # verifica se existe a aresta
        return 0
    return 1

  def completo(self):
    for i in range(self.n):
      for j in range(self.n):
        if i != j and self.adj[i][j] == -1:
          print("\nEste grafo não é completo!")
          return
    print("\nEste grafo é completo!")

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

  # def grafoReduzido(self):
  #   # encontrar r- e r+ de dada vertice, cada iteração vai formar um componente reduzido (intersecção de r- e r+)
  #   def dfs(copia, v, visitados, componente_f_conexa):
  #     def dfs_T(v):
  #       fechoTransitivo.append(v)
  #       for u in range(len(copia)):
  #         if copia[v][u] != -1 and u not in fechoTransitivo:
  #           dfs_T(u)
          
  #     def dfs_I(v):
  #       fechoInverso.append(v)
  #       for u in range(len(copia)):
  #         if copia[u][v] != -1 and u not in fechoInverso:
  #           dfs_I(u)
  #     fechoTransitivo = []
  #     fechoInverso = []
  #     dfs_T(v)
  #     dfs_I(v)
  #     componente_f_conexa = list(set(fechoTransitivo) & set(fechoInverso))
  #     print("Interssecao: ", componente_f_conexa)
  #     for i in range(len(copia)):
  #       if i in componente_f_conexa:
  #         visitados[i] = True
  #     return visitados, componente_f_conexa
      
      
        
  #   def encontrar_componentes(copia):
  #     visitados = [False] * len(copia)
  #     componentes_f_conexas = []
  #     for v in range(len(copia)):
  #       if not visitados[v]:
  #         componente_f_conexa = []
  #         visitados, componente = dfs(copia, v, visitados, componente_f_conexa)
  #         componentes_f_conexas.append(componente)
  #     return componentes_f_conexas
    
  #   copia = self.adj
  #   componentes_f_conexas = encontrar_componentes(copia)
  #   print("COMPONENTES F-CONEXAS:")
  #   print(componentes_f_conexas)
  #   grafo_reduzido = TGrafo(len(componentes_f_conexas))
  #   for componente in componentes_f_conexas:
  #     for u in componente:
  #       for v in range(self.n):
  #           if copia[u][v] != -1 and v not in componente:
  #             peso = copia[u][v]
  #             rua = ' ' #iremos usar sem rua o grafo reduzido
  #             origem = componentes_f_conexas.index(componente)
  #             destino = componentes_f_conexas.index([x for x in componentes_f_conexas if v in x][0])
  #             if grafo_reduzido.adj[origem][destino] == -1:
  #               grafo_reduzido.insereA(origem, destino, peso, rua)
  #   return grafo_reduzido
    
  def grafoReduzido(self):
    
    def achar_r_negativo(matriz, vertice):
      lista = [vertice]
      for i in range(len(matriz)):
        if i == vertice:
          continue
        if matriz[i][vertice] != -1:
          lista.append(i)
      return lista

    def achar_r_positivo(matriz, vertice):
      lista = [vertice]
      for i in range(len(matriz)):
        if i == vertice:
          continue
        if matriz[vertice][i] != -1:
          lista.append(i)
      return lista 
    
    novo_grafo = []
    iteracoes = self.n
    
    for i in range(iteracoes):
      r_negativo = []
      r_positivo = []
      
      #achar r-

      #achar r+
      #intersecção de r- com r+
      #unir vértices achados na 

  def dijkstra(self,origem):
    # -1 é custo infinito
    distancias = [-1]*self.n
    distancias[origem] = 0
    relacoes = [[0,origem]]
    h = HeapMin()
    h.adiciona_no(0, self.rua[origem], origem)
    
    while h.tamanho() > 0:
      dist_vertice, vertice = h.remove_no()
      for vizinho, peso in enumerate(self.adj[vertice]):
        if peso != -1:  # se existe aresta para o vizinho
          novaDistancia = distancias[vertice] + peso
          if distancias[vizinho] == -1 or novaDistancia < distancias[vizinho]:
            distancias[vizinho] = novaDistancia
            h.adiciona_no(novaDistancia, vizinho)
            # Verifica se o vértice já está na lista de relações
            encontrado = False
            for i, r in enumerate(relacoes):
              if r[1] == vizinho:
                relacoes[i] = [novaDistancia, vizinho]  # Atualiza a relação
                encontrado = True
                break
            if not encontrado:
                relacoes.append([novaDistancia, vizinho])  # Adiciona nova relação
    
    # Ordena a lista de relações com base no indice
    relacoes.sort(key=lambda x: x[1])
    return relacoes

#optamos por utilizar uma estrutura de dados HeapMin para auxiliar no codigo que implementa algoritmo de Dijkstra
class HeapMin:
  def __init__(self):
    self.nos = 0
    self.heap = []

  def adiciona_no(self, peso, rua, indice):
    # "u" é o peso e "indice" é o indice do vertice na matriz/grafo
    self.heap.append([peso, rua, indice])
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
        if self.heap[f][0][0] < self.heap[f-1][0][0]:
          f+=1
      if self.heap[p-1][0][0] <= self.heap[f-1][0][0]:
          break
      else:
        self.heap[p-1] , self.heap[f-1] = self.heap[f-1] , self.heap[p-1]
        p = f
    return x

  def tamanho(self):
    return self.nos
