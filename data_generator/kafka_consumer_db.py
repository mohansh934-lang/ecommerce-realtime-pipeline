from kafka import KafkaConsumer
import json
import psycopg2
from datetime import datetime

class OrderConsumerDB:
    def __init__(self, topic='orders', bootstrap_servers='localhost:9092'):
        # Kafka consumer
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            group_id='order-db-consumer',
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            auto_offset_reset='earliest'
        )
        
        # PostgreSQL connection
        self.conn = psycopg2.connect(
            host="localhost",
            database="ecommerce_analytics",
            user="postgres",
            password="mohan"  # Change if different
        )
        self.cursor = self.conn.cursor()
        print("Connected to PostgreSQL!")
    
    def consume_and_save(self):
        print("Consuming orders and saving to database...")
        try:
            for message in self.consumer:
                order = message.value
                self.save_order(order)
                print(f"Saved: {order['order_id']}")
        except KeyboardInterrupt:
            print("\nStopped.")
        finally:
            self.cursor.close()
            self.conn.close()
            self.consumer.close()
    
    def save_order(self, order):
        query = """
        INSERT INTO orders 
        (order_id, user_id, product_id, product_name, category, 
         quantity, price, payment_method, timestamp, status, location)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (order_id) DO NOTHING
        """
        
        values = (
            order['order_id'],
            order['user_id'],
            order['product_id'],
            order['product_name'],
            order['category'],
            order['quantity'],
            order['price'],
            order['payment_method'],
            datetime.fromisoformat(order['timestamp']),
            order['status'],
            order['location']
        )
        
        self.cursor.execute(query, values)
        self.conn.commit()

if __name__ == "__main__":
    consumer = OrderConsumerDB()
    consumer.consume_and_save()