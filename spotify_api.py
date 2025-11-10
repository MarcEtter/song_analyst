import pandas as pd
import requests
import json
import time
import os
from dotenv import load_dotenv

#python script to extract random spotify songs by searching for list of keywords

load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

#obtain spotify api access token
url = "https://accounts.spotify.com/api/token"
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
response = requests.post(url, data=data, headers=headers)
access_token = json.loads(response.text)['access_token']

with open('google-10000-english.txt', 'r') as file:
    content = file.read()   
words = content.split('\n')

track_ids = list()
for word in words:
    url = f'https://api.spotify.com/v1/search?q={word}&type=track'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url = url, headers = headers)
    tracks = json.loads(response.text)['tracks']
    ids = [x['id'] for x in tracks['items']]
    track_ids.append(ids)
    print(f'Appending {len(ids)} ids: {ids[1:3]} ...')

for track_id in track_ids:
    spotify_id = track_id
    #spotify_id = '4pRms8DFBAvUrdxZxnh7xL' #get tracks by spotify id
    url = f'https://api.reccobeats.com/v1/track?ids={spotify_id}'
    main_features = json.loads(requests.get(url).text)
    reccobeats_id = main_features['id'] #get audio features by reccobeats id
    audio_features = f'https://api.reccobeats.com/v1/track/{reccobeats_id}/audio-features'

    time.sleep(0.01)
