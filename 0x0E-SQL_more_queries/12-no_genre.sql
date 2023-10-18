-- Switch to the hbtn_0d_tvshows database

-- Select the title of the TV show and its associated genre ID
-- Use a LEFT JOIN to include shows with no linked genres
-- Filter the results to only include shows without a linked genre
-- Order the results by title in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;

