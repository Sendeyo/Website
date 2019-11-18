import requests

request = requests.get('http://18.189.117.13:2011/requestM')

def DashData():
    data = request.json()
    return data
    
print(DashData()[-1])
    