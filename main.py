# TEORIA DOS GRAFOS - ATIVIDADE PROJETO 2 - ARQUIVO FONTE FUNÇÃO PRINCIPAL
# BRUNO CASTRO TOMAZ - RA: 10389988
# GUSTAVO SAAD MALUHY ANDRADE - RA: 10332747
# LAURA FONTE ABI DAUD - RA: 10395586

from grafoMatriz import *
import os

def menu():
  print('##########################################')
  print('TEORIA DOS GRAFOS - ATIVIDADE PROJETO 2')
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
  print('11) Verificar informações cruzamento')
  print('12) Verificar Grafo Euleriano')
  print('13) Verificar Grafo Hamiltoniano')
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

def lerArquivo(nomeArquivo):
  grafo = None
  with open(nomeArquivo, "r") as file:
    tipo = file.readline().strip()
    if tipo == '6':
      n = int(file.readline().strip())
      grafo = TGrafo(n) # cria matriz de adjacências

      for i in range(n):
        vertice = file.readline().strip()
        grafo.vertices.append(int(vertice))

      m = int(file.readline().strip())
      while m > 0:
        linha = file.readline().rstrip('\n').split(';')
        grafo.insereA(int(linha[0]) - 1, int(linha[1]) - 1, int(linha[3]), linha[2])
        m -= 1
    print("\nLEITURA DO ARQUIVO CONCLUÍDA: GRAFO CONSTRUÍDO!!!")
  espera_Enter()
  return grafo


def gravarArquivo(grafo):
  arquivo = "grafoSaida.txt"

  with open(arquivo, "w") as file:
    file.write("6\n")
    file.write(f"{grafo.n}\n")
    for i in grafo.vertices:
      file.write(f"{i}\n")
    file.write(f"{grafo.m}")
    for i in range(grafo.n):
      for j in range(grafo.n):
        if grafo.adj[i][j] != -1:
          file.write(f"\n{grafo.vertices[i]};{grafo.vertices[j]};{grafo.rua[i][j]};{grafo.adj[i][j]}")

def inserirVertice(grafo):
  novo_vertice = grafo.insereV()
  grafo.vertices.append(novo_vertice)
  print(f"\nVértice {novo_vertice} inserido com sucesso!!")
  espera_Enter()

def inserirAresta(grafo):
  origem = convert_to_int(input('Digite o vértice origem: '))
  while origem not in grafo.vertices:
    print(f'\nO Vértice não existe!\n{grafo.vertices}\nDigite um vértice do grafo:')
    origem = convert_to_int(input())

  destino = convert_to_int(input('Digite o vértice de destino: '))
  while destino not in grafo.vertices:
    print(f'\nO Vértice não existe!\n{grafo.vertices}\nDigite um vértice do grafo:')
    destino = convert_to_int(input())

  if (grafo.adj[grafo.vertices.index(origem)][grafo.vertices.index(destino)] != -1):
    verifica = get_confirmation('aresta já existe')
    if (not verifica):
      return # caso já exista a aresta, pergunta se quer continuar
    else:
      #se aresta existe e quer continuar, remove 1 aresta do grafo
      grafo.removeA(grafo.vertices.index(origem), grafo.vertices.index(destino))

  peso = input_in_range(f'o peso da aresta entre {origem} e {destino}', 1, 1000000) #valor muito alto simboliza infinito
  if peso is None:
    return
  rotulo = input("Digite o rótulo da nova aresta (rua): ")


  grafo.insereA(grafo.vertices.index(origem), grafo.vertices.index(destino), peso, rotulo)
  print("\nAresta inserida com sucesso!!")
  espera_Enter()

def removerVertice(grafo):
  if grafo.n == 0:
    print("Grafo vazio.")
  else:
    vertice = convert_to_int(input('Digite o vértice a ser removido: '))
    while vertice not in grafo.vertices:
      print(f'\nO Vértice não existe!\n{grafo.vertices}\nDigite um vértice do grafo:')
      vertice = convert_to_int(input())

    grafo.removeV(grafo.vertices.index(vertice))
    #remover o vertice da lista de vertices
    grafo.vertices.remove(vertice)
    print(f"\nVértice {vertice} removido com sucesso!")
  espera_Enter()

def removerAresta(grafo):
  origem = convert_to_int(input('Digite o vértice origem: '))
  while origem not in grafo.vertices:
    print(f'\nO Vértice não existe!\n{grafo.vertices}\nDigite um vértice do grafo:')
    origem = convert_to_int(input())

  destino = convert_to_int(input('Digite o vértice de destino: '))
  while destino not in grafo.vertices:
    print(f'\nO Vértice não existe!\n{grafo.vertices}\nDigite um vértice do grafo:')
    destino = convert_to_int(input())

  if not grafo.removeA(grafo.vertices.index(origem), grafo.vertices.index(destino)):
    print('\nAresta não existe')
  else:
    print("\nAresta removida com sucesso!")
  espera_Enter()

