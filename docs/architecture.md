# Real-Time Streaming Fraud Detection Architecture

## Overview
This platform is engineered to process 50,000+ financial transaction events per second with sub-second anomaly detection latency.

## Key Design Considerations
1. **Exactly-Once Semantics**: Maintained using PySpark Structured Streaming checkpointing and Delta Lake transactional log guarantees.
2. **Stateful Stream Processing**: Implemented via `groupBy(window(...), col("user_id"))` to track user velocity across sliding 60-second periods.
3. **Late-Data Handling**: Watermarking set to 10 minutes ensures late events are integrated into state stores before eviction.
