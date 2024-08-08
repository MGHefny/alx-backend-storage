--create user table
CREATE TABLE IF NOT EXISTS users (
	id int AUTOINCREMENT PRIMARY KEY,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
);
