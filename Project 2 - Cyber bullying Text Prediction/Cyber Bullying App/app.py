import streamlit as st
import streamlit.components.v1 as stc
from app_content import *
from data import *



def main():
    menu = ['Home', 'Machine Learning']
    choice = st.sidebar.selectbox("Menu", menu)
    # Tulisan di sidebar dengan style HTML untuk pusat
    st.write(css, unsafe_allow_html=True)
    st.sidebar.write("<div style='text-align:center; margin:40px 0px 10px 0px;'>By</div>", unsafe_allow_html=True)
    st.sidebar.write("<div class='elegant-text'>Muhammad Naufal Fadhilah</div>", unsafe_allow_html=True)
    
    if choice == 'Home':
        home_content()
        
    elif choice == 'Machine Learning':
        ml_content()


if __name__ == '__main__':
    main()
