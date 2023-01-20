-- Script prepares a MySQL server
-- Create a new database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new USER
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
USE hbnb_test_db;
-- grant priviledges to new user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- grant select privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
