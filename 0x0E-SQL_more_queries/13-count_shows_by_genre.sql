-- Switch to the hbtn_0d_tvshows database
-- Select the genre name and count the number of shows linked to each genre
-- Use an INNER JOIN to link genres with shows through tv_show_genres
-- Group the results by genre name
-- Order the results by the number of shows linked in descending order
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
