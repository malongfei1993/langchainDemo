from openpyxl import load_workbook
import os
from langchain.tools import tool
from pydantic import BaseModel, Field
import time

#Current ratio 电流比
#transmittance 透过率
#AAsize

# 亮度=透过率*BLU亮度*97%（默认margin 3%)*0.95(Aging参考）
# BLU亮度=参考产品BLU亮度
# 对应的数据是
# 354.8=6.35%*BLU亮度*97%*0.95
# BLU亮度=5969.7

@tool("Calculate parameter",return_direct=False)
def calculator(test:str) -> str:
  '''useful for when you need calculate parameter'''
  print("调用亮度计算公式API接口")
  time.sleep(1)
  return '''
  亮度nit=透过率*BLU亮度*97%（默认margin 3%)*0.95(Aging参考）,
  BLU亮度=参考产品BLU亮度*1.021234.
  '''

@tool("Review BrightNess parameter",return_direct=False)
def review_brightness_parameter(test:str) -> str:
  '''useful for when you need review brightness parameter'''
  time.sleep(1)
  return '''
    参考产品是：透过率:5.34%,参考产品BLU亮度:5864.1
'''

