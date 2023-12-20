CREATE DATABASE tyrell_corp;

USE tyrell_corp;

CREATE TABLE nexus6 (
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO nexus6 (id, name) VALUES (1, 'Leon');

GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

SHOW TABLES;

SELECT * FROM nexus6;
