from typing import List
from fastapi import APIRouter
import api.schemas.task as task_schema

router = APIRouter()


# タスク一覧を取得
@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つめのTODOタスク")]

# 新しいタスクを追加
@router.post("/tasks")
async def create_task():
    pass

# タスクの情報を変更
@router.put("/tasks/{task_id}")
async def update_task():
    pass

# タスクを削除
@router.delete("tasks/{task_id}")
async def delete_task():
    pass