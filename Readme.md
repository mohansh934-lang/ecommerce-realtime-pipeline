# Real-Time E-Commerce Analytics Pipeline

## 📋 Project Overview

End-to-end streaming data pipeline that simulates e-commerce transactions, processes them in real-time using Apache Kafka, and stores analytics-ready data in PostgreSQL.

## 🏗️ Architecture
```
Data Generator (Python) 
    ↓
Kafka Producer (orders topic)
    ↓
Apache Kafka (3 partitions)
    ↓
Kafka Consumer
    ↓
PostgreSQL Database
    ↓
Analytics & Insights
```

## 🛠️ Tech Stack

- **Python 3.x** - Data generation & processing
- **Apache Kafka** - Real-time message streaming
- **Zookeeper** - Kafka coordination
- **PostgreSQL** - Data warehouse
- **Docker** - Container orchestration
- **Faker** - Realistic test data generation

## 📊 Features

- Real-time order generation with realistic e-commerce data
- Distributed streaming with Kafka (3 partitions)
- Automatic data persistence to PostgreSQL
- Analytics-ready data warehouse schema
- Scalable architecture (producer-consumer pattern)

## 🚀 Setup Instructions

### Prerequisites

- Python 3.x
- Docker & Docker Compose
- PostgreSQL 13+
- Git

### Installation

1. **Clone repository**
```bash
   git clone <your-repo-url>
   cd ecommerce-realtime-pipeline
```

2. **Create virtual environment**
```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Start Kafka & Zookeeper**
```bash
   cd kafka_jobs
   docker-compose up -d
```

5. **Create Kafka topic**
```bash
   docker exec -it kafka kafka-topics --create --topic orders --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```

6. **Setup PostgreSQL**
```bash
   sudo -u postgres psql -f sql_scripts/schema.sql
```

## ▶️ Running the Pipeline

### Terminal 1: Start Producer
```bash
source venv/bin/activate
python3 data_generator/kafka_producer.py
```

### Terminal 2: Start Consumer (saves to DB)
```bash
source venv/bin/activate
python3 data_generator/kafka_consumer_db.py
```

### Terminal 3: View live data (optional)
```bash
sudo docker exec -it kafka kafka-console-consumer --topic orders --bootstrap-server localhost:9092
```

## 📈 Analytics Queries

Access PostgreSQL:
```bash
sudo -u postgres psql ecommerce_analytics
```

**Total Revenue:**
```sql
SELECT SUM(price * quantity) as total_revenue, COUNT(*) as total_orders FROM orders;
```

**Revenue by Category:**
```sql
SELECT category, COUNT(*) as orders, SUM(price * quantity) as revenue 
FROM orders GROUP BY category ORDER BY revenue DESC;
```

**Status Distribution:**
```sql
SELECT status, COUNT(*) as count, 
ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage 
FROM orders GROUP BY status;
```

## 📁 Project Structure
```
ecommerce-realtime-pipeline/
├── data_generator/
│   ├── order_generator.py      # Fake data generation
│   ├── kafka_producer.py       # Kafka producer
│   ├── kafka_consumer.py       # Simple consumer (print)
│   └── kafka_consumer_db.py    # Consumer with DB integration
├── kafka_jobs/
│   └── docker-compose.yml      # Kafka + Zookeeper setup
├── sql_scripts/
│   └── schema.sql              # PostgreSQL schema
├── requirements.txt
└── README.md
```

## 🎯 Key Learnings

- Real-time data streaming with Kafka
- Producer-consumer pattern implementation
- Database integration with streaming data
- Docker containerization
- Data pipeline architecture

## 🔮 Future Enhancements

- [ ] Add PySpark for stream processing
- [ ] Implement data quality checks
- [ ] Add monitoring (Prometheus/Grafana)
- [ ] Deploy to AWS (MSK, RDS)
- [ ] Add CI/CD pipeline

## 👤 Author

**Mohan**  
Data Engineering Portfolio Project