#-*- coding:utf-8 -*-
# __author__ : mummywho
# __data__  :
import sys
import cv2
import numpy
import time
import base64



from celery import task

from .sendFrameDataByHttpWithWebCamUsed import main
# @task
# def sendByHttpWebCam(userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam, clientId, webCamId, clientSecret, frequencyCatched):
#     sendFrameDataWithWebCam(userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam, clientId, webCamId, clientSecret, frequencyCatched)

@task
def test(id):
    print('hi'+str(id))
    return

@task
def sendFrameWithCam(userForWebCam,pwdForWebCam,ipForWebCam,portForWebCam,clientId,webCamId,clientSecret):
    main(userForWebCam,pwdForWebCam,ipForWebCam,portForWebCam,clientId,webCamId,clientSecret)
    return

