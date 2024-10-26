SELECT name
FROM people
WHERE people.id IN (
    SELECT person_id
    FROM stars JOIN movies ON movies.id = stars.movie_id
    WHERE movie_id IN (
        SELECT movie_id
        FROM movies JOIN stars
        ON stars.movie_id = movies.id
        JOIN people
        ON people.id = stars.person_id
        WHERE people.id IN (
            SELECT id
            FROM people
            WHERE people.name = 'Kevin Bacon' AND people.birth = 1958
        )
    )
)
EXCEPT SELECT name FROM people WHERE people.name = "Kevin Bacon" AND people.birth = 1958;
-- SELECT name
-- FROM people
-- WHERE ID IN (
--     SELECT person_id
--     FROM stars
--     WHERE movie_id IN (
--         SELECT movie_id
--         FROM stars
--         WHERE person_id = (
--             SELECT id
--             FROM people
--             WHERE name = 'Kevin Bacon' AND birth = 1958
--         )
--     )
-- );

-- SELECT id
-- FROM people
-- WHERE name = 'Kevin Bacon' AND birth = 1958;
-- Kevin Bacon ID 102

-- SELECT name
-- FROM people
-- WHERE ID IN (
--     SELECT person_id
--     FROM stars
--     WHERE movie_id IN (
--         SELECT movie_id
--         FROM stars JOIN people
--         ON stars.person_id = people.id
--         WHERE name = 'Kevin Bacon' AND birth = 1958
--         )
--     );


