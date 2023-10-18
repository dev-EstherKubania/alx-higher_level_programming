-- Switch to the hbtn_0d_tvshows database
-- Select the titles of shows that do not have the genre "Comedy"
SELECT tv_shows.title FROM tv_shows LEFT JOIN (SELECT tv_shows.title FROM tv_shows INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name = "Comedy" ORDER BY tv_shows.id) comedy_shows ON comedy_shows.title = tv_shows.title WHERE comedy_shows.title IS NULL ORDER BY tv_shows.title;
