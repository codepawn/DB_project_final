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


def db_commit_decoration(func):
    def wrapper():
        DB = connect()
        cur = DB.cursor()
        cur.execute(func())
        DB.commit()
        DB.close()
    return wrapper


@db_commit_decoration
def deleteMatches():
    """Remove all the match records from the database."""
    query = "delete from matches"
    return query


@db_commit_decoration
def deletePlayers():
    """Remove all the player records from the database."""
    query = "delete from players"
    return query


def countPlayers():
    """Returns the number of players currently registered."""
    players_container = 0
    DB = connect()
    cur = DB.cursor()
    query = "select count(id) from players"
    cur.execute(query)
    players_container = cur.fetchone()
    DB.close()
    return players_container[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    cur = DB.cursor()
    query = "insert into players (name) values(%s)"
    data = (bleach.clean(name),)
    cur.execute(query, data)
    DB.commit()
    DB.close()


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
    select players.id, players.name, view_wins.winner, view_matches.matches
    from players left join view_wins on players.id = view_wins.id
    left join view_matches on players.id = view_matches.id
    group by players.id, players.name, view_wins.winner, view_matches.matches
    order by view_wins.winner desc;
    """
    cur.execute(query)
    players = cur.fetchall()
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
    query = "insert into matches (winner,loser) values({},{}) ".format(
        winner, loser)
    cur.execute(query)
    DB.commit()
    DB.close()


def gruping(list, size=2):
    size = max(1, size)
    return [list[i:i + size] for i in range(0, len(list), size)]


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
    standings = playerStandings()
    if len(standings) % 2 != 0:
        raise "Odd number of players"
    grouped_standings = gruping(standings, 2)
    matched_pairs = list()

    for stand in grouped_standings:
        pair = list()
        for player in stand:
            pair.append(player[0])
            pair.append(player[1])
        matched_pairs.append(pair)
    return matched_pairs

print playerStandings()
print swissPairings()

if __name__ == "__main__":
    print "Hello world"
