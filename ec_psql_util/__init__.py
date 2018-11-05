__author__ = 'Scot Powell'
import logging
import socket

import psycopg2

SQL_QUERY_STREETS = "SELECT st_full_name FROM address.unique_street_names ORDER BY st_full_name"
SQL_QUERY_ADDRESSES = "SELECT add_address FROM address.view_unique_addresses ORDER by add_address"


def psql_connection(_database=r"ec", _user=r"sde", _password=r"sde", _host=r"localhost", _port=r"5432", _read_only=False):
    database = _database
    user = _user
    password = _password
    host = _host
    port = _port
    db = None
    if socket.gethostname() == "gis-development":
        database = r"ec"
    if socket.gethostname() == "gis":
        port = r"5432"
        host = r"localhost"
        database = r"ec"
        user = r"sde"
        password = r"sde"
    if socket.gethostname() == "home-gis":
        port = r"5432"
        host = r"localhost"
        database = r"ec"
        user = r"sde"
        password = r"sde"

    try:
        db = psycopg2.connect(database=database,
                              user=user,
                              password=password,
                              host=host,
                              port=port)
        db.set_session(readonly=_read_only, autocommit=False)

    except psycopg2.Error as e:
        logging.error(e)
        return None

    return db


def sql_get_streets():
    print("sql_get_streets")
    con = psql_connection("ec", "sde", "sde", "localhost", "5432")
    list_streets = list()

    try:
        if con is None:
            logging.debug("Connection is None")
            return
        cur = con.cursor()
        cur.execute(SQL_QUERY_STREETS)
        rows = cur.fetchall()

        for row in rows:
            list_streets.append({"street": row[0]})

        logging.debug(list_streets)
        return list_streets

    except psycopg2.Error as e:
        logging.error(e)

    finally:
        if con:
            con.commit()
            con.close()


def sql_get_addresses():
    print("sql_get_addresses")
    con = psql_connection("ec", "sde", "sde", "localhost", "5432")
    list_addresses = list()

    try:
        if con is None:
            logging.debug("Connection is None")
            return
        cur = con.cursor()
        cur.execute(SQL_QUERY_ADDRESSES)
        rows = cur.fetchall()

        for row in rows:
            list_addresses.append({"address": row[0]})

        logging.debug(list_addresses)
        return list_addresses

    except psycopg2.Error as e:
        logging.error(e)

    finally:
        if con:
            con.commit()
            con.close()
