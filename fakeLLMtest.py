from langchain.llms.fake import FakeListLLM
from langchain.agents import AgentType, initialize_agent
from Tools.load_excel_tool import getExcelNameAndSheetNameTest
from langchain.agents import Tool
from Tools.Reference_products_tool import python_calculator
responses = [''' 需要使用科学计算器进行计算
Action: scientific calculator
Action Input: 亮度计算方式，参考数据
Observation:''']

# 目前出现一种情况，final answer和action只能出现一个，
# 如果在response里都有，那么会报错。https://github.com/langchain-ai/langchain/discussions/7403

llm = FakeListLLM(responses=responses)
tools = [ Tool(func=python_calculator, 
              name="scientific calculator", 
              description="userful for when you need to accurately calculate a formula.",
                args_schema=None,priority=1)]
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,
)
agent.run(
   '''
Answer the following questions as best you can. You have access to the following tools:

Calculation formula: useful for when you get formula
get screen parameter of reference product: this tool can get screen parameter you need of reference product .
scientific calculator: userful for when you need to accurately calculate a formula.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Calculation formula, get screen parameter of reference product, scientific calculator]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: 获取亮度计算方式,之后获取参考数据，再使用科学计算器算出数值 .
Thought:需要使用科学计算器进行计算，需要先获取亮度计算方式和参考数据
Action: Calculation formula
Action Input: 亮度计算方式
Observation:
  亮度=透过率*BLU亮度*97%（默认margin 3%)*0.95(Aging参考）,
  BLU亮度=1.021234*参考产品BLU亮度.

Thought:需要使用科学计算器进行计算，需要先获取参考数据
Action: get screen parameter of reference product
Action Input:
Thought:
    
'''
)

