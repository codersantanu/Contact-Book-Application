-- Create the database
CREATE DATABASE IF NOT EXISTS contact_book;

-- Use the database
USE contact_book;

-- Create the contacts table
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some sample data (optional)
INSERT INTO contacts (name, phone, email) VALUES
('John Doe', '1234567890', 'john@example.com'),
('Jane Smith', '9876543210', 'jane@example.com');
