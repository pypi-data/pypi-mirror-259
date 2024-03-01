from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma

class RAGInferencing:

    def get_answers(self, similarity_embeddings, llm_model, user_input, database_directory,chain_type_kwargs,
                    chroma_settings, hide_source=False, target_source_chunks=4):

        embeddings_model_name = similarity_embeddings
        persist_directory = database_directory


        embeddings = embeddings_model_name
        db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=chroma_settings)
        retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})

        qa = RetrievalQA.from_chain_type(llm=llm_model, chain_type="stuff", retriever=retriever,
                                         chain_type_kwargs=chain_type_kwargs,
                                         return_source_documents=not hide_source)

        query = user_input
        # Get the answer from the chain
        res = qa(query)
        answer, docs = res['result'], [] if hide_source else res['source_documents']

        #
        # # Print the result
        # print("\n\n> Question:")
        # print(query)
        # print(answer)
        #
        # # Print the relevant sources used for the answer
        document_names = []
        document_paragraphs = []
        # #
        for i, document in enumerate(docs):
            document_names.append(document.metadata["source"])
            document_paragraphs.append(document.page_content)
        return answer.strip(), document_names, document_paragraphs