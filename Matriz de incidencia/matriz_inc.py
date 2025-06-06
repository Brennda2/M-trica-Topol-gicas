# IMPORTAÇÃO DAS BIBLIOTECAS NECESSÁRIAS
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random


# LEITURA DO ARQUIVO EXCEL COM OS DADOS DO FORMULÁRIO
df = pd.read_excel('dataset.xlsx')

# FUNÇÃO PARA CRIAR A MATRIZ DE DADOS COM NOME, SERVIÇOS E ESPORTES
def criar_matriz_dados():
    matriz_dados = []
    for _, row in df.iterrows():
        nome = row['Qual é seu nome?']
        servico1 = row['Qual seu serviço de streaming favorito?']
        servico2 = row['Qual seu segundo serviço de streaming favorito?']
        servicos = [str(s).strip() for s in [servico1, servico2] if pd.notna(s)]

        esporte1 = row['Qual o seu esporte favorito?']
        esporte2 = row['Qual o seu segundo esporte favorito?']
        esportes = [str(e).strip() for e in [esporte1, esporte2] if pd.notna(e)]

        matriz_dados.append([nome, servicos, esportes])
    return matriz_dados

# FUNÇÃO PARA FORMATAR OS NOMES DAS PESSOAS
def formatar_nomes(lista_nomes):
    nomes_formatados = []
    for nome in lista_nomes:
        if pd.isna(nome):
            nome = "Não informado"
        nome_limpo = ' '.join(str(nome).strip().split())
        nome_formatado = nome_limpo.title()
        nomes_formatados.append(nome_formatado)
    return nomes_formatados

# FUNÇÃO PARA EXTRAIR TODAS AS CATEGORIAS (SERVIÇOS + ESPORTES)
def extrair_servicos_esportes(matriz_dados):
    conjunto = set()
    for _, servicos, esportes in matriz_dados:
        conjunto.update(servicos)
        conjunto.update(esportes)
    return conjunto

# FUNÇÃO PARA CRIAR MATRIZ DE INCIDÊNCIA COM 1 ONDE A PESSOA ESCOLHEU O ITEM
def criar_matriz_incidencia(matriz_dados, categorias_unicas, nomes_pessoas):
    colunas = sorted(categorias_unicas)
    matriz = []
    for nome, servicos, esportes in matriz_dados:
        interesses = set(servicos + esportes)
        linha = [1 if item in interesses else 0 for item in colunas]
        matriz.append(linha)
    return pd.DataFrame(matriz, columns=colunas, index=nomes_pessoas)

# CRIA A MATRIZ DE DADOS
matriz_dados = criar_matriz_dados()

# EXTRAI E FORMATA OS NOMES DAS PESSOAS
nomes_crus = [linha[0] for linha in matriz_dados]
nomes = formatar_nomes(nomes_crus)

# EXTRAI TODAS AS CATEGORIAS POSSÍVEIS (INTERESSES)
categorias = extrair_servicos_esportes(matriz_dados)

# CRIA A MATRIZ DE INCIDÊNCIA
incidencia = criar_matriz_incidencia(matriz_dados, categorias, nomes)

# EXIBE A MATRIZ NO TERMINAL
print(incidencia)

# CRIA UM GRAFO DIRECIONADO BIPARTIDO (PESSOAS → INTERESSES)
D = nx.DiGraph()

# ADICIONA OS NÓS DAS PESSOAS
for nome in nomes:
    D.add_node(nome, bipartite=0, tipo="pessoa")

# ADICIONA OS NÓS DAS CATEGORIAS (INTERESSES)
for categoria in categorias:
    D.add_node(categoria, bipartite=1, tipo="categoria")

# GERA CORES ALEATÓRIAS PARA AS PESSOAS
cores_pessoas = {nome: f"#{random.randint(0, 0xFFFFFF):06x}" for nome in nomes}
cor_categorias = "lightgreen"

# CRIA AS ARESTAS ENTRE PESSOAS E INTERESSES
for i, pessoa in enumerate(matriz_dados):
    nome = nomes[i]
    servicos = pessoa[1]
    esportes = pessoa[2]

    for categoria in servicos + esportes:
        D.add_edge(nome, categoria, color=cores_pessoas[nome])

# INICIA O PLOT DO GRAFO BIPARTIDO
plt.figure(1, figsize=(18, 10))

# SEPARA OS NÓS DE PESSOAS E CATEGORIAS
nomes_nodes = [n for n, d in D.nodes(data=True) if d["bipartite"] == 0]
categorias_nodes = [n for n, d in D.nodes(data=True) if d["bipartite"] == 1]

# DEFINE O LAYOUT BIPARTIDO (VERTICAL)
posD = nx.bipartite_layout(D, nomes_nodes, align='vertical', scale=5)

# AJUSTA POSIÇÃO HORIZONTAL DAS CATEGORIAS
for cat in categorias_nodes:
    posD[cat] = (posD[cat][0] + 5, posD[cat][1])

# DESENHA OS NÓS DAS PESSOAS
nx.draw_networkx_nodes(
    D, posD,
    nodelist=nomes_nodes,
    node_color=[cores_pessoas[n] for n in nomes_nodes],
    node_size=1000,
    label="Pessoas"
)

# DESENHA OS NÓS DAS CATEGORIAS
nx.draw_networkx_nodes(
    D, posD,
    nodelist=categorias_nodes,
    node_color=cor_categorias,
    node_size=1000,
    label="Categorias"
)

