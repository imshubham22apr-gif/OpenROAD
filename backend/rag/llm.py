import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from backend.config import Config

class LLMWrapper:
    def __init__(self, model_name=None):
        self.model_name = model_name or Config.MODEL_NAME
        self.api_key = Config.OPENAI_API_KEY
        
        if not self.api_key or self.api_key == "your_key_here":
            # For demonstration, we'll initialize but it will fail if not provided
            pass
            
        self.llm = ChatOpenAI(
            model=self.model_name,
            openai_api_key=self.api_key,
            temperature=0
        )
        
        self.prompt_template = PromptTemplate(
            template="""You are an expert in chip design and OpenROAD flows.

Use ONLY the provided context to answer.

Context:
{context}

Question: {question}

If unsure, say:
"I don't know based on the available documents."

Always include citations:
[source: filename]

Answer:""",
            input_variables=["context", "question"]
        )

    def get_response(self, context, question):
        try:
            formatted_prompt = self.prompt_template.format(context=context, question=question)
            response = self.llm.invoke(formatted_prompt)
            return response.content
        except Exception as e:
            return f"I don't know the answer, please check logs. Error: {str(e)}"
