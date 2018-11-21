import pyodbc

__author__ = 'Scot Powell'
import logging
import socket

import psycopg2

SQL_QUERY_STREETS = "SELECT st_full_name FROM address.unique_street_names ORDER BY st_full_name"
SQL_QUERY_ADDRESSES = "SELECT add_address FROM address.unique_addresses ORDER BY add_address"

def sql_server_connect(driver, server, database, trusted_connection, uid):
    try:
        return pyodbc.connect(Driver=driver, Server=server, Database=database, Trusted_Connection=trusted_connection, uid=uid)

    # "Driver={SQL Server Native Client 11.0};"
    #                         "Server=HOME-GIS\SQLEXPRESS;"
    #                         "Database=ec;"
    #                         "Trusted_Connection=yes;"
    #                         "uid=HOME-GIS\\sde;pwd=sde")
    except Exception as e:
        logging.error("{} {}".format(inspect.stack()[0][3], e))

def sql_get_streets():
    con = sql_server_connect(driver=r"{SQL Server Native Client 11.0};",
                                     server="HOME-GIS\SQLEXPRESS;",
                                     database="ec;",
                                     trusted_connection="yes;",
                                     uid="HOME-GIS\\sde;pwd=sde;")
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
    con = sql_server_connect(driver=r"{SQL Server Native Client 11.0};",
                                     server="HOME-GIS\SQLEXPRESS;",
                                     database="ec;",
                                     trusted_connection="yes;",
                                     uid="HOME-GIS\\sde;pwd=sde;")
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
