from typing import Union, Any

from fastapi import FastAPI
from pydantic import BaseModel

from request.processor import RequestEventTaskCommand

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class TaskRequest(BaseModel):
    some_required_field: str
    other_data: Any = None

@app.post("/process-task/")
async def process_task(request: TaskRequest):
    """
    Processes a task using a predefined sequence of commands.
    """
    task_command = RequestEventTaskCommand()

    try:
        # Execute the entire command chain with the request data
        result = task_command.execute(request.model_dump())
        return {"status": "success", "data": result}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}