
CREATE DATABASE IF NOT EXISTS db;
USE db;
CREATE TABLE IF NOT EXISTS table_name(id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, col1 LONGTEXT, col2 LONGTEXT);
CREATE USER 'user'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON db.table_name TO 'user'@'%';
INSERT INTO table_name(col1, col2) VALUES ('Ich bin ein Berliner', 'I am a Berliner');