#! /usr/bin/python
# -*-coding=utf-8 -*-

#import pickle
from urllib.request import urlopen
from urllib.parse import urlencode

import hashlib
import time
import json

def post(server_url, params):
    """
    data = urllib.urlencode(params)
    request = urllib2.Request(server_url, data)
    return json.loads(urllib2.urlopen(request, timeout=10).read())
    """
    """
    from urllib.request import urlopen
    from urllib.parse import urlencode
    url = "http://192.168.40.129:8080/cgi-bin/newtest1.py"
    params = urlencode({"personName":"tomjao","personAge":52,"personSex":"Fax"}).encode('utf-8')
    reply = urlopen(url,params).read()
    print(reply.decode("utf-8"))
    """
    params = urlencode(params).encode('utf-8')
    reply = urlopen(server_url,params).read()
    return reply

def deletFaceData(server_url, params):
    result = post(server_url, params).decode("utf-8")
    ret = json.loads(result)
    print(ret)
    return ret



if __name__ == "__main__":

   #url = "http://192.168.1.219/cgi-bin/v0.13/facemng/delete.py"
   url = "http://192.168.1.219/v0.13/facemng/delete"
    
   timestamp = int(time.time())
   clientId = 33
   clientSecret = "abc123"
    
   #faceId = "33_22"
   faceId = "33_63"

   params = {"client_id":clientId, "client_secret":clientSecret,"face_id":faceId,"timestamp":timestamp}

   paramNamesForSignature = sorted(["client_secret","face_id","client_id","timestamp"],key=str.lower)
   #print(paramNamesForSignature)
   paramValuesStr = ""
   for index in range(0, len(paramNamesForSignature)):
       param = paramNamesForSignature[index]
       paramValuesStr += str(params[param])

   #print(paramValuesStr)

   m = hashlib.md5()
   m.update(paramValuesStr.encode("utf-8"))
   signatureStr=m.hexdigest()
   #print(signatureStr)

   params["signature"]=signatureStr

   deletFaceData(url, params)
