import json
import logging
import yaml
from kafka import KafkaConsumer
from database import create_connection, create_table, insert_message

logging.basicConfig(level=logging.INFO)

def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

def consume_messages():
    config = load_config()
    consumer = KafkaConsumer(
        config['kafka']['topic'],
        bootstrap_servers=config['kafka']['bootstrap_servers'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id=config['kafka']['group_id'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    db_conn = create_connection(config['database']['path'])
    create_table(db_conn)
    
    for message in consumer:
        msg_value = message.value
        try:
            insert_message(db_conn, msg_value)
            logging.info(f'Received and stored: {msg_value}')
        except Exception as e:
            logging.error(f'Error storing message: {e}')

if __name__ == '__main__':
    consume_messages()
