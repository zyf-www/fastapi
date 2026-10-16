import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import ChatOpenAI

from rag.loader import db

load_dotenv(override=True)

deepseek = ChatOpenAI(
    base_url = os.getenv("DEEPSEEK_BASE_URL"),
    api_key = os.getenv("DEEPSEEK_API_KEY"),
    model = "deepseek-flash"
)

message = """
你是一名ai助手,请仅根据上下文来回答用户的问题
问题:
{question}
上下文:
{content}
如果资料不足以进行回答，如实告知。这是资料库测试，你的不知道也是一种正确的回答
"""
def format_docs(docs: list) -> str:
    return "\n\n".join([d.page_content for d in docs])

doc_find = RunnableLambda(db.similarity_search).bind(k=6) | format_docs
prompt_template  = ChatPromptTemplate.from_template(message)
chain = {"question":RunnablePassthrough(),"content":doc_find}  | prompt_template | deepseek

def ask(question):
    response = chain.invoke(question)
    return response.content



