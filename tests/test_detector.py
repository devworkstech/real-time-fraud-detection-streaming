import pytest
from src.detector import FraudDetector

def test_legitimate_transaction():
    detector = FraudDetector()
    tx = {"amount": 45.50, "merchant_category": "grocery"}
    is_fraud, score, reasons = detector.evaluate_transaction(tx)
    assert is_fraud is False
    assert score < 0.6
    assert len(reasons) == 0

def test_fraud_transaction_high_amount():
    detector = FraudDetector(high_amount_limit=5000.0)
    tx = {"amount": 8000.0, "merchant_category": "electronics"}
    is_fraud, score, reasons = detector.evaluate_transaction(tx)
    assert is_fraud is True
    assert score >= 0.6
    assert any("High amount anomaly" in r for r in reasons)

def test_geo_distance():
    dist = FraudDetector.calculate_distance_km(40.7128, -74.0060, 34.0522, -118.2437)
    assert 3900 < dist < 4000
