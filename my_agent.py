
from langchain.agents import AgentType, initialize_agent
from langchain.agents import Tool
from Ali_LLM import ali_LLM
from Tools.find_tools import find_params_yield_tool
llm = ali_LLM()
tools = [Tool(func=find_params_yield_tool, 
              name="Obtaining screen parameters from document", 
              description="useful for when you need obtaining screen parameters from data requires repeated calls.",
                args_schema=None,priority=3)
         ]


agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, stop=["\nObservation:"],
)


def agentRun(msg):
    extra_prompt = "从文档中查找下面参数的值，一直重复直到找到值:{}是多少，并整理为键值对的方式".format(msg)
    return agent.run(extra_prompt)

#agentRun("auto run Function")
#agent.run('''从文档中查找下面参数的值，一直重复直到找到值:Module Size是多少''')
#输入机光检讨模板参数，多少参数都可以，但不能输入别的值
#print(agentRun("Mod_Size"))


#10.15 反向
# agent.run('''
#  There is a word:"Module_Size".          
#   now to find the document of the screen parameters to match and assign until you find it.
# ''')




#尝试把每个参数进行解释，加入到observation中 10.14 
#10.15 尝试成功，Resolution_V，Resolution_H增加解释即可成功搜素且取出数值

# agentRun('''Find the values of {Mod_Size, Resolution_V, Resolution_H, PPI} and organize them into the format of JSON key-value pairs:
# Resolution_H refers to the horizontal resolution of the screen, Resolution_V refers to the vertical resolution of the screen.''')
# agentRun('''找出{Mod_Size,Resolution_V,Resolution_H,PPI}的值,并整理为JSON键值对的格式:
#          Resolution_H指的是屏幕的水平分辨率 ,Resolution_V指的是屏幕的垂直分辨率.''')
# agentRun('''找出Mod_Size,Resolution_V,Resolution_H,PPI,关键参数的值并整理为JSON键值对的格式:
#          Resolution_H指的是屏幕的水平分辨率 ,Resolution_V指的是屏幕的垂直分辨率.
#          你应该思考当工具返回的结果匹配哪个参数，如果没有匹配则继续调用工具进行查找，如果工具返回"已经没有数据了，不需要
#          查找"，则可以完成任务''')
