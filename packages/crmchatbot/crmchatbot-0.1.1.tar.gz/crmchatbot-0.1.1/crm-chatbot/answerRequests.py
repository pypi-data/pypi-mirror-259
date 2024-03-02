from langchain.pydantic_v1 import BaseModel, Field
from langchain.agents import tool
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()


class Request(BaseModel):
    input: str = Field(description="The question asked by the user.")


@tool(args_schema=Request)
def answer_request(input)-> str:
    """
        A tool to answer the user request if it was related to crm data.      
        Args:
            input (str) : The question that needs to be answered.
           

        Returns:
            str: The answer for the user request.
    """
    chat_template = ChatPromptTemplate.from_messages([
            ("system", f"""
                ***PAY ATTENTION TO THE RULES AND EXAMPLES BELOW BETWEEN THE ''' ''', THEY'RE VERY IMPORTANT.***
                    '''
                    -  You are a CRM specialist, for microsoft dynamics CRM.
            
                    - You are designed to answer user requests if it was crm related.
             

                    '''
           """),
            ("human",input)
        ])

    llm = AzureChatOpenAI(api_version="2023-07-01-preview", azure_deployment="mystery_game")
    messages = chat_template.format_messages(input=input)
    response = llm.invoke(messages)
    
    print(f"This is the response for request tool {response.content}")
    return response.content


   