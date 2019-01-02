import markovify
import json
import time
from mastodon import Mastodon

api_base_url = "https://beeping.town"

client = Mastodon(
        client_id="clientcred.secret", 
        access_token="usercred.secret", 
        api_base_url=api_base_url)

with open("corpus.txt") as fp:
    model = markovify.NewlineText(fp.read())

print("posting")
sentence = None
# you will make that damn sentence
while sentence is None:
    sentence = model.make_sentence(tries=100000)
client.status_post(sentence.replace("\0", "\n"),visibility="unlisted")
