from langchain.tools import tool
import requests
from typing import Optional, Type
from pydantic import BaseModel, Field


class EmailInput(BaseModel):
    name: str = Field(description="should be a name")

@tool
def email_post(url: str, body: dict, parameters: Optional[dict] = None) -> str:
    """通过给出的参数发送email"""
    result = requests.post(url, json=body, params=parameters)
    return f"Status: {result.status_code} - {result.text}"