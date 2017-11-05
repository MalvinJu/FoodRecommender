# Food Recommender

This will recommend food from food blogger's Instagram feed. 

## Data
The data was carwal from Instagram using Instagram-Scraper and then formatted according to our recommender system.

First, install instagram-scrapper:
```bash
$ pip install instagram-scraper
```

Then, write list of food blogger's username in **listUsername.txt** with this format:
```
username1
username2
username3
.
.
.
```

Finally, run dataConverted.py to convert and get only the useful data:
```bash
$ python dataConverted.py
```