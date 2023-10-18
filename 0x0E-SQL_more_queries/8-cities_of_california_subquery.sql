-- List all cities of California in hbtn_0d_usa

USE hbtn_0d_usa; -- Switch to the database

SELECT * 
FROM cities
WHERE state_id = (
    SELECT id 
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;

