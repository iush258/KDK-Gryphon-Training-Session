import psycopg2

con = psycopg2.connect(
    host = "Localhost",
    port="5432",
    database="postgres",
    user="ayush",
    password="dmonlol@4429"
    )

cur=con.cursor()

