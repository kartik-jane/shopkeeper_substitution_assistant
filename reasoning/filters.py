def apply_filters(G, candidates, max_price, required_tags):
    results = []

    for pid, depth in candidates:
        p = G.nodes[pid]

        if not p["in_stock"]:
            continue
        if p["price"] > max_price:
            continue
        if not set(required_tags).issubset(set(p["attributes"])):
            continue

        results.append((pid, depth))

    return results
