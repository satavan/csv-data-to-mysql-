import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
user='root',
passwd='singh',
db='indianpostal')

cursor = mydb.cursor()

csv_data = csv.reader(file('all_india_pin_code.csv'))

for row in csv_data:

    cursor.execute('INSERT INTO `postal` VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',row)
#close the connection to the database.
mydb.commit()
cursor.close()
import os


print "Done"
