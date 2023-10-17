from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from Ali_LLM import ali_LLM
llm = ali_LLM()
tools = load_tools(["llm-math"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
def agentRunCalculate(msg):
  return agent.run(msg)

#agent.run("请重新计算：5.34%*5864.1*97%*0.95*1.021234")