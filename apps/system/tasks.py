#-*- coding:utf-8 -*-
# __author__ : mummywho
# __data__  :
import sys
import cv2
import numpy
import time
import base64



from celery import task
# from apps.utils.sendFrameDataByHttpWithWebCamUsed import sendFrameDataByHttp,sendFrameDataWithWebCam
# @task
# def sendByHttpWebCam(userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam, clientId, webCamId, clientSecret, frequencyCatched):
#     sendFrameDataWithWebCam(userForWebCam, pwdForWebCam, ipForWebCam, portForWebCam, clientId, webCamId, clientSecret, frequencyCatched)

@task
def test(id):
    print('hi'+id)
    return


