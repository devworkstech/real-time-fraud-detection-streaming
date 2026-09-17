"""High-throughput synthetic transaction generator with injected fraud patterns."""
import json
import random
import time
import uuid
from datetime import datetime

MERCHANT_CATEGORIES = ["grocery", "electronics", "airline", "crypto_exchange", "restaurant", "luxury_goods"]

def generate_transaction(inject_fraud: bool = False) -> dict:
    user_id = f"user_{random.randint(1000, 9999)}"
    amount = round(random.uniform(5.0, 300.0), 2)
    category = random.choice(MERCHANT_CATEGORIES)

    if inject_fraud:
        amount = round(random.uniform(4500.0, 15000.0), 2)
        category = "crypto_exchange"

    return {
        "transaction_id": str(uuid.uuid4()),
        "user_id": user_id,
        "card_number_masked": f"****-****-****-{random.randint(1000, 9999)}",
        "amount": amount,
        "currency": "USD",
        "merchant_id": f"merch_{random.randint(100, 500)}",
        "merchant_category": category,
        "location_lat": round(random.uniform(25.0, 48.0), 4),
        "location_lon": round(random.uniform(-122.0, -70.0), 4),
        "timestamp": datetime.utcnow().isoformat(),
        "ip_address": f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}",
        "device_id": f"dev_{random.randint(1000, 9999)}"
    }

if __name__ == "__main__":
    print("Generating sample transactions...")
    for _ in range(3):
        print(json.dumps(generate_transaction(), indent=2))
