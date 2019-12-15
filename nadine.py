import display
from twython import Twython
import json


def main():
	display.move_cursor(0,49)

	nadine()

def nadine():
	username = "nadine__morano"

	n = 0
	n = display.print_49(n, "="*5 + "[" + ("@" + username).center(20) +"]" + "="*4)
	n = display.print_49(n, "in dev")

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


	tweets = twitter.get_user_timeline(screen_name = username, count = 1, include_rts = False)

	for t in tweets:
		n = display.breakline_49(n, 30, t['text'])
		n = display.print_49(n, '='*30)




main()
