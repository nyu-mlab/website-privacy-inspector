import requests
import time
import pandas as pd
import multiprocessing

#function to call the API created in main.py
def post_request(data):
    server_url = "http://127.0.0.1:8000/privacy/"
    x = requests.post(server_url, headers = {"accept": "application/json","Content-Type":"application/json"},json = data)

if __name__ == '__main__':
    df = pd.read_csv("data.csv")
    df = df.reset_index(drop=True)
    url_list = df['url']
    
    no_of_urls = len(url_list)
    no_of_cores_used = 8 
    
    data_list = []
    start_index = 0
    
    """
    below we create a list of dictionaries in whihc each dictionary is of the form {"urls" :[<list of urls>] }
    and acts as an argument for the FAST API in main.py
    """
    for i in range(0, no_of_urls, (no_of_urls//no_of_cores_used)):
        if i== 0:
            continue
        data_part = {"urls": url_list[start_index: i].values.tolist()}
        data_list.append(data_part)
        start_index = i
        if start_index < no_of_urls:
            data_list[-1]["urls"] += url_list[start_index :].values.tolist()

    start_time = time.time()
    
    #we use the Pool class to initiate multiple processes for multiprocessing
    with multiprocessing.Pool() as p:
        p.map(post_request, data_list)
    end_time = time.time()
    time_diff = end_time - start_time
    print("Time taken by execution is", time_diff)
