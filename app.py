import json
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import networkx as nx

# Load clustered MITRE data
with open("clustered_mitre_data.json", "r", encoding="utf-8") as file:
    techniques = json.load(file)

df = pd.DataFrame(techniques)
df["cluster"] = df["cluster"].astype(str)  # for dropdown

# Generate a dummy network graph
G = nx.Graph()
for idx, row in df.iterrows():
    G.add_node(row["id"], label=row["name"], cluster=row["cluster"])
edges = [(df.iloc[i]["id"], df.iloc[j]["id"]) for i in range(len(df)) for j in range(i+1, len(df)) if df.iloc[i]["cluster"] == df.iloc[j]["cluster"]]
G.add_edges_from(edges)

# Prepare positions
pos = nx.spring_layout(G, seed=42)
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

# Dash App
app = dash.Dash(__name__)
app.title = "Threat Intelligence Framework"

app.layout = html.Div([
    html.H1("Threat Intelligence Visualization", style={"textAlign": "center"}),

    dcc.Dropdown(
        id="cluster-filter",
        options=[{"label": f"Cluster {c}", "value": c} for c in sorted(df["cluster"].unique())] + [{"label": "All Clusters", "value": "all"}],
        value="all",
        clearable=False,
        style={"width": "50%", "margin": "auto"}
    ),

    dcc.Graph(id="3d-scatter", style={"height": "80vh"}),
    dcc.Graph(id="network-graph", style={"height": "80vh"})
])

@app.callback(
    Output("3d-scatter", "figure"),
    [Input("cluster-filter", "value")]
)
def update_3d_graph(selected_cluster):
    filtered_df = df if selected_cluster == "all" else df[df["cluster"] == selected_cluster]
    fig = px.scatter_3d(
        filtered_df,
        x="id", y="cluster", z="name",
        text="name",
        color="cluster",
        template="plotly_dark"
    )
    fig.update_layout(
        margin=dict(l=0, r=0, b=0, t=50),
        hovermode="closest"
    )
    fig.update_traces(marker=dict(size=4))
    return fig

@app.callback(
    Output("network-graph", "figure"),
    [Input("cluster-filter", "value")]
)
def update_network(selected_cluster):
    filtered_nodes = [n for n, attr in G.nodes(data=True) if selected_cluster == "all" or attr["cluster"] == selected_cluster]
    subgraph = G.subgraph(filtered_nodes)
    sub_pos = nx.spring_layout(subgraph, seed=42)

    edge_x = []
    edge_y = []
    for edge in subgraph.edges():
        x0, y0 = sub_pos[edge[0]]
        x1, y1 = sub_pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    node_x = []
    node_y = []
    node_text = []
    for node in subgraph.nodes():
        x, y = sub_pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(subgraph.nodes[node]['label'])

    fig = px.scatter()
    fig.add_scatter(x=edge_x, y=edge_y, mode="lines", line=dict(width=0.5, color="#888"), hoverinfo="none")
    fig.add_scatter(x=node_x, y=node_y, mode="markers+text", text=node_text, textposition="top center", marker=dict(size=10, color="LightSkyBlue"))

    fig.update_layout(
        showlegend=False,
        hovermode="closest",
        margin=dict(l=0, r=0, t=20, b=20),
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False)
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)
