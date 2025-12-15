from kg.graph_builder import build_graph

def test_graph_build():
    G = build_graph()

    print("\n--- NODES ---")
    for node, data in G.nodes(data=True):
        print(node, data)

    print("\n--- EDGES ---")
    for u, v, data in G.edges(data=True):
        print(u, "->", v, data)

if __name__ == "__main__":
    test_graph_build()
