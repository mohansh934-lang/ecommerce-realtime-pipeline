# Real-Time E-Commerce Analytics Pipeline

## Overview
End-to-end real-time streaming data pipeline for e-commerce analytics.
This project simulates live order data and processes it using Kafka and Python-based consumers.

## Tech Stack
- Python
- Apache Kafka
- PostgreSQL
- Docker & Docker Compose

## Architecture
Order Generator → Kafka Producer → Kafka Consumer → PostgreSQL

## Components
- **data_generator/**
  - order_generator.py – generates fake e-commerce orders
  - kafka_producer.py – streams orders to Kafka
- **kafka_consumer.py** – consumes data from Kafka
- **kafka_consumer_db.py** – stores Kafka data into PostgreSQL
- **schema.sql** – database schema
- **docker-compose.yml** – Kafka & DB setup

## Progress
- [x] Data Generator (Faker-based)
- [x] Kafka Producer
- [x] Kafka Consumer
- [x] PostgreSQL Integration
- [x] Docker Setup
- [ ] PySpark Streaming
- [ ] Analytics Queries / Dashboard

## Status
🚧 Work in progress – building step-by-step as a real-time data engineering project.
