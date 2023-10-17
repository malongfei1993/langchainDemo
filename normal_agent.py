from Ali_LLM import ali_LLM
llm = ali_LLM()

def AgentRunNormal(msg):
    return llm(msg)

# print(AgentRunNormal('''
# 请回答问题，客户需求是：亮度参数的值为300 nit +/-15%，整理为键值对的方式为{"brightness": "300 nit +/-15%"}。 检讨结果是：294.68nit 请通过计算，比较是否满足需求，并说明原因
# '''))