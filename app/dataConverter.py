import json
import datetime
import codecs
import os
from instagram_scraper.app import InstagramScraper
from instagram_scraper.constants import *
from pprint import pprint

posts =[]
usernames=[]

def notNone(var, notNullValue, defaultValue):
    if var is None:
        return defaultValue
    else:
        return var[notNullValue]

def scraper(list_username):
	dir_path = os.path.dirname(os.path.realpath(__file__))

	args = {
	    'usernames': list_username,
	    'destination': dir_path,
	    'login_user': None,
	    'login_pass': None,
	    'quiet': True,
	    'comments': True,
	    'maximum': 0,
	    'retain_username': False,
	    'media_metadata': True,
	    'media_types': ['image', 'video', 'story'],
	    'latest': False
	}

	scraper = InstagramScraper(**args)
	scraper.scrape()

def convertFormat(username):
	filename = username + ".json"
	with open(filename, encoding="UTF-8") as data_file:    
	    data = json.load(data_file)

	for post in data:
		convertedPost ={}
		convertedPost['caption'] = notNone(post["caption"], "text", "")
		convertedPost['location'] = notNone(post["location"], "name", "")
		convertedPost['media'] = post["urls"]
		convertedPost['time'] = datetime.datetime.fromtimestamp(int(post["created_time"])).strftime('%Y-%m-%d %H:%M:%S')
		convertedPost['likesCount'] = post["likes"]["count"]

		comments=[]
		if post["comments"]["count"] > 0:
			for comment in post["comments"]["data"]:
				comments.append(comment['text'])
		convertedPost['comments'] = comments

		posts.append(convertedPost)
	
""" MAIN PROGRAM """

with open('listUsername.txt', encoding="UTF-8") as lines:    
	    for line in lines:
	    	usernames.append(line.rstrip())

print(usernames)

scraper(usernames)
for username in usernames:
	convertFormat(username)

with open("convertedData.json", 'wb') as f:
	json.dump(posts, codecs.getwriter('utf-8')(f), indent=4, sort_keys=True, ensure_ascii=False)

# json.dumps(posts)

# f = open('converted.json', 'w')
# f.write(posts)
# f.close()
