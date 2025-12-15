def score_products(G, products, requested_product, preferred_brand=None):
    scores = []

    req = G.nodes[requested_product]

    for pid, depth in products:
        score = 0
        p = G.nodes[pid]

        if p["category"] == req["category"]:
            score += 5
        if preferred_brand and p["brand"] == preferred_brand:
            score += 3
        if p["price"] < req["price"]:
            score += 1

        score -= depth  # closer in graph = better

        scores.append((pid, score))

    return sorted(scores, key=lambda x: x[1], reverse=True)
