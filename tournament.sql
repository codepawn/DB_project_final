-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE IF EXISTS players CASCADE;


DROP TABLE IF EXISTS matches CASCADE;


CREATE DATABASE tournament;

\c tournament;


CREATE TABLE players(id serial UNIQUE PRIMARY KEY,
                                              name varchar(30));


CREATE TABLE matches(matche_id serial UNIQUE PRIMARY KEY,
                                                     winner serial REFERENCES players(id),
                                                                              loser serial REFERENCES players(id));
