import streamlit as st
import pandas as pd

st.title("بروجكت Streamlit الأول 🚀")

data = {
    "الاسم": ["مريم", "أحمد", "خالد"],
    "الدرجة": [95, 88, 76]
}

df = pd.DataFrame(data)

st.write("الدرجات:")
st.dataframe(df)

if st.button("احسب المتوسط"):
    avg = df["الدرجة"].mean()
    st.success(f"متوسط الدرجات = {avg:.2f}")
