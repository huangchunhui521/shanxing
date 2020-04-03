import requests,json
url = "https://temple.dev.renrenfo.cn:2443/ts/v2/temple/app/v4/temple/61/masters"
req=requests.get(url)#发送get请求
print(req.text)#获取结果直接返回的就是json串
print(type(req.text)) #str
print(json.loads(req.text))#json转字典
print(req.json())#获取结果就是字典,只有返回的是json串的话才能用req.json()
print(type(req.json()))#dict