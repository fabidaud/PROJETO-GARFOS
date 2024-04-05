# TEORIA DOS GRAFOS - ATIVIDADE PROJETO 1 - ARQUIVO FONTE FUNÇÃO PRINCIPAL
# BRUNO CASTRO TOMAZ - RA: 10389988
# GUSTAVO SAAD MALUHY ANDRADE - RA: 10332747
# LAURA FONTE ABI DAUD - RA: 10395586

from grafoMatriz import *
import os

def menu():
  print('##########################################')
  print('TEORIA DOS GRAFOS - ATIVIDADE PROJETO 1')
  print('BRUNO CASTRO TOMAZ - RA: 10389988')
  print('GUSTAVO SAAD MALUHY ANDRADE - RA: 10332747')
  print('LAURA FONTE ABI DAUD - RA: 10395586')
  print('##########################################')
  print('\n\n============TRAFFIC SOLVER============')
  print('1) Ler dados do arquivo ')
  print('2) Gravar dados no arquivo ')
  print('3) Inserir vértice')
  print('4) Inserir aresta')
  print('5) Remover vértice')
  print('6) Remover aresta')
  print('7) Mostrar conteúdo do arquivo')
  print('8) Mostrar grafo')
  print('9) Apresentar a conexidade do grafo')
  print('10) GPS')
  print('0) Encerrar a aplicação')

def convert_to_int(var):
  try:
    return int(var)
  except ValueError:
    return None

def input_in_range(title, min, max):
  var = convert_to_int(input(f'Digite {title}: '))
  while var not in range(min, max+1):
    os.system('clear')
    print(f'Valor inválido! Digite um valor entre {min} e {max}')
    var = input(f'Digite {title}, [c] para cancelar: ')
    if var == 'c':
      return None
    var = convert_to_int(var)
  return var
    
def get_confirmation(mensagem):
  print(mensagem)
  var = input('Deseja continuar? [s/n]: ')
  while var not in ['s', 'n']:
    os.system('clear')
    var = input('Deseja continuar? [s/n]: ')
  if var == 's':
    return True
  return False

def espera_Enter():
  print("\nPressione ENTER para continuar...")
  input()

def lerArquivo():
  grafo = None
  vertices = []
  with open("grafo.txt", "r") as file:
    tipo = file.readline().strip()
    if tipo == '6':
      n = int(file.readline().strip())
      grafo = TGrafo(n) # cria matriz de adjacências
      
      for i in range(n):
        vertice = file.readline().strip()
        vertices.append(int(vertice))
        
      m = int(file.readline().strip()) 
      while m > 0:
        linha = file.readline().rstrip('\n').split(';')
        grafo.insereA(int(linha[0]) - 1, int(linha[1]) - 1, int(linha[3]), linha[2])
        m -= 1
    print("\nLEITURA DO GRAFO CONCLUÍDA!")
  espera_Enter()
  return grafo, vertices


def gravarArquivo(grafo, vertices):
  arquivo = "grafoSaida.txt"

  with open(arquivo, "w") as file:
    file.write("6\n")
    file.write(f"{grafo.n}\n")
    for i in vertices:
      file.write(f"{i}\n")
    file.write(f"{grafo.m}")
    for i in range(grafo.n):
      for j in range(grafo.n):
        if grafo.adj[i][j] != -1:
          file.write(f"\n{vertices[i]};{vertices[j]};{grafo.rua[i][j]};{grafo.adj[i][j]}")  


def inserirVertice(grafo, vertices):
  novo_vertice = grafo.insereV()
  vertices.append(novo_vertice)
  print(f"\nVértice {novo_vertice} inserido com sucesso!")
  espera_Enter()

def inserirAresta(grafo, vertices):
  origem = input_in_range('o vértice origem', vertices[0], grafo.n)
  # os.system('clear')
  if origem is None:
    return
  
  destino = input_in_range('o vértice destino', vertices[0], grafo.n)
  os.system('clear')
  if destino is None:
    return

  if (grafo.adj[origem-1][destino-1] != -1):
    verifica = get_confirmation('aresta já existe')
    if (not verifica):
      return # caso já exista a aresta, pergunta se quer continuar
    else:
      #se aresta existe e quer continuar, remove 1 aresta do grafo
      grafo.removeA(origem-1, destino-1) 
     
  peso = input_in_range(f'o peso da aresta entre {origem} e {destino}', 1, 1000000) #valor muito alto simboliza infinito
  if peso is None:
    return
  rotulo = input("Digite o rótulo da nova aresta (rua): ")
  

  grafo.insereA(origem-1, destino-1, peso, rotulo)
  print("\nAresta inserida com sucesso!")
  espera_Enter()

def removerVertice(grafo, vertices):  
  vertice = input_in_range('o vértice a ser removido', vertices[0], grafo.n)
  
  if vertice is None:
    return
  
  grafo.removeV(vertice-1)
  # remover o vertice da lista de vertices
  for i in range(len(vertices)):
    if vertices[i] == vertice:
      vertices.remove(vertice)[1,2,3,5,6]
  print(f"\nVértice {vertice} removido com sucesso!")
  espera_Enter()

