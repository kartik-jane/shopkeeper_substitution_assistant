def generate_explanation(G, pid, requested_product):
    """
    Generate explicit rule-based explanation
    as required by the assignment.
    """

    p = G.nodes[pid]
    req = G.nodes[requested_product]

    rules = []

    # Rule: Category + Brand combination
    if p["category"] == req["category"]:
        if p["brand"] == req["brand"]:
            rules.append("RULE: same_category_same_brand")
        else:
            rules.append("RULE: same_category_diff_brand")
    else:
        rules.append("RULE: related_category")

    # Rule: Required attributes
    rules.append("RULE: all_required_tags_matched")

    # Rule: Cheaper option
    if p["price"] < req["price"]:
        rules.append("RULE: cheaper_option")

    return ", ".join(rules)