# DESENHA AS ARESTAS COLORIDAS POR PESSOA
edge_colors = [D[u][v]['color'] for u, v in D.edges()]
nx.draw_networkx_edges(
    D, posD,
    edgelist=D.edges(),
    edge_color=edge_colors,
    width=1.5,
    arrows=True,
    arrowsize=20,
    arrowstyle="->"
)

# DESENHA OS RÓTULOS DOS NÓS
nx.draw_networkx_labels(D, posD, font_size=8)

# EXIBE O GRAFO BIPARTIDO
plt.title("GRAFO DE INCIDÊNCIA (PESSOA → INTERESSE)")
plt.legend()
plt.axis("off")
plt.tight_layout()

# FUNÇÃO PARA NORMALIZAR NOMES
def normalizar_nome(nome):
    if pd.isna(nome):
        return "Não Informado"
    return ' '.join(str(nome).strip().split()).title()

# CRIA UM NOVO GRAFO DIRECIONADO (PESSOA → INTERESSE) COM LAYOUT DE MOLA
L = nx.DiGraph()
nomes_normalizados = []

for nome, servicos, esportes in matriz_dados:
    nome = normalizar_nome(nome)
    nomes_normalizados.append(nome)

    L.add_node(nome, tipo='pessoa')

    for interesse in servicos + esportes:
        interesse = ' '.join(str(interesse).strip().split())
        L.add_node(interesse, tipo='interesse')
        L.add_edge(nome, interesse)

# DEFINE O LAYOUT COM SPRING (MOLA)
posL = nx.spring_layout(L, seed=42, k=0.5)

# DEFINE CORES DOS NÓS
cor_interesse = "#cccccc"
cores_disponiveis = list(mcolors.TABLEAU_COLORS.values()) + list(mcolors.CSS4_COLORS.values())
random.seed(42)
cores_unicas = random.sample(cores_disponiveis, len(nomes))

# MAPEIA CADA PESSOA PARA UMA COR ÚNICA
mapa_cor_pessoa = {nome: cor for nome, cor in zip(nomes, cores_unicas)}

# GERA LISTAS DE CORES PARA OS NÓS E ARESTAS
node_colors = []
edge_colors = []

for node in L.nodes():
    if L.nodes[node]['tipo'] == 'pessoa':
        node_colors.append(mapa_cor_pessoa[node])
    else:
        node_colors.append(cor_interesse)

for u, v in L.edges():
    edge_colors.append(mapa_cor_pessoa[u])

# DESENHA O SEGUNDO GRAFO
plt.figure(2, figsize=(14, 10))
nx.draw(
    L,
    posL,
    with_labels=True,
    node_color=node_colors,
    edge_color=edge_colors,
    node_size=1000,
    font_size=9,
    arrows=True,
    width=2,
    arrowstyle='-|>',
    connectionstyle='arc3,rad=0.1'
)
plt.title("GRAFO DE INCIDÊNCIA (PESSOA → INTERESSE)")
plt.tight_layout()

# EXIBE OS DOIS GRAFOS
plt.show()

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

# GRAFO DE INCIDÊNCIA (D)
print("\n--- Métrica Topológicas: Grafo de Incidência ---")
print("\nVértices do Grafo de Incidência:\n")
print(identificar_vertices(D))
print("\nNúmero total de vértices no Grafo de Incidência:", contar_vertices(D))


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

print("\n---- Ligações dos Grafos (Nó1, Nó2, Peso) ------\n")

ligacoes_D = listar_ligacoes(D)
for ligacao in ligacoes_D:
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

print("\n---- Contagem de Arestas do Grafo ----")

total_arestas_D = contar_arestas(D)
print(f"Número total de arestas: {total_arestas_D}")




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

graus_D_df = graus_vertice(D, grau_minimo=1)
print(graus_D_df.to_string(index=False)) # Usar to_string para melhor formatação

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

print("\n---- Grau Médio do Grafo")
media_D = grau_medio(D)
print(f"Grau médio: {media_D:.2f}")

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

print("\n---- Pesos do Grafo (DE, PARA, PESO) ----\n")
# Para os grafos D e grafo (Similaridade), se não houver pesos explícitos, o peso padrão será 1.
# A função mostrar_pesos_grafo já trata isso.
df_pesos_D = mostrar_pesos_grafo(D, exibir=False, como_dataframe=True)
df_pesos_D_ordenado = df_pesos_D.sort_values(by='PESO', ascending=False)
print(df_pesos_D_ordenado.to_string(index=False))

# Salvar no CSV (mantido apenas para o grafo G, como estava no seu código original)
df_pesos_D.to_csv('pesos_grafo.csv', index=False)


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

print("\n---- Força de Conectividade Média ----")
forca_media_D = calcular_forca_conectividade_media(D)
print(f"Força de conectividade média: {forca_media_D:.4f}")


# --------- FUNÇÃO 9 - Densidade

def calcular_densidade_rede(grafo):
    """
    Calcula a densidade de um grafo.

    Retorno:
    - Float: a densidade do grafo.
    """
    return nx.density(grafo)

# -------- SAIDA DA FUNÇÃO 9

print("\n----  Densidade  ----")
densidade_D = calcular_densidade_rede(D)
print(f"Densidade do grafo: {densidade_D:.4f}")
