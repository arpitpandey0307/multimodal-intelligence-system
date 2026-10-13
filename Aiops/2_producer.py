from confluent_kafka import Producer
from cloud_config import kafka_config
import time

# 1. Connect to our secure Aiven Cloud Broker using the certificates
p = Producer(kafka_config)

# 2. Send 5 messages to the cloud
for i in range(5):
    data = f"User Click {i}"
    
    # produce() sends data to a topic named 'ml_topic', please make a ml_topic in Aiven website left sidepy 2
    p.produce('ml_topic', value=data.encode('utf-8'))
    print(f"📤 Sent to Aiven Cloud: {data}")
    time.sleep(1) # Pause for 1 second

# 3. flush() guarantees all remaining messages are pushed over the internet before closing
p.flush()
