"""
Creates empty database

References
    https://docs.python.org/3.6/library/sqlite3.html
    https://www.sqlite.org/
"""

import sqlite3
import os.path

sqlite_file = '../../data/databases/min_booking_database.db'

if os.path.isfile(sqlite_file):
    raise IOError('Database file "' + sqlite_file + '" already exists. Database should be created in a new file.')

conn = sqlite3.connect(sqlite_file)

with conn: # conn.commit() is called if next statements execute successfully

    conn.executescript("""
        CREATE TABLE bookings (
            booking_id          INTEGER PRIMARY KEY NOT NULL,
            booking_id_string   TEXT NOT NULL,
            county_name         TEXT NOT NULL,
            booking_timestamp   TEXT NOT NULL,
            release_timestamp   TEXT,
			on_roster			INTEGER,
            known_misdemeanor   INTEGER NOT NULL
        );
    """)

conn.close()

print('Done initializing database stored in "' + sqlite_file + '"')

