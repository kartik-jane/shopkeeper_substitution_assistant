import streamlit as st
from kg.graph_builder import build_graph
from services.substitution_service import find_substitutes

st.set_page_config(page_title="Product Substitution Assistant")

st.title("🛒 Shopkeeper Product Substitution Assistant")

# Build graph
G = build_graph()

# Get product list from KG
product_ids = [
    node for node, data in G.nodes(data=True)
    if data.get("type") == "product"
]

# Select OR type product
selected_product = st.selectbox(
    "Select Product (optional)",
    [""] + product_ids
)

typed_product = st.text_input("type product ID")

# Resolve product input
product = typed_product if typed_product else selected_product

max_price = st.number_input(
    "Maximum Price",
    min_value=0,
    max_value=500,
    value=60
)

tags = st.multiselect(
    "Required Tags",
    ["veg", "lactose_free", "sugar_free", "dairy"]
)

brand = st.text_input("Preferred Brand (optional)")

if st.button("Find Alternatives"):

    if not product:
        st.warning("⚠️ Please select or type a product.")
    
    elif product not in product_ids:
        st.error("❌ Product not found in Knowledge Graph.")
    
    else:
        result = find_substitutes(
            product_id=product,
            max_price=max_price,
            tags=tags,
            brand=brand or None
        )

        # Exact match available
        if "exact" in result:
            st.success("✅ Product Available")
            st.write(f"🛒 {result['exact']['name']}")
            st.write(f"💰 Price: ₹{result['exact']['price']}")

        # Alternatives
        else:
            alternatives = result.get("alternatives", [])

            if not alternatives:
                # GAP 4 covered here
                st.warning(
                    "❌ No alternatives found that satisfy "
                    "stock, price, and required tag constraints."
                )
            else:
                st.subheader("🔁 Suggested Alternatives")
                for alt in alternatives:
                    st.markdown(f"### {alt['product']['name']}")
                    st.write(f"💰 Price: ₹{alt['product']['price']}")
                    st.caption(f"🧠 {alt['explanation']}")
