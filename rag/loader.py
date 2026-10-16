import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv(override=True)

# 项目根目录（rag/loader.py 的上一级），避免依赖启动时的工作目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

embeddings = DashScopeEmbeddings(
    model="text-embedding-v2",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
)

db = Chroma(
    collection_name="fastapi",
    embedding_function=embeddings,
    persist_directory=os.path.join(BASE_DIR, "chroma_db")
)


def init_db():
    # 如果数据库里已经有数据，直接跳过
    if db._collection.count() > 0:
        print(f"数据库已有 {db._collection.count()} 条数据，跳过加载")
        return

    print("数据库为空，开始加载文档...")
    loader = DirectoryLoader(
        os.path.join(BASE_DIR, "docs", "rag_corpus"),
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader,
    )
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = splitter.split_documents(docs)
    db.add_documents(documents)
    print(f"已存入 {len(documents)} 个碎片")


# 导入这个模块时自动执行
init_db()