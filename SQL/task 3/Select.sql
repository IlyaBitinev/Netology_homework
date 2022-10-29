SELECT name, year_of_release 
  FROM album 
 WHERE TO_CHAR(year_of_release, 'YYYY') = '2018'
 ;

SELECT name, time
  FROM track
 ORDER BY time DESC
 LIMIT 1
 ;

SELECT name, time
  FROM track
 WHERE time > 210
 ORDER BY time DESC
 ;
 
SELECT name, year_of_release
  FROM collection
 WHERE year_of_release BETWEEN '2018-01-01'
   AND '2020-12-31'
 ;

SELECT name
  FROM musician
 WHERE name NOT LIKE '% %'
;


SELECT name
  FROM track
 WHERE name LIKE '% мой %' 
    OR name LIKE '% me %'
; 