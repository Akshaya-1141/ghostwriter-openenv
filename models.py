from pydantic import BaseModel
from typing import List, Optional

class Observation(BaseModel):
    draft_text: str
    style_guide: str
    task_id: str
    current_step: int

class Action(BaseModel):
    action_type: str  # e.g., "rewrite_paragraph", "fix_typo", "submit"
    target_index: Optional[int] = None
    suggested_text: str

class Reward(BaseModel):
    score: float
    feedback: str
    done: bool
