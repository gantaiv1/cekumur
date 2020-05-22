import requests
url = ' https://eu121.chat-api.com/message?token=ypajx5p2wrb7ko9s '
data = ({"phone": "081245726184"}, {"body": "Hello, World!"})
res = requests.post(url, json=data)
print res.text