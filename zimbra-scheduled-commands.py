#!/usr/bin/python
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
  
import subprocess
import MySQLdb as mdb
from dbConfig import *

conn = mdb.Connection(db=DB_NAME, host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD)

# Fetch the queued commands in DB
cursor = conn.cursor()
updateCur = conn.cursor()
sql = "SELECT id, command FROM queue_commands WHERE status = 0"
cursor.execute(sql)

if int(cursor.rowcount) == 0:
	print "No queued commands to run."

# Run each queued command
for row in cursor:
	returncode = subprocess.call(["su", "-", ZIMBRA_USER, "-c", row[1]])

	# If command run successful then update the command status in queued_commands table.
	if returncode == 0:
		updateCur.execute("UPDATE queue_commands SET status = %s WHERE id = %s",("1", row[0]))

cursor.close()
updateCur.close()
conn.close()
