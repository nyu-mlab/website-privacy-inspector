import subprocess
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import base64
class Urls(BaseModel):
    urls : List[str]

app = FastAPI()

@app.post("/privacy/")
async def create_item(url_list: Urls):
    urls_dict = url_list.dict()
    #subprocess.run(["node","example.js",website])
    encoded_url = []
    for url in url_list.urls:
        encoded_url.append(base64.b64encode(url.encode("ascii")).decode("ascii"))
    encoded_url_str = ",".join(encoded_url)
    subprocess.run(["node","example.js",encoded_url_str])
    return encoded_url