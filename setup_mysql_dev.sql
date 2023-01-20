-- Script prepares a MySQL server
-- Create a new database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new USER
SET GLOBAL validate_password.policy = 0;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant priviledges to new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- grant select privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
