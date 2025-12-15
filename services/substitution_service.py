from kg.graph_builder import build_graph
from reasoning.availability_checker import check_availability
from reasoning.graph_traversal import find_candidate_products
from reasoning.filters import apply_filters
from reasoning.scoring import score_products
from reasoning.explanations import generate_explanation

# Build Knowledge Graph once
G = build_graph()


def find_substitutes(product_id, max_price, tags, brand=None):
    """
    Main orchestration function:
    - Checks availability
    - Traverses Knowledge Graph
    - Applies filters and scoring
    - Generates rule-based explanations
    """

    # Step 1: Exact availability check
    exact_product = check_availability(G, product_id)
    if exact_product:
        return {
            "exact": exact_product
        }

    # Step 2: Graph traversal (BFS)
    candidates = find_candidate_products(G, product_id)

    # Step 3: Rule-based filtering
    filtered_candidates = apply_filters(
        G,
        candidates,
        max_price=max_price,
        required_tags=tags
    )

    # Step 4: Rule-based scoring
    ranked_products = score_products(
        G,
        filtered_candidates,
        requested_product=product_id,
        preferred_brand=brand
    )

    # Step 5: Select top 3 substitutes with explanations
    alternatives = []
    for pid, score in ranked_products[:3]:
        alternatives.append({
            "product": G.nodes[pid],
            "explanation": generate_explanation(G, pid, product_id)
        })

    return {
        "alternatives": alternatives
    }
