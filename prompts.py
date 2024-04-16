from langchain.prompts import PromptTemplate


def prompt_format(system_prompt, instruction):
    B_INST, E_INST = "[INST]", "[/INST]"
    B_SYS, E_SYS = "<SYS>>\n", "\n<</SYS>>\n\n"
    SYSTEM_PROMPT = B_SYS + system_prompt + E_SYS
    prompt_template = B_INST + SYSTEM_PROMPT + instruction + E_INST
    return prompt_template


def model_prompt():
    system_prompt = """You are a helpful assistant and an expert in coding and code analysis. You have full access to the codes, files and documentations in the vector database.
    You will use the provided context to answer user questions. Attach relevant code from the context in your answer to properly answer user question with explaination.
    Read the given context before answering questions and think step by step and answer question based on the provided context. Please do not repeat user question in your answer.
    If you can not answer a user question based on the provided context, inform the user.
    Do not use any other information for answering user."""
    instruction = """
    Context: {context}
    User: {question}"""
    return prompt_format(system_prompt, instruction)


def custom_question_prompt():
    que_system_prompt = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question 
    and give only the standalone question as output in the tags <question> and </question>.
    """

    instr_prompt = """Chat History:
    {chat_history}
    Follow Up Input: {question}
    Standalone question:"""

    return prompt_format(que_system_prompt, instr_prompt)
