SELECT title
FROM movies
JOIN stars estrela1 ON movies.id = estrela1.movie_id
JOIN people pessoa1 ON estrela1.person_id = pessoa1.id
JOIN stars estrela2 ON movies.id = estrela2.movie_id
JOIN people pessoa2 ON estrela2.person_id = pessoa2.id
WHERE pessoa1.name = 'Bradley Cooper' AND pessoa2.name = 'Jennifer Lawrence';