import streamlit as st
import bin2dec as db
import dec2bin as bd

st.markdown("<h1 style='text-align: center; color: red; font-size: 50px;'>Welcome to Binary-Decimal Converter</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 25px;'>Aron James C. Toverada</h1>", unsafe_allow_html=True)
st.subheader('Binary to Decimal Converter', divider="red")

# user input for binary to decimal conversion
st.text_input('Enter the Binary Number:', key="binary_number")
print(st.session_state)
st.button('Convert', key='convert_button_2')

# conversion function
if st.session_state["convert_button_2"]:
    decimal_num = db.bin2dec(str(st.session_state["binary_number"]))
    st.session_state["dec_number"] = decimal_num
    st.write("Binary number equivalent to Decimal = ", str(decimal_num))

st.divider()
st.subheader('Decimal to Binary Converter', divider='red')
# user input for decimal to binary conversion
st.text_input('Enter the Decimal Number:', key='decimal_number')
print(st.session_state)
st.button('Convert', key='convert_button')

# conversion function
if st.session_state['convert_button']:
    binary_num = bd.dec2bin(int(st.session_state['decimal_number']))
    st.session_state['bin_number'] = binary_num
    st.write('Decimal number equivalent to binary =', str(binary_num))
