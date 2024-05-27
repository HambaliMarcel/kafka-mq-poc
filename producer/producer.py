from kafka import KafkaProducer
import json
import time

def produce_messages():
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    while True:
        message = {'message': 'Hello, Kafka!', 'timestamp': time.time()}
        producer.send('test_topic', value=message)
        print(f'Sent: {message}')
        time.sleep(2)

if __name__ == '__main__':
    produce_messages()
