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
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404

from system.models import Role,Menu
from system.models import SystemSetup

from .models import AttendanceInfo,ImageTmp
from facedata.models import FaceData
from django.contrib.auth import get_user_model
from system.views_structure import GetClientIDInfo
from apps.utils.doRecognizeWithImgFileOnClientTest import sendLocalImageFile
#from apps.utils.doRecognizeWithWebCamTestV1 import sendDataBySocketV1,sendDataBySocket
from apps.utils.doRecognizeWithVideoFrameTest import sendFrameDataByHttp
import datetime
User = get_user_model()

class RecognizeWithVideoFrame(View):
    def get(self,request):
        ret = Menu.get_menu_by_request_url(url=request.path_info)

        return render(request, 'oa/attendance/attendance_recognizewithvideo.html', ret)

    def post(self,request):

        ret = ()
        image = request.FILES.get('face_image')
        imagetmp = ImageTmp(image=image)
        imagetmp.save()
        imagepath = imagetmp.image.path

        #sendDataBySocketV1(clientId, webCamId, stringImgData, "")
        f = open(imagepath, "rb")
        img_raw_data = f.read()
        f.close()
        stringImgData = base64.b64encode(img_raw_data)

# '''
#         clientId = int(GetClientIDInfo(request.user.id).get_clientid())
#         webCamId = 123
#
#         send_local_image = sendDataBySocketV1(clientId, webCamId, stringImgData, "")
# '''
        clientId = int(GetClientIDInfo(request.user.id).get_clientid())
        clientSecret = GetClientIDInfo(request.user.id).get_clientsecret()
        webCamId = 123
        send_local_image = sendFrameDataByHttp(clientId, clientSecret, webCamId, stringImgData)
        imagetmp.delete()

        # facedata = FaceData.objects.get(id=2)
        # attendate = AttendanceInfo(facedata=facedata,image=image)
        # attendate.save()
        res = dict()
        if send_local_image['result'] =='success':

            if send_local_image['recognized_face_num'] > 0:

                face_ids = send_local_image['recognized_face_ids_list'].split('#')

                department = request.user.department
                if department:  # 找到所在的单位
                    if department.parent:
                        parent = department.parent
                        index_depart = 1
                    else:
                        parent = department
                        index_depart = 2



                for face_id in face_ids:

                    facedata = FaceData.objects.get(face_id=face_id)
                    attendate = AttendanceInfo(facedata=facedata, image=image,recorded_datetime=send_local_image['datetime'])
                    attendate.save()

                res = {
                    'status': 'success',
                    'send_local_image': '{}识别成功！'.format(face_ids)
                }
            else:
                res = {
                    'status': 'fail',
                    'send_local_image': '未识别出对象！'
                }

        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = send_local_image['error_msg']

            res = {
                'status': 'fail',
                'send_local_image': errors
            }

        return HttpResponse(json.dumps(res), content_type='application/json')



