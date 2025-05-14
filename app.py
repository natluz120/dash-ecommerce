import pandas as pd

# Lê o CSV
df = pd.read_csv("ecommerce_estatistica (2).csv")

# Visualiza as primeiras linhas
print(df.head())

import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Lê o CSV
df = pd.read_csv("ecommerce_estatistica (2).csv")

# Cria o app Dash
app = Dash(__name__)

# Exemplo de gráfico 1: histograma de valores
histograma = px.histogram(df, x='ValorPedido', nbins=30, title='Distribuição do Valor dos Pedidos')

# Exemplo de gráfico 2: boxplot por categoria (se tiver)
if 'Categoria' in df.columns:
    boxplot = px.box(df, x='Categoria', y='ValorPedido', title='Boxplot: Valor por Categoria')
else:
    boxplot = None

# Layout do app
app.layout = html.Div([
    html.H1("Dashboard E-commerce"),
    dcc.Graph(figure=histograma),
    dcc.Graph(figure=boxplot) if boxplot else html.P("Coluna 'Categoria' não encontrada."),
])

if __name__ == '__main__':
    app.run_server(debug=True)
