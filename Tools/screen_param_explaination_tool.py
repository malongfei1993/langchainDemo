from langchain.tools import tool
from pydantic import BaseModel, Field




@tool("explain_screen_params", return_direct=False)
def explain_screen_params(test:str) -> str:
    """When you need to find screen parameters, it's best to use this tool first to see the specific explanation of the parameter"""
    return '''
      mod_size refers to the Module Size.
      Resolution_H refers to the horizontal resolution of the screen,
      Resolution_V refers to the vertical resolution of the screen.'''
