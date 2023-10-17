from langchain.tools import tool
from pydantic import BaseModel, Field



@tool("获取RFQ的数据分析结果", return_direct=False)
def getRFQ_Analyze_result() -> str:
    """返回RFQ数据分析结果"""
   
    return {}