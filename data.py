import requests

def DashData():
    request = requests.get('http://18.189.117.13:2011/requestM')
    data = request.json()
    return data


def Responces():
    request = requests.get('http://18.189.117.13:2011/responses')
    data = request.json()
    return data
    
print(DashData()[-1])
    