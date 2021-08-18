import subprocess
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import base64
import os
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
    return encoded_url
