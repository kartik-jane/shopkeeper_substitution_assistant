import networkx as nx
import json

def build_graph():
    G = nx.Graph()

    # Load data
    products = json.load(open("data/products.json"))
    categories = json.load(open("data/categories.json"))

    # Add category similarity edges
    for cat, similar in categories.items():
        for s in similar:
            G.add_edge(cat, s, relation="SIMILAR_TO")

    # Add products
    for p in products:
        pid = p["id"]
        G.add_node(pid, **p, type="product")

        G.add_node(p["category"], type="category")
        G.add_edge(pid, p["category"], relation="IS_A")

        G.add_node(p["brand"], type="brand")
        G.add_edge(pid, p["brand"], relation="HAS_BRAND")

        for attr in p["attributes"]:
            G.add_node(attr, type="attribute")
            G.add_edge(pid, attr, relation="HAS_ATTRIBUTE")

    return G
