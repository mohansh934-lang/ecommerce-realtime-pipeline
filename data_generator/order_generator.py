from faker import Faker
import json
import random
from datetime import datetime
import time

fake = Faker()

class OrderGenerator:
    def __init__(self):
        self.categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']
        self.payment_methods = ['credit_card', 'debit_card', 'upi', 'wallet']
    
    def generate_order(self):
        """Generate a single order"""
        return {
            'order_id': fake.uuid4(),
            'user_id': random.randint(1000, 9999),
            'product_id': random.randint(100, 999),
            'product_name': fake.word().capitalize(),
            'category': random.choice(self.categories),
            'quantity': random.randint(1, 5),
            'price': round(random.uniform(99.99, 9999.99), 2),
            'payment_method': random.choice(self.payment_methods),
            'timestamp': datetime.now().isoformat(),
            'status': random.choice(['pending', 'confirmed', 'shipped', 'delivered', 'cancelled']),
            'location': fake.city()
        }
    
    def generate_batch(self, count=10):
        """Generate multiple orders"""
        return [self.generate_order() for _ in range(count)]
    
    def stream_orders(self, interval=2):
        """Continuously generate orders"""
        print("Starting order stream...")
        try:
            while True:
                order = self.generate_order()
                print(json.dumps(order, indent=2))
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nStream stopped.")

# Test
if __name__ == "__main__":
    generator = OrderGenerator()
    
    # Test single order
    print("=== Single Order ===")
    print(json.dumps(generator.generate_order(), indent=2))
    
    # # Test batch
    # print("\n=== Batch of 5 ===")
    # for order in generator.generate_batch(5):
    #     print(json.dumps(order, indent=2))
    
    # # Test streaming (uncomment to run)
    # print("\n=== Streaming Orders (Press Ctrl+C to stop) ===")
    # print(json.dumps(generator.stream_orders(), indent=2))