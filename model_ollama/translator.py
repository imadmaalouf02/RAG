from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_translation_chain(llm, target_language):
    translation_prompts = {
        "English": "Translate the following text into English:\nText: {text}",
        "French": "Traduisez le texte suivant en français :\nTexte : {text}",
        "Arabic": "ترجم النص التالي إلى العربية:\nالنص: {text}"
    }
    translation_prompt = translation_prompts[target_language]
    translation_prompt_template = PromptTemplate(template=translation_prompt, input_variables=["text"])
    return LLMChain(llm=llm, prompt=translation_prompt_template)


def translate_text(translation_chain, text):
    return translation_chain.run({"text": text})

