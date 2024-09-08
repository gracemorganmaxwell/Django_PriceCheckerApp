-- Create the database
CREATE DATABASE IF NOT EXISTS PriceCheck;
USE PriceCheck;

-- Drop tables if they exist
DROP TABLE IF EXISTS UserStorePreference;
DROP TABLE IF EXISTS Profile;
DROP TABLE IF EXISTS PriceHistory;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Store;
DROP TABLE IF EXISTS SupermarketChain;
DROP TABLE IF EXISTS auth_user;

-- Create the auth_user table (simplified version for this example)
CREATE TABLE auth_user (
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(150) NOT NULL UNIQUE,
email VARCHAR(254) NOT NULL,
password VARCHAR(128) NOT NULL
) ENGINE=InnoDB;

-- Create the SupermarketChain table
CREATE TABLE SupermarketChain (
chain_id INT AUTO_INCREMENT PRIMARY KEY,
chain_name VARCHAR(2) NOT NULL,
CHECK (chain_name IN ('Nw', 'Cd', 'Ps', 'Fc', 'Wh'))
) ENGINE=InnoDB;

-- Create the Store table
CREATE TABLE Store (
store_id INT AUTO_INCREMENT PRIMARY KEY,
store_name VARCHAR(20) NOT NULL,
store_address TEXT NOT NULL,
store_region VARCHAR(15) NOT NULL,
chain_id INT,
FOREIGN KEY (chain_id) REFERENCES SupermarketChain(chain_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create the Product table
CREATE TABLE Product (
product_id INT AUTO_INCREMENT PRIMARY KEY,
product_name VARCHAR(25) NOT NULL,
product_image VARCHAR(255),
unit_type VARCHAR(10) NOT NULL,
store_id INT,
product_code VARCHAR(10) UNIQUE NOT NULL,
unit_price DECIMAL(10, 2) NOT NULL,
on_sale BOOLEAN NOT NULL,
FOREIGN KEY (store_id) REFERENCES Store(store_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create the PriceHistory table
CREATE TABLE PriceHistory (
price_history_id INT AUTO_INCREMENT PRIMARY KEY,
product_id INT,
price DECIMAL(10, 2) NOT NULL,
date DATE NOT NULL,
on_sale BOOLEAN NOT NULL,
FOREIGN KEY (product_id) REFERENCES Product(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create the Profile table
CREATE TABLE Profile (
user_id INT PRIMARY KEY,
user_type VARCHAR(30),
FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create the UserStorePreference table
CREATE TABLE UserStorePreference (
USP_id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
store_id INT,
FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE,
FOREIGN KEY (store_id) REFERENCES Store(store_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Insert mock data into auth_user
INSERT INTO auth_user (username, email, password) VALUES
('admin', 'admin@example.com', 'password123'),
('customer', 'customer@example.com', 'password456');

-- Insert mock data into SupermarketChain
INSERT INTO SupermarketChain (chain_name) VALUES
('Nw'), ('Cd'), ('Ps'), ('Fc'), ('Wh');

-- Insert mock data into Store
INSERT INTO Store (store_name, store_address, store_region, chain_id) VALUES
('New World Albany', '123 Main St', 'Auckland', 1),
('Countdown Newmarket', '456 High St', 'Auckland', 2),
('Pak n Save Manukau', '789 Low St', 'Auckland', 3),
('Fresh Choice Nelson', '101 Beach Rd', 'Nelson', 4),
('Warehouse Chch', '202 River Ln', 'Christchurch', 5);

-- Insert mock data into Product
INSERT INTO Product (product_name, product_image, unit_type, store_id, product_code, unit_price, on_sale) VALUES
('Milk', 'products/milk.jpg', 'ltr', 1, 'P001', 3.99, FALSE),
('Bread', 'products/bread.jpg', 'loaf', 2, 'P002', 2.49, TRUE),
('Eggs', 'products/eggs.jpg', 'dozen', 3, 'P003', 4.99, FALSE),
('Cheese', 'products/cheese.jpg', 'kg', 4, 'P004', 8.99, TRUE),
('Apples', 'products/apples.jpg', 'kg', 5, 'P005', 2.99, FALSE);

-- Insert mock data into PriceHistory
INSERT INTO PriceHistory (product_id, price, date, on_sale) VALUES
(1, 3.99, '2023-01-01', FALSE),
(1, 3.79, '2023-01-15', TRUE),
(2, 2.49, '2023-01-01', TRUE),
(3, 4.99, '2023-01-01', FALSE),
(4, 8.99, '2023-01-01', TRUE),
(5, 2.99, '2023-01-01', FALSE);

-- Insert mock data into Profile
INSERT INTO Profile (user_id, user_type) VALUES
(1, 'admin'),
(2, 'customer');

-- Insert mock data into UserStorePreference
INSERT INTO UserStorePreference (user_id, store_id) VALUES
(1, 1),
(2, 2),
(2, 3);
