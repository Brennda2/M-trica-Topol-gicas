import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Dados (mantive só o seu dataframe 'df' como no seu código)

dados = [
    {"Nome": "Felipe", "Streaming Principal": "HBO MAX", "Streaming Secundário": "Netflix", "Esporte Principal": "Ciclismo", "Esporte Secundário": "Atletismo"},
    {"Nome": "caio", "Streaming Principal": "Netflix", "Streaming Secundário": "Disney+", "Esporte Principal": "Futebol", "Esporte Secundário": "Musculação"},
     {"Nome": "Felipe", "Streaming Principal": "Netflix", "Streaming Secundário": "HBO MAX", "Esporte Principal": "Futebol", "Esporte Secundário": "Basquete"},
    {"Nome": "Fábio", "Streaming Principal": "Netflix", "Streaming Secundário": "HBO MAX", "Esporte Principal": "Musculação", "Esporte Secundário": "Futebol"},
    {"Nome": "Daniel", "Streaming Principal": "Netflix", "Streaming Secundário": "Crunchyroll", "Esporte Principal": "Futebol", "Esporte Secundário": "Vôlei"},
    {"Nome": "Lucas", "Streaming Principal": "Netflix", "Streaming Secundário": "HBO MAX", "Esporte Principal": "Futebol", "Esporte Secundário": "Basquete"},
    {"Nome": "Brennda", "Streaming Principal": "Netflix", "Streaming Secundário": "Globo Play", "Esporte Principal": "Musculação", "Esporte Secundário": "Basquete"},
    {"Nome": "Diogo", "Streaming Principal": "Netflix", "Streaming Secundário": "HBO MAX", "Esporte Principal": "Basquete", "Esporte Secundário": "Futebol"},
    {"Nome": "Ana", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Futebol", "Esporte Secundário": "Basquete"},
    {"Nome": "Bruno", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Futebol", "Esporte Secundário": "Vôlei"},
    {"Nome": "Hanry", "Streaming Principal": "Netflix", "Streaming Secundário": "Crunchyroll", "Esporte Principal": "Futebol", "Esporte Secundário": "Vôlei"},
    {"Nome": "Pedro", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Musculação", "Esporte Secundário": ""},
    {"Nome": "Carolina", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Vôlei", "Esporte Secundário": "Musculação"},
    {"Nome": "Guilherme", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Futebol", "Esporte Secundário": "Vôlei"},
    {"Nome": "Miguel", "Streaming Principal": "Netflix", "Streaming Secundário": "HBO MAX", "Esporte Principal": "Futebol", "Esporte Secundário": "Basquete"},
    {"Nome": "Caio", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Musculação", "Esporte Secundário": "Futebol"},
    {"Nome": "João", "Streaming Principal": "HBO MAX", "Streaming Secundário": "Crunchyroll", "Esporte Principal": "Vôlei", "Esporte Secundário": "Musculação"},
    {"Nome": "Marcos", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Vôlei", "Esporte Secundário": "Natação"},
    {"Nome": "Alessandro", "Streaming Principal": "Crunchyroll", "Streaming Secundário": "Netflix", "Esporte Principal": "Musculação", "Esporte Secundário": ""},
    {"Nome": "Felipe", "Streaming Principal": "Amazon Prime Video", "Streaming Secundário": "Netflix", "Esporte Principal": "Futebol", "Esporte Secundário": "Não gosto"},
    {"Nome": "Carlos", "Streaming Principal": "Amazon Prime Video", "Streaming Secundário": "Netflix", "Esporte Principal": "Vôlei", "Esporte Secundário": "Natação"},
    {"Nome": "Giovanna", "Streaming Principal": "Crunchyroll", "Streaming Secundário": "", "Esporte Principal": "Skate", "Esporte Secundário": "Vôlei"},
    {"Nome": "Guilherme", "Streaming Principal": "HBO MAX", "Streaming Secundário": "Globo Play", "Esporte Principal": "Não gosto", "Esporte Secundário": "Não gosto"},
    {"Nome": "Levi", "Streaming Principal": "Netflix", "Streaming Secundário": "Crunchyroll", "Esporte Principal": "Vôlei", "Esporte Secundário": "Basquete"},
    {"Nome": "Caio", "Streaming Principal": "Netflix", "Streaming Secundário": "Disney+", "Esporte Principal": "Futebol", "Esporte Secundário": "Musculação"},
    {"Nome": "Javier", "Streaming Principal": "Amazon Prime Video", "Streaming Secundário": "Disney+", "Esporte Principal": "Musculação", "Esporte Secundário": "Ciclismo"},
    {"Nome": "Guilherme", "Streaming Principal": "Netflix", "Streaming Secundário": "Crunchyroll", "Esporte Principal": "Futebol", "Esporte Secundário": "Vôlei"},
    {"Nome": "Bruno", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Futebol", "Esporte Secundário": "Vôlei"},
    {"Nome": "Enzo", "Streaming Principal": "Netflix", "Streaming Secundário": "HBO MAX", "Esporte Principal": "Futebol", "Esporte Secundário": "Skate"},
    {"Nome": "Gabriel", "Streaming Principal": "Netflix", "Streaming Secundário": "Disney+", "Esporte Principal": "Futebol", "Esporte Secundário": "Musculação"},
    {"Nome": "Guilherme", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Futebol", "Esporte Secundário": "Basquete"},
    {"Nome": "Amanda", "Streaming Principal": "HBO MAX", "Streaming Secundário": "Disney+", "Esporte Principal": "Basquete", "Esporte Secundário": "Natação"},
    {"Nome": "Bruno", "Streaming Principal": "Netflix", "Streaming Secundário": "Disney+", "Esporte Principal": "Basquete", "Esporte Secundário": "Musculação"},
    {"Nome": "Davi", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Não gosto", "Esporte Secundário": "Não gosto"},
    {"Nome": "Igor", "Streaming Principal": "Netflix", "Streaming Secundário": "Disney+", "Esporte Principal": "Musculação", "Esporte Secundário": "Skate"},
    {"Nome": "Adam", "Streaming Principal": "Netflix", "Streaming Secundário": "Disney+", "Esporte Principal": "Futebol", "Esporte Secundário": "Vôlei"},
    {"Nome": "Sidnei", "Streaming Principal": "Netflix", "Streaming Secundário": "HBO MAX", "Esporte Principal": "Futebol", "Esporte Secundário": "Ciclismo"},
    {"Nome": "Lucas", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Musculação", "Esporte Secundário": "Não gosto"},
    {"Nome": "Luis", "Streaming Principal": "Amazon Prime Video", "Streaming Secundário": "Netflix", "Esporte Principal": "Futebol", "Esporte Secundário": "Musculação"},
    {"Nome": "Igor", "Streaming Principal": "Netflix", "Streaming Secundário": "Crunchyroll", "Esporte Principal": "Futebol", "Esporte Secundário": "Vôlei"},
    {"Nome": "Gabriela", "Streaming Principal": "Disney+", "Streaming Secundário": "Netflix", "Esporte Principal": "Natação", "Esporte Secundário": "Não gosto"},
    {"Nome": "Ana", "Streaming Principal": "Globo Play", "Streaming Secundário": "Disney+", "Esporte Principal": "Não gosto", "Esporte Secundário": "Não gosto"},
    {"Nome": "Josiane", "Streaming Principal": "Disney+", "Streaming Secundário": "Netflix", "Esporte Principal": "Vôlei", "Esporte Secundário": "Basquete"},
    {"Nome": "Igor", "Streaming Principal": "Netflix", "Streaming Secundário": "Disney+", "Esporte Principal": "Vôlei", "Esporte Secundário": "Natação"},
    {"Nome": "Anderson", "Streaming Principal": "Netflix", "Streaming Secundário": "HBO MAX", "Esporte Principal": "Futebol", "Esporte Secundário": "Atletismo"},
    {"Nome": "Amanda", "Streaming Principal": "Netflix", "Streaming Secundário": "Crunchyroll", "Esporte Principal": "Vôlei", "Esporte Secundário": "Futebol"},
    {"Nome": "Silvania", "Streaming Principal": "Netflix", "Streaming Secundário": "Globo Play", "Esporte Principal": "Musculação", "Esporte Secundário": "Natação"},
    {"Nome": "Kauã", "Streaming Principal": "Globo Play", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Não gosto", "Esporte Secundário": "Não gosto"},
    {"Nome": "Amábile", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Musculação", "Esporte Secundário": "Não gosto"},
    {"Nome": "Kauê", "Streaming Principal": "Netflix", "Streaming Secundário": "Crunchyroll", "Esporte Principal": "Musculação", "Esporte Secundário": "Futebol"},
    {"Nome": "Diogo", "Streaming Principal": "Netflix", "Streaming Secundário": "Crunchyroll", "Esporte Principal": "Basquete", "Esporte Secundário": "Musculação"},
    {"Nome": "Andreas", "Streaming Principal": "Netflix", "Streaming Secundário": "Crunchyroll", "Esporte Principal": "Não gosto", "Esporte Secundário": "Não gosto"},
    {"Nome": "Hugo", "Streaming Principal": "HBO MAX", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Basquete", "Esporte Secundário": "Natação"},
    {"Nome": "Kauê", "Streaming Principal": "Amazon Prime Video", "Streaming Secundário": "Netflix", "Esporte Principal": "Musculação", "Esporte Secundário": "Atletismo"},
    {"Nome": "João", "Streaming Principal": "HBO MAX", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Basquete", "Esporte Secundário": "Futebol"},
    {"Nome": "Joaquim", "Streaming Principal": "Crunchyroll", "Streaming Secundário": "Netflix", "Esporte Principal": "Musculação", "Esporte Secundário": "Atletismo"},
    {"Nome": "Brenno", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Basquete", "Esporte Secundário": "Musculação"},
    {"Nome": "Paulo", "Streaming Principal": "Crunchyroll", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Futebol", "Esporte Secundário": "Vôlei"},
    {"Nome": "Pedro", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Musculação", "Esporte Secundário": "Futebol"},
    {"Nome": "Enzo", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Futebol", "Esporte Secundário": "Musculação"},
    {"Nome": "Giovanni", "Streaming Principal": "Netflix", "Streaming Secundário": "Disney+", "Esporte Principal": "Futebol", "Esporte Secundário": "Musculação"},
    {"Nome": "Gabriel", "Streaming Principal": "Netflix", "Streaming Secundário": "Amazon Prime Video", "Esporte Principal": "Musculação", "Esporte Secundário": "Futebol"},
    {"Nome": "Matheus", "Streaming Principal": "HBO MAX", "Streaming Secundário": "Netflix", "Esporte Principal": "Futebol", "Esporte Secundário": "Vôlei"},
    {"Nome": "Bruno", "Streaming Principal": "Netflix", "Streaming Secundário": "Crunchyroll", "Esporte Principal": "Não gosto", "Esporte Secundário": "Não gosto"},
    {"Nome": "Lucas", "Streaming Principal": "HBO MAX", "Streaming Secundário": "Netflix", "Esporte Principal": "Basquete", "Esporte Secundário": "Futebol"}
]

df = pd.DataFrame(dados)

G = nx.Graph()

# Construção do grafo
for _, row in df.iterrows():
    preferencias = [
        row['Streaming Principal'],
        row['Streaming Secundário'],
        row['Esporte Principal'],
        row['Esporte Secundário']
    ]
    preferencias = [pref for pref in preferencias if pref and pref != ""]

    for i in range(len(preferencias)):
        for j in range(i + 1, len(preferencias)):
            if G.has_edge(preferencias[i], preferencias[j]):
                G[preferencias[i]][preferencias[j]]['weight'] += 1
            else:
                G.add_edge(preferencias[i], preferencias[j], weight=1)

# Layout ajustado
pos = nx.spring_layout(G, seed=42, k=1.8)

plt.figure(figsize=(16, 12))

# Desenhar arestas
edges = G.edges(data=True)
weights = [min(edata['weight'], 5) for _, _, edata in edges]
nx.draw_networkx_edges(G, pos, edgelist=edges, width=weights, alpha=0.4, edge_color='gray')

# Adicionando os pesos (numerando as conexões)
edge_labels = {(u, v): d['weight'] for u, v, d in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Categorias
streamings = set(df['Streaming Principal'].unique()).union(df['Streaming Secundário'].unique())
esportes = set(df['Esporte Principal'].unique()).union(df['Esporte Secundário'].unique())

# Cores dos nós
node_colors = []
for node in G.nodes():
    if node in streamings:
        node_colors.append('#8ecae6')  # azul clarinho
    elif node in esportes:
        node_colors.append('#90be6d')  # verde clarinho
    else:
        node_colors.append('lightgray')

# Desenhar nós e labels
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color=node_colors, edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=9)

plt.title("Grafo de Coocorrência de Streaming e Esporte", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()

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

print("\n--- Métrica Topológicas: Grafo de Coocorrência ---")
print("\nVértices do Grafo de Coocorrência:\n")
print(identificar_vertices(G))
print("\nNúmero total de vértices no Grafo de Coocorrência:", contar_vertices(G))


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

print("\n---- Ligações do Grafo (Nó1, Nó2, Peso) ------")
ligacoes_G = listar_ligacoes(G)
for ligacao in ligacoes_G:
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

print("\n---- Contagem de Arestas ----")
total_arestas_G = contar_arestas(G)
print(f"Número total de arestas: {total_arestas_G}")



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
graus_G_df = graus_vertice(G, grau_minimo=1)
print(graus_G_df.to_string(index=False))


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

media_G = grau_medio(G)
print(f"Grau médio: {media_G:.2f}")

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

# A função mostrar_pesos_grafo já exibe os pesos para G por padrão
df_pesos_G = mostrar_pesos_grafo(G, exibir=False, como_dataframe=True)
df_pesos_G_ordenado = df_pesos_G.sort_values(by='PESO', ascending=False)
print(df_pesos_G_ordenado.to_string(index=False))

# Salvar no CSV (mantido apenas para o grafo G, como estava no seu código original)
df_pesos_G.to_csv('pesos_grafo.csv', index=False)


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

print("\n---- Força de Conectividade ----")

forca_media_G = calcular_forca_conectividade_media(G)
print(f"Força de conectividade média: {forca_media_G:.4f}")


# --------- FUNÇÃO 9 - Densidade

def calcular_densidade_rede(grafo):
    """
    Calcula a densidade de um grafo.

    Retorno:
    - Float: a densidade do grafo.
    """
    return nx.density(grafo)

# -------- SAIDA DA FUNÇÃO 9

print("\n----  Densidade ----")

densidade_G = calcular_densidade_rede(G)
print(f"Densidade do grafo: {densidade_G:.4f}")

