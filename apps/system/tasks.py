#-*- coding:utf-8 -*-
# __author__ : mummywho
# __data__  :
import sys
import cv2
import numpy
import time
import base64



from celery import task
from .models import CameraSet
from .sendFrameDataByHttpWithWebCamUsed import main
# @task
# def sendByHttpWebCam(userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam, clientId, webCamId, clientSecret, frequencyCatched):
#     sendFrameDataWithWebCam(userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam, clientId, webCamId, clientSecret, frequencyCatched)



@task
def test(id):
    print('hi'+str(id))
    return
@task
def add(x,y):
    print (x+y)
    print('beat')

    return

@task
def sendFrameWithCam():
    camerasets = CameraSet.objects.all()
    for cameraset in camerasets:
        userForWebCam = cameraset.usercam
        pwdForWebCam = cameraset.pwdcam
        ipForWebCam = cameraset.ipcam
        portForWebCam = cameraset.portcam
        webCamId = cameraset.webcamid
        clientId = cameraset.company.client_id
        clientSecret = cameraset.company.client_secret
        try:
            main(userForWebCam,pwdForWebCam,ipForWebCam,portForWebCam,clientId,webCamId,clientSecret)
        except:
            print('第{0}号摄像头故障'.format(cameraset.id))
    return

