import streamlit as st
import numpy as np
import Adding_matrices as am
import Multiplying_matrices as mm
import Determinant_of_matrices as dm
import Transpose_of_matrices as tm
import Inverse_of_matrices as im

st.markdown(
    """
    <style>
    .stApp{
        background-color : #3BBA9C;

    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center; color: #2E3047; font-size: 50px;'>MATRIX CALCULATOR</h1>", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
            <h1 style="font-size: 24px; text-align: center">
            Enter the size of the matrices:
            </h1>
        """, unsafe_allow_html=True)
with col2:
    row = st.number_input("ROW:", min_value=1, max_value=5, key='row')
with col3:
    column = st.number_input("COLUMN:", min_value=1, max_value=5, key='column')

col4, col5 = st.columns(2)
with col4:
    st.markdown("""
            <h1 style="font-size: 24px; text-align: center;">
            Matrix A
            </h1>
        """, unsafe_allow_html=True)
    for row_index in range(row):
        columns = st.columns(column)
        for col_index, col in enumerate(columns):
            with col:
                st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')

with col5:
    st.markdown("""
                <h1 style="font-size: 24px; text-align: center;">
                Matrix B
                </h1>
            """, unsafe_allow_html=True)
    for row_index in range(row):
        columns = st.columns(column)
        for col_index, col in enumerate(columns):
            with col:
                st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
matA = []
matB = []
for i in range(row):
    rowSum = []
    for j in range(column):
        for value in st.session_state:
            if value == f"Arow{i+1}Acol{j+1}":
                rowSum.append(st.session_state[value])
    matA.append(rowSum)
print(matA)
for i in range(row):
    rowSum = []
    for j in range(column):
        for value in st.session_state:
            if value == f"Brow{i+1}Bcol{j+1}":
                rowSum.append(st.session_state[value])
    matB.append(rowSum)
print(matB)
print(st.session_state)

option = st.selectbox("Operation", ("A + B", "A x B", "Determinant", "Transpose of the matrices", "Inverse"))
if option == "A + B":
    calculate = st.button("Calculate", key='AplusB')
    if calculate:
        st.markdown("""
                        <h1 style="font-size: 24px; text-align: 'Center';">
                        Matrix Result
                        </h1>
                    """, unsafe_allow_html=True)
        matrix_Result = am.get_sumOfMatrices(matA, matB)
        col6, col7, col8 = st.columns(3)
        with col7:
            for row_index in range(row):
                columns = st.columns(column)
                for col_index, col in enumerate(columns):
                    with col:
                        st.text_input("", value=matrix_Result[row_index][col_index],
                                      key=f'Rrow{row_index + 1}Rcol{col_index + 1}')

if option == "A x B":
    calculate = st.button("Calculate", key='AtimesB')
    if calculate:
        st.markdown("""
                        <h1 style="font-size: 24px; text-align: 'Center';">
                        Matrix Result
                        </h1>
                    """, unsafe_allow_html=True)
        matrix_Result = mm.multiply_matrices(matA, matB)
        col6, col7, col8 = st.columns(3)
        with col7:
            for row_index in range(row):
                columns = st.columns(column)
                for col_index, col in enumerate(columns):
                    with col:
                        st.text_input("", value=matrix_Result[row_index][col_index],
                                      key=f'Rrow{row_index + 1}Rcol{col_index + 1}')

if option == "Determinant":
    calculate = st.button("Calculate", key='determinantAB')
    if calculate:
        if len(matA[0]) != len(matB):
            st.error("Cannot perform calculation. The matrices must be squared.")
        else:
            Amat, Bmat = dm.determinant_matrices(matA, matB)
            col6, col7 = st.columns(2)
            with col6:
                st.markdown("""
                        <h1 style="font-size: 24px; text-align: center; color: #2E3047;">
                        Determinant of Matrix A</h1>
                        """, unsafe_allow_html=True)
                st.text_input("", value = str(Amat))
            with col7:
                st.markdown("""
                        <h1 style="font-size: 24px; text-align: center; color: #2E3047;">
                        Determinant of Matrix B
                         </h1>
                        """, unsafe_allow_html=True)
                st.text_input("", value = str(Bmat))

if option == "Transpose of the matrices":
    calculate = st.button("Calculate", key='transposeAB')
    if calculate:
        Amat, Bmat = tm.transpose_matrices(matA, matB)
        col6, col7 = st.columns(2)
        with col6:
            st.markdown("""
                            <h1 style="font-size: 24px; text-align: center; color: #2E3047;">
                            Transpose of Matrix A</h1>
                            """, unsafe_allow_html=True)
            st.text_input("", value=str(Amat))
        with col7:
            st.markdown("""
                            <h1 style="font-size: 24px; text-align: center; color: #2E3047;">
                            Transpose of Matrix B
                             </h1>
                            """, unsafe_allow_html=True)
            st.text_input("", value=str(Bmat))

if option == "Inverse":
    calculate = st.button("Calculate", key='inverseAB')
    if calculate:
        Amat, Bmat = im.inverse_matrices(matA, matB)
        col6, col7 = st.columns(2)
        with col6:
            st.markdown("""
                            <h1 style="font-size: 24px; text-align: center; color: #2E3047;">
                            Inverse of Matrix A</h1>
                            """, unsafe_allow_html=True)
            st.text_input("", value=str(Amat))
        with col7:
            st.markdown("""
                            <h1 style="font-size: 24px; text-align: center; color: #2E3047;">
                            Inverse of Matrix B
                             </h1>
                            """, unsafe_allow_html=True)
            st.text_input("", value=str(Bmat))