#!/usr/bin/python
import MySQLdb
import json

def create_table(cursor):
	foodTableSql = """CREATE TABLE FOOD (
			ID INT NOT NULL AUTO_INCREMENT,
			NAME  CHAR(40),
			LOCATION  CHAR(40),
			COUNTRY CHAR(30),  
			REVIEW DECIMAL(19,4),
			LIKES INT,
			CAPTION TEXT,
			UPLOAD_TIME DATETIME,
			primary key (ID))"""
	
	cursor.execute(foodTableSql)

	mediaTableSql = """CREATE TABLE MEDIA (
						ID INT,
						MEDIA_URL TEXT
					)"""
	
	cursor.execute(mediaTableSql)

	commentTableSql = """CREATE TABLE COMMENTS (
						ID INT,
						COMMENT TEXT
					)"""

	cursor.execute(commentTableSql)

def add_data(name, location, country, comments, review, likes, caption, uploadTime, medium):
	sql = 'INSERT INTO FOOD ( \
				NAME, LOCATION, COUNTRY, REVIEW, LIKES, CAPTION, UPLOAD_TIME) \
			VALUES ("%s", "%s", "%s", "%s", "%d", "%s", "%s" )' % \
					(name, location, country, "{:.9f}".format(review) , likes, caption, uploadTime)


	try:
		cursor.execute(sql)

		cursor.execute("SELECT LAST_INSERT_ID()")
		lastID = cursor.fetchone()[0]

		for comment in comments:
			sql = 'INSERT INTO COMMENTS ( \
						ID, COMMENT) \
					VALUES ("%d", "%s")' % \
						(lastID, comment)
			cursor.execute(sql)

		for media in medium:
			print media
			sql = "INSERT INTO MEDIA ( \
						ID, MEDIA_URL) \
					VALUES ('%d', '%s')" % \
						(lastID, media)
			cursor.execute(sql)

			db.commit()
	except:
		db.rollback()

# Open database connection
db = MySQLdb.connect("localhost","root","","food_recommendation", charset='utf8')

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Create Table for first time usage
# create_table(cursor)

# add data to database
with open("final.json") as data_file:    
    data = json.load(data_file)

for post in data:
	add_data(post["location"], post["location"], "australia", post["comments"], post["rating"], post["likesCount"], post["caption"], post["time"], post["media"])

# disconnect from server
db.close()