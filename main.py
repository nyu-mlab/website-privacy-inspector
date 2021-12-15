import subprocess
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import base64
import os
import json
from datetime import datetime
import hashlib
class Urls(BaseModel):
    urls : List[str]

app = FastAPI()

@app.post("/privacy/")
async def create_item(url_list: Urls):
    log = ""
    log = log + str(datetime.now()) + "  Website Privacy Inspection requested for below sites :" + "\n"
    log = log +"  " +  str(url_list.urls) + "\n"

    encoded_url_list = []
    encoded_url_uncached = []
    url_hash_list = []
    url_hash_list_uncached = []
    
    log = log + str(datetime.now()) + "  URL encoding started" + "\n"

    for url in url_list.urls:
        #hashing url for caching
        url_hash = hashlib.sha256(url.encode('utf-8')).hexdigest()
        url_hash_list.append(url_hash)
        log = log + str(datetime.now()) + "  "+ url + "  hashed to  " + url_hash +"\n" 
        
        #encoding url
        url_64 = base64.urlsafe_b64encode(url.encode("ascii")).decode("ascii")
        encoded_url_list.append(url_64)
        
        log = log + str(datetime.now()) + "  "+ url + "  converted to  " + url_64 +"\n"  
        path = url_hash
        
        if not (os.path.isdir(path)):
            log = log + str(datetime.now()) + " " + url + "is not cached \n"
            encoded_url_uncached.append(url_64)
            url_hash_list_uncached.append(url_hash)

        else:
            log = log + str(datetime.now()) + "  " + url+ "  is cached \n"  

    encoded_url_str = ",".join(encoded_url_uncached)
    url_hash_str = ",".join(url_hash_list_uncached)

    # Below all uncached urls are sent to blacklight.js
    if not (encoded_url_uncached == []):
        log = log + str(datetime.now()) + " Uncached URLs sent to blacklight for inspection \n " 
        subprocess.run(["node", "blacklight.js", encoded_url_str, log, url_hash_str])
        log = ""
    
    current_path = os.getcwd()
    result_json = {}
    
    i = 0
    log = log + str(datetime.now()) + "  Integrating results to create a json response \n"
    
    #The results of blacklight are stored in a file inspection.json in the hashed folder for each url. Below we search for all the urls' results in order to integrate them as a json  
    for url_hash in url_hash_list:
        path = url_hash
        search_path = current_path + "/"+path

        try:
            os.chdir(search_path)

        except FileNotFoundError:
            log = log + str(datetime.now()) + " path not found \n"
            log = log+ " " +search_path + "\n"

        if os.path.exists('./inspection.json'):
            log = log + str(datetime.now()) + " Results for " + path + " found \n" 
            f = open('inspection.json')
            data = json.load(f)
            f.close()

        else:
            log = log + str(datetime.now()) + " Results for " + path + " not found \n"
            data = {'Results not found'}
        result_json[url_list.urls[i]] = data
        i = i + 1

    os.chdir(current_path)
    if not (encoded_url_uncached == []):
        logfile = open("logfile.txt", "a")
        logfile.write(log)
    else:
        logfile = open("logfile.txt", "w")
        logfile.write(log)
    logfile.close()
    return result_json
