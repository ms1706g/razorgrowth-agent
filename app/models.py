from pydantic import BaseModel, Field


class GrowthAction(BaseModel):
    action_type: str
    customer_ids: list[int] = Field(default_factory=list)
    amount: float = Field(gt=0)
    reason: str


class ActionResult(BaseModel):
    success: bool
    action_id: int | None = None
    message: str
    reference: str | None = None