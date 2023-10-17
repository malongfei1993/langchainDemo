# from my_LLM import my_LLM


# from langchain.agents import load_tools
# from langchain.agents import initialize_agent
# from langchain.agents import AgentType

# llm = my_LLM(n=10)
# tools = load_tools(["llm-math"], llm=llm)
# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# agent.run("15的三次方是多少？")
from flask import Flask, request
import time
import random
import os
from werkzeug.utils import secure_filename
from my_agent import agentRun 

app = Flask(__name__)


TODOList = {
    "task":"TODOLIST",
    "list": [{"projectName":"1 HD720 TN NB Dell LCM A-si 30Hz NTSC 11% 200nit Quest多现地联调08311025","taskName":"检讨任务"
             ,"customerTerminal": "Test客户终端系列","customer": "Dell","terrain": "B3"},
            {"projectName": "1 HD720 TN NB Dell LCM A-si 30Hz NTSC 11% 200nit Quest多现地联调08311025","customerTerminal": "Test客户终端系列",
             "taskName": "分配一级担当","customer": "Dell","terrain": "B6"}]
             }

TODOLIST_LLM_RESULT = '''目前有两个待办事项，分别是关于
1 HD720 TN NB Dell LCM A-si 30Hz NTSC 11% 200nit Quest多现地联调08311025项目的检讨任务
和关于1 HD720 TN NB Dell LCM A-si 30Hz NTSC 11% 200nit Quest多现地联调08311025项目的分配担当任务。
<table border="1"> <tr> <td>Project Name</td> <td>Task Name</td> 
<td>Customer Terminal</td> <td>Customer</td> <td>Terrain</td> </tr>
 <tr> <td>1 HD720 TN NB Dell LCM A-si 30Hz NTSC 11% 200nit Quest多现地联调08311025</td> <td>检讨任务</td> <td>Test客户终端系列</td> <td>Dell</td> <td>B3</td> </tr> <tr> <td>1 HD720 TN NB Dell LCM A-si 30Hz NTSC 11% 200nit Quest多现地联调08311025</td> <td>分配一级担当</td> <td>Test客户终端系列</td> <td>Dell</td> <td>B6</td> </tr> </table>'''

ABSTRACT_INFO='''一、关键参数

·产品型号：未确定

·屏幕类型：IPS／TN

·尺寸：17.0英寸

·分辨率：2560x1600

·面板类型：ADS Pro

·色彩比例：16：10

·视角：最大89／89／89／89度，最小80／80／80／80度

·亮度：典型值350nit，最低值297.5nit

·对比度：典型值1200：1，最低值1000：1

·色域：典型值DCI—P399％，最低值95％

·色温：典型值6500K

·响应时间：典型值30ms，最小值35ms

·可视角度：水平89°，垂直89°

·触摸功能：支持

·重量：最大262克

·接口类型：LVDS， eDP， MIPI

·厚度：最大值2.35毫米'''

ONLINE_EXCEL = '''<a target="_blank" href="http://10.80.135.64:9090/demo-index.html">1 HD720 TN NB Dell LCM A-si 30Hz NTSC 11% 200nit Quest多现地联调08311025</a><br/>
<a target="_blank" href="http://10.80.135.64:9090/demo-index.html">1 HD720 TN NB Dell LCM A-si 30Hz NTSC 11% 200nit Quest多现地联调08311025</a>'''
EMAIL_AUDUIT = '''已经发送邮件给负责人'''
ANALYZE = '''{"xAxis":["马龙飞", "刘洋", "张强", "李子烨", "张艺潇", "何玉婷", "叶爱华"],"data":[120, 200, 150, 80, 70, 110, 130]}'''
def switch_case(argument):
    result = ''
    if argument == "查询我的所有待办任务":
        result = TODOLIST_LLM_RESULT
        # 执行操作1
        pass
    elif argument == "提取第一个项目的关键参数并找到已检讨完成的类似历史RFQ":
        # 执行操作2
        result = ABSTRACT_INFO
        pass
    elif argument == "打开第一个项目":
        # 执行操作3
        result = ONLINE_EXCEL
        pass
    elif argument == "发送邮件给审核人，提醒及时审核":
        # 执行操作3
        result = EMAIL_AUDUIT
        pass
    elif argument == '''根据RFQ项目数据，画出每个担当今年内处理RFQ的数量，横轴是担当名称，纵轴是RFQ的数量，使用条形图绘制''':
        # 执行操作3
        result = ANALYZE
        pass
    elif argument == "总结上图信息，并发送邮件给负责人":
        # 执行操作3
        result = EMAIL_AUDUIT
        pass
    else:
        # 默认情况
        result = "请重新输入"
        pass
    return result

@app.route('/api/RFQ', methods=['POST'])
def my_endpoint():
    # 处理请求逻辑
    data = request.json
    print(data)
    # 进行处理...
    result =agentRun(data.get('msg'))
    #result = switch_case()
    #result = agentRun(data)
    #模拟延时加载
    delay = random.uniform(1,2)
    time.sleep(delay)
    return {
    "success": True,
    "message": "success",
    "code": 200,
    "result": result
}
from Tool2RFQ_agent import agentRunTool
@app.route('/api/Tool', methods=['POST'])
def my_secondPoint():
    # 处理请求逻辑
    data = request.json
    print(data)
    # 进行处理...
    result =agentRunTool(data.get('msg'))
    #result = switch_case()
    #result = agentRun(data)
    #模拟延时加载
    delay = random.uniform(1,2)
    time.sleep(delay)
    return {
    "success": True,
    "message": "success",
    "code": 200,
    "result": result
}

UPLOAD_FOLDER = '/Files'  # 设置上传文件保存的目录
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    # 检查请求中是否包含文件
    if 'file' not in request.files:
        return {'message': 'No file uploaded'}, 400

    file = request.files['file']

    # 检查文件名是否为空
    if file.filename == '':
        return {'message': 'No file selected'}, 400

    # 确保文件名的安全性
    filename = secure_filename(file.filename)

    # 保存文件到服务器
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return {'message': 'File uploaded successfully'}, 200

#13-1

if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0'))

