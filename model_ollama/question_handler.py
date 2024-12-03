from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_question_answer_chain(llm):
    question_answer_prompt = """
    Answer the following question based on the provided text:
    Question: {question}
    Text: {text}
    """
    question_prompt_template = PromptTemplate(template=question_answer_prompt, input_variables=["question", "text"])
    return LLMChain(llm=llm, prompt=question_prompt_template)

def answer_question(question_chain, question, text):
    return question_chain.run({"question": question, "text": text})
