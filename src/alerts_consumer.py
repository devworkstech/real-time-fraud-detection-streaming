"""Alerts consumer dispatching real-time notifications for confirmed fraud."""
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handle_fraud_alert(alert: dict):
    logger.warning("FRAUD ALERT: User=" + str(alert.get("user_id")) + " | Score=" + str(alert.get("fraud_score")))

if __name__ == "__main__":
    mock_alert = {"user_id": "user_4912", "fraud_score": 0.95}
    handle_fraud_alert(mock_alert)
