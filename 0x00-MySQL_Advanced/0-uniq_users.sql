--create user table  to add id and email and name 
-- id is primer key
CREATE TABLE IF NOT EXISTS users (
	id INTEGER AUTOINCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
