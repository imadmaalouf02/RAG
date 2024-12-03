from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_translation_chain(llm):
    translation_prompt = """
    Translate the following text into English:
    Text: {text}
    """
    translation_prompt_template = PromptTemplate(template=translation_prompt, input_variables=["text"])
    return LLMChain(llm=llm, prompt=translation_prompt_template)

def translate_text(translation_chain, text):
    return translation_chain.run({"text": text})