def removerAresta(grafo, vertices):  
  origem = input_in_range('o vértice origem', vertices[0], grafo.n)
  if origem is None:
    return
  
  destino = input_in_range('o vértice destino', vertices[0], grafo.n)
  if destino is None:
    return

  if not grafo.removeA(origem-1, destino-1):
    print('Aresta não existe')
  print("\nAresta removida com sucesso!")
  espera_Enter()

def mostrarArquivo(vertices):
  try:
    with open("grafoSaida.txt", "r") as file:
      tipo = file.readline().strip()
      if tipo == '6':
        n = int(file.readline().strip())
        grafo_arquivo = TGrafo(n) # cria matriz
  
        for i in range(n):
          file.readline().strip()
  
        m = int(file.readline().strip()) # lê qtde de arestas
        while m > 0:
          linha = file.readline().rstrip('\n').split(';')
          grafo_arquivo.insereA(int(linha[0]) - 1, int(linha[1]) - 1, int(linha[3]), linha[2])
          m -= 1
        print(f"Tipo do grafo: {tipo} => Grafo orientado com peso nas arestas", tipo)
        print("Número de vértices: ", grafo_arquivo.n)
        print("Numero de arestas: ", grafo_arquivo.m)
        grafo_arquivo.show_list_rotulos(vertices)

  except FileNotFoundError:
    print("Arquivo não encontrado!") 
  espera_Enter()

def mostrarGrafo(grafo, vertices):
  grafo.show_list(vertices)
  espera_Enter()

def grafoReduzido(grafo):
  print("GRAFO ATUAL:")
  conexidade = grafo.conexidade()
  if (conexidade == 3):
    print("\nEste grafo é fortemente conexo, categoria C3!\n")
  elif (conexidade == 2):
    print("\nEste grafo é semifortemente conexo, categoria C2!\n")
  elif (conexidade == 1):
    print("\nEste grafo é simplesmente conexo, categoria C1!\n")
  elif (conexidade == 0):
    print("\nEste grafo é desconexo, categoria C0!\n")
  
  print("\nGRAFO REDUZIDO:\n")
  grafoReduzido = grafo.grafoReduzido()
  
  
  espera_Enter()
  
def definir_rota(grafo, vertices):
  os.system('clear')
  origem = input_in_range('o seu local atual', vertices[0], grafo.n)
  if origem is None:
    return

  destino = input_in_range('o local de destino: ', vertices[0], grafo.n)
  os.system('clear')
  if destino is None:
    return

  if(origem == destino):
    print("Você já está em seu destino!\n")
    espera_Enter()
    return
  resultado = grafo.dijkstra(origem-1)
  # print("\nesquema de melhores rotas após algoritmo de dijkstra: ")
  # print(resultado)
  for subgrafo in resultado:
    if subgrafo is not None:
      distancia_total, distancia_parcial, ruas, final = subgrafo
      if final == destino-1:
        print(f"\nRota de {vertices[origem-1]} para {vertices[destino-1]}:\n")
        for i in range(len(distancia_parcial)):
          print(f"Siga por {distancia_parcial[i]} metros em {ruas[i]}\n")
        print(f"Você chegou ao seu destino: {vertices[final]}\n")
        print(f"Distância total percorrida: {distancia_total} metros\n")
        break
      else:
        continue
  espera_Enter()

def main():
  option = -1
  vertices = []
  grafo = None

  while option != 0:
    os.system("clear") 
    menu()
    print("\nEscolha Sua opção: ", end ='')
    option = convert_to_int(input())
    
    if option == 1:
      os.system("clear")
      grafo, vertices = lerArquivo()

    elif option == 2:
      if grafo is None:
        print('grafo não inicializado')
        espera_Enter()
      else:
        os.system("clear") 
        gravarArquivo(grafo, vertices)
        print("\nGRAFO GRAVADO NO ARQUIVO!")
        espera_Enter()

    elif option == 3:
      if grafo is None:
        print('grafo não inicializado')
        espera_Enter()
      else:
        os.system("clear") 
        inserirVertice(grafo, vertices)

    elif option == 4:
      if grafo is None:
        print('grafo não inicializado')
        espera_Enter()
      else:
        os.system("clear")
        inserirAresta(grafo, vertices)

    elif option == 5:
      if grafo is None:
        print('grafo não inicializado')
        espera_Enter()
      else:
        os.system("clear") 
        removerVertice(grafo, vertices)

    elif option == 6:
      if grafo is None:
        print('grafo não inicializado')
        espera_Enter()
      else:
        os.system("clear") 
        removerAresta(grafo, vertices)

    elif option == 7:
      os.system("clear") 
      gravarArquivo(grafo, vertices)
      mostrarArquivo(vertices)

    elif option == 8:
      if grafo is None:
        print('grafo não inicializado')
        espera_Enter()
      else:
        os.system("clear") 
        mostrarGrafo(grafo, vertices)

    elif option == 9:
      if grafo is None:
        print('grafo não inicializado')
        espera_Enter()
      else:
        os.system("clear") 
        grafoReduzido(grafo)
    
    elif option == 10:
      if grafo is None:
        print('grafo não inicializado')
        espera_Enter()
      else:
        os.system("clear") 
        definir_rota(grafo, vertices)

    elif option == 0:
      print("Encerrando Programa....")

    else:
      print("\nOpção inválida! Tente novamente.")
      espera_Enter()

  return 0

main()
