import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(dbname='financial', user='admin', host='192.168.0.147', password='2206')
        print("Connection established")

    except Exception as e:
        print("Could not connect to db: " + str(e))
        raise SystemExit(1)
    
    return conn

def insert_file(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("COPY exmployees(first_name, last_name, dob) FROM 'Enter file path here' DELIMITER ',' CSV HEADER;")

    except Exception as e:
        print("Could not insert file: " + str(e))

def main():
    conn = connect_to_db()
    insert_file(conn)
