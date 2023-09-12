import psycopg2

try:
    con = psycopg2.connect(dbname='financial', user='admin', host='192.168.0.147', password='2206')

except Exception as e:
    print("Error: " + str(e))