import streamlit as st
import random
import openai

st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="centered")

# Logo animation
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

menu = st.sidebar.selectbox("Choose a topic", [
    "🏠 Home", "🧬 Functional Groups", "🔤 IUPAC Naming",
    "📈 Homologous Series", "🧠 Quick Quiz", "🤖 AI Compound Naming"
])

if menu == "🏠 Home":
    st.image("https://cdn.pixabay.com/photo/2020/02/06/08/19/science-4825122_960_720.jpg", use_column_width=True)
    st.header("Welcome to the Organic Chemistry Tutor")
    st.markdown("""
    ### 🎯 What this app offers:
    - Learn **functional groups**
    - Practice **IUPAC naming**
    - Explore **homologous series**
    - Take a quick quiz 🧠
    - Use **AI** to name organic compounds
    """)
    st.success("Use the sidebar on the left to explore each section 👈")

elif menu == "🧬 Functional Groups":
    groups = {
        "Alkane": {"Group": "C-C", "Example": "Ethane (C2H6)", "Desc": "Only single bonds."},
        "Alkene": {"Group": "C=C", "Example": "Ethene (C2H4)", "Desc": "Contains a double bond."},
        "Alkyne": {"Group": "C≡C", "Example": "Ethyne (C2H2)", "Desc": "Contains a triple bond."},
        "Alcohol": {"Group": "-OH", "Example": "Ethanol (C2H5OH)", "Desc": "Contains hydroxyl group."}
    }
    for name, info in groups.items():
        with st.expander(name):
            st.write(f"**Group:** {info['Group']}")
            st.write(f"**Example:** {info['Example']}")
            st.write(f"**Description:** {info['Desc']}")

elif menu == "🔤 IUPAC Naming":
    formula = st.text_input("Enter a formula (e.g., CH3COOH):")
    lookup = {"CH3COOH": "Ethanoic Acid", "C2H5OH": "Ethanol"}
    if formula:
        st.markdown(f"**IUPAC Name:** {lookup.get(formula, 'Not found')}")

elif menu == "📈 Homologous Series":
    n = st.slider("Select value of n", 1, 10, 1)
    st.write(f"Alkane: C{n}H{2*n+2}")
    st.write(f"Alkene: C{n}H{2*n}")
    st.write(f"Alkyne: {'Invalid' if n < 2 else f'C{n}H{2*n-2}'}")
    st.write(f"Alcohol: C{n}H{2*n+1}OH")

elif menu == "🧠 Quick Quiz":
    question = "What group is in ethanol?"
    options = ["Ketone", "Alcohol", "Alkene"]
    answer = st.radio(question, options)
    if st.button("Submit"):
        if answer == "Alcohol":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. It's Alcohol.")

elif menu == "🤖 AI Compound Naming":
    st.subheader("Use AI to suggest IUPAC names")
    openai.api_key = st.secrets.get("openai_api_key", "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")
    user_input = st.text_input("Enter compound description or formula:")
    if user_input and openai.api_key != "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":
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You're a chemistry tutor. Give IUPAC names."},
                        {"role": "user", "content": f"Name this compound: {user_input}"}
                    ],
                    max_tokens=100
                )
                st.success(response.choices[0].message['content'].strip())
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
    elif user_input:
        st.warning("⚠️ Please add your OpenAI API key in Streamlit Secrets.")
