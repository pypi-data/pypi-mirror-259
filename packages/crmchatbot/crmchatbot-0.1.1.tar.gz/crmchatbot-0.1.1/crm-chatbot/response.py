from .agent import create_agent
from .get_data import get_data
from .formatData import format_data
from .handle_user_input import handle_invalid_request

def get_response(input : str):
   
        agent = create_agent(input)
        content = agent.invoke({"input": input})
        if content["output"].startswith("/"):
            result = get_data(content["output"])
            if not result:
                content = handle_invalid_request(input)
                return content
            else:
                if isinstance(result, dict):
                    format = format_data(result)
                    return format
        else:
            return content["output"]
    
