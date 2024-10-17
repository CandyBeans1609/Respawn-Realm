-- 1. Create Database
CREATE DATABASE formdata;

-- 2. Use the Database
USE formdata;

-- 3. Create Table
CREATE TABLE FormData (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(80) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    plan VARCHAR(20) NOT NULL,
    menu_choices VARCHAR(50) NOT NULL
);

-- 4a. Insert Data (Create)
INSERT INTO FormData (username, email, phone, plan, menu_choices) 
VALUES ('CandyBeans', 'candy@example.com', '9175947532', 'plan5', '6,14');

-- 4b. Retrieve All Data (Read)
SELECT * FROM FormData;

-- 4c. Retrieve Specific Data by ID (Read)
SELECT * FROM FormData WHERE id = 7;

-- 4d. Update Data (Update)
UPDATE FormData 
SET email = 'new_email@example.com', plan = 'new_plan'
WHERE id = 7;

-- 4e. Delete Data (Delete)
DELETE FROM FormData WHERE id = 7;
