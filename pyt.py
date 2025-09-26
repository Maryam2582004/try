import streamlit as st
import streamlit.components.v1 as components

# نقرأ محتوى ملف HTML ونمرره للـ components
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=500, scrolling=True)
