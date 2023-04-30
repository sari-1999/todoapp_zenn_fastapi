from fastapi import APIRouter

router = APIRouter()


# 終了したタスクにチェックを入れる
@router.put("/tasks/{task_id}/done")
async def mark_task_as_done():
    pass

# タスクのチェックを外す
@router.delete("/tasks/{task_id}/done")
async def unmark_task_as_done():
    pass