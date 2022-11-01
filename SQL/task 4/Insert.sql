INSERT INTO genre (name)
VALUES 
       ('Hip-hop'),
       ('Pop'),
       ('Rock'),
       ('Reggae'),
       ('House')
;

INSERT INTO musician (name)
VALUES 
       ('ATL'),
       ('Justin Timberlake'),
       ('Bob Marley'),
       ('Ghostemane'),
       ('Coolio'),
       ('Brennan Savage'),
       ('Avicii'),
       ('Skillet')
;

INSERT INTO music_genre (genre_id, musician_id)
VALUES 
       (1, 1),
       (2, 2),
       (4, 3),
       (1, 4),
       (3, 4),
       (1, 5),
       (1, 6),
       (5, 7),
       (3, 8)
;
       

INSERT INTO album (name, year_of_release)
VALUES 
       ('Марабу', '2015-10-27'),
       ('Man_of_the Woods', '2018-02-02'),
       ('Survival', '1979-10-02'),
       ('Anti-Icon', '2020-10-21'),
       ('Gangstas_Paradise', '1995-11-07'),
       ('Badlands', '2017-05-17'),
       ('True', '2013-09-13'),
       ('Awake', '2009-08-25')
;
       
INSERT INTO musician_album(musician_id, album_id)
VALUES 
       (1, 1),
       (2, 2),
       (3, 3),
       (4, 4),
       (5, 5),
       (6, 6),
       (7, 7),
       (8, 8)
;

INSERT INTO track (name, time, album_id)
VALUES 
       ('Пчелки', 166, 1),
       ('Марабу', 173, 1),
       ('Filthy', 293, 2),
       ('Say_Something', 279, 2),
       ('Survival', 234, 3),
       ('Wake_up_and_live', 300, 3),
       ('Fed_up', 151, 4),
       ('Al', 174, 4),
       ('Gangstas_Paradise', 240, 5),
       ('Too_hot', 219, 5),
       ('Badiands', 104, 6),
       ('Lonely_world', 102, 6),
       ('Wake me up', 246, 7),
       ('Hey_brother', 255, 7),
       ('Hero', 186, 8),
       ('Monster', 177, 8),
       ('Vagabond', 114, 4)
;

INSERT INTO collection (name, year_of_release)
VALUES 
       ('Mp-3 Collection', '2010-01-01'),
	   ('Unreleased', '2018-01-01'),
	   ('Best', '2019-02-04'),
	   ('Rock_Hit', '2020-02-05'),
	   ('Studio Collection', '2022-05-06'),
	   ('Greatest Hits', '2021-02-05'),
	   ('Pop', '2018-12-22'),
	   ('Favorite', '2020-08-09'),
	   ('Rap', '2022-01-02')
;

INSERT INTO track_collection (track_id, collection_id)
VALUES 
       (1, 3),
       (2, 8),
       (3, 6),
       (4, 5),
       (5, 1),
       (6, 1),
       (7, 4),
       (8, 7),
       (9, 8),
       (10, 1),
       (11, 2),
       (12, 2),
       (13, 5),
       (14, 3),
       (15, 4),
       (16, 3),
       (17, NULL)
;
