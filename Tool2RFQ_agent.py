
from langchain.agents import AgentType, initialize_agent
from langchain.agents import Tool
from Ali_LLM import ali_LLM
from Tools.Reference_products_tool import review_brightness_parameter,calculator
llm = ali_LLM()
tools = [
                Tool(func=calculator, 
              name="Calculate parameter", 
              description="useful for when you need calculate parameter",
                args_schema=None),
               Tool(func=review_brightness_parameter, 
              name="get screen parameter of reference product", 
              description="this tool can get screen parameter you need of reference product .",
                args_schema=None)
         ]
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, stop=["\nObservation:"],
)

def agentRunFind(msg):
    extra_prompt = '''计算{}，根据计算公式,获取参考数据，算出数值是多少'''.format(msg)
    return agent.run(extra_prompt)



#agentRunFind("亮度")
#agent.run('''Calculate the brightness, obtain the reference data according to the calculation formula, and calculate the value.''')

