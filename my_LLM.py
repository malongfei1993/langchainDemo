from typing import Any, List, Mapping, Optional
from langchain.llms.base import LLM
import requests
import json
from langchain.llms.utils import enforce_stop_tokens

class my_LLM(LLM):
 
    n: int
 
    @property
    def _llm_type(self) -> str:
        return "custom"
 
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None
    ) -> str:
        
                # 构造请求体的 JSON 数据
        data = {
            "aideMoldId": "1706109733800378370",
            "password": "H@ppy8888",
            "queryText": prompt,
            "username": "10160895"
        }
        print("发送llm请求")
        print(prompt)
        # 发送 POST 请求并获取返回内容
        response = requests.post('http://10.251.104.233:31001/aigc-app/ai/aiApi/AideExtService/callBySyn', json=data)
        
        content = json.loads(response.text)["result"]
        print(content)
        # if stop is not None:
        content = enforce_stop_tokens(content, ["Observation:"])
        print(content)
        
        return content
 
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"n": self.n}
    
# llm = my_LLM(n=10)
# output=llm("hello")
 