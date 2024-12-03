from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_summary_chain(llm):
    summary_prompt = """
    Summarize the following text (maximum 100 words):
    Text: {text}
    """
    summary_prompt_template = PromptTemplate(template=summary_prompt, input_variables=["text"])
    return LLMChain(llm=llm, prompt=summary_prompt_template)

def summarize_document(summary_chain, doc_content):
    return summary_chain.run({"text": doc_content})
