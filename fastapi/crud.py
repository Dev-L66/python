from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    name: str
    description: str

todos = []

@app.get('/')
def show_todos():
    return todos

@app.post('/')
def create_todos(todo:Todo):
    todos.append(todo)
    return {"message":"Todo created successfully."}
    
@app.put('/{todo_id}')
def update_todo(todo_id:int, updated_todo:Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i]= updated_todo
            return{"message": "Todo updated successfully."}
    return {"message": "Todo not found"}


@app.delete('/{todo_id}')
def delete_todo(todo_id:int):
    global todos
    new_todos = [todo for todo in todos if todo.id != todo_id]
    return{"message": "Todo deleted successfully."}
