-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- lists all rows of a database that have one column in common
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN
(SELECT genre_id FROM tv_show_genres WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter'))
ORDER BY tv_genres.name ASC;
