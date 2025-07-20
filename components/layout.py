import streamlit as st

def render_header():
    st.image("assets/cover_light.png", use_container_width=True)

    st.markdown(
        "<h1 style='text-align: center;'>Westeros Coffee Shop Performance Overview </h1>",
        unsafe_allow_html=True,
    )
