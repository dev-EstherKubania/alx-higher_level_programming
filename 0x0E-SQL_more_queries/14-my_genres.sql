-- Switch to the hbtn_0d_tvshows database
-- Select the genre name and count the number of shows linked to each genre for the show "Dexter"
-- Use INNER JOINs to link genres, show genres, and shows
-- Filter the results to only include shows with the title "Dexter"
-- Group the results by genre id
-- Order the results by the number of shows linked in descending order, and genre id in ascending order

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC, tv_genres.id ASC;

