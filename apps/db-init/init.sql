CREATE DATABASE IF NOT EXISTS webstack;
USE webstack;

CREATE TABLE IF NOT EXISTS settings (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

INSERT INTO settings (id, name)
VALUES (1, 'Andrei Vlaicu')
ON DUPLICATE KEY UPDATE name = VALUES(name);
