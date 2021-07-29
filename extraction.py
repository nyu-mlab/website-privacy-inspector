# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:40:03 2021

@author: shekh

The below code extracts all the useful information from inspection.json file emitted from blacklight

"""

import json
import pandas as pd


def third_party_hosts(data):
    third_party_hosts_list = data["hosts"]["requests"]["third_party"]
    print(len(third_party_hosts_list))
    
def listener_extraction(data):
    df_listeners = pd.DataFrame()
    df_mouse = pd.DataFrame()
    df_touch = pd.DataFrame()
    df_sensor = pd.DataFrame()

    listeners_list = data["reports"]["behaviour_event_listeners"].keys()
    
    df_listeners["listener"]= data["reports"]["behaviour_event_listeners"]["KEYBOARD"].keys()
    df_listeners["device"] = "Keyboard"
    df_listeners["details"] = data["reports"]["behaviour_event_listeners"]["KEYBOARD"].values()


    df_mouse["listener"] = data["reports"]["behaviour_event_listeners"]["MOUSE"].keys()
    df_mouse["device"] = "Mouse"
    df_mouse["details"] = data["reports"]["behaviour_event_listeners"]["MOUSE"].values()
    df_listeners = df_listeners.append(df_mouse)
    
    if "TOUCH" in listeners_list:
        df_touch["listener"] = data["reports"]["behaviour_event_listeners"]["TOUCH"].keys()
        df_touch["device"] = "TOUCH"
        df_touch["details"] = data["reports"]["behaviour_event_listeners"]["TOUCH"].values()
        df_listeners = df_listeners.append(df_touch)
        
    if "SENSOR" in listeners_list:
        df_sensor["listener"] = data["reports"]["behaviour_event_listeners"]["SENSOR"].keys()
        df_touch["device"] = "SENSOR"
        df_touch["details"] = data["reports"]["behaviour_event_listeners"]["SENSOR"].values()
        df_listeners = df_listeners.append(df_sensor)

    df_listeners.to_csv("listeners.csv", index= False)
    
def cookies_extraction(data):
    try:
        cookies = data["reports"]["cookies"]
        domain_third_party = [x['domain'] for x in cookies if x['third_party'] == True] 
        print(len(domain_third_party))
    except KeyError:
        print("No third part cookies found")

def third_party_tracker_extraction(data):
    try:
        tracker_data = data["reports"]["third_party_trackers"]
        tracker_list = [x['url'].split('/')[2] for x in tracker_data]
        print(len(tracker_list))
    except KeyError:
        print("Third Party Ad Trackers not found")
    
def fb_pixelevent_extraction(data):
    try:
        event_name = [x["eventName"] for x in data["reports"]["fb_pixel_events"]]
        page_url = [x["pageUrl"] for x in data["reports"]["fb_pixel_events"]]
        print(event_name)
    except KeyError:
        print("No facebook pixel events found")
        
def canvas_fingerprinters(data):
    try:
        data_url = [x["fingerprinters"] for x in data["reports"]["canvas_fingerprinters"]]
        print(data_url)
    except TypeError:
        print("No canvas fingerprinters found")
    
    
f = open("inspection.json")
data = json.load(f)

third_party_hosts(data)
listener_extraction(data)
cookies_extraction(data)
third_party_tracker_extraction(data)
fb_pixelevent_extraction(data)
canvas_fingerprinters(data)
