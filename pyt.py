import streamlit as st
import streamlit.components.v1 as components

# افتحي ملف الـ HTML بتاعك
with open("genoscene.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# غلاف CSS يخلي الـ iframe ياخد كل حجم النافذة
full_screen_html = f"""
<style>
iframe {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100% !important;
    height: 100% !important;
    border: none;
    margin: 0;
    padding: 0;
}}
</style>
{html_code}
"""

# نعرض الـ HTML جوه Streamlit
components.html(full_screen_html, height=900, scrolling=False)
