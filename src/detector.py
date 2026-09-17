"""Rules-based Fraud Evaluation Engine."""
import math
from typing import Dict, Any, List, Tuple

HIGH_RISK_CATEGORIES = {"crypto_exchange", "luxury_goods", "wire_transfer"}
HIGH_AMOUNT_THRESHOLD = 5000.0

class FraudDetector:
    def __init__(self, high_amount_limit: float = HIGH_AMOUNT_THRESHOLD):
        self.high_amount_limit = high_amount_limit

    def evaluate_transaction(self, tx: Dict[str, Any]) -> Tuple[bool, float, List[str]]:
        reasons = []
        score = 0.0

        amount = float(tx.get("amount", 0.0))
        if amount >= self.high_amount_limit:
            score += 0.6
            reasons.append("High amount anomaly threshold exceeded")
        elif amount > 2500.0:
            score += 0.3
            reasons.append("Elevated amount threshold exceeded")

        cat = tx.get("merchant_category", "").lower()
        if cat in HIGH_RISK_CATEGORIES:
            score += 0.35
            reasons.append("High-risk merchant category detected: " + cat)

        is_fraud = score >= 0.6
        return is_fraud, min(score, 1.0), reasons

    @staticmethod
    def calculate_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        R = 6371.0
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c
