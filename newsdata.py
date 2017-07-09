#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def run_query(query):
    """Connect into the database and execute the query"""
    try:
        db = psycopg2.connect(database=DBNAME)
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()
        return result
    except:
        print("Error: Not possible to connect into database")


def question1():
    """Print the three most popular articles"""

    query = ("SELECT articles.title, COUNT(*) AS view_count FROM log "
             "INNER JOIN articles ON ('/article/'||articles.slug)=log.path "
             "WHERE log.status = '200 OK' GROUP BY articles.title "
             "ORDER BY view_count DESC LIMIT 3;")

    results = run_query(query)
    print("What are the most popular three articles of all time?")
    for result in results:
        print("\b", result[0], " - ", str(result[1]), "views")


def question2():
    """Print the most popular article authors (in order)"""

    query = ("SELECT authors.name, COUNT(*) AS view_count FROM log "
             "INNER JOIN articles ON ('/article/'||articles.slug)=log.path "
             "INNER JOIN authors ON authors.id = articles.author "
             "WHERE log.status = '200 OK' GROUP BY authors.name "
             "ORDER BY view_count DESC;")

    results = run_query(query)
    print("\nWho are the most popular article authors of all time?")
    for result in results:
        print("\b", result[0], " - ", str(result[1]), "views")


def question3():
    """Print the days that had more than 1% requests that lead to error"""

    query = ("SELECT date, CAST(((100.0*errors)/total) AS NUMERIC(16,2)) "
             "AS perc_error FROM (SELECT time::date AS date, COUNT(*) "
             "AS total, COUNT(CASE WHEN status = '404 NOT FOUND' THEN 1 END) "
             "AS errors FROM log GROUP BY date) request_log WHERE "
             "CAST(((100.0*errors)/total) AS FLOAT) > 1 "
             "GROUP BY request_log.date,request_log.errors,request_log.total "
             "ORDER BY perc_error DESC;")

    results = run_query(query)
    print("\nOn which days did more than 1% of requests lead to errors?")
    if (len(results) > 0):
        for result in results:
            print("\b", result[0], " - ", str(result[1]), "% errors")
    else:
        print("\bNone days")


question1()
question2()
question3()
