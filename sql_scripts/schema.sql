-- Create database
CREATE DATABASE ecommerce_analytics;

-- Connect
\c ecommerce_analytics;

-- Create orders table
CREATE TABLE orders (
    order_id VARCHAR(100) PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER,
    product_name VARCHAR(255),
    category VARCHAR(50),
    quantity INTEGER,
    price DECIMAL(10, 2),
    payment_method VARCHAR(50),
    timestamp TIMESTAMP,
    status VARCHAR(50),
    location VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);