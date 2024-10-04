import streamlit as st
import numpy as np

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
st.markdown("<h1 style='text-align: center; color: #2E3047; font-size: 60px;'>SYSTEMS OF EQUATIONS CALCULATOR</h1>", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown("""
                <h1 style="font-size: 24px; text-align: center">
                Enter the size of the matrices:
                </h1>
            """, unsafe_allow_html=True)
with col2:
    row = st.number_input("", min_value = 2, max_value = 5,)

a = []
b = []

for i in range(row):
    st.markdown(f"<h1 style='text-align: center; color: #66FCF1; font-size: 30px;'> Equation {i + 1}</h1>", unsafe_allow_html=True)
    col = st.columns(row, gap="medium")
    for j in range(row):
        with col[j]:
            st.markdown(f"<span style='align: center; color: #C5C6C7;'> Coefficient {j + 1}</span>", unsafe_allow_html=True)
            coeff = st.number_input("", key=f"coeff_{i}_{j}", format="%f")
            a.append(coeff)
        if j == row - 1:
            with col[j]:
                st.markdown(f"<span style='color: #45A29E   ; text-align: center;'>Constant:</span>", unsafe_allow_html=True)
                const = st.number_input("", key=f"const_{i}")
                b.append(const)
st.divider()
def inverse_matrix(a):
    matrix_inv = np.linalg.inv(a)
    return matrix_inv


def solve_system(a,b):
    coefficients = np.array(a)
    constants = np.array(b)

    matrix_inv = np.linalg.inv(a)
    solution = np.dot(matrix_inv, constants)
    return solution

a = np.array(a).reshape(row,row)
b = np.array(b)

if st.button("Solve"):

    if a.shape[0] != a.shape[1]:
        raise ValueError("Coefficients matrix must be square.")

    if np.linalg.det(a) == 0:
        raise ValueError("Coefficients matrix is singular and cannot be inverted.")

    A = inverse_matrix(a)
    B = b
    X = solve_system(a,b)

    st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
                            <h1 style="font-size: 30px; text-align: center; color:#C5C6C7">
                            Inverse of A:
                            </h1>
                            """, unsafe_allow_html=True)
        st.write(np.round(A, 2))

    with col2:
        st.markdown("""
                                        <h1 style="font-size: 30px; text-align: center; color: #C5C6C7">
                                        B:
                                        </h1>
                                        """, unsafe_allow_html=True)
        st.write(np.round(b, 2))
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
                       <h1 style="font-size: 30px; text-align: center; color: #66FCF1">
                       THE ROOTS OF AN EQUATION:
                       </h1>
                       """, unsafe_allow_html=True)
    for i, root in enumerate(X):
        st.markdown(f"<h3 style='color: white; text-align: center;'>X<sub>{i + 1}</sub>: {root}</h3>", unsafe_allow_html=True)

st.write('##')
st.write('##')
st.write('##')
st.write('##')
st.write('##')

st.markdown("<h2 style='text-align: center; color: #66FCF1; font-size: 20px;'>Aron James C. Toverada</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #66FCF1; font-size: 20px;'>Mario D. Naive Jr.</h2>", unsafe_allow_html=True)




