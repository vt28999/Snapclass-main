import streamlit as st


def footer_home():
      logo_url = "https://i.ibb.co/KxF3FG88/photo.jpg"
      st.markdown(f"""
       <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
       <p style="font-weight:bold; color:white;">created by ❤️</p>
       <img src='{logo_url}' style='max-height:60px' />
      
     </div>

     

        """,  unsafe_allow_html=True)