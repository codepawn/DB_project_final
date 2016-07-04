-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE IF EXISTS players CASCADE;
DROP TABLE IF EXISTS matches CASCADE;
\c vagrant;
DROP DATABASE tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players(
  id serial UNIQUE PRIMARY KEY,
  name varchar(30));

CREATE TABLE matches(
  matche_id serial UNIQUE PRIMARY KEY,
  winner serial REFERENCES players(id),
  loser serial REFERENCES players(id));

-- INSERT INTO players (name) VALUES ('Hanjo');
-- INSERT INTO players (name) VALUES ('76');
-- INSERT INTO players (name) VALUES ('Genzi');
-- INSERT INTO players (name) VALUES ('Widow');
--
-- INSERT INTO matches (winner,loser) VALUES (1,2);
-- INSERT INTO matches (winner,loser) VALUES (2,3);
-- INSERT INTO matches (winner,loser) VALUES (4,1);
-- INSERT INTO matches (winner,loser) VALUES (4,1);

CREATE VIEW view_wins AS
  SELECT players.id, count(matches.winner) as winner
  FROM players LEFT JOIN matches
  ON players.id = matches.winner
  GROUP BY players.id, matches.winner;

CREATE VIEW view_matches AS
  SELECT players.id, count(matches) as matches
  FROM players LEFT JOIN matches
  ON(players.id = matches.winner)
  OR (players.id = matches.loser)
  GROUP BY players.id
