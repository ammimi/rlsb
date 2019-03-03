import json
import re
import base64
import hashlib
import time

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.conf import settings
from .models import FaceData
from .forms import FaceDataCreateForm,FaceDataUpdateForm
from system.models import Menu,SystemSetup
from system.mixin import LoginRequiredMixin
from system.views_structure import GetClientIDInfo
import imghdr
import time
from apps.utils.sendFaceDataOnClientTest import sendLocalImage
from apps.utils.deleteFaceDataOnClientTest import deletFaceData
from apps.utils.updateFaceDataOnClientTest import updateFaceData
from apps.utils.doRecognizeWithImgFileOnClientTest import sendLocalImageFile

class SendFaceDataView(LoginRequiredMixin, View):
    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            facedata = get_object_or_404(FaceData, pk=request.POST.get('id'))
            faceName = facedata.face_name
            faceCName = facedata.face_cname
            file_path = facedata.face_image.path
            #imageFileExtention = file_path.split('.')[-1]
            imageFileExtention = imghdr.what(facedata.face_image)
            timestamp = int(time.time())
            url = settings.RLSBURL+"facemng/add"
            clientId = GetClientIDInfo(facedata.id).get_clientid()
            clientSecret = GetClientIDInfo(facedata.id).get_clientsecret()


            params = {"client_id": clientId, "client_secret": clientSecret, "face_name": faceName, "face_cname": faceCName,
                      "timestamp": timestamp, "image_file_extention": imageFileExtention}

            paramNamesForSignature = sorted(
                ["client_secret", "face_name", "client_id", "timestamp", "image_file_extention"], key=str.lower)
            # print(paramNamesForSignature)
            paramValuesStr = ""
            for index in range(0, len(paramNamesForSignature)):
                param = paramNamesForSignature[index]
                paramValuesStr += str(params[param])

            # print(paramValuesStr)

            m = hashlib.md5()
            m.update(paramValuesStr.encode("utf-8"))
            signatureStr = m.hexdigest()
            # print(signatureStr)

            params["signature"] = signatureStr

            send_local_image = sendLocalImage(url, params, file_path)
            res = dict()
            if send_local_image['result'] =='success':
                res['status'] = 'success'
                facedata.face_id = send_local_image['face_id']
                facedata.ifsync = True
                facedata.save()
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = send_local_image['error_msg']

                res = {
                    'status': 'fail',
                    'send_local_image': errors
                }

        return HttpResponse(json.dumps(res), content_type='application/json')


class DeleteFaceDataView(LoginRequiredMixin, View):
    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            facedata = get_object_or_404(FaceData, pk=request.POST.get('id'))
            faceId = facedata.face_id

            timestamp = int(time.time())
            url = settings.RLSBURL + "facemng/delete"
            clientId = GetClientIDInfo(facedata.id).get_clientid()
            clientSecret = GetClientIDInfo(facedata.id).get_clientsecret()

            params = {"client_id": clientId, "client_secret": clientSecret, "face_id": faceId, "timestamp": timestamp}

            paramNamesForSignature = sorted(["client_secret", "face_id", "client_id", "timestamp"], key=str.lower)
            # print(paramNamesForSignature)
            paramValuesStr = ""
            for index in range(0, len(paramNamesForSignature)):
                param = paramNamesForSignature[index]
                paramValuesStr += str(params[param])

            # print(paramValuesStr)

            m = hashlib.md5()
            m.update(paramValuesStr.encode("utf-8"))
            signatureStr = m.hexdigest()
            # print(signatureStr)

            params["signature"] = signatureStr

            delete_facedata = deletFaceData(url, params)

            res = dict()
            if delete_facedata['result'] == 'success':
                res['status'] = 'success'
                facedata.ifsync = False
                facedata.save()
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = delete_facedata['error_msg']

                res = {
                    'status': 'fail',
                    'delete_facedata': errors
                }

        return HttpResponse(json.dumps(res), content_type='application/json')

class UpdateFaceDataView(LoginRequiredMixin, View):
    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            facedata = get_object_or_404(FaceData, pk=request.POST.get('id'))
            faceId = facedata.face_id
            faceName = facedata.face_name
            faceCName = facedata.face_cname
            file_path = facedata.face_image.path
            imageFileExtention = imghdr.what(facedata.face_image)

            timestamp = int(time.time())
            url = settings.RLSBURL + "facemng/update"
            clientId = GetClientIDInfo(facedata.id).get_clientid()
            clientSecret = GetClientIDInfo(facedata.id).get_clientsecret()

            params = {"client_id": clientId, "client_secret": clientSecret, "face_id": faceId, "face_name": faceName,
                      "face_cname": faceCName, "timestamp": timestamp, "image_file_extention": imageFileExtention}

            paramNamesForSignature = sorted(
                ["client_secret", "face_name", "client_id", "face_id", "timestamp", "image_file_extention"],
                key=str.lower)
            # print(paramNamesForSignature)
            paramValuesStr = ""
            for index in range(0, len(paramNamesForSignature)):
                param = paramNamesForSignature[index]
                paramValuesStr += str(params[param])

            # print(paramValuesStr)

            m = hashlib.md5()
            m.update(paramValuesStr.encode("utf-8"))
            signatureStr = m.hexdigest()
            # print(signatureStr)

            params["signature"] = signatureStr

            update_facedata = updateFaceData(url, params, file_path)

            res = dict()
            if update_facedata['result'] == 'success':
                facedata.ifsync = True
                facedata.save()
                res['status'] = 'success'

            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = update_facedata['error_msg']

                res = {
                    'status': 'fail',
                    'update_facedata': errors
                }

        return HttpResponse(json.dumps(res), content_type='application/json')

#人工打卡
class ManualClockView(LoginRequiredMixin, View):
    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            facedata = get_object_or_404(FaceData, pk=request.POST.get('id'))

            file_path = facedata.face_image.path
            imageFileExtention = imghdr.what(facedata.face_image)

            timestamp = int(time.time())
            url = settings.RLSBURL + "facerecognize/doRecognizeWithImgFile"
            clientId = GetClientIDInfo(facedata.id).get_clientid()
            clientSecret = GetClientIDInfo(facedata.id).get_clientsecret()

            params = {"client_id": clientId, "client_secret": clientSecret, "timestamp": timestamp}

            paramNamesForSignature = sorted(["client_secret", "client_id", "timestamp"], key=str.lower)
            # print(paramNamesForSignature)
            paramValuesStr = ""
            for index in range(0, len(paramNamesForSignature)):
                param = paramNamesForSignature[index]
                paramValuesStr += str(params[param])

            # print(paramValuesStr)

            m = hashlib.md5()
            m.update(paramValuesStr.encode("utf-8"))
            signatureStr = m.hexdigest()
            # print(signatureStr)

            params["signature"] = signatureStr

            send_local_image = sendLocalImageFile(url, params, file_path)

            res = dict()
            if send_local_image['result'] == 'success':
                #需添加考勤记录

                res['status'] = 'success'

            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = send_local_image['error_msg']

                res = {
                    'status': 'fail',
                    'send_local_image': errors
                }

        return HttpResponse(json.dumps(res), content_type='application/json')