import streamlit as st
import os
from llama_index.llms import GradientBaseModelLLM
# from llama_index import VectorStoreIndex,SimpleDirectoryReader
from llama_index import StorageContext,load_index_from_storage
from llama_index.embeddings import GradientEmbedding
from dotenv import load_dotenv
from llama_index import ServiceContext,set_global_service_context

def app():
    st.markdown("""### Pride and Prejudice """)
    def configure():
        load_dotenv()

    configure()

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

        storage_context = StorageContext.from_defaults(persist_dir="./pride_and_prej")
        new_index = load_index_from_storage(storage_context=storage_context)
        query_engine = new_index.as_query_engine()
        response = query_engine.query(inp)
        if response is not None:
            st.write(response.response)
