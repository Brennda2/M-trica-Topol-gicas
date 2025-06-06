import csv
import networkx as nx
import numpy as np
import pandas as pd

nomes = []
servico_fav = []
servico_fav2 = []
esporte_fav = []
esporte_fav2 = []

preferencias = ["Netflix", "Disney+", "HBO MAX", "Crunchyroll", "Globo Play", "Amazon Prime Video",
                "Atletismo", "Musculação", "Basquete", "Futebol", "Vôlei", "Natação", "Não gosto",
                "Ciclismo", "Skate"]
#15 total
with open('dataset.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    for row in spamreader:
      if count == 0:
        count = 1
        continue
      nomes.append(row[1])
      servico_fav.append(row[2])
      servico_fav2.append(row[3])
      esporte_fav.append(row[4])
      esporte_fav2.append(row[5])

#criando a matriz de similaridade
matriz_similaridade = [0] * len(nomes)
for i in range(0, len(nomes)):
  matriz_similaridade[i] = [0] * len(preferencias)

#calculando matriz de similaridade
for i in range(0, len(nomes)):
  for j in range(0, len(preferencias)):
    if servico_fav[i] == preferencias[j] or servico_fav2[i] == preferencias[j] or esporte_fav[i] == preferencias[j] or esporte_fav2[i] == preferencias[j]:
      matriz_similaridade[i][j] = 1
    else:
      matriz_similaridade[i][j] = 0

for i in range(0, len(nomes)):
  for j in range(0, len(preferencias)):
    print(matriz_similaridade[i][j], " ", end="")
  print()

#convertendo a matriz em uma matriz numpy
numpy_matriz = np.asmatrix(matriz_similaridade)

grafo = nx.Graph()

num_rows = numpy_matriz.shape[0]
num_cols = numpy_matriz.shape[1]

#adicionar vertices dos nomes
for i in range(num_rows):
  grafo.add_node(nomes[i], bipartite=0)

#adicionar vertices dos servicos
for i in range(num_cols):
  grafo.add_node(preferencias[i], bipartite=1)

#adicionar arestas
for i in range(num_rows):
  for j in range(num_cols):
    if numpy_matriz[i, j] == 1:
      grafo.add_edge(nomes[i], preferencias[j])

#variavel pra mudar a separação dos vertices
pos = nx.spring_layout(grafo, k=6.1)

nx.draw(grafo, pos, with_labels=True)


# --------------- MÉTRICAS TOPOLÓGICAS ------------------

# --------- FUNÇÃO 1 -  Identificar os Vértices

def identificar_vertices(grafo):
    """
    Esta função recebe um grafo da biblioteca networkx como entrada
    e retorna uma lista com todos os seus vértices (ou nós).
    O método .nodes() é um método do objeto grafo que retorna
    uma visualização de todos os nós presentes no grafo.
    """
    return list(grafo.nodes())


# --------- FUNÇÃO 2 - Contagem do Número de Vértices

def contar_vertices(grafo):
    """
    Esta função recebe um grafo da biblioteca networkx e retorna
    a quantidade total de vértices. O método .number_of_nodes()
    calcula e retorna eficientemente o número de nós no grafo.
    É equivalente a usar len(grafo.nodes()).
    """
    return grafo.number_of_nodes()


# --------- SAIDA DA FUNÇÃO 1 E 2

# GRAFO DE SIMILARIDADE (grafo)
print("\n--- Métrica Topológicas: Grafo de Similaridade ---\n")
print("Vértices do Grafo de Similaridade:\n")
print(identificar_vertices(grafo))
print("\nNúmero total de vértices no Grafo de Similaridade:", contar_vertices(grafo))
print("\n")


# --------- FUNÇÃO 3 - Identifica as ligações

def listar_ligacoes(grafo):
    """
    Esta função recebe um grafo NetworkX e retorna uma lista de arestas (ligações)
    com os pesos associados, que representam quantos serviços em comum cada par de pessoas tem.

    Retorno:
    - Lista de tuplas: (nó1, nó2, peso da conexão)
    """
    ligacoes = grafo.edges(data=True)
    # Tenta obter 'weight', se não existir, usa 1 como padrão (para grafos sem pesos explícitos)
    return [(u, v, d.get('weight', 1)) for u, v, d in ligacoes]


# --- SAIDA DA FUNÇÃO 3

print("---- Ligações do Grafo (Nó1, Nó2, Peso) ------\n")

ligacoes_grafo = listar_ligacoes(grafo)
for ligacao in ligacoes_grafo:
    print(ligacao)



# --------- FUNÇÃO 4  - Contagem do número de arestas

def contar_arestas(grafo):
    """
    Esta função recebe um grafo NetworkX e retorna o número total de arestas (ligações)
    presentes no grafo. Cada aresta representa uma conexão entre dois nós.

    Retorno:
    - Inteiro com a quantidade de arestas no grafo.
    """
    return grafo.number_of_edges()


# -------- SAIDA DA FUNÇÃO 4

print("\n---- Contagem de Arestas dos Grafos ----")
total_arestas_grafo = contar_arestas(grafo)
print(f"Número total de arestas: {total_arestas_grafo}")




# --------- FUNÇÃO 5 - Grau Vertice

def graus_vertice(grafo, grau_minimo=0):
    """
    Calcula os graus dos vértices de um grafo e retorna-os em um DataFrame.
    Filtra vértices com grau maior ou igual ao grau_minimo especificado e ordena.

    Retorno:
    - DataFrame: com as colunas 'Nó' e 'Grau'.
    """
    graus = dict(grafo.degree())  # Retorna um dicionário {nó: grau}

    df_graus = pd.DataFrame(graus.items(), columns=['Nó', 'Grau'])  # Converte o dicionário para um DataFrame

    df_graus = df_graus[df_graus['Grau'] >= grau_minimo]  # Filtra os vértices

    df_graus = df_graus.sort_values(by='Grau', ascending=False).reset_index(drop=True)  # Ordena o DataFrame

    return df_graus


# -------- SAIDA DA FUNÇÃO 5

print("\n---- Tabela Grau de Vértice ----\n")

graus_grafo_df = graus_vertice(grafo, grau_minimo=1)
print(graus_grafo_df.to_string(index=False))


# --------- FUNÇÃO 6 - Grau Médio

def grau_medio(grafo):
    """
    Calcula o grau médio de um grafo.

    Retorno:
    - Float: o grau médio do grafo.
    """
    graus = dict(grafo.degree())  # Obtém os graus de todos os nós do grafo como um dicionário {nó: grau}
    media = sum(graus.values()) / len(graus) if len(graus) > 0 else 0  # Calcula a média
    return media

# -------- SAIDA DA FUNÇÃO 6

print("\n---- Grau Médio dos Grafos")
media_grafo = grau_medio(grafo)
print(f"Grau médio: {media_grafo:.2f}")

# --------- FUNÇÃO 7 - Pesos do grafo

def mostrar_pesos_grafo(grafo, exibir=True, como_dataframe=False):
    """
    Exibe ou retorna os pesos das arestas de um grafo.

    Retorno:
    - DataFrame (opcional): com as colunas 'DE', 'PARA' e 'PESO'.
    """
    pesos = []
    if exibir:
        print("\n------ PESOS DO GRAFO ------ \n")
    for u, v, d in grafo.edges(data=True):
        peso = d.get('weight', 1) # Obtém o peso, ou 1 se não existir
        pesos.append({'DE': u, 'PARA': v, 'PESO': peso})
        if exibir:
            print(f"{u} -- {v}: {peso}")

    if como_dataframe:
        return pd.DataFrame(pesos)
    return None


# -------- SAIDA DA FUNÇÃO 7

print("\n---- Pesos do Grafo (DE, PARA, PESO) ----")
# Para os grafos D e grafo (Similaridade), se não houver pesos explícitos, o peso padrão será 1.
# A função mostrar_pesos_grafo já trata isso.

df_pesos_grafo = mostrar_pesos_grafo(grafo, exibir=False, como_dataframe=True)
df_pesos_grafo_ordenado = df_pesos_grafo.sort_values(by='PESO', ascending=False)
print(df_pesos_grafo_ordenado.to_string(index=False))

# Salvar no CSV (mantido apenas para o grafo G, como estava no seu código original)
df_pesos_grafo.to_csv('pesos_grafo.csv', index=False)


# --------- FUNÇÃO 8 - Conectividade

def calcular_forca_conectividade_media(grafo):
    """
    Calcula a força de conectividade média de um grafo.

    Retorno:
    - Float: a força de conectividade média.
    """
    forcas = [grafo.degree(n, weight='weight') for n in grafo.nodes()]
    return sum(forcas) / len(forcas) if forcas else 0

# -------- SAIDA DA FUNÇÃO 8

print("\n---- Força de Conectividade Média dos Grafos ----")
forca_media_grafo = calcular_forca_conectividade_media(grafo)
print(f"Força de conectividade média: {forca_media_grafo:.4f}")

# --------- FUNÇÃO 9 - Densidade

def calcular_densidade_rede(grafo):
    """
    Calcula a densidade de um grafo.

    Retorno:
    - Float: a densidade do grafo.
    """
    return nx.density(grafo)

# -------- SAIDA DA FUNÇÃO 9

print("\n----  Densidade da Rede dos Grafos ----")
densidade_grafo = calcular_densidade_rede(grafo)
print(f"Densidade do grafo: {densidade_grafo:.4f}")
