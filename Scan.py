#!/usr/bin/env python
# coding: utf-8

# In[61]:


import requests
import json
env = json.load(open("env.json"))
"""
env.json
[
    "BSCscan": bscscan apikey,
    "FTMscan": ftmscan apikey,
    "SNOWtrace": snowtrace apikey
]
"""


# In[58]:


tokenList = [
    {
        "chain":"BSC",
        "token":"TAC",
        "contract":"0x6adbaa7c9ed1f29d647e37b1970e32bb41fb18ab",
        "decimal":9
    },
    {
        "chain":"BSC",
        "token":"XEUS",
        "contract":"0x52eb4a4af85bf7921813a12b7cc9ec02b5e94d6e",
        "decimal":9
    },
    {
        "chain":"FTM",
        "token":"SPA",
        "contract":"0x8e2549225E21B1Da105563D419d5689b80343E01",
        "decimal":9
    },
    {
        "chain":"FTM",
        "token":"HEC",
        "contract":"0x75bdef24285013387a47775828bec90b91ca9a5f",
        "decimal":9
    },
    {
        "chain":"FTM",
        "token":"EXOD",
        "contract":"0x8de250c65636ef02a75e4999890c91cecd38d03d",
        "decimal":9
    },
    {
        "chain":"AVAX",
        "token":"TIME",
        "contract":"0x136acd46c134e8269052c62a67042d6bdedde3c9",
        "decimal":9
    },
]


# In[59]:


for token in tokenList:
    if token["chain"] == "BSC":
        url = "https://api.bscscan.com/api"
        api = env["BSCscan"]
    elif token["chain"] == "FTM":
        url = "https://api.ftmscan.com/api"
        api = env["FTMscan"]
    else:
        url = "https://api.snowtrace.io/api"
        api = env["SNOWtrace"]
        
    dico = {"module":"account",
        "action":"tokenbalance",
        "contractaddress":token["contract"],
        "address":"0x97A0bD28796621FAa6d168ee414B814b307517FF",
        "tag":"latest",
        "apikey":api}
    r = requests.get(url, params=dico)
    print(f"""{token["token"]} : {int(r.json()["result"])/(10**token["decimal"])}""")

