import streamlit as st
import random
import openai
from PIL import Image

# Set up Streamlit app configuration
st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="centered")

# Custom HTML logo animation
st.markdown("""
<style>
.logo-container {
  text-align: center;
  padding-bottom: 20px;
}
.logo-container img {
  width: 120px;
  animation: spin 4s linear infinite;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
<div class="logo-container">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Chemical_structure.svg/1024px-Chemical_structure.svg.png" />
</div>
""", unsafe_allow_html=True)

st.title("🌿 Organic Chemistry Tutor")

# Sidebar menu selection
menu = st.sidebar.selectbox("Choose a topic", [
    "🏠 Home",
    "🧬 Functional Groups",
    "🔤 IUPAC Naming",
    "📈 Homologous Series",
    "🧠 Quick Quiz",
    "🤖 AI Compound Naming"
])

# ------------------------ Home Page ------------------------
if menu == "🏠 Home":
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/DNA_double_helix_structure.svg/640px-DNA_double_helix_structure.svg.png", use_container_width=True)
    st.header("Welcome to the Organic Chemistry Tutor")
    st.markdown("""
    ### 🎯 What this app offers:
    - Understand **functional groups** with interactive cards
    - Master **IUPAC naming** of compounds
    - Explore **homologous series** with adjustable formulas
    - Challenge yourself with a **Quick Quiz**
    - Use **AI** to name complex compounds instantly 🔬

    📚 Whether you're in SS2 or just curious, this app is your chemistry toolkit!
    """)
    st.success("Tip: Use the sidebar on the left to explore each section 👈")

# ------------------------ Functional Groups ------------------------
elif menu == "🧬 Functional Groups":
    st.header("🧬 Common Functional Groups")

    groups = {
        "Alkane": {"Group": "C-C (single bond)", "Example": "Ethane (C2H6)", "Desc": "Saturated hydrocarbon with only single bonds."},
        "Alkene": {"Group": "C=C (double bond)", "Example": "Ethene (C2H4)", "Desc": "Unsaturated hydrocarbon with one or more double bonds."},
        "Alkyne": {"Group": "C≡C (triple bond)", "Example": "Ethyne (C2H2)", "Desc": "Unsaturated hydrocarbon with one or more triple bonds."},
        "Alcohol": {"Group": "-OH", "Example": "Ethanol (C2H5OH)", "Desc": "Contains a hydroxyl group."},
        "Carboxylic Acid": {"Group": "-COOH", "Example": "Ethanoic acid (CH3COOH)", "Desc": "Contains a carboxyl group; acidic."},
        "Ketone": {"Group": "C=O (within chain)", "Example": "Propanone (CH3COCH3)", "Desc": "Contains a carbonyl group bonded to two carbon atoms."},
        "Aldehyde": {"Group": "-CHO", "Example": "Ethanal (CH3CHO)", "Desc": "Carbonyl group at end of chain."},
        "Ester": {"Group": "-COO-", "Example": "Ethyl ethanoate (CH3COOC2H5)", "Desc": "Formed from acid + alcohol."},
        "Amine": {"Group": "-NH2", "Example": "Methylamine (CH3NH2)", "Desc": "Contains an amino group."}
    }

    for name, info in groups.items():
        with st.expander(name):
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Organic_functional_groups.svg/640px-Organic_functional_groups.svg.png", width=400)
            st.write(f"**Functional Group:** {info['Group']}")
            st.write(f"**Example:** {info['Example']}")
            st.write(f"**Description:** {info['Desc']}")

# ------------------------ IUPAC Naming ------------------------
elif menu == "🔤 IUPAC Naming":
    st.header("🔤 IUPAC Naming of Organic Compounds")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/IUPAC-2.svg/640px-IUPAC-2.svg.png", width=500)

    formula = st.text_input("Enter a compound formula (e.g., CH3COOH, C2H5OH):")
    if formula:
        sample_responses = {
            "CH3COOH": "**Ethanoic Acid** – A carboxylic acid with two carbon atoms.",
            "C2H5OH": "**Ethanol** – A two-carbon alcohol with a hydroxyl group.",
            "CH3CH2CH3": "**Propane** – A three-carbon alkane.",
            "CH3CH=CH2": "**Propene** – A three-carbon alkene with a double bond."
        }
        result = sample_responses.get(formula.strip(), "Compound not in database. Try a common organic molecule.")
        st.markdown(result)

# ------------------------ Homologous Series ------------------------
elif menu == "📈 Homologous Series":
    st.header("📈 Homologous Series and General Formulas")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Alkanes.svg/640px-Alkanes.svg.png", width=500)

    n = st.slider("Value of n (1–10)", min_value=1, max_value=10, value=1)

    st.subheader("Alkanes (CₙH₂ₙ₊₂)")
    st.write(f"Formula: C{n}H{2*n + 2}")

    st.subheader("Alkenes (CₙH₂ₙ)")
    st.write(f"Formula: C{n}H{2*n}")

    st.subheader("Alkynes (CₙH₂ₙ₋₂)")
    st.write(f"Formula: C{n}H{2*n - 2}" if n >= 2 else "Formula not valid for n < 2")

    st.subheader("Alcohols (CₙH₂ₙ₊₁OH)")
    st.write(f"Formula: C{n}H{2*n + 1}OH")

# ------------------------ Quick Quiz ------------------------
elif menu == "🧠 Quick Quiz":
    st.header("🧠 Quick Quiz: Functional Groups & Naming")

    quiz_questions = [
        {"question": "Which functional group does ethanol contain?", "options": ["Ketone", "Alcohol", "Alkene"], "answer": "Alcohol"},
        {"question": "What is the general formula for alkenes?", "options": ["CₙH₂ₙ", "CₙH₂ₙ₊₂", "CₙH₂ₙ₋₂"], "answer": "CₙH₂ₙ"},
        {"question": "Which group is represented by -COOH?", "options": ["Alcohol", "Ester", "Carboxylic Acid"], "answer": "Carboxylic Acid"},
        {"question": "Which hydrocarbon has a triple bond?", "options": ["Alkene", "Alkyne", "Alkane"], "answer": "Alkyne"},
        {"question": "Which functional group is present in esters?", "options": ["-OH", "-COOH", "-COO-"], "answer": "-COO-"}
    ]

    score = 0
    for q in quiz_questions:
        st.subheader(q["question"])
        user_answer = st.radio("Select one:", q["options"], key=q["question"])
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer is: {q['answer']}")

    st.markdown(f"### 🏁 Final Score: **{score} / {len(quiz_questions)}**")

# ------------------------ AI Naming Assistant ------------------------
elif menu == "🤖 AI Compound Naming":
    st.header("🤖 AI Compound Naming Assistant")
    st.image("https://upload.wikimedia.org/w
