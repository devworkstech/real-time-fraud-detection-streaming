"""Transaction schemas and data definitions."""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

class Transaction(BaseModel):
    transaction_id: str
    user_id: str
    card_number_masked: str
    amount: float
    currency: str = "USD"
    merchant_id: str
    merchant_category: str
    location_lat: float
    location_lon: float
    timestamp: datetime
    ip_address: str
    device_id: str

class FraudAlert(BaseModel):
    alert_id: str
    transaction_id: str
    user_id: str
    fraud_score: float
    reasons: List[str]
    timestamp: datetime
