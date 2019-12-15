import display
from twython import Twython
import json


def main():
	display.move_cursor(0,49)
	nadine()

def nadine():
	# T1h0S6XQCCoQxLFdNQDuW0unI (API Key)
	# 1qfhBFHZH7NCuQxnIzWvVK83wB0RaxRz68bRnYgcyIOZMpNj5j (API secret Key)

	#893087546-YncCVCH8ago2lJk5s3ZZRqUrvBr0bGwcnzagYvdE (Access token)
	#zedKZSJ6jka0nEN4MWcVX1Ogoo8TBNVWDMlgvFHzayhB8 (Access token secret)
	#Read and write (Access level)


	# Enter your keys/secrets as strings in the following fields
	credentials = {}
	credentials['CONSUMER_KEY'] = "T1h0S6XQCCoQxLFdNQDuW0unI"
	credentials['CONSUMER_SECRET'] = "1qfhBFHZH7NCuQxnIzWvVK83wB0RaxRz68bRnYgcyIOZMpNj5j"
	credentials['ACCESS_TOKEN'] = "893087546-YncCVCH8ago2lJk5s3ZZRqUrvBr0bGwcnzagYvdE"
	credentials['ACCESS_SECRET'] = "zedKZSJ6jka0nEN4MWcVX1Ogoo8TBNVWDMlgvFHzayhB8"

	# Save the credentials object to file
	with open("twitter_credentials.json", "w") as file:
	    json.dump(credentials, file)



	n = 0
	n = display.print_49(n, "="*10 + "[" + "nadine".center(10) +"]" + "="*9)

	n = display.print_49(n, "in dev")
