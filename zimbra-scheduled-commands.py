#!/usr/bin/python

import subprocess
import MySQLdb

DB_NAME = 'db_name'
DB_HOST = 'db_host'
DB_USER = 'db_user'
DB_PASSWORD = 'db_password'

conn = MySQLdb.Connection(db=DB_NAME, host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD)

cursor = conn.cursor()
sql = """select command from queue_commands where status=0"""
cursor.execute(sql)

for row in cursor:
        subprocess.call(["su", "-", "zimbra", "-c", row[0]])

cursor.close()
conn.close()
