
import sys
import cv2
import numpy
import time
import base64

from urllib.request import urlopen
from urllib.parse import urlencode

import hashlib
import json

import threading

server_url = "http://222.128.127.3:8185/v0.13/facerecognize/doRecognizeWithVideoFrame"


def sendFrameDataWithWebCam(userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam, clientId, webCamId, clientSecret, frequencyCatched = 100):    
    global framesList
    webCamUrl = "rtsp://%s:%s@%s:%s/h264/ch1/main/av_stream" % (userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam);

    video_capture = cv2.VideoCapture(webCamUrl)        

    if not video_capture.isOpened():
       print("网络摄像头尚未开启，请检查后再试。") 
       return

    frameNum=0
    while (video_capture.isOpened()):    
       ret, frame = video_capture.read()

       if not ret:
          continue
        
       """
       if frameNum%frequencyCatched == 0:
          if frame is not None:
             millisecond_timestamp = int(round(time.time() * 1000))
             threadObj = threading.Thread(target=handleFrameData, args=(millisecond_timestamp,frame))#创建线程
             threadObj.setDaemon(True)#设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
             threadObj.start()#开启线程
             
          frameNum=0
       """
       
       if frameNum%frequencyCatched == 0:
          if frame is not None:
             millisecond_timestamp = int(round(time.time() * 1000))
             framesList.append((millisecond_timestamp,frame))
          frameNum=0

       frameNum +=1

    return


def sendFrameDataByHttp(clientId, clientSecret, webCamId, base64ImgData):

    millisecond_timestamp = int(round(time.time() * 1000))

    params = {"client_id":clientId, "client_secret":clientSecret,"webcam_id":webCamId,"image":base64ImgData,"millisecond_timestamp":millisecond_timestamp}

    paramNamesForSignature = sorted(["client_secret","client_id","millisecond_timestamp","webcam_id"],key=str.lower)

    paramValuesStr = ""
    for index in range(0, len(paramNamesForSignature)):
        param = paramNamesForSignature[index]
        paramValuesStr += str(params[param])

    m = hashlib.md5()
    m.update(paramValuesStr.encode("utf-8"))
    signatureStr=m.hexdigest()

    params["signature"]=signatureStr
    
    params = urlencode(params).encode('utf-8')
    reply = urlopen(server_url,params).read()
    result = reply.decode("utf-8")
    ret = json.loads(result)
    print(ret)
    
    return


def sendFrameDataByHttpV1(clientId, clientSecret, webCamId, millisecond_timestamp, frame):
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    if not result:
        return

    imgData = numpy.array(imgencode)
    stringImgData = imgData.tostring()
    base64ImgData = base64.b64encode(stringImgData)

    params = {"client_id": clientId, "client_secret": clientSecret, "webcam_id": webCamId, "image": base64ImgData,
              "millisecond_timestamp": millisecond_timestamp}

    paramNamesForSignature = sorted(["client_secret", "client_id", "millisecond_timestamp", "webcam_id"], key=str.lower)

    paramValuesStr = ""
    for index in range(0, len(paramNamesForSignature)):
        param = paramNamesForSignature[index]
        paramValuesStr += str(params[param])

    m = hashlib.md5()
    m.update(paramValuesStr.encode("utf-8"))
    signatureStr = m.hexdigest()

    params["signature"] = signatureStr

    params = urlencode(params).encode('utf-8')
    reply = urlopen(server_url, params).read()
    result = reply.decode("utf-8")
    ret = json.loads(result)
    print(ret)

    return


def handleFrameData(millisecond_timestamp, frame):
    sendFrameDataByHttpV1(clientId, clientSecret, webCamId, millisecond_timestamp, frame)
    return


def processFrameData():
    global framesList
    while True:
        if len(framesList) > 0:
            millisecond_timestamp, frame = framesList.pop(0)
            sendFrameDataByHttpV1(clientId, clientSecret, webCamId, millisecond_timestamp, frame)
    return


def main(userForWebCam,pwdForWebCam,ipForWebCam,portForWebCam,clientId,webCamId,clientSecret):
    server_url = "http://222.128.127.3:8185/v0.13/facerecognize/doRecognizeWithVideoFrame"
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),100]


    #python sendFrameDataByHttpWithWebCamTestV1.py "admin" "MHQAFM" "192.168.1.243" "554" 33 9 "abc123"
    #python sendFrameDataByHttpWithWebCamTestV1.py "admin" "MHQAFM" "192.168.1.243" "554" 33 9 "1234567890"

    """
    userForWebCam = "admin"
    pwdForWebCam = "MHQAFM"
    ipForWebCam = "192.168.1.243"
    portForWebCam = "554"
    clientId = 33
    webCamId = 9
    #clientSecret = "abc123"
    clientSecret = "1234567890"
    """
    frequencyCatched = 20
    framesList = []
    threadObj = threading.Thread(target=processFrameData, args=())#创建线程
    threadObj.setDaemon(True)#设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
    threadObj.start()#开启线程
    sendFrameDataWithWebCam(userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam, clientId, webCamId, clientSecret, frequencyCatched)


