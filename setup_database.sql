CREATE DATABASE IF NOT EXISTS expense_project;
USE expense_project;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE,
    amount DECIMAL(10, 2),
    merchant VARCHAR(255),
    payment_method VARCHAR(100),
    category VARCHAR(100),
    notes TEXT
);