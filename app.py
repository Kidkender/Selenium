import twitterbot as tb
import credential
import sys

# hashtag = sys.argv[1]

credentials = credential.get_credentials()

bot = tb.TwitterBot(credentials["email"], credentials["password"])
bot.logout()
bot.login()
print("Login successful")
bot.post_tweet(image_path="")