# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# %%
# Carrega os dados do arquivo CSV
df = pd.read_csv("mushroom_data.csv")
print(df.head())
# %%
# Converte a coluna 'Bruises' para string
for index in range(0,len(df['Bruises'])):
    df['Bruises'] = df['Bruises'].astype(str)
# Lista de nomes das colunas
columns = df.columns.tolist()
# Imprime os nomes das colunas
for column in df.columns:
    print(column)
    
# %%
# Gera gráficos de contagem para cada coluna
for column in columns:
    sns.countplot(x = df[column], data=df, order=df[column].value_counts().index)    
    plt.xticks(rotation=30, fontsize=10)
    plt.xlabel(column, fontsize=12)
    plt.title(column + " Value Counts")
    plt.show()
    plt.clf()
# %%
# Contagem de cogumelos comestíveis e venenosos
sns.countplot(x='Class', data=df)
plt.title("Distribuição de Cogumelos por Classe (Comestível vs Venenoso)")
plt.show()
# %%
# Contagem da forma mais comum
cap_shape_counts = df['Cap Shape'].value_counts()

print("Distribuição de Cap Shape:")
print(cap_shape_counts)

# Gráfico de barras para visualização
sns.countplot(x='Cap Shape', data=df, order=cap_shape_counts.index)
plt.title("Distribuição de Formas do Chapéu (Cap Shape)")
plt.xticks(rotation=30)
plt.show()
# %%
# %%
odor_counts = df['Odor'].value_counts()
print("Odor predominante nos cogumelos comestíveis:")
print(odor_counts)

# Gráfico de barras para visualização
sns.countplot(x='Odor', data=df, order=odor_counts.index)
plt.title("Distribuição de Odor nos Cogumelos Comestíveis")
plt.xticks(rotation=30)
plt.show()
# %%
#Conferindo os valores
print(df['Odor'].nunique())
# %%
# Tabela de contingência entre Cap Color e Odor
contingency_table = pd.crosstab(df['Cap Color'], df['Odor'])

print(contingency_table)

# Gráfico de barras
sns.countplot(x='Cap Color', hue='Odor', data=df)
plt.title("Relação entre Cap Color e Odor")
plt.xticks(rotation=30)
plt.show()

# %%
# Gráfico de barras para relação entre Bruises e Class
sns.countplot(x='Class', hue='Bruises', data=df)
plt.title("Cogumelos com que são 'Bruises' tendem a ser comestíveis ou venenosos?")
plt.show()

# %%
# Relação entre Gill Size e Class
sns.countplot(x='Gill Size', hue='Class', data=df)
plt.title("Relação entre tamanho das branquias e Classe")
plt.show()

# Relação entre Gill Color e Class
sns.countplot(x='Gill Color', hue='Class', data=df)
plt.title("Relação entre cor das branquias e Classe")
plt.xticks(rotation=30)
plt.show()

# %%
# Gráfico de barras para distribuição de cogumelos por Habitat
plt.figure(figsize=(10, 6))
sns.countplot(x='Habitat', data=df)
plt.title("Distribuição de Cogumelos por Tipo de Habitat")
plt.xlabel("Habitat")
plt.ylabel("Contagem de Cogumelos")
plt.xticks(rotation=30)
plt.show()

# %%
# Filtrando cogumelos venenosos
poisonous_mushrooms = df[df['Class'] == 'Poisonous']

# Gráfico de barras para distribuição de cogumelos venenosos por Population
plt.figure(figsize=(10, 6))
sns.countplot(x='Population', data=poisonous_mushrooms)
plt.title("Distribuição de Cogumelos Venenosos por Population")
plt.xlabel("Population")
plt.ylabel("Contagem de Cogumelos Venenosos")
plt.xticks(rotation=30)
plt.show()

# %%
import seaborn as sns
import matplotlib.pyplot as plt

# Filtrar cogumelos que crescem no habitat 'urban'
urban_mushrooms = df[df['Habitat'] == 'Urban']

# Gráfico de barras para a Class dos cogumelos no habitat urban
plt.figure(figsize=(10, 6))
sns.countplot(x='Cap Color', hue='Class', data=urban_mushrooms)
plt.title("Distribuição de Cogumelos por Cap Color no Habitat Urban")
plt.xlabel("Cap Color")
plt.ylabel("Contagem")
plt.xticks(rotation=30)
plt.legend(title='Class')
plt.show()

# %%
# Contagem de cogumelos por habitat
total_cogumelos = df.shape[0]
urban_cogumelos = df[df['Habitat'] == 'Urban'].shape[0]

# Proporção atual de cogumelos no habitat urban
urban_ratio = urban_cogumelos / total_cogumelos
print(f"Proporção atual de cogumelos no habitat urban: {urban_ratio:.2%}")

# Projeção para um cenário futuro com 10.000 novos registros
futuro_total_cogumelos = 10000
projecao_urban = int(futuro_total_cogumelos * urban_ratio)
print(f"Projeção de cogumelos que crescerão no habitat urban: {projecao_urban}")

# %%
