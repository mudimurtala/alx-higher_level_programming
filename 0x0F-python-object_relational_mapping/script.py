"""This script is for practicing how to use MySQLdb"""
import MySQLdb
db = MySQLdb.connect(host="localhost", user="user", passwd="ComplexPassword123!", db="friday_19th_db")
cursor = db.cursor()
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)
db.close()
