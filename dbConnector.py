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
        #read the file with the data to insert into the table
        with open('/home/mperez/Documents/Tasks/HoneyOrg/employees.csv', 'r') as f:
            next(f)
            for line in f:
                print(line.rstrip('\n').split(','))
                #split the line into seperate data elements 
                values = line.rstrip('\n').split(',')
                #Insert the elements into the db table
                cursor.execute("INSERT INTO employees (emp_id, first_name, last_name, dob) VALUES (%s, %s, %s, %s)", (values[0], values[1], values[2], values[3]))
            conn.commit()

    except Exception as e:
        print("Could not insert file: " + str(e))

    #Print the data from the table to ensure the change was successful
    cursor.execute("SELECT * FROM employees;")
    all_data = cursor.fetchall()
    for line in all_data:
        print(line)

def retreive_file(conn):
    '''Retreive all data from the employees table and wrtie to a CSV'''
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
    #insert_file(conn)
    retreive_file(conn)
if __name__ == '__main__':
    main()
