import requests, json
token = "u1748961-e804b6fac522972ca5b0fbee"
#url = "https://api.uptimerobot.com/v2/getMonitors?api_key="

#get = requests.get(url + token)
#print(get)

def new(name, domain):
    url = "https://api.uptimerobot.com/v2/newMonitor"
          
    payload = f"api_key={token}&format=json&type=1&url=https%3A%2F%2F{domain}&friendly_name={name}"
    headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }
          
    response = requests.request("POST", url, data=payload, headers=headers).text
    
    data = json.loads(response)
    idku = data["monitor"]["id"]

    if '{"stat":"ok"' in response:
        return f"succeed, monitor id : `{idku}`"
    else:
        return response

def hapus(id):
    url = "https://api.uptimerobot.com/v2/deleteMonitor"
          
    payload = f"api_key={token}&format=json&id={id}"
    headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
        }
          
    response = requests.request("POST", url, data=payload, headers=headers).text
          
    if '{"stat":"ok"' in response:
        return 'successfully deleted'
    else:
        return response

#print(hapus(""))
