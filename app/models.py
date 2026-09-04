from typing import List, Optional

from pydantic import BaseModel, Field


class GrowthAction(BaseModel):
    action_type: str
    customer_ids: List[int] = Field(default_factory=list)
    amount: float = Field(gt=0)
    reason: str


class ActionResult(BaseModel):
    success: bool
    action_id: Optional[int] = None
    message: str
    reference: Optional[str] = None