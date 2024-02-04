import streamlit as st
import os
from llama_index.llms import GradientBaseModelLLM
# from llama_index import VectorStoreIndex,SimpleDirectoryReader
from llama_index import StorageContext,load_index_from_storage
from llama_index.embeddings import GradientEmbedding
from dotenv import load_dotenv
from llama_index import ServiceContext,set_global_service_context
from streamlit_card import card
import base64
def app():
    st.markdown("""### Of Mice and Men """)

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

    def configure():
        load_dotenv()

    configure()

    def show_pdf(file):
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    show_pdf('OfMiceAndMen.pdf')

    inp = st.text_input("input")
    if inp is not None:
        llm = GradientBaseModelLLM(
            base_model_slug="llama2-7b-chat",
            max_tokens=400
        )

        embed_model = GradientEmbedding(
            gradient_access_token=os.environ['GRADIENT_ACCESS_TOKEN'],
            gradient_workspace_id=os.environ['GRADIENT_WORKSPACE_ID'],
            gradient_model_slug="bge-large"
        )

        service_context = ServiceContext.from_defaults(llm=llm,
                                                       embed_model=embed_model,
                                                       chunk_size=256
                                                       )
        set_global_service_context(service_context=service_context)

        storage_context = StorageContext.from_defaults(persist_dir="./of_mice_men")
        new_index = load_index_from_storage(storage_context=storage_context)
        query_engine = new_index.as_query_engine()
        response = query_engine.query(inp)
        if response is not None:
            st.write(response.response)
