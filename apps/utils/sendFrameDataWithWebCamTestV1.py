

import sys
import cv2
import time
from socket import *
import numpy
import struct


def recvall(sock, count):
    buf = b''
    while count:
          newbuf = sock.recv(count)
          if not newbuf:
             return None
          buf += newbuf
          count -= len(newbuf)
    return buf

def sendFrameDataWithVideoFile(videoFilePathName, clientId, webCamId, frequencyCatched = 100):    

    serverHost = "192.168.1.219"
    serverPort = 60054

    video_capture = cv2.VideoCapture(videoFilePathName)
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    
    frameNum=0
    ret = True
    while ret:
       ret, frame = video_capture.read()

       if not ret:
          break

       if frameNum%frequencyCatched == 0:    
          result, imgencode = cv2.imencode('.jpg', frame, encode_param)
          imgData = numpy.array(imgencode)
          stringImgData = imgData.tostring()
          sendDataBySocket(serverHost,serverPort,clientId,webCamId,stringImgData,"")
          frameNum=0

       frameNum +=1
       
    return


def sendFrameDataWithWebCam(userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam, clientId, webCamId, frequencyCatched = 100):    

    webCamUrl = "rtsp://%s:%s@%s:%s/h264/ch1/main/av_stream" % (userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam);

    video_capture = cv2.VideoCapture(webCamUrl)        

    if not video_capture.isOpened():
       print("网络摄像头尚未开启，请检查后再试。") 
       return

    #encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),100]
    
    frameNum=0
    ret = True
    while (ret and video_capture.isOpened()):
       ret, frame = video_capture.read()

       if not ret:
          break
        
       
       if frameNum%frequencyCatched == 0:    
          result, imgencode = cv2.imencode('.jpg', frame, encode_param)
          imgData = numpy.array(imgencode)
          stringImgData = imgData.tostring()
          #sendDataBySocket(clientId,webCamId,stringImgData,"")
          sendDataBySocketV1(clientId,webCamId,stringImgData,"")
          frameNum=0
       
       frameNum +=1

    return

def sendDataBySocket(clientId,webCamId,frame,gray):    
    sockobj = socket(AF_INET, SOCK_STREAM) # make a TCP/IP socket object
    sockobj.connect((serverHost, serverPort)) # connect to server machine + port
    clientHost, clientPort = sockobj.getsockname()

    #timestamp = int(time.time())  #秒级时间戳
    timestamp = int(round(time.time() * 1000))  #毫秒级时间戳

    print(len(frame))
    #print(frame)

    countLen=len(frame)
    #structFormat = "<4I%ds" % countLen
    structFormat = "<3Iq%ds" % countLen
    tx_buf = struct.pack(structFormat, countLen, clientId, webCamId, timestamp, frame)
    
    sockobj.sendall(tx_buf)
    data = sockobj.recv(1024) # receive line from server: up to 1k
    print("Receive Response From Server Side: %s" % data.decode("utf-8"))
    sockobj.close()

