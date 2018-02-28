import praw
import re
import os

reddit = praw.Reddit('Splunge Bot v1', client_id=os.environ['REDDIT_CLIENT_ID'], client_secret=os.environ['REDDIT_CLIENT_SECRET'], password=os.environ['REDDIT_PASSWORD'], username=os.environ['REDDIT_USERNAME'])
subreddit = reddit.subreddit('tubasaur')
for submission in subreddit.new(limit=5):
	for top_level_comment in submission.comments:
		if re.search('splunge', top_level_comment.body, re.IGNORECASE):
			top_level_comment.reply("Well, yeah, splunge for me too!")
			print("Splunged.")

