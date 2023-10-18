-- Switch to the hbtn_0d_tvshows database
-- Select the title of the TV show and its associated genre name
-- Use LEFT JOINs to include shows without a linked genre
-- Order the results by title and genre name in ascending order
SELECT tv_shows.title, tv_genres.name FROM tv_shows LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id ORDER BY tv_shows.title, tv_genres.name;
