from kafka import KafkaConsumer
import json

def consume_messages():
    # Initialize Kafka consumer without the 'value_serializer' config
    consumer = KafkaConsumer(
        'test_topic',
        bootstrap_servers='localhost:9092',
        group_id='my-group',
        auto_offset_reset='earliest'
    )

    # Consume messages from the topic
    for message in consumer:
        # Deserialize the message value manually
        value = json.loads(message.value.decode('utf-8'))
        print(f"Received message: {value}")

if __name__ == "__main__":
    consume_messages()
