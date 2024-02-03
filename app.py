import streamlit as st
from Multiapp import Multipage
from apps import pride_and_prejudice,animal_farm,the_universe,oldmansea
from apps import of_mice_men


def apps():
    app = Multipage()
    app.add_page("Pride and Prejudice", pride_and_prejudice.app)
    app.add_page("Animal Farm",animal_farm.app)
    app.add_page("The Theory of Everything The Origin and Fate of the Universe", the_universe.app)
    app.add_page("Old Man and the Sea",oldmansea.app)
    app.add_page("Of Mice and Men", of_mice_men.app)
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



