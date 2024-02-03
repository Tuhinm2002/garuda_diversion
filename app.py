import streamlit as st
from Multiapp import Multipage
from apps import pride_and_prejudice,animal_farm


def apps():
    app = Multipage()
    app.add_page("Pride and Prejudice", pride_and_prejudice.app)
    app.add_page("Animal Farm",animal_farm.app)
    app.add_page("The Alchemist",the_alchemist.app)
    app.add_page("The Theory of Everything",theory_of_everything.app)
    app.run()
apps()
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")



