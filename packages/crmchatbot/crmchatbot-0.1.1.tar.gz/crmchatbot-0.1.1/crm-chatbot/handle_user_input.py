from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()


llm = AzureChatOpenAI(api_version="2023-07-01-preview", azure_deployment="mystery_game")


def handle_invalid_request(intent):
        chat_template = ChatPromptTemplate.from_messages([
            ("system", f"""
                ***PAY ATTENTION TO THE RULES AND EXAMPLES BELOW BETWEEN THE ''' ''', THEY'RE VERY IMPORTANT.***
                    '''
                    -  You are a CRM specialist, for microsoft dynamics CRM.
            
                    - You are designed to inform the user that the data theyre looking for isn't found.
             
                   


                    '''
    """),




            ("human",intent)
        ])




    
        messages = chat_template.format_messages(intent=intent)
        response = llm.invoke(messages)
        
        
        return response.content