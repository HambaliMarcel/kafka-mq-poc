# Kafka MQ PoC

## Overview

This project is a proof of concept (PoC) demonstrating the use of Apache Kafka as a distributed event store and stream-processing platform. It includes a simple setup with a producer and a consumer, orchestrated using Docker Compose.

## Project Structure

```
kafka-mq-poc/
├── producer/
│   ├── producer.py
├── consumer/
│   ├── consumer.py
├── docker-compose.yml
├── requirements.txt
├── README.md
```

### Prerequisites

- Docker
- Docker Compose
- Python 3.x

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/kafka-mq-poc.git
   cd kafka-mq-poc
   ```

2. **Install dependencies:**

   Create a virtual environment and install the required Python packages.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Running the Project

1. **Start Kafka and Zookeeper using Docker Compose:**

   ```bash
   docker-compose up -d
   ```

2. **Run the producer:**

   ```bash
   python producer/producer.py
   ```

3. **Run the consumer:**

   ```bash
   python consumer/consumer.py
   ```

### Stopping the Services

To stop and remove the Docker containers, run:

```bash
docker-compose down
```

Happy testingg :)
