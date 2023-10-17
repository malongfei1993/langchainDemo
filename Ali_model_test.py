# sk-87a5d03112fc49fb8fab6d9076837edf
from dashscope import Generation
from http import HTTPStatus
import json
import dashscope
def Ali_response(text):
    dashscope.api_key = "sk-87a5d03112fc49fb8fab6d9076837edf"
    response = Generation.call(
        model='qwen-turbo',
        parameters={"temperature":0.8},
        prompt=text)

    if response.status_code == HTTPStatus.OK:
        return (response.output)["text"]
    else:
        print('Code: %d, status: %s, message: %s' %
            (response.status_code, response.code, response.message))
