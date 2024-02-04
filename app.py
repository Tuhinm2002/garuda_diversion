import streamlit as st
import streamlit_option_menu as option_menu
from Multiapp import Multipage
from apps import pride_and_prejudice,animal_farm,oldmansea
from apps import of_mice_men,the_alchemist,the_universe

st.set_page_config(layout="wide")

bg_image = """
                <style>
                [data-testid = "stAppViewContainer"] > .main {
                background-image: url("https://i.pinimg.com/originals/a7/9e/69/a79e69f1e792d396467b4a49f52f6497.gif");
                background-size: 100%;
                background-repeat: no-repeat;
                background-attachment: local;
                }
                </style>
                """
st.markdown(bg_image,unsafe_allow_html=True)

st.title("AI Library")
st.subheader("Not just read books, now chat with them and be tha part of the story")

with (st.container()):
    menu = option_menu.option_menu(
        menu_title= None,
        options=['Chat Area','About Us'],
        icons=['code-slash','person'],
        orientation='horizontal'
    )

    if menu == 'Chat Area':
        with st.container():

                st.title("Welcome to :rainbow[*Chat Area*]")
                st.write("##")
                st.write("##")

                def main():
                    def apps():
                        app = Multipage()
                        app.add_page("Pride and Prejudice", pride_and_prejudice.app)
                        app.add_page("Animal Farm", animal_farm.app)
                        app.add_page("The Alchemist", the_alchemist.app)
                        app.add_page("The Theory of Everything The Origin and Fate of the Universe", the_universe.app)
                        app.add_page("Old Man and the Sea", oldmansea.app)
                        app.add_page("Of Mice and Men", of_mice_men.app)
                        app.run()
                    apps()
                if __name__ == "__main__":
                    main()

st.write("##")
st.write("##")
st.write("---")
st.title("Subscribe to our :rainbow[*Newsletter*]")
email = st.text_input("Please subscribe to our page. (Enter your email address)")
rate = st.selectbox("Please give us a rating", ('Outstanding', 'Good', 'Understandable', 'Poor'))
button = st.button("Submit")
if button:
    st.markdown(f"""
    Your Inputs
    \nEmail: :rainbow[{email}]
    \nRating: :rainbow[{rate}]
    """)