from confluent_kafka import Consumer
from cloud_config import kafka_config
import sys

kafka_config["group.id"] = "fraud_detection_team"  # Identifies our consumer team
kafka_config["auto.offset.reset"] = "latest" # focuses on fresh incoming stream

worker_name = sys.argv[1] if len(sys.argv) > 1 else "Worker_Main"

c = Consumer(kafka_config)
c.subscribe(["test"])

print(f" {worker_name} joined 'fraud detection team' and is waiting for assigned partitions...")

try:
    while True:
        msg = c.poll(1.0)
        
        if msg is None:
            continue
        if msg.error():
            print(f" Error : {msg.error()}")
            continue
        
        print(
            f"[{worker_name}] Partition: {msg.partition()} | "
            f"Offset: {msg.offset()} | "
            f"Key: {msg.key().decode('utf-8') if msg.key() else 'None'} | "
            f"Data: {msg.value().decode('utf-8')}"
        )
except KeyboardInterrupt:
    print(f"{worker_name} leaving the group...")
finally:
    c.close()