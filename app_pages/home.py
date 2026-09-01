import streamlit as st

def show():

    st.title("Welcome to Oil & Gas Calculators")
    st.markdown("""**Oil & Gas Engineering Calculator Suite**, a lightweight application designed to streamline common calculations used in drilling, mud logging, and wellsite operations.

Use the navigation sidebar to access the available engineering calculators. Each tool is designed to deliver fast, accurate, and user-friendly calculations to support operational decision-making in the field.

This application is continuously developed and improved to enhance productivity and reduce calculation errors.

**Developed by Hassan Abdelghany**

**SDL Field Engineer • Python Developer • Petroleum Geologist**
""")
    st.markdown("\n")
    st.markdown("Currently, the following calculator is available:")
    st.markdown("- Slug Effect Calculator")
    st.markdown("- Pump Output Calculator")