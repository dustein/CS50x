-- SELECT avg(energy)
-- FROM songs
-- WHERE artist_id = (
--     SELECT id
--     FROM artists
--     WHERE name = 'Drake'
-- );

-- SELECT songs.name, artists.name
-- FROM songs JOIN artists
-- ON artists.id = songs.artist_id
-- WHERE artists.name = 'Drake';

SELECT avg(energy)
FROM songs JOIN artists
ON artists.id = songs.artist_id
WHERE artists.name = 'Drake';