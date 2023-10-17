from langchain.tools import tool
from pydantic import BaseModel, Field


class TodoListInput(BaseModel):
    name: str = Field(description="should be a name")


@tool("个人待办查询", return_direct=False, args_schema=TodoListInput)
def getToDOList_api(name: str) -> str:
    """查询待办的API."""
    print("name is :{}".format(name))
    return [{"projectName":"1 HD720 TN NB Dell LCM A-si 30Hz NTSC 11% 200nit Quest多现地联调08311025","taskName":"检讨任务"},
            {"projectName":"2 HD1020 TN NB Dell LCM A-si 30Hz NTSC 11% 200nit","taskName":"分配担当任务"}]