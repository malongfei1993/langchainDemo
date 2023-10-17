from typing import Any, List, Mapping, Optional
from langchain.llms.base import LLM
import requests
import json
from langchain.llms.utils import enforce_stop_tokens
from Ali_model_test import Ali_response
class ali_LLM(LLM):
 
 
    @property
    def _llm_type(self) -> str:
        return "custom"
 
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None
    ) -> str:
        
      
        # print("发送llm请求")
        #print(prompt)
        # 发送 POST 请求并获取返回内容
        content = Ali_response(prompt)
       
        
        # if stop is not None:
        content = enforce_stop_tokens(content, ["Observation:"])
        #print(content)
        
        return content
 

    
# llm = ali_LLM()
# output=llm("hello")
 