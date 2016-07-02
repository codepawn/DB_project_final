#-*- coding: utf-8 -*-
#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#


import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def db_commit_for_add(query, data):
    DB = connect()
    cur = DB.cursor()
    cur.execute(query, data)
    DB.commit()
    DB.close()


def db_commit1_for_run(query):
    DB = connect()
    cur = DB.cursor()
    cur.execute(query)
    DB.commit()
    DB.close()


def deleteMatches():
    """Remove all the match records from the database."""
    query = "delete from matches"
    db_commit1_for_run(query)


def deletePlayers():
    """Remove all the player records from the database."""
    query = "delete from players"
    db_commit1_for_run(query)


def countPlayers():
    """Returns the number of players currently registered."""
    players_container = 0
    DB = connect()
    cur = DB.cursor()
    query = "select count(*) from players"
    cur.execute(query)
    players_container = cur.fetchone()
    DB.commit()
    DB.close()
    return players[0]


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
    players = ()
    DB = connect()
    cur = DB.cursor()
    query = """
    select players.id, players.name, matches.winner, matches.loser
    from players left join matches
    on players.id = matches.id;
    """
    cur.execute(query)
    players = cur.fetchall()
    print players
    DB.commit()
    DB.close()
    return players


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    cur = DB.cursor()
    query = "insert into matches values({},{}) ".format(winner, loser)
    cur.execute(query)
    DB.commit()
    DB.close()


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

if __name__ == "__main__":
    # deleteMatches()
    # deletePlayers()
    # print countPlayers()
    # registerPlayer('Young Ahn')
