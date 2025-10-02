from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db
from sqlalchemy.orm import Session
from models import Todo
from typing import List

router = APIRouter()

class TodoCreate(BaseModel):
    title: str
    description: str
    done: bool

class TodoResponse(TodoCreate):
    id: int
   

todos = []

@router.get('/', response_model=List[TodoResponse])
def show_todos(db:Session = Depends(get_db)):
    return db.query(Todo).all()

@router.post('/', response_model=TodoResponse)
def create_todos(todo:TodoCreate, db: Session = Depends(get_db)):
    new_todo = Todo(title=todo.title, description=todo.description, done=todo.done)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
    
# @router.put('/{todo_id}')
# def update_todo(todo_id:int, updated_todo:Todo):
#     for i, todo in enumerate(todos):
#         if todo.id == todo_id:
#             todos[i]= updated_todo
#             return{"message": "Todo updated successfully."}
#     return {"message": "Todo not found"}


# @router.delete('/{todo_id}')
# def delete_todo(todo_id:int):
#     global todos
#     new_todos = [todo for todo in todos if todo.id != todo_id]
#     return{"message": "Todo deleted successfully."}
