#!/usr/bin/python

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
import MySQLdb

# Database connection parameters
DB_NAME = 'db_name'
DB_HOST = 'db_host'
DB_USER = 'db_user'
DB_PASSWORD = 'db_password'

conn = MySQLdb.Connection(db=DB_NAME, host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD)

# Fetch the queued commands in DB
cursor = conn.cursor()
sql = """select command from queue_commands where status=0"""
cursor.execute(sql)

# Run each command
for row in cursor:
        subprocess.call(["su", "-", "zimbra", "-c", row[0]])
	# Status should be updated to '1' after the scheduled command runs successfully

cursor.close()
conn.close()
