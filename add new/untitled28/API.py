# coding=utf-8
import requests

def getDetailById(url):
    a=requests.get(url)
    return a.text

def postCreateDev(sn):
    a=requests.post(url="http://192.168.1.200:8888/1/dev/createDev",json={
   "access_token":"xxxxx",
   "agencyId":1,
   "userId":3,
    "sn":sn,
    "name":"设备名",
    "modelId":1,
    "describe":"描述内容"
})
    return a.text



