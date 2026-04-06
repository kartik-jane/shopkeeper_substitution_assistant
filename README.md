# 🛒 Shopkeeper Product Substitution Assistant  
**(Knowledge Graph + Rule-Based Reasoning | Streamlit App)**

🔗 **Live App:**  
https://shopkeeper-substitute.streamlit.app/

🔗 **GitHub Repository:**  
https://github.com/<kartik-jane>/shopkeeper_substitution_assistant

---

## 📌 Project Overview

This project is a **Streamlit-based web application** that assists shopkeepers in finding **suitable alternative products** when a requested item is **out of stock**.

Unlike ML-based recommenders, this system is built using:
- a **Knowledge Graph (KG)**  
- **classical graph traversal**
- **explicit rule-based reasoning**

This ensures transparency, explainability, and deterministic behavior.

---

## 🎯 Key Features

- Search for a product by name
- Apply constraints:
  - maximum price
  - required attributes (tags)
  - optional brand
- If product is **in stock** → show it directly
- If product is **out of stock** → suggest up to **3 substitutes**
- Each substitute includes a **clear rule-based explanation**

---

## 🧠 Knowledge Graph Design

### Node Types
- **Product**
- **Category**
- **Brand**
- **Attribute**

### Edge Types
- `IS_A` → Product → Category  
- `HAS_BRAND` → Product → Brand  
- `HAS_ATTRIBUTE` → Product → Attribute  
- `SIMILAR_TO` → Category → Category (optional)

The Knowledge Graph is implemented using **NetworkX**.

---

## 🔍 Reasoning & Search Approach

### Graph Traversal
- BFS traversal starting from the requested product
- Priority order:
  1. Same category products
  2. Related category products

### Filtering Rules
- Product must be **in stock**
- Must satisfy **all required attributes**
- Must be within **maximum price**

### Scoring Factors
- Category closeness
- Brand match (if provided)
- Attribute match
- Price comparison

Top 3 products are returned after scoring.

---

## 🧾 Rule-Based Explanations

Each suggested product includes explanations derived from **explicit rules**, such as:

- `same_category_same_brand`
- `same_category_diff_brand`
- `all_required_tags_matched`
- `cheaper_option`

Example explanation:
> “Suggested because it belongs to the same category, matches all required attributes, and is priced within your budget.”

---

## 🖥 Streamlit User Interface

### Inputs
- Product selection (dropdown / text)
- Max price
- Required attributes (multi-select)
- Optional brand

### Outputs
- Exact product (if available)
- OR up to 3 substitute products with explanations
- Clear message if no alternative is found

---

## 📁 Project Structure
```
shopkeeper_substitution_assistant/
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│ ├── attributes.json
│ ├── brands.json
│ ├── categories.json
│ └── products.json
│
├── kg/
│ └── graph_builder.py
│
├── reasoning/
│ ├── availability_checker.py
│ ├── graph_traversal.py
│ ├── filters.py
│ ├── scoring.py
│ └── explanations.py
│
├── services/
│ └── substitution_service.py
│
└── tests/
└── test_graph.py

```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<kartik-jane>/shopkeeper_substitution_assistant.git
cd shopkeeper_substitution_assistant
```

2️⃣ Create and activate virtual environment
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell
```
3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Run tests
```bash
python -m tests.test_graph
```

5️⃣ Start the application
```bash
streamlit run app.py
```
🚀 Deployment

The application is deployed using Streamlit Community Cloud.

🔗 Live URL:
https://shopkeeper-substitute.streamlit.app/

## ✅ Assignment Compliance Checklist
Requirement	Status
### Knowledge Graph implementation  ✅
### Graph traversal reasoning	      ✅
### Rule-based explanations	        ✅
### Streamlit UI	                  ✅
### Deployed application	          ✅

## 👤 Author

- Kartik Jane
- Shopkeeper Product Substitution Assistant
- Knowledge Graph & Rule-Based Reasoning Project
