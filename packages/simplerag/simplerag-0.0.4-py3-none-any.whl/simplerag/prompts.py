from langchain.prompts import PromptTemplate
from langchain.memory import ConversationSummaryMemory


class Prompt_Template:
    # def __init__(self,chain_type):
    #     self.chain_type = chain_type

    def stuff_template(self,
                       prompt="You are a question answering expert. Use the following pieces of context to answer the question at the end. Don't add anything which is not present in the given text. If you don't know the answer, just say that you don't know, don't try to make up an answer.\nGive a very detailed answer.\n{context}\n\nQuestion: {question}\nHelpful Answer:",
                       input_variables_names=["context", "question"], verbose=False):
        prompt_template = PromptTemplate(
            template=prompt, input_variables=input_variables_names)

        chain_type_kwargs = {"verbose": verbose, "prompt": prompt_template}

        return chain_type_kwargs

    def map_reduce_template(self, llm,
                            prompt="""You are a question answering expert. Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.\nGive a very detailed answer.\n{context}\n\nQuestion: {question}\nHelpful Answer:""",
                            combine_prompt="Generate a summary of the following text that includes the following elements:\n\n* A title that accurately reflects the content of the text.\n* An introduction paragraph that provides an overview of the topic.\n* Bullet points that list the key points of the text.\n* A conclusion paragraph that summarizes the main points of the text.\n\nText:`{context}`",
                            qa_input_variables_names=['context', 'question'], combine_input_variables=["context"],
                            verbose=False):
        prompt = PromptTemplate(template=prompt,
                                input_variables=qa_input_variables_names)

        combine_prompt_template = PromptTemplate(
            template=combine_prompt,
            input_variables=combine_input_variables)

        chain_type_kwargs = {
            "verbose": verbose,
            "question_prompt": prompt,
            "combine_prompt": combine_prompt_template,
            "combine_document_variable_name": "context",
            "memory": ConversationSummaryMemory(
                llm=llm,
                memory_key="history",
                input_key="question",
                return_messages=True)}

        return chain_type_kwargs