def sendDataBySocketV1(clientId,webCamId,frame,gray):    
    sockobj = socket(AF_INET, SOCK_STREAM) # make a TCP/IP socket object
    sockobj.connect((serverHost, serverPort)) # connect to server machine + port
    clientHost, clientPort = sockobj.getsockname()

    #timestamp = int(time.time())  #秒级时间戳
    timestamp = int(round(time.time() * 1000))  #毫秒级时间戳

    print(len(frame))
    #print(frame)

    countLen=len(frame)
    #structFormat = "<4I%ds" % countLen
    structFormat = "<3Iq%ds" % countLen
    tx_buf = struct.pack(structFormat, countLen, clientId, webCamId, timestamp, frame)
    
    sockobj.sendall(tx_buf)

    recognResult = {}
    
    recognizedFacesNum_struct = recvall(sockobj, 4)
    recognizedFacesNum = struct.unpack("<I", bytes(recognizedFacesNum_struct))[0]
    
    timestamp_struct = recvall(sockobj,8)
    timestamp = struct.unpack("<q",bytes(timestamp_struct))[0]
    timeArray = time.localtime(int(timestamp / 1000))
    strDatetime = time.strftime("%H时%M分%S秒", timeArray)

    recognResult["Recognized_faces_num"] = recognizedFacesNum
    recognResult["Recorded_datetime"] = strDatetime

    """
    if (recognizedFacesNum > 0):
       lengthOfRecognizedFacesNamesList_struct = recvall(sockobj, 4)
       lengthOfRecognizedFacesNamesList = struct.unpack("<I",bytes(lengthOfRecognizedFacesNamesList_struct))[0]
       recognizedFacesNamesList_struct = recvall(sockobj, lengthOfRecognizedFacesNamesList)
       recognizedFacesNamesList = struct.unpack("<%ds" % lengthOfRecognizedFacesNamesList, bytes(recognizedFacesNamesList_struct))[0]
       recognizedFacesNamesList = recognizedFacesNamesList.decode("utf8")
       recognResult["Recognized_faces_names_list"] = recognizedFacesNamesList
       
       lengthOfRecognizedFacesCNamesList_struct = recvall(sockobj, 4)
       lengthOfRecognizedFacesCNamesList = struct.unpack("<I",bytes(lengthOfRecognizedFacesCNamesList_struct))[0]
       recognizedFacesCNamesList_struct = recvall(sockobj, lengthOfRecognizedFacesCNamesList)
       recognizedFacesCNamesList = struct.unpack("<%ds" % lengthOfRecognizedFacesCNamesList, bytes(recognizedFacesCNamesList_struct))[0]
       recognizedFacesCNamesList = recognizedFacesCNamesList.decode("utf8")
       recognResult["Recognized_faces_cnames_list"] = recognizedFacesCNamesList

       lengthOfRecognizedFacesIdsList_struct = recvall(sockobj, 4)
       lengthOfRecognizedFacesIdsList = struct.unpack("<I",bytes(lengthOfRecognizedFacesIdsList_struct))[0]
       recognizedFacesIdsList_struct = recvall(sockobj, lengthOfRecognizedFacesIdsList)
       recognizedFacesIdsList = struct.unpack("<%ds" % lengthOfRecognizedFacesIdsList, bytes(recognizedFacesIdsList_struct))[0]
       recognizedFacesIdsList = recognizedFacesIdsList.decode("utf8")
       recognResult["Recognized_faces_ids_list"] = recognizedFacesIdsList
    """

    
    lengthOfRecognizedFacesNamesList_struct = recvall(sockobj, 4)
    lengthOfRecognizedFacesNamesList = struct.unpack("<I",bytes(lengthOfRecognizedFacesNamesList_struct))[0]
    recognizedFacesNamesList_struct = recvall(sockobj, lengthOfRecognizedFacesNamesList)
    recognizedFacesNamesList = struct.unpack("<%ds" % lengthOfRecognizedFacesNamesList, bytes(recognizedFacesNamesList_struct))[0]
    recognizedFacesNamesList = recognizedFacesNamesList.decode("utf8")
    recognResult["Recognized_faces_names_list"] = recognizedFacesNamesList
       
    lengthOfRecognizedFacesCNamesList_struct = recvall(sockobj, 4)
    lengthOfRecognizedFacesCNamesList = struct.unpack("<I",bytes(lengthOfRecognizedFacesCNamesList_struct))[0]
    recognizedFacesCNamesList_struct = recvall(sockobj, lengthOfRecognizedFacesCNamesList)
    recognizedFacesCNamesList = struct.unpack("<%ds" % lengthOfRecognizedFacesCNamesList, bytes(recognizedFacesCNamesList_struct))[0]
    recognizedFacesCNamesList = recognizedFacesCNamesList.decode("utf8")
    recognResult["Recognized_faces_cnames_list"] = recognizedFacesCNamesList

    lengthOfRecognizedFacesIdsList_struct = recvall(sockobj, 4)
    lengthOfRecognizedFacesIdsList = struct.unpack("<I",bytes(lengthOfRecognizedFacesIdsList_struct))[0]
    recognizedFacesIdsList_struct = recvall(sockobj, lengthOfRecognizedFacesIdsList)
    recognizedFacesIdsList = struct.unpack("<%ds" % lengthOfRecognizedFacesIdsList, bytes(recognizedFacesIdsList_struct))[0]
    recognizedFacesIdsList = recognizedFacesIdsList.decode("utf8")
    recognResult["Recognized_faces_ids_list"] = recognizedFacesIdsList   
       
    print("Receive Response From Server Side: ", recognResult)
    sockobj.close() 

       
if len(sys.argv)<7:
   print("错误: ","缺少脚本所需参数")
   exit()

userForWebCam = sys.argv[1]
pwdForWebCam = sys.argv[2]
ipForWebCam = sys.argv[3]
portForWebCam = sys.argv[4]
clientId = int(sys.argv[5])
webCamId = int(sys.argv[6])

#python sendFrameDataWithWebCamTest.py "admin" "MHQAFM" "192.168.1.243" "554" 33 9

"""
userForWebCam = "admin"
pwdForWebCam = "MHQAFM"
ipForWebCam = "192.168.1.243"
portForWebCam = "554"
clientId = 33
webCamId = 9
"""
frequencyCatched = 20
#frequencyCatched = 10
serverHost = "192.168.1.219"
serverPort = 60054
sendFrameDataWithWebCam(userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam, clientId, webCamId, frequencyCatched)

