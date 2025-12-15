import networkx as nx

def find_candidate_products(G, start_product, max_depth=2):
    visited = nx.single_source_shortest_path_length(
        G, start_product, cutoff=max_depth
    )

    candidates = []
    for node, depth in visited.items():
        if G.nodes[node].get("type") == "product" and node != start_product:
            candidates.append((node, depth))

    return candidates
