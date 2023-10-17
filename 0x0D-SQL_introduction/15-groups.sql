-- Task: List the number of records with the same score in second_table

-- List score and number of records for each score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

