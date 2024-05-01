import streamlit as st
from pass_generate import Pin_code, Random_password, Memorable_password

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDm49qNBlWlNlOg3nO0BB0mf87TYGbMFzsRQ&s",600,200)
st.title("Password_generator")

opthion = st.radio("pleas select type",["pincode", "random_passwor", "memorable_password"])

if opthion == "pincode":
    length = st.slider("range paswword",4,12)
    seprator = st.text_input("seprator")
    password = Pin_code(length ,seprator)
    st.write(password.generate())

if opthion == "random_passwor":
    length = st.slider("pleas select length of password", 4, 12)
    seprator = st.text_input("seprator")
    includ_symbol = st.toggle("password contain of symbol", value=False)
    include_number = st .toggle("password contain of number", value=False)
    password = Random_password(length, seprator, include_number, includ_symbol)
    st.write(password.generate())

if opthion == "memorable_password":
    seprator = st.text_input("seprator")
    number_of_words = st.slider("pleas select number of words", 4, 12)
    capitalize = st.toggle("random of capitalize words", value=False)
    password = Memorable_password(number_of_words, capitalize, seprator)
    st.write(password.generate())
  