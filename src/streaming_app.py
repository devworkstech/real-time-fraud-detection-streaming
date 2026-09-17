"""PySpark Structured Streaming Application for Real-Time Fraud Ingestion."""
import logging
from src.detector import FraudDetector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Initializing PySpark Structured Streaming Engine...")
    detector = FraudDetector()
    sample = {"amount": 7500.0, "merchant_category": "crypto_exchange"}
    is_fraud, score, reasons = detector.evaluate_transaction(sample)
    logger.info("Sample result: Fraud=" + str(is_fraud) + ", Score=" + str(score) + ", Reasons=" + str(reasons))
