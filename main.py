from flask import Flask, render_template,make_response  
from flask import request,session
import time
from my_agent import agentRun 
from Tool2RFQ_agent import agentRunFind
from Caculate_agent import agentRunCalculate
from normal_agent import AgentRunNormal
app = Flask(__name__)  
app.secret_key="RFQREQUEST"



@app.route('/')  
def index():  
    return render_template('index.html')  
def switch_case(argument):
    result = ''
    param0 = "内容提取："
    param1 = "检讨："
    param2 = "计算器："
    param3 = "报告："
    
    if param0 in argument:
        result = argument.replace(param0,"")
        response = findApi(result)
        session["REQUEST_PARAMETER"] = response
        return response
        # 执行操作1
        pass
    elif param1 in argument:
        # 执行操作2
        result = argument.replace(param1,"")
        response = reviewApi(result)
        session["REVIEW_PARAMETER"] = response
        judgeMent = getReviewResult()
        response["result"] = response.get("result")+judgeMent
        return response
        pass
    elif param2 in argument:
        # 执行操作3
        result = argument.replace(param2,"")     
        response = calculateApi(result)
        #加个单位
        session["REVIEW_PARAMETER"] = response+"nit"
        judgeMent = getReviewResult()
        response["result"] = response.get("result")+judgeMent
        return response
        pass
    elif param3 in argument:
        # 执行操作3
        result = argument.replace(param3,"")
        return downloadApi()
        pass
    else:
        # 默认情况
        print("other tool")
        return normalApi(argument)
        pass
    return result

def getReviewResult():
    template = '''请回答问题，客户需求是：{} 检讨结果是：{} 请通过计算，比较是否满足需求，并说明原因'''.format(session.get("REQUEST_PARAMETER"),session.get("REVIEW_PARAMETER"))
    return AgentRunNormal(template)

def normalApi(msg):
    print(msg)
    result = AgentRunNormal(msg)
    return {
    "success": True,
    "message": "success",
    "code": 200,
    "result": result
}

@app.route('/api/result', methods=['POST'])
def testApi():
    # 处理请求逻辑
    data = request.json
    print(data)
    # 进行处理...
    result = switch_case(data.get("msg"))
    return result


# @app.route('/api/result', methods=['POST'])
# def my_endpoint():
#     # 处理请求逻辑
#     data = request.json
#     print(data)
#     # 进行处理...
#     #result =agentRun(data.get('msg'))
#     #result = switch_case()
#     #result = agentRun(data)
#     #模拟延时加载
#     delay = random.uniform(1,2)
#     time.sleep(delay)
#     return {
#     "success": True,
#     "message": "success",
#     "code": 200,
#     "result": "test"
# }

def findApi(data):
    # 处理请求逻辑
    print(data)
    # 进行处理...
    result =agentRun(data)
    return {
    "success": True,
    "message": "success",
    "code": 200,
    "result": result
}

def reviewApi(data):
    # 处理请求逻辑
    print(data)
    # 进行处理...
    result =agentRunFind(data)
    return {
    "success": True,
    "message": "success",
    "code": 200,
    "result": result
}

def calculateApi(data):
    # 处理请求逻辑
    print(data)
    # 进行处理...
    result =agentRunCalculate(data)
    return {
    "success": True,
    "message": "success",
    "code": 200,
    "result": result
}

@app.route('/api/upload', methods=['POST'])
def upload_file():
    # 检查请求中是否包含文件
    # if 'file' not in request.files:
    #     return {'message': 'No file uploaded'}, 400

    # file = request.files['file']

    # # 检查文件名是否为空
    # if file.filename == '':
    #     return {'message': 'No file selected'}, 400

    # # 确保文件名的安全性
    # filename = secure_filename(file.filename)

    # # 保存文件到服务器
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    time.sleep(1)
    return {
    "success": True,
    "message": "success",
    "code": 200,
    "result": "文件上传成功！请开始检讨。"
}

@app.route('/api/download')
def downloadApi():
    file_path = '/Files/report.pptx'
    response = make_response(file_path)
    response.headers['Content-Disposition'] = 'attachment; filename=report.pptx'
    return response
# @app.route('/events', methods=['GET', 'POST'])  
# def events():  
#     msg=request.args.get("msg")
#     category=request.args.get("category")
#     def event_generator(msg,category):  
#         if category == "RFQ":
#            result = agentRun(msg)
#            yield result
#            time.sleep(1)  
#         if category == "Tool":
#            result = agentRunTool(msg)
#            yield result
#            time.sleep(1)  
#         # # 在这里编写生成SSE事件的内容  
#         # yield 'data: {"event": "message", "message": "Hello, World!"}'  
#         # yield '\n'  
          
#         # # 模拟每隔1秒发送一次事件  
#         # while True:  
#         #     yield 'data: {"event": "time", "time": "' + str(datetime.datetime.now()) + '"}'  
#         #     yield '\n'  
            
              
#     return Response(event_generator(msg,category), mimetype='text/event-stream')  
  
if __name__ == '__main__':  
    app.run(debug=True,host='0.0.0.0')