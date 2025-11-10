import pandas as pd
import requests
import json
import time


#python script to extract random spotify songs by searching for list of keywords



tracks = 'asdf'

for track in tracks:

    spotify_id = '4pRms8DFBAvUrdxZxnh7xL' #get tracks by spotify id
    url = f'https://api.reccobeats.com/v1/track?ids={spotify_id}'
    main_features = json.loads(requests.get(url).text)
    reccobeats_id = main_features['id'] #get audio features by reccobeats id
    audio_features = f'https://api.reccobeats.com/v1/track/{reccobeats_id}/audio-features'


    time.sleep(0.01)
