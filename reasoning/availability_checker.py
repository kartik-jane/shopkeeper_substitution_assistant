def check_availability(G, product_id):
    if product_id not in G:
        return None

    product = G.nodes[product_id]
    if product.get("in_stock"):
        return product

    return None