def mostrarArquivo(nomeArquivo):
  try:
    grafo = None
    with open(nomeArquivo, "r") as file:
      tipo = file.readline().strip()
      if tipo == '6':
        n = int(file.readline().strip())
        grafo = TGrafo(n) # cria matriz de adjacências
        for i in range(n):
          vertice = file.readline().strip()
          grafo.vertices.append(int(vertice))

        m = int(file.readline().strip())
        while m > 0:
          linha = file.readline().rstrip('\n').split(';')
          grafo.insereA(int(linha[0]) - 1, int(linha[1]) - 1, int(linha[3]), linha[2])
          m -= 1
      print(f"Tipo do grafo: 6 => Grafo orientado com peso nas arestas")
      print("Número de vértices: ", grafo.n)
      print("Numero de arestas: ", grafo.m)
      grafo.show_list_rotulos()
  except FileNotFoundError:
    print("Arquivo não encontrado!")
  espera_Enter()

def mostrarGrafo(grafo):
  grafo.show_list()
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
  grafo.grafoReduzido()

  espera_Enter()

def GPS(grafo):
  os.system('clear')
  print('\n\n============TRAFFIC SOLVER============')
  origem = convert_to_int(input('Digite o local de origem: '))
  while origem not in grafo.vertices:
    print(f'\nO Local {origem} não existe!\n{grafo.vertices}\nDigite um local válido:')
    origem = convert_to_int(input())

  destino = convert_to_int(input('Digite o local de destino: '))
  while destino not in grafo.vertices:
    print(f'\nO Local {destino} não existe!\n{grafo.vertices}\nDigite um local válido:')
    destino = convert_to_int(input())

  print('\n\n============TRAFFIC SOLVER============')
  if(origem == destino):
    print("Você já está em seu destino!\n")
    espera_Enter()
    return
  resultado = grafo.dijkstra(grafo.vertices.index(origem))

  for subgrafo in resultado:
    if subgrafo is not None:
      distancia_total, distancia_parcial, ruas, final = subgrafo
      if final == grafo.vertices.index(destino):
        print(f"\nRota de {origem} para {destino}:\n")
        mudarRua = ruas[0]
        distanciaRua = distancia_parcial[0]
        for i in range(1, len(distancia_parcial)):
          if ruas[i] == mudarRua:
            distanciaRua += distancia_parcial[i]
            if i == len(distancia_parcial)-1:
              print(f"Siga por {distanciaRua} metros em {mudarRua}\n")
            continue
          print(f"Siga por {distanciaRua} metros em {mudarRua}\n")
          mudarRua = ruas[i]
          distanciaRua = distancia_parcial[i]
          if i == len(distancia_parcial)-1:
            print(f"Siga por {distanciaRua} metros em {mudarRua}\n")
        print(f"Você chegou ao seu destino: {destino}\n")
        print(f"Distância total percorrida: {distancia_total} metros\n")
        break
      else:
        continue
  espera_Enter()

def verificarCruzamento(grafo):
  os.system('clear')
  print('\n\n============TRAFFIC SOLVER============')
  vertice = convert_to_int(input('Digite o vértice a ser analisado: '))
  while vertice not in grafo.vertices:
    print(f'\nO Vértice não existe!\n{grafo.vertices}\nDigite um vértice do grafo:')
    vertice = convert_to_int(input())
  entrada, saida =  grafo.grau_vertice(grafo.vertices.index(vertice))
  print(f'\nQuantidade de ruas que entram no cruzamento:{entrada}\n')
  print(f'Quantidade de ruas que saem do cruzamento:{saida}\n')
  espera_Enter()

def grafoEuleriano(grafo):
  os.system('clear')
  print('\n\n============TRAFFIC SOLVER============')
  grafo.ehEuleriano()
  espera_Enter()

def grafoHamiltoniano(grafo):
  os.system('clear')
  print('\n\n============TRAFFIC SOLVER============')
  grafo.ehHamiltoniano()
  espera_Enter()

def main():
  option = -1
  grafo = None

  while option != 0:
    os.system("clear")
    menu()
    print("\nEscolha Sua opção: ", end ='')
    option = convert_to_int(input())

    if option == 1:
      os.system("clear")
      grafo = lerArquivo("grafo.txt")

    elif option == 2:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        gravarArquivo(grafo)
        print("\nGRAFO GRAVADO NO ARQUIVO!")
        espera_Enter()

    elif option == 3:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        inserirVertice(grafo)

    elif option == 4:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        inserirAresta(grafo)

    elif option == 5:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        removerVertice(grafo)

    elif option == 6:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        removerAresta(grafo)

    elif option == 7:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        gravarArquivo(grafo)
        mostrarArquivo("grafoSaida.txt")

    elif option == 8:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        mostrarGrafo(grafo)

    elif option == 9:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        grafoReduzido(grafo)

    elif option == 10:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        GPS(grafo)

    elif option == 11:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        verificarCruzamento(grafo)

    elif option == 12:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        grafoEuleriano(grafo)

    elif option == 13:
      if grafo is None:
        print('grafo não inicializado!')
        espera_Enter()
      else:
        os.system("clear")
        grafoHamiltoniano(grafo)

    elif option == 0:
      print("Encerrando Programa....")

    else:
      print("\nOpção inválida! Tente novamente.")
      espera_Enter()

  return 0

main()
