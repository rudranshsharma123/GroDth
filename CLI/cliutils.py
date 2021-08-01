## CLI UTILS AHEAD ----->>>>>>>


import os
import sys
import requests
from time import sleep
# from untils.utils import datafile
datafile = '/mnt/d/My projects/selfiehacks/jina/data/smol.csv'

def clear_everything():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer_anim(textBlob):
    for char in textBlob:
        print(char, end="", flush=True)
        sleep(0.02)

def get_categories(category):
    import pandas as pd
    df = pd.read_csv(datafile)
    return list(df[df['category'] == category]['hash'])

def get_tags(text):
    headers = {
        'Content-Type': 'application/json',
    }

    data = '{"top_k":1,"mode":"search","data":["' + text + '"]}'

    response = requests.post(
        'http://0.0.0.0:12345/search', headers=headers, data=data)

    res = response.json()
    data_list = res["data"]['docs']
    tags = []
    number = []
    for i in data_list:
        if i['tags']['hash'] not in tags:
            tags.append(i['tags']['hash'])
            number.append(i['tags']['number'])
   
    type_writer_anim("""Found these tags! These should be very similar to the text you \nhave entered to search for. The format is #Hastags: Number Of Posts 
    """)
    print('\n')

    for i, v in enumerate(tags):
        print(v +":"+number[i])
    
    print('\n')
    