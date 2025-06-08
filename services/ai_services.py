import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv(dotenv_path=".env")

print(os.getenv("AZURE_OPENAI_ENDPOINT"))
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")

llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_AI_MODEL_NAME"),
    api_version=os.getenv("AZURE_AI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_AI_API_ENDPOINT")
)
sqorz_base_url = os.getenv("SQORZ_API_BASE_ENDPOINT")

def test(test: str):
    print("hello" + test)

sqorz_api_docs = """
GET /org/ffc
Get informations about french bmx race's organization
Response: JSON object with data about regionnal and subregionnal comities
"""

def summarize(sqorz_data_input: str):
    #TODO : summarize data
    print("summarize method end")