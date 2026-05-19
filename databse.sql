CREATE DATABASE women_safety;
USE women_safety;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(255)
);

CREATE TABLE incidents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    latitude FLOAT,
    longitude FLOAT,
    risk_level VARCHAR(20),
    crime_rate FLOAT,
    hour INT,
    month INT,
    anomaly_flag BOOLEAN,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE distress_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    message TEXT,
    distress_flag BOOLEAN,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);