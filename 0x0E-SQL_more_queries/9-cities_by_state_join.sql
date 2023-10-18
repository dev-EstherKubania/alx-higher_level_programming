-- List all cities with their IDs, names, and associated state names

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states on cities.state_id = states.id
ORDER BY cities.id ASC;
