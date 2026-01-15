from kafka import KafkaProducer
from order_generator import OrderGenerator
import json
import time

class OrderProducer:
    def __init__(self, topic='orders', bootstrap_servers='localhost:9092'):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = topic
        self.generator = OrderGenerator()
    
    def send_order(self, order):
        """Send a single order to Kafka"""
        self.producer.send(self.topic, order)
        self.producer.flush()
        print(f"Sent order ID: {order['order_id']}")
    
    def stream_orders(self, interval=2):
        """Continuously generate and send orders to Kafka"""
        print("Starting order stream to Kafka...")
        try:
            while True:
                order = self.generator.generate_order()
                self.send_order(order)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nStream stopped.")
            self.producer.close()

if __name__ == "__main__":
    producer = OrderProducer()
    producer.stream_orders(interval=5) # Send an order every 5 seconds