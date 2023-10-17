from langchain.tools import tool
from pydantic import BaseModel, Field


class OnlineExcelInput(BaseModel):
    name: str = Field(description="should be a name")

#formData
data = {
  "method": 1,
  "params": {
    "userId": "10.80.130.108",
    "fileId": "441c1ae4e35d492fb651bbed48ecedf6_1261368576",
    "filePath": "/工作表 在 D  RFQ评估邀请 NO.66 VIST22011-12.3 SGM358 Legacy 12.3inch  incell TFT  STSOW20220815.xls",
    "userRight": 0,
    "mobileFlag": False,
    "saveFlag": False,
    "fallbackUrl": "http://10.80.135.64:9090/demo-index.html"
  },
  "indexFlag": True
}
url = "http://10.80.135.64:8080/api.do"
method = "post"

@tool("在线打开Excel", return_direct=False, args_schema=OnlineExcelInput)
def getOnlineExcel_api(name: str) -> str:
    """根据项目信息获取在线Excel的地址"""
    print("name is :{}".format(name))
    
    return {"excelPath":"http://10.80.135.64:9099/weboffice/s/ss.html?av=null&wv=3.3.8.0062&fid=441c1ae4e35d492fb651bbed48ecedf6_1072279280&core=8pWs4MLkF2Mem1gOI1kc5DaqsDEjkT5KFxl8SUjee1c%3D&sig=72feae829f544375bf318df73aa970bb"}