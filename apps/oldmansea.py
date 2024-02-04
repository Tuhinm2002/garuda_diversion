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
    st.markdown("""### Old Man and the Sea """)

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

    def configure():
        load_dotenv()

    configure()

    def show_pdf(file):
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    show_pdf('oldmansea.pdf')

    inp = st.text_input("input")
    try:
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

            storage_context = StorageContext.from_defaults(persist_dir="./oldmansea")
            new_index = load_index_from_storage(storage_context=storage_context)
            query_engine = new_index.as_query_engine()
            response = query_engine.query(inp)
            if response is not None:
                st.write(response.response)
    except:
        pass
