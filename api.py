import requests
import json

class API:
    def __init__(self,base_url):
        self.base_url=base_url
        
    def get(self,endpoint,params=None):
        url=self.base_url+endpoint
        response=requests.get(url,params=params)
        if response.status_code==200:
            return response.json()
        else:
            raise Exception(f"GET request failed with status code {response.status_code}:{response.text}")

    def post(self,endpoint,data=None,headers=None):
        url=self.base_url+endpoint
        if headers is None:
            headers={"Content-Type":"application/json"}
        response=requests.post(url,json=data,headers=headers)
        if response.status_code in (200,201):
            return response.json()
        else:
            raise Exception(f"POST request failed with status code {response.status_code}:{response.text}")
        
Get=API("https://api.open-meteo.com/v1/forecast?latitude=27.7172&longitude=85.3240&current=temperature_2m")

data=Get.get("")
print(data)
print(json.dumps(data,indent=4))
print(data["current"]["temperature_2m"])
