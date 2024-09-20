from langchain import PromptTemplate
#from langchain_core.prompts.PromptTemplate import PromptTemplate
from langchain_experimental.llms.ollama_functions import OllamaFunctions
#from langchain_ollama import ChatOllama
#from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain.schema import SystemMessage
import logging