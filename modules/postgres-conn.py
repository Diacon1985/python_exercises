import psycopg2

conn = None
try:
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host='localhost',
        dbname='deliveries',
        user='postgres',
        password='root',
        port=5432
    )

    # Creating a cursor with name cur.
    cur = conn.cursor()
    print('Connected to the PostgreSQL database')

    # Execute a query:
    # To display the PostgreSQL
    # database server version
    cur.execute('SELECT * FROM activities')
    rows = cur.fetchall()
    print('delivery_id',' emp_id','activity_id','start_time',' end_time',' t_time')
    for row in rows:
        print('\t',row[0],'\t\t|',' ',row[1],  '|','\t',row[2],'\t   |',row[3],'|',row[4],'|',row[5],)
        print('-'*63)

#another aproach to show the results
    columns = [desc[0] for desc in cur.description]

    print("-"*60)
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}" .format(*columns))
    print("-" * 60)

    for row in rows:
        print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*[str(value) for value in row]))

    print("-" * 60)


    # Close the connection
    cur.close()

except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')