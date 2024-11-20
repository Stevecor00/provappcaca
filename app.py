import streamlit as st

st.text("ibijerubjejgi")

def main():
    st.text("il front-end funziona")
    num1=st.slider("inserisci il lato1", 0, 100, 2)
    num2=st.slider("inserisci il lato2", 0, 100, 3)
    r= num1+num2
    st.write("la somma è ", r)

if __name__=="__main__":
    main()