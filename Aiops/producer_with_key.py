from confluent_kafka import Producer
from cloud_config import kafka_config
import time

p=Producer(kafka_config)

# We are simulating two diffrent users clicking on our app.
users = ["user_A", "user_B"]

for i in range(100):
    #Alternate between the two users
    current_user = users[i % 2]
    data = f"Action {i} from {current_user}"

    #Adding the 'key' ensure this message will always go to the same partition for the same user.
    p.produce(
        'ml_topic',
        key=current_user.encode('utf-8'),   #the key is the user id, so all messages from the same user will go to the same partition
        value=data.encode('utf-8')   #the value is the actual data we want to send to the topic.
    )

    print(f"Produced record to topic ml_topic: key = {current_user}, value = {data}")
    time.sleep(1)

p.flush()