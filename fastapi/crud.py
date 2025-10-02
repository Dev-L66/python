from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db
from sqlalchemy.orm import Session
from models import Todo
from typing import List, Optional

router = APIRouter()

class TodoCreate(BaseModel):
    # id: int
    title: str
    description: Optional [str] = None
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
    
@router.put('/{todo_id}', response_model=TodoResponse)
def update_todo(todo_id:int, todo: TodoCreate, db:Session=Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="Todo Not Found.")
    db_todo.title = todo.title
    db_todo.description = todo.description
    db_todo.done = todo.done
    db.commit()
    db.refresh(db_todo)
    return db_todo
    


@router.delete('/{todo_id}')
def delete_todo(todo_id:int, db: Session=Depends(get_db)):
   db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
   if not db_todo:
        raise HTTPException(status_code=404,detail="Todo Not Found.")
   db.delete(db_todo)
   db.commit()
   return {"message": "Todo deleted successfully."}
