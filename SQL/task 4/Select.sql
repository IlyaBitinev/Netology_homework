-- количество исполнителей в каждом жанре

SELECT genre.name, COUNT(DISTINCT musician_id) AS musician
  FROM genre 
  JOIN music_genre USING(genre_id)
 GROUP BY genre.name;

-- количество треков, вошедших в альбомы 2019-2020 годов

SELECT album.name, year_of_release, COUNT(track.name) 
  FROM album
  JOIN track USING(album_id)
 WHERE year_of_release BETWEEN '2019-01-01' 
   AND '2020-12-31'
 GROUP BY album.name, year_of_release;
 
-- средняя продолжительность треков по каждому альбому

SELECT album.name, ROUND(AVG(time), 2) 
    AS avg_duration 
  FROM album
  JOIN track USING(album_id)
 GROUP BY album.name;
	
-- все исполнители, которые не выпустили альбомы в 2020 году

SELECT musician.name
  FROM musician 
  JOIN musician_album USING(musician_id)
  JOIN album USING(album_id)
 WHERE musician_id  NOT IN (SELECT musician_id
							  FROM musician_album
							 INNER JOIN album USING(album_id)
							 WHERE TO_CHAR(album.year_of_release, 'YYYY') LIKE '%2020%')
 GROUP BY musician.name;
 
-- названия сборников, в которых присутствует конкретный исполнитель

SELECT musician.name, collection.name 
  FROM collection
  JOIN track_collection USING(collection_id)
  JOIN track USING(track_id)
  JOIN album USING(album_id)
  JOIN musician_album USING(album_id)
  JOIN musician USING(musician_id)
WHERE musician.name LIKE 'ATL'
GROUP BY collection.name, musician.name;

-- название альбомов, в которых присутствуют исполнители более 1 жанра

SELECT album.name, musician.name, count(album_id) 
  FROM album
  JOIN musician_album USING(album_id)
  JOIN musician USING(musician_id)
  JOIN music_genre USING(musician_id)
  JOIN genre USING(genre_id)
 GROUP BY album.name, musician.name
HAVING COUNT(genre.name) > 1;

-- наименование треков, которые не входят в сборники

SELECT track.name
  FROM track 
  JOIN track_collection USING(track_id)
 WHERE track_collection.collection_id is NULL 
 GROUP BY track.name;
 
-- исполнитель, написавшего самый короткий по продолжительности трек 

SELECT musician.name, track.time
  FROM musician 
 INNER JOIN musician_album USING(musician_id)
 INNER JOIN album USING(album_id)
 INNER JOIN track USING(album_id)
 WHERE track.time = (SELECT MIN(track.time)
				       FROM track)
 GROUP BY musician.name, track.time;

-- название альбомов, содержащих наименьшее количество треков

SELECT album.name, COUNT(track.name) 
  FROM album
 INNER JOIN track USING (album_id)
 GROUP BY album.name
HAVING COUNT(track.name) = (SELECT COUNT(track.name) AS t
						      FROM album
							 INNER JOIN track USING(album_id)
							 GROUP BY album.name
							 ORDER BY t
							 LIMIT 1);