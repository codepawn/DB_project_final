#-*- coding: utf-8 -*-
#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#


import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    print ("Connecting successful")
    return psycopg2.connect("dbname=tournament")


def db_commit_for_add(query, data):
    DB = connect()
    c = DB.cursor()
    c.execute(query, data)
    DB.commit()
    DB.close()


def db_commit1_for_get(query):
    DB = connect()
    c = DB.cursor()
    c.execute(query)
    DB.commit()
    DB.close()


def deleteMatches():
    """Remove all the match records from the database."""


def deletePlayers():
    """Remove all the player records from the database."""
    query = "delete from players"
    db_commit1_for_get(query)

deletePlayers()


def countPlayers():
    """Returns the number of players currently registered."""


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    query = "insert into players (name) values(%s)"
    data = (bleach.clean(name),)
    db_commit_for_add(query, data)

# registerPlayer('jeniffer kim')


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


# 1.보안 sql injection 과 bleach(script injection 방어) 추가
# 2.decorater 추가
