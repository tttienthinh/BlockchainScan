#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests, json, time
env = json.load(open("env.json"))
"""
env.json
[
    "BSCscan": bscscan apikey,
    "FTMscan": ftmscan apikey,
    "SNOWtrace": snowtrace apikey
]
"""
proxy = False
proxies = {
    "http":"192.168.122.6:3128",
    "https":"192.168.122.6:3128",
    "ftp":"192.168.122.6:3128"
}


# In[34]:


tokenList = [
    {
        "chain":"BSC",
        "token":"TAC",
        "contract":"0x6adbaa7c9ed1f29d647e37b1970e32bb41fb18ab",
        "decimal":9,
        "ids":"taichi"
    },
    {
        "chain":"BSC",
        "token":"XEUS",
        "contract":"0x52eb4a4af85bf7921813a12b7cc9ec02b5e94d6e",
        "decimal":9,
        "ids":"xeus"
    },
    {
        "chain":"FTM",
        "token":"SPA",
        "contract":"0x8e2549225E21B1Da105563D419d5689b80343E01",
        "decimal":9,
        "ids":"spartacus"
    },
    {
        "chain":"FTM",
        "token":"HEC",
        "contract":"0x75bdef24285013387a47775828bec90b91ca9a5f",
        "decimal":9,
        "ids":"hector-dao"
    },
    {
        "chain":"FTM",
        "token":"EXOD",
        "contract":"0x8de250c65636ef02a75e4999890c91cecd38d03d",
        "decimal":9,
        "ids":"exodia"
    },
    {
        "chain":"AVAX",
        "token":"TIME",
        "contract":"0x136acd46c134e8269052c62a67042d6bdedde3c9",
        "decimal":9,
        "ids":"wonderland"
    },
    {
        "chain":"AVAX",
        "token":"SB",
        "contract":"0xE9Eb40d52CE4744322204d4a29Af63C30f0260a4",
        "decimal":9,
        "ids":"snowbank"
    },
    {
        "chain":"ONE",
        "token":"RVRS",
        "contract":"0xE9Eb40d52CE4744322204d4a29Af63C30f0260a4",
        "decimal":9,
        "numbers":8.95,
        "staking":266600/100,
        "starting":1638032419,
        "ids":"reverse-protocol"
    },
    {
        "chain":"ONE",
        "token":"ODAO",
        "contract":"0xE9Eb40d52CE4744322204d4a29Af63C30f0260a4",
        "decimal":9,
        "numbers":0.003308,
        "staking":1_400_000_000/100,
        "starting":1638032419,
        "ids":"onedao-finance"
    },
]


# In[41]:


result = 0
for token in tokenList:
    if token["chain"] == "ONE":
        numbers = token["numbers"]*(token["staking"]**((time.time()-token["starting"])/(60*60*24*365)))
    else:
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
        if proxy:
            r = requests.get(url, params=dico, proxies=proxies)
        else:
            r = requests.get(url, params=dico)
        numbers = int(r.json()["result"])/(10**token["decimal"])
        if token["ids"] == "snowbank":
            numbers = numbers*2/3
    dico = {
        "ids":token["ids"],
        "vs_currencies":"usd"
    }
    r = requests.get(
        "https://api.coingecko.com/api/v3/simple/price", 
        params=dico
    )
    price = r.json()[token["ids"]]["usd"]
    tt = numbers*price
    result += tt
    print(f"""{token["token"]} : {numbers} at price {price} egal {tt}""")
print()
print(f"Total : {result} $")


# In[42]:


repartition = [
    ("4T", 0.2),
    ("Gouillou", 0.14),
    ("Couillet", 0.14),
    ("Synold", 0.14),
    ("Rigot", 0.14),
    ("Djafri", 0.11),
    ("Ferro", 0.09),
    ("Pot", 0.03),
]
for name, taux in repartition:
    print(f"{name} : {taux*result} $")

