from pydantic import BaseModel
import uuid

class PolicyGrant(BaseModel):
    policy_id: uuid.UUID
    user_id: uuid.UUID

class PolicyRevoke(PolicyGrant):
    pass
