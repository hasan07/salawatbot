#!/usr/bin/python

import praw
import time

SALAWAT_TEXT = '[Salawat](%s) ^(I am a bot. I replied because you mentioned the prophet pbuh.)' %'http://i.imgur.com/TyQPbKQ.jpg'

MATCH_STRINGS = [
	'prophet muhammad',
	'prophet muhammed', 
	'prophet mohammad', 
	'imam ali', 
	'the prophet',
	'Holy Prophet']

def write_to_cache(id):
	file = open('./cached_comment_ids', 'a')
	print 'Writing %s to cache' % id
	file.write('%s\n' % id)
	file.close()

def get_cached_ids():
	cache_file = open('./cached_comment_ids', 'r')
	print 'Creating a list of cached IDs'
	cached_ids_list = [id[:-1] for id in cache_file.readlines()]
	cache_file.close()

	return cached_ids_list

def run_bot(r, cached_ids_list):
    print 'Grabbing subreddit...'
    subreddit = r.get_subreddit('islam')
    print 'Fetching comments...'
    comments = subreddit.get_comments(limit=100)

    for comment in comments:
    	if comment.id not in cached_ids_list:
    		comment_text = comment.body.lower()
    		isMatch = any(string in comment_text for string in MATCH_STRINGS)
    		if isMatch:
    			print 'Comment found!'
    			print 'Replying...'
    			comment.reply(SALAWAT_TEXT)
    			write_to_cache(comment.id)

def main():
	
	print 'Initiating Reddit...'
	r = praw.Reddit(user_agent = "First b0t")
	print 'Logging in...'
	r.login()

	while True:
		run_bot(r, get_cached_ids())
		time.sleep(1000)

if __name__ == '__main__':
  main()
