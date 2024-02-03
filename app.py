import streamlit as st
import streamlit_option_menu as option_menu
from Multiapp import Multipage
from apps import pride_and_prejudice,animal_farm,oldmansea
from apps import of_mice_men,the_alchemist,the_universe
from streamlit_card import card

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

with (st.container()):
    menu = option_menu.option_menu(
        menu_title= None,
        options=['Chat Area', 'Library', 'Pdf', 'About Us'],
        icons=['code-slash', 'eye', 'chat-left-text-fill', 'person'],
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

    if menu == 'Library':
        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.title("Welcome to :rainbow[*Library*]")
                st.write("##")
                st.write("##")
                res = card(
                    title="Pride and Prejudice",
                    text="The second novel by English author Jane Austen, published in 1813",
                    image="https://th.bing.com/th/id/OIP.wcZjPkH4FZD5QYi_2kfxxAAAAA?rs=1&pid=ImgDetMain",
                    styles={
                        "card": {
                            "width": "500px",
                            "height": "500px",
                            "border-radius": "0px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                        },
                        "text": {
                            "font-family": "serif",
                        }
                    }
                )
                st.write("##")
                st.write("##")
                st.write("##")
                res = card(
                    title="The Alchemist",
                    text="A novel by Brazilian author Paulo Coelho which was first published in 1988",
                    image="https://i.thenile.io/r1000/9781627656573.jpg?r=5e978aebc799f",
                    styles={
                        "card": {
                            "width": "500px",
                            "height": "500px",
                            "border-radius": "0px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                        },
                        "text": {
                            "font-family": "serif",
                        }
                    }
                )
                st.write("##")
                st.write("##")
                st.write("##")
                res = card(
                    title="Old Man and the Sea",
                    text="Written by the American author Ernest Hemingway between December 1950 and 1951",
                    image="https://imgv2-2-f.scribdassets.com/img/word_document/224414142/original/3addc8aa71/1618839523?v=1",
                    styles={
                        "card": {
                            "width": "500px",
                            "height": "500px",
                            "border-radius": "0px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                        },
                        "text": {
                            "font-family": "serif",
                        }
                    }
                )
            with col2:
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                res = card(
                    title="Animal Farm",
                    text="A satirical allegorical novella, by George Orwell, published in 1945.",
                    image="https://images.thenile.io/r1000/9780582434479.jpg",
                    styles={
                        "card": {
                            "width": "500px",
                            "height": "500px",
                            "border-radius": "0px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                        },
                        "text": {
                            "font-family": "serif",
                        }
                    }
                )
                st.write("##")
                st.write("##")
                st.write("##")
                res = card(
                    title="The Theory of Everything The Origin and Fate of the Universe",
                    text="Hawking reviews ideas about the universe from Aristotle to Einstein12.",
                    image="https://baazimagess3.s3-ap-southeast-1.amazonaws.com/product_media/9788179925911/md_9788179925911.jpg",
                    styles={
                        "card": {
                            "width": "500px",
                            "height": "500px",
                            "border-radius": "0px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                        },
                        "text": {
                            "font-family": "serif",
                        }
                    }
                )
                st.write("##")
                st.write("##")
                st.write("##")
                res = card(
                    title="Of Mice and Men",
                    text="A novella written by John Steinbeck. Published in 1937",
                    image="https://www.simbasible.com/wp-content/uploads/2017/08/micemen-877x1024.jpg",
                    styles={
                        "card": {
                            "width": "500px",
                            "height": "500px",
                            "border-radius": "0px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                        },
                        "text": {
                            "font-family": "serif",
                        }
                    }
                )
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