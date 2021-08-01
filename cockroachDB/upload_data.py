
from cockroachDB.db_helper import get_data, conn
import psycopg2
from cockroach import cockroachDB

tags, number, cat = get_data()



c = cockroachDB(conn= conn)
c.create_table()
c.add_values( 
    [tags, number, cat]
)