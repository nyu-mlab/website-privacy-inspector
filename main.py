import subprocess
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import base64
import os
import json
class Urls(BaseModel):
    urls : List[str]

app = FastAPI()

@app.post("/privacy/")
async def create_item(url_list: Urls):
    urls_dict = url_list.dict()
    #subprocess.run(["node","example.js",website])
    encoded_url = []
    encoded_url_uncached = []
    for url in url_list.urls:
        url_64 = base64.b64encode(url.encode("ascii")).decode("ascii")
        encoded_url.append(url_64)
        if not (os.path.isdir(url_64)):
            print("inside if")
            encoded_url_uncached.append(url_64)
    encoded_url_str = ",".join(encoded_url_uncached)
    if not (encoded_url_uncached == []):
        subprocess.run(["node","example.js",encoded_url_str])
    current_path = os.getcwd()
    result_json = {}
    i = 0
    for url_64 in encoded_url:
        search_path = current_path + "/"+url_64
        os.chdir(search_path)
        f = open('inspection.json')
        data = json.load(f)
        result_json[url_list.urls[i]] = data
        f.close()
        i = i+1
    os.chdir(current_path)
    return result_json
