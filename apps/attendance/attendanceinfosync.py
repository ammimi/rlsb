##用于定时同步考勤数据

#-*- coding:utf-8 -*-

#先导入django环境

import os
import hashlib
import time
import json
from django.conf import settings

from system.views_structure import GetClientIDInfo
from facedata.models import FaceData
from system.models import Structure
from apps.utils.getFaceRecognRecordsOnClientTest import getFaceRecognRecords

def getRecords(structure):
    timestamp = int(time.time())
    clientId = structure.client_id
    clientSecret = structure.client_secret
    url = settings.RLSBURL + "historydata/getFaceRecognRecords?"
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

    params["from_year"] = "2019"
    params["from_month"] = "01"
    params["from_day"] = "01"
    params["from_hour"] = "12"
    params["from_minute"] = "32"
    params["from_second"] = "40"

    params["to_year"] = "2019"
    params["to_month"] = "01"
    params["to_day"] = "19"
    params["to_hour"] = "13"
    params["to_minute"] = "54"
    params["to_second"] = "15"

    for key in params:
        url += "%s=%s&" % (key, params[key])
    print (url)
    params = {}
    getFaceRecognRecords(url, params)


def main():
    structures = Structure.objects.filter(type='unit')
    for structure in structures:
        getRecords(structure)


if __name__ == '__main__':
    main()