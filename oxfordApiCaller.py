# Sjekke her for mer info om requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json

# Her er API KEY og ID til Oxford kontoen
app_id = 'd97eda3a'
app_key = '95676303f37bf84a4313bb7628d69bd1'


language = 'en'
# Ordet som skal sjekkes er i word_id
word_id = 'running'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))