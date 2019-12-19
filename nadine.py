import display
from twython import Twython
import json
import requests


def main():
	display.move_cursor(0,49)

	nadine()

def getText(data):
	try: text = data['retweeted_status']['extended_tweet']['full_text']
	except:
		try: text = data['retweeted_status']['full_text']
		except:
			try: text = data['extended_tweet']['full_text']
			except:
				try: text = data['full_text']
				except:
					try: text = data['retweeted_status']['text']
					except:
						try: text = data['text']
						except:
							text = ''
	return text

def nadine():
	username = "RERC_SNCF"
	nb_tweet = 5
	include_rt = True

	n = 0
	n = display.print_49(n, "="*5 + "[" + ("@" + username).center(20) +"]" + "="*4)

	# Enter your keys/secrets as strings in the following fields
	credentials = {}
	credentials['CONSUMER_KEY'] = "T1h0S6XQCCoQxLFdNQDuW0unI"
	credentials['CONSUMER_SECRET'] = "1qfhBFHZH7NCuQxnIzWvVK83wB0RaxRz68bRnYgcyIOZMpNj5j"
	credentials['ACCESS_TOKEN'] = "893087546-YncCVCH8ago2lJk5s3ZZRqUrvBr0bGwcnzagYvdE"
	credentials['ACCESS_SECRET'] = "zedKZSJ6jka0nEN4MWcVX1Ogoo8TBNVWDMlgvFHzayhB8"

	# Save the credentials object to file
	with open("twitter_credentials.json", "w") as file:
	    json.dump(credentials, file)

	twitter = Twython(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])


	res = twitter.get_user_timeline(screen_name = username, count = nb_tweet, exclude_replies=True, tweet_mode="extended", include_rts = include_rt)

	for t in res:
		n = display.breakline_49(n, 30, display.remove_link(getText(t)))
		n = display.print_49(n, '-'*30)
