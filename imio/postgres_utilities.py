#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# postgresql utility methods
# IMIO <support@imio.be>
#

import psycopg2
from system_utilities import error, trace

#------------------------------------------------------------------------------


#dsn="host=localhost port=5432 dbname= user= password="
def openConnection(dsn):
    """ open a postgres connection """
    conn = None
    try:
        conn = psycopg2.connect(dsn)
    except Exception, message:
        msg = "Cannot connect to database with dsn '%s': %s" % (dsn, message)
        error(msg)
        raise Exception(msg)
    return conn

#------------------------------------------------------------------------------


def insertInTable(conn, table, columns, vals, TRACE=False):
    """ insert values in a table """
    cursor = conn.cursor()
    req = "insert into %s(%s) values(%s)" % (table, columns, vals)
    trace(TRACE, "Insertion: %s" % req)
    try:
        cursor.execute(req)
        cursor.close()
    except Exception, message:
        conn.rollback()
        error("Cannot insert in database : %s" % message)
        error("Request was : '%s'" % req)
        return False
    conn.commit()
    return True

#------------------------------------------------------------------------------


def updateTable(conn, table, updates, condition='', TRACE=False):
    """ update columns in a table """
    cursor = conn.cursor()
    req = "update %s set %s" % (table, updates)
    if condition:
        req += ' where %s' % condition
    trace(TRACE, "Update: %s" % req)
    try:
        cursor.execute(req)
        cursor.close()
    except Exception, message:
        conn.rollback()
        error("Cannot update in database : %s" % message)
        error("Request was : '%s'" % req)
        return False
    conn.commit()
    return True

#------------------------------------------------------------------------------


def selectWithSQLRequest(conn, sql, TRACE=False):
    """ select multiple lines in a table with a complete sql """
    cursor = conn.cursor()
    req = sql
    trace(TRACE, "Selection: %s" % req)
    try:
        cursor.execute(req)
        data = cursor.fetchall()
        cursor.close()
    except Exception, message:
        error("Cannot select from database : %s" % message)
        error("Request was : '%s'" % req)
        return None
    return data

#------------------------------------------------------------------------------


def selectAllInTable(conn, table, selection, condition='', TRACE=False):
    """ select multiple lines in a table """
    cursor = conn.cursor()
    req = "select %s from %s" % (selection, table)
    if condition:
        req += ' where %s' % condition
    trace(TRACE, "Selection: %s" % req)
    try:
        cursor.execute(req)
        data = cursor.fetchall()
        cursor.close()
    except Exception, message:
        error("Cannot select from database : %s" % message)
        error("Request was : '%s'" % req)
        return None
    return data

#------------------------------------------------------------------------------


def selectOneInTable(conn, table, selection, condition='', TRACE=False):
    """ select a single line in a table """
    cursor = conn.cursor()
    req = "select %s from %s" % (selection, table)
    if condition:
        req += ' where %s' % condition
    trace(TRACE, "Selection: %s" % req)
    try:
        cursor.execute(req)
        data = cursor.fetchone()
        cursor.close()
    except Exception, message:
        error("Cannot select from database : %s" % message)
        error("Request was : '%s'" % req)
        return None
    return data

#------------------------------------------------------------------------------


def deleteTable(conn, table, condition='', TRACE=False):
    """ delete a table """
    cursor = conn.cursor()
    req = "delete from %s" % (table)
    if condition:
        req += ' where %s' % condition
    trace("Deletion : %s" % req)
    try:
        cursor.execute(req)
        cursor.close()
    except Exception, message:
        conn.rollback()
        error("Cannot delete from database : %s" % message)
        error("Request was : '%s'" % req)
        return False
    conn.commit()
    return True

#------------------------------------------------------------------------------
