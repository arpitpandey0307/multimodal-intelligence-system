from confluent_kafka import Producer
from cloud_config import kafka_config
import json, time, random

p = Producer(kafka_config)

print("Streaming Data Generator Started...")

for i in range(100):
    transaction = {
        "tx_id": f"TXN-{i}",
        'user': random.choice(['Alice', 'Bob', 'Charlie', 'David']),
        'amount': random.randint(100, 10000),
        'status': 'PENDING'
    }
    
    serialized_data = json.dumps(transaction).encode('utf-8')
    p.produce('test', value=serialized_data)
    print(f"Produced transaction: {transaction}")
    time.sleep(1)  # Simulate a delay between transactions

p.flush()