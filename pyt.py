import streamlit as st
import streamlit.components.v1 as components

# افتحي ملف HTML اللي معاكي
with open("genoscene.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# نضيف JavaScript يخلي الارتفاع يساوي ارتفاع نافذة المتصفح
full_screen_html = f"""
<script>
    function resizeIframe() {{
        var ifr = window.frameElement;
        if (ifr) {{
            ifr.style.height = window.innerHeight + "px";
            ifr.style.width = window.innerWidth + "px";
        }}
    }}
    window.onload = resizeIframe;
    window.onresize = resizeIframe;
</script>
{html_code}
"""

components.html(full_screen_html, height=0, scrolling=False)
