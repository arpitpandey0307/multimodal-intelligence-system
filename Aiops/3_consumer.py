from confluent_kafka import Consumer
from cloud_config import kafka_config 

# 1. Add consumer-specific rules to our existing cloud config
kafka_config['group.id'] = 'ml_team_alpha'     # Identifies our consumer team
kafka_config['auto.offset.reset'] = 'earliest' # If no bookmark exists, start from the beginning

# 2. Connect to Aiven Cloud and subscribe to the topic
c = Consumer(kafka_config)
c.subscribe(['ml_topic'])

print("📡 Listening to Aiven Cloud for new data...")

# 3. Continuous loop to keep checking the cloud for new messages
while True:
    # poll(1.0) checks the cloud for new data every 1 second
    msg = c.poll(1.0) 
    
    if msg is None:
        continue # No new data arrived in this second, keep waiting
        
    if msg.error():
        print(f"⚠️ Error: {msg.error()}")
        continue

    # Decode the binary data sent over the internet back into a readable string
    print(f"📥 Read from cloud: {msg.value().decode('utf-8')}")
