
#! /usr/bin/python
# -*-coding=utf-8 -*-

from urllib.request import urlopen
from urllib.parse import urlencode

import base64

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

def remote_image(server_url, image_url):
    """
    网络图片处理

    :param server_url: 服务器端HTTP服务URL
    :param image_url: 图片URL
    """
    content = requests.get(image_url)
    params = {"content": content}
    print(post(server_url, params))


def local_image(server_url, image_path):
    """
    本地图片处理

    :param server_url: 服务器端HTTP服务URL
    :param image_path: 图片本地地址
    """
    f = open(image_path,"rb")
    img_raw_data = f.read()
    f.close()
    base64_content_string = base64.b64encode(img_raw_data)

    #params = {"personName":"Tom Josn", "personAge":56, "content":base64_content_string}
    params = {"client_id":"33", "client_secret":"abc123","face_name":"liyang","face_cname":"李阳","face_image":base64_content_string,"timestamp":332444,"signature":"eererer3eeer3fsxxerfe"}
    #client_id=22345&client_secret=abc123&face_name=liyang&face_cname=李阳&face_image=kjggkekskgjuuiyiuytrregksldlgjgkdjgrtu5ereetrtkfdgjgjfdkfgjfgkfgjkfgjfkgjkfgjwqswdefdgfgeterter&signature=ffgfg
    print(post(server_url, params).decode("utf-8"))



def updateFaceData(server_url, params, image_path):
    f = open(image_path,"rb")
    img_raw_data = f.read()
    f.close()
    base64_content_string = base64.b64encode(img_raw_data)

    #params = {"client_id":"33", "client_secret":"abc123","face_name":"liyang","face_cname":"李阳","face_image":base64_content_string,"timestamp":332444,"signature":"eererer3eeer3fsxxerfe"}
    params["face_image"]=base64_content_string
    #print(post(server_url, params).decode("utf-8"))
    result = post(server_url, params).decode("utf-8")
    ret = json.loads(result)
    print(ret)
    return ret


if __name__ == "__main__":

    #url = "http://192.168.1.219/cgi-bin/v0.13/facemng/update.py"
    url = "http://192.168.1.219/v0.13/facemng/update"
    
    timestamp = int(time.time())
    clientId = 33
    #clientId = 34
    clientSecret = "abc123"
    
    #faceId = "33_23"
    #faceName = "xuli"
    #faceCName = "徐丽"
    #imageFileExtention = "png"
    #file_path = "D:\\pythoncodes\\2ce45ba610d0883d99f2f3de0ba15602.png"


    faceId = "33_63"
    faceName = "naying"
    faceCName = "那英"
    imageFileExtention = "jpeg"
    file_path = "D:\\pythoncodes\\facerecognapp\\known_imgs\\naying.jpeg"

    params = {"client_id":clientId, "client_secret":clientSecret,"face_id":faceId,"face_name":faceName,"face_cname":faceCName,"timestamp":timestamp,"image_file_extention":imageFileExtention}

    paramNamesForSignature = sorted(["client_secret","face_name","client_id","face_id","timestamp","image_file_extention"],key=str.lower)
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

    updateFaceData(url, params, file_path)
    

