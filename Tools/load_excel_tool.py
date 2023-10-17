from langchain.tools import tool
from pydantic import BaseModel, Field
from utils.openExcel2Str import read_excel_sheet



@tool("整理关键RFQ数据", return_direct=False)
def getRFQ_Key_Data(test:str) -> str:
    """getRFQ_Key_Data() -> str"""
    return "将上述的RFQ内容的10个关键的参数整理成HTML的Table格式，并且只输出Table代码，请输出："

@tool("获取RFQ的Excel数据", return_direct=False)
def getRFQ_Excel_Data(test:str) -> str:
    """getRFQ_Excel_Data(filePath: str,sheetName:str) -> str"""
    file_path = 'Files/【更新】Display_RFI_CS25_TBG_13inch_08132023.xlsx'  # 替换为你的 Excel 文件路径
    sheet_name = '13-1'  # 替换为你要读取的 sheet 名称
    print("filePath is :{}".format(file_path))
    print("sheetName is :{}".format(sheet_name))
    content = read_excel_sheet(file_path=file_path,sheet_name=sheet_name)
    
    return content

@tool("获取RFQ的Excel数据之前，需要获取文件名称和sheet名称", return_direct=False)
def getExcelNameAndSheetName(test:str) -> dict:
    """
    获取 Excel 文件路径和工作表名称的函数。
    
    返回一个包含文件路径和工作表名称的字典，格式如下：
    {
        "filePath": 文件路径,
        "sheetName": 工作表名称
    }
    """
    
    
    file_path = 'Files/【更新】Display_RFI_CS25_TBG_13inch_08132023.xlsx'  # 替换为你的 Excel 文件路径
    sheet_name = '13-1'  # 替换为你要读取的 sheet 名称
    return {"filePath":file_path,"sheetName":sheet_name}

@tool("获取RFQ的Excel数据之前，需要获取文件名称和sheet名称", return_direct=False)
def getExcelNameAndSheetNameTest(test:str) -> str:
    '''返回空'''
    return "1234"