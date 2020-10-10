import streamlit as st
from execbox_side import execbox_side

st.beta_set_page_config(layout="wide")

execbox_side("""
import streamlit as st

with st.sidebar:
    st.write("Hello world!")

st.button("Press me!")

""", autorun=True, line_numbers=True)