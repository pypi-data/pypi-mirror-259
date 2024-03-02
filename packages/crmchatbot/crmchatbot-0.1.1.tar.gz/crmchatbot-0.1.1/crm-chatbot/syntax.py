from langchain.pydantic_v1 import BaseModel, Field
from langchain.agents import tool
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
load_dotenv()


from datetime import datetime

current_datetime = datetime.now()

current_year = current_datetime.year
current_month = current_datetime.month
current_day = current_datetime.day
current_time = current_datetime.strftime("%H:%M:%S")

class ChatBot(BaseModel):
    input: str = Field(description="The question asked by the user.")
   

@tool(args_schema=ChatBot)
def fetchXML_syntax(input)-> str:
    """
        A tool to format the user request if it was related to crm data.      
        Args:
            input (str) : The question that needs to be formatted.
            history (List) : The chat history.

        Returns:
            str: Formatted data.
    """
    chat_template = ChatPromptTemplate.from_messages([
            ("system", f"""
                ***PAY ATTENTION TO THE RULES AND EXAMPLES BELOW BETWEEN THE ''' ''', THEY'RE VERY IMPORTANT.***
                    '''
                    -  You are a CRM specialist, your role is to analyze user input, and transform it to fetchXML format, that Microsoft Dynamics CRM would understand
            
                    - Do not generate any extra text, only generate the XML format 
            
                    - The format should look something like this:
                        --Example : 
                            - User: "List all accounts."
                              /accounts              
                            - User: "I want to view/check/retrieve/see/look for/ ask about data from account[Entity] where name is equal to MS Account info"
                              /accounts?$select=name$filter=name eq 'MS Account info'
                            - User: "I want to see all contacts."
                              /contacts?$select=fullname,contactid,emailaddress1
                            -User:"Show me all open oppurtunities this quarter"
                              /opportunities?$filter=statecode eq 0 and estimatedclosedate ge 2024-01-01 and estimatedclosedate le 2024-12-31
                            -User:"Show me my meetings for the year 2024 month feb"
                              /appointments?$filter=scheduledstart ge 2024-02-01T00:00:00Z and scheduledstart le 2024-02-28T23:59:59Z and statuscode eq 1
                            - User : "find the full names of all leads that were created on this month"
                                /leads?$select=fullname,createdon&$filter=createdon ge 2024-02-01T00:00:00Z and createdon le 2024-02-28T23:59:59Z


                     - DO NOT GENERATE ANY EXTRA TEXT,  ALL I WANT IS THE FORMATTED DATA. NOT EVEN TO CLARIFY THE USER INTENT, JUST THE FORMATTED DATA.
                     - DO NOT CLARIFY ONLY RETURN THE SINGLE VALUE EXAMPLE: accounts
                     - Just give me the response itself, without using words like: system, human, etc.
                     - If the contact isn't found in the data, respond with "No record found for this user.",For example if the user entered "Give me the account details 
                       for Aseel Alzubaidi",and the user is not found generate No record found for this user.

                     - refer to the chat history to make sure if the question asked is in refernece to an already answered question
             
                     - You're in time : {current_time,current_year,current_month,current_day}

                    '''
    """),
            ("human",input)
        ])

    llm = AzureChatOpenAI(api_version="2023-07-01-preview", azure_deployment="mystery_game")
    messages = chat_template.format_messages(input=input)
    response = llm.invoke(messages)
    return response.content


    

    

   