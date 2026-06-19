from app.core.database.db import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Enum, Float, Text, func, DateTime
import uuid
from app.enum.subscription_type import SubscriptionType

class Subscription(Base):
    __tablename__ = "subscriptions"

    subscription_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subscription_name = Column(Enum(SubscriptionType), unique=True, nullable=False)
    cost = Column(Float, nullable=False)
    details = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())