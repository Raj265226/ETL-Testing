To know the driver name you need to run below code - 
import pyodbc
print(pyodbc.drivers())
from that output you will get driver name. here, driver = MySQL ODBC 9.7 Unicode Driver

DATABASE Setup -
CREATE DATABASE etl_testing;
USE etl_testing;

CREATE TABLE source_users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO source_users
(user_id, user_name, email)
VALUES
(1, 'Rohit', 'rohit@xyz.com'),
(2, 'Raj', 'raj@xyz.com'),
(3, 'Rahul', 'rahul@gmail.com');

CREATE TABLE target_users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(100),
    user_email VARCHAR(20)
);

INSERT INTO target_users
(user_id, user_name, user_email)
VALUES
(1, 'Rohit', 'rohit@xyz.com'),
(2, 'Raj', 'raj@xyz.com');