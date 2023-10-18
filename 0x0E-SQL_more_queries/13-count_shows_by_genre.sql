-- Switch to the hbtn_0d_tvshows database
-- Select the genre name and count the number of shows linked to each genre
-- Use an INNER JOIN to link genres with shows through tv_show_genres
-- Group the results by genre name
-- Order the results by the number of shows linked in descending order
SELECT genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;

