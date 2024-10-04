import streamlit as st
from streamlit import switch_page

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://wallpapercave.com/wp/8mwqkt3.png");
    background-size: 100vw 40vh;
    background-position: 0px 0px;  
    background-repeat: no-repeat;
    background-attachment: local, scroll;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stApp{
        background-color : #1F2833;

    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center; color: #2E3047; font-size: 50px;'>COMPILATION OF CODING EXERCISES IN ADVANCED MATH</h1>", unsafe_allow_html=True)

st.write('##')
st.write('##')

col1, col2, col3 = st.columns(3, gap='medium')
with col1:
    st.markdown("<h4 style='text-align: left; color:#00ffff'>A systems of equations calculator</h4> <h4 style='text-align: left;'>that simplifies solving multiple equations, providing quick solutions for variables with step-by-step explanations.</h4>", unsafe_allow_html=True)

with col2:
    st.markdown(
        "<h4 style='text-align: left; color:#00ffff'>A binary-decimal converter</h4> <h4 style='text-align: left;'>that translates numbers between binary systems for computational use.</h4>" ,unsafe_allow_html=True)
with col3:
    st.markdown(
        "<h4 style='text-align: left; color:#00ffff'>A matrix calculator</h4> <h4 style='text-align: left;'>that performs operations like addition, multiplication, and inversion on matrices for mathematical computations.</h4>",
        unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)
with col4:
    if st.button("Calculator", key="button"):
        switch_page("pages/Systems of Equations Calculator.py")
with col5:
    if st.button("Calculator", key="button2"):
        switch_page("pages/Binary-Decimal Converter.py")
with col6:
    if st.button('Calculator', key='button3'):
        switch_page('pages/Matrix Calculator.py')

st.write('##')

st.markdown("<h1 style='text-align: center; color: #00ffff; font-size: 20px;'> A COMPILATION BY ARON JAMES C.TOVERADA</h1>", unsafe_allow_html=True)













