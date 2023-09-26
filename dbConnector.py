import psycopg2
import csv

def connect_to_db():
    '''Establish initial DB connection'''
    try:
        conn = psycopg2.connect(dbname='financial', user='admin', host='192.168.0.147', password='2206')
        print("Connection established")

    except Exception as e:
        print("Could not connect to db: " + str(e))
        raise SystemExit(1)
    
    return conn

def insert_file(conn):
    '''Insert a local file into the DB'''
    try:
        cursor = conn.cursor()
        with open('/home/mperez/Documents/Tasks/HoneyOrg/testfile.csv', 'r') as f:
            next(f)
            for line in f:
                print(line.rstrip('\n'))
            cursor.copy_from(f, 'employees', sep=',')
        #cursor.execute("COPY employees(first_name, last_name, dob) FROM 'Enter file path here' DELIMITER ',' CSV HEADER;")
        conn.commit()

    except Exception as e:
        print("Could not insert file: " + str(e))

def retreive_file(conn):
    '''Retreive all data from teh employees table and wrtie to a CSV'''
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees;")
        all_data = cursor.fetchall()
        f = open('testfile.csv', 'w')
        writer = csv.writer(f, delimiter=',')
        writer.writerow(["Employee ID", "First Name", "Last Name", "Date of Birth"])
        for data in all_data:
            print(data)
            #with open('testfile.csv', 'a') as f:
               #writer = csv.writer(f, delimiter=',')
            writer.writerow(data)

    except Exception as e:
        print("Error retreiving file: " + str(e))

def main():
    conn = connect_to_db()
    insert_file(conn)
    #retreive_file(conn)
if __name__ == '__main__':
    main()
