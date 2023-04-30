from typing import Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="猫を飼う")
    done: bool = Field(False, description="完了フラグ")