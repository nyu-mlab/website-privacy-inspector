import subprocess
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import base64
import os
import json
from datetime import datetime
class Urls(BaseModel):
    urls : List[str]

app = FastAPI()

@app.post("/privacy/")
async def create_item(url_list: Urls):
    log = ""
    log = log + str(datetime.now()) + "  Website Privacy Inspection requested for below sites :" + "\n"
    log = log +"  " +  str(url_list.urls) + "\n"


    encoded_url = []
    encoded_url_uncached = []

    log = log + str(datetime.now()) + "  URL encoding started" + "\n"

    for url in url_list.urls:

        url_64 = base64.b64encode(url.encode("ascii")).decode("ascii")
        encoded_url.append(url_64)
        log = log + str(datetime.now()) + "  "+ url + "  converted to  " + url_64 +"\n"
        if not (os.path.isdir(url_64)):
            #print("inside if")
            log = log + str(datetime.now()) + " " + url + "is not cached \n"
            encoded_url_uncached.append(url_64)

        else:
            log = log + str(datetime.now()) + "  " + url+ "  is cached \n"

    encoded_url_str = ",".join(encoded_url_uncached)

    if not (encoded_url_uncached == []):
        log = log + str(datetime.now()) + " Uncached URLs sent to blacklight for inspection \n "
        subprocess.run(["node", "example.js", encoded_url_str, log])
        log = ""

    current_path = os.getcwd()
    result_json = {}
     i = 0
    log = log + str(datetime.now()) + "  Integrating results to create a json response \n"
    for url_64 in encoded_url:

        search_path = current_path + "/"+url_64
        try:
            os.chdir(search_path)
        except FileNotFoundError:
            log = log + str(datetime.now()) + " path not found \n"

        if os.path.exists('./inspection.json'):
            log = log + str(datetime.now()) + " Results for " + url_64 + " found \n"
            f = open('inspection.json')
            data = json.load(f)
            f.close()

        else:
            log = log + str(datetime.now()) + " Results for " + url_64+ " not found \n"
            data = {'Results not found'}
        result_json[url_list.urls[i]] = data
        i = i+1

    os.chdir(current_path)
    if not (encoded_url_uncached == []):
        logfile = open("logfile.txt", "a")
        logfile.write(log)
    else:
        logfile = open("logfile.txt", "w")
        logfile.write(log)
    logfile.close()
    return result_json
