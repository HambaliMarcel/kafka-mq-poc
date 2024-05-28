import time
import json
import logging
import yaml
from kafka import KafkaProducer

logging.basicConfig(level=logging.INFO)

def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

def produce_messages():
    config = load_config()
    producer = KafkaProducer(
        bootstrap_servers=config['kafka']['bootstrap_servers'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    message_frequency = config['producer']['message_frequency']
    
    while True:
        message = {
            'type': 'user_activity',
            'user_id': 'user_123',
            'action': 'login',
            'timestamp': time.time()
        }
        try:
            producer.send(config['kafka']['topic'], value=message)
            logging.info(f'Sent: {message}')
        except Exception as e:
            logging.error(f'Error sending message: {e}')
        time.sleep(message_frequency)

if __name__ == '__main__':
    produce_messages()
