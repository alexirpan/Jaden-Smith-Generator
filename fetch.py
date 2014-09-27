import requests
import base64
APP_KEY='cZObNB56DaNJpNHNiMPFzfCjI'
APP_SECRET='EjnsuMLQ1fKP6WVlb6KGPxnvoRKMsc6UkHjfi7ubbXGrRUl9Nd'

headers = {'Authorization': 'Basic ' + base64.b64encode('%s:%s' % (APP_KEY, APP_SECRET)),
           'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
           
token_response = requests.post(
    'https://api.twitter.com/oauth2/token',
    data='grant_type=client_credentials',
    headers=headers
)

access_token = token_response.json()['access_token']
url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?count=200&trim_user=true&exclude_replies=true&include_rts=false&user_id=262794965&screen_name=officialjaden'

tweets = requests.get(
    url,
    headers={'Authorization': 'Bearer %s' % access_token},
)
