from kafka import KafkaConsumer
import json

class OrderConsumer:
    def __init__(self, topic='orders', bootstrap_servers='localhost:9092', 
                 group_id='order-consumer-group'):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True
        )
        self.topic = topic
    
    def consume_orders(self):
        print(f"Consuming from topic '{self.topic}'...")
        try:
            for message in self.consumer:
                order = message.value
                print(f"\n--- Order Received ---")
                print(f"Order ID: {order['order_id']}")
                print(f"User: {order['user_id']}")
                print(f"Product: {order['product_name']} ({order['category']})")
                print(f"Price: ${order['price']}")
                print(f"Status: {order['status']}")
                print(f"Partition: {message.partition}, Offset: {message.offset}")
        except KeyboardInterrupt:
            print("\nConsumer stopped.")
        finally:
            self.consumer.close()

if __name__ == "__main__":
    consumer = OrderConsumer()
    consumer.consume_orders()