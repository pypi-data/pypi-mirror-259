import json
import hashlib
import time
import socket
import requests
import urllib3
import os, sys
import random
import datetime
import base64
import ping3
import uuid

import mecord.pb.uauth_common_pb2 as uauth_common_pb2
import mecord.pb.uauth_ext_pb2 as uauth_ext_pb2
import mecord.pb.user_ext_pb2 as user_ext_pb2
import mecord.pb.common_ext_pb2 as common_ext_pb2
import mecord.pb.aigc_ext_pb2 as aigc_ext_pb2
import mecord.pb.rpcinput_pb2 as rpcinput_pb2
from mecord import store 
from mecord import utils 
from mecord import taskUtils 
from mecord import constant 
from mecord import xy_network 

OFFICIAL_PRODUCT_TOKEN = "NDl8NWU5OGI1ODk4N2ExNTZmZWE1MmI4YzM3MTNjNjI0MDd8ZjI2MzYwZTA2ZWVkODg0Y2ZlNjZlZTBlNzVhZDM1OWY="
NORMAL_TOKEN = "NzN8OGZmZmQ0N2UyNWY1NTY5ZWFhYWNjMzA5OGRiNDcxOTZ8YThmOWM3Nzg2NTM3YzVmMzMzNzY0MTI1NWM4MmZlNzU="
# NORMAL_TOKEN = "NzB8OGMzYzZkYzVhMTQzNWRmOWEyODliMGMzMDMwYjIwYWN8MWFiNzE4ODA1YzczMjhmZTgxNzdlMmU4MTA3MmJjYjE="
COUNTRY_DOMAIN =  {
    "us" : "https://api.mecordai.com/proxymsg",
    "sg" : "https://api-sg.mecordai.com/proxymsg"
}

def supportCountrys(isProduct):
    if isProduct:
        return ["US", "SG"]
    else:
        return ["test"]
    
def real_token():
    if store.is_product():
        return OFFICIAL_PRODUCT_TOKEN
    else:
        tk = store.token()
        if tk == OFFICIAL_PRODUCT_TOKEN:
            tk = NORMAL_TOKEN
        return tk

def _aigc_post_product(country, request, function, objStr="mecord.aigc.AigcExtObj"):
    domain = COUNTRY_DOMAIN["us"]
    if country.lower() in COUNTRY_DOMAIN:
        domain = COUNTRY_DOMAIN[country.lower()]
    return _post(url=domain, 
                 objStr=objStr, 
                 request=request, 
                 function=function,
                 token=OFFICIAL_PRODUCT_TOKEN)
def _aigc_post(request, function, objStr="mecord.aigc.AigcExtObj"):
    tk = store.token()
    if tk == OFFICIAL_PRODUCT_TOKEN:
        tk = NORMAL_TOKEN 
    return _post(url="https://mecord-beta.2tianxin.com/proxymsg", 
                 objStr=objStr, 
                 request=request, 
                 function=function,
                 token=tk)

def _post(url, objStr, request, function, token):
    req = request.SerializeToString()
    opt = {
        "lang": "zh-Hans",
        "region": "CN",
        "appid": "80",
        "application": "mecord",
        "version": "1.0",
        "X-Token": token,
        "uid": "1",
    }
    input_req = rpcinput_pb2.RPCInput(obj=objStr, func=function, req=req, opt=opt)
    try:
        res_content = xy_network.post(url, input_req.SerializeToString())
        pb_rsp = rpcinput_pb2.RPCOutput()
        pb_rsp.ParseFromString(res_content)
        if pb_rsp.ret == 0:
            return 0, "", pb_rsp.rsp
        else:
            taskUtils.taskPrint(None, f'''=============== request err_code={pb_rsp.ret} err_desc={pb_rsp.desc} {datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')} {"product" if store.is_product() else "test"} ===============
url={url}
func={function}
token={token}

req=
{request}
respose=
{res_content}
===============
''')
            return pb_rsp.ret, pb_rsp.desc, "" 
    except Exception as e:
        taskUtils.taskPrint(None, f'''=============== mecord server error {datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')} {"product" if store.is_product() else "test"} ===============
url={url}
func={function}
token={token}

req=
{request}
exception={e}
===============
''')
        return -99, str(e), ""
    
#======================================== Task Function ==============================
def _extend():
    extInfo = store.readDeviceInfo()
    extInfo["app_version"] = constant.app_version
    extInfo["app_bulld_number"] = constant.app_bulld_number
    extInfo["app_name"] = constant.app_name
    extInfo["dts"] = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')
    extInfo["trace_id"] = ''.join(str(uuid.uuid4()).split('-'))
    extInfo["host_name"] = utils.get_hostname()
    return json.dumps(extInfo)

def GetTask(country):
    req = aigc_ext_pb2.GetTaskReq()
    req.version = constant.app_version
    req.DeviceKey = utils.generate_unique_id()
    map = store.widgetMap()
    for it in map:
        if isinstance(map[it], (dict)):
            if map[it]["isBlock"] == False:
                req.widgets.append(it)
        else:
            req.widgets.append(it)
    req.token = real_token()
    req.limit = store.multitaskNum()
    req.extend = _extend()
    req.apply = False
    
    rsp = aigc_ext_pb2.GetTaskRes()
    if store.is_product():
        r1, r2, r3 = _aigc_post_product(country, req, "GetTask")
    else:
        r1, r2, r3 = _aigc_post(req, "GetTask")
    if r1 != 0:
        return [], 10
    rsp.ParseFromString(r3)
    datas = []
    for it in rsp.list:
        datas.append({
            "taskUUID": it.taskUUID,
            "pending_count": rsp.count - rsp.limit,
            "config": it.config,
            "data": it.data,
        })
    #Previous tasks may have failed due to network problems, so collect and resend
    retryLastTaskNotify()
    return datas, rsp.timeout

TASK_NOTIFY_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"task_notify_data.json")
def saveTaskNotifyData(country, taskUUID, status, msg, dataStr):
    taskUtils.taskPrint(taskUUID, f"save {taskUUID} to next notify")
    try:
        if not os.path.exists(TASK_NOTIFY_DATA):
            with open(TASK_NOTIFY_DATA, 'w') as f:
                json.dump([], f)
        with open(TASK_NOTIFY_DATA, 'r') as f:
            data = json.load(f)
        data.append({
            "taskUUID":taskUUID,
            "status":status,
            "country":country,
            "msg":msg,
            "dataStr":dataStr
        })
        with open(TASK_NOTIFY_DATA, 'w') as f:
            json.dump(data, f)
    finally:
        return
def resetLastTaskNotify(taskUUID):
    try:
        if os.path.exists(TASK_NOTIFY_DATA):
            with open(TASK_NOTIFY_DATA, 'r') as f:
                data = json.load(f)
            newData = []
            for it in data:
                if it["taskUUID"] != taskUUID:
                    newData.append(it)
            with open(TASK_NOTIFY_DATA, 'w') as f:
                json.dump(newData, f)
    finally:
        return
def retryLastTaskNotify():
    try:
        if os.path.exists(TASK_NOTIFY_DATA):
            with open(TASK_NOTIFY_DATA, 'r') as f:
                data = json.load(f)
            newData = []
            for it in data:
                msg = it["msg"]
                counrty = "US"
                if "country" in it:
                    counrty = it["country"]
                if TaskNotify(counrty, it["taskUUID"], it["status"], f"{msg} *", it["dataStr"]) == False:
                    newData.append(it)
            with open(TASK_NOTIFY_DATA, 'w') as f:
                json.dump(newData, f)
    finally:
        return

def TaskNotify(country, taskUUID, status, msg, dataStr):
    req = aigc_ext_pb2.TaskNotifyReq()
    req.version = constant.app_version
    req.taskUUID = taskUUID
    if status:
        req.taskStatus = common_ext_pb2.TaskStatus.TS_Success
    else:
        req.taskStatus = common_ext_pb2.TaskStatus.TS_Failure
    req.failReason = msg
    req.data = dataStr
    req.extend = _extend()
    
    rsp = aigc_ext_pb2.TaskNotifyRes()
    service_country = "test"
    if store.is_product():
        service_country = "US"
        r1, r2, r3 = _aigc_post_product(country, req, "TaskNotify")
    else:
        r1, r2, r3 = _aigc_post(req, "TaskNotify")
    if r1 != 0:
        #tasks may have failed due to network problems, so collect and resend
        saveTaskNotifyData(country, taskUUID, status, msg, dataStr)
        return False
    rsp.ParseFromString(r3)
    taskUtils.taskPrint(taskUUID, f"receive server {rsp.ok} notify_id = {rsp.notify_id}")
    if len(rsp.notify_id) == 0:
        #tasks may have failed due to network problems, so collect and resend
        saveTaskNotifyData(country, taskUUID, status, msg, dataStr)
    ok = rsp.ok == True
    if ok:
        taskUtils.taskPrint(taskUUID, f" task : {taskUUID} notify server success")
    else:
        taskUtils.taskPrint(taskUUID, f" task : {taskUUID} server fail~~")
        taskUtils.notifyServerError(taskUUID, service_country)
    return ok

    
def TaskUpdateProgress(country, taskUUID, progress, dataStr):
    req = aigc_ext_pb2.TaskUpdateReq()
    req.taskUUID = taskUUID
    req.progress = progress
    req.data = dataStr
    
    rsp = aigc_ext_pb2.TaskUpdateRes()
    if store.is_product():
        r1, r2, r3 = _aigc_post_product(country, req, "TaskUpdate")
    else:
        r1, r2, r3 = _aigc_post(req, "TaskUpdate")
    if r1 != 0:
        return False
    rsp.ParseFromString(r3)
    return True

def GetOssUrl(country, ext):
    req = aigc_ext_pb2.UploadFileUrlReq()
    req.token = real_token()
    req.version = constant.app_version
    req.fileExt = ext

    rsp = aigc_ext_pb2.UploadFileUrlRes()
    if store.is_product():
        r1, r2, r3 = _aigc_post_product(country, req, "UploadFileUrl")
    else:
        r1, r2, r3 = _aigc_post(req, "UploadFileUrl")
    if r1 != 0:
        return "", r2
    rsp.ParseFromString(r3)
    return rsp.url, rsp.contentType

def UploadMarketModel(country, name, cover, model_url, type, taskuuid):
    req = aigc_ext_pb2.MarketModelCreateWithTaskReq()
    req.name = name
    req.cover = cover
    req.url = model_url
    req.type = type
    req.TaskUUID = taskuuid

    rsp = aigc_ext_pb2.MarketModelCreateWithTaskRes()
    if store.is_product():
        r1, r2, r3 = _aigc_post_product(country, req, "MarketModelCreateWithTask")
    else:
        r1, r2, r3 = _aigc_post(req, "MarketModelCreateWithTask")
    if r1 != 0:
        return 0
    rsp.ParseFromString(r3)
    return True

#======================================== Other Function ==============================
def DeviceUnbind():
    req = aigc_ext_pb2.AigcDeviceUnBindReq()
    req.deviceToken = store.token()

    rsp = aigc_ext_pb2.AigcDeviceUnBindRes()
    r1, r2, r3 = _aigc_post(req, "DeviceUnBind")
    if r1 != 0:
        return False
    rsp.ParseFromString(r3)
    return False

def GetAigcDeviceInfo():
    req = aigc_ext_pb2.AigcDeviceInfoReq()
    req.version = constant.app_version
    req.deviceKey = utils.generate_unique_id()
    extInfo = store.readDeviceInfo()
    extInfo["app_version"] = constant.app_version
    extInfo["app_bulld_number"] = constant.app_bulld_number
    extInfo["app_name"] = constant.app_name
    req.extend = json.dumps(extInfo)

    rsp = aigc_ext_pb2.AigcDeviceInfoRes()
    r1, r2, r3 = _aigc_post(req, "DeviceInfo")
    if r1 != 0:
        if r1 != 11000:
            print(f'get DeviceInfo failed: {r1} {r2}')
        return False
    rsp.ParseFromString(r3)
    
    if len(rsp.groupUUID) > 0:
        sp = store.Store()
        data = sp.read()
        data["groupUUID"] = rsp.groupUUID
        data["token"] = rsp.token
        if rsp.isCreateWidget == True:
            data["isCreateWidget"] = rsp.isCreateWidget
        sp.write(data)
        return True
    return False

def GetSystemConfig(country, k):
    req = user_ext_pb2.SystemConfigReq()
    req.key = k

    rsp = user_ext_pb2.SystemConfigRes()
    if store.is_product():
        r1, r2, r3 = _aigc_post_product(country, req, "GetSystemConfig", "mecord.user.UserExtObj")
    else:
        r1, r2, r3 = _aigc_post(req, "GetSystemConfig", "mecord.user.UserExtObj")
    if r1 != 0:
        return None
    rsp.ParseFromString(r3)
    
    if rsp.key == k:
        return rsp.value
    else:
        return None

def CreateWidgetUUID():
    req = aigc_ext_pb2.ApplyWidgetReq()
    rsp = aigc_ext_pb2.ApplyWidgetRes()
    r1, r2, r3 = _aigc_post(req, "ApplyWidget")
    if r1 != 0:
        return ""
    rsp.ParseFromString(r3)
    return rsp.widgetUUID

def DeleteWidget(widgetid):
    req = aigc_ext_pb2.DeleteAigcWidgetReq()
    req.widgetUUID = widgetid
    req.deviceToken = store.token()
    rsp = aigc_ext_pb2.DeleteAigcWidgetRes()
    r1, r2, r3 = _aigc_post(req, "DeleteWidget")
    if r1 != 0:
        return False
    rsp.ParseFromString(r3)
    return True

def GetTaskCount(widgetid):
    req = aigc_ext_pb2.TaskCountReq()
    req.deviceToken = store.token()
    rsp = aigc_ext_pb2.TaskCountRes()
    r1, r2, r3 = _aigc_post(req, "TaskCount")
    if r1 != 0:
        return []
    rsp.ParseFromString(r3)
    datas = []
    for it in rsp.items:
        datas.append({
            "widgetUUID": it.widgetUUID,
            "taskCount": it.taskCount
        })
    return datas

def RemoteWidgetList(widgetid):
    req = aigc_ext_pb2.AigcWidgetListReq()
    req.deviceToken = store.token()
    rsp = aigc_ext_pb2.AigcWidgetListRes()
    r1, r2, r3 = _aigc_post(req, "WidgetList")
    if r1 != 0:
        return []
    rsp.ParseFromString(r3)
    datas = []
    for it in rsp.items:
        datas.append({
            "uuid": it.uuid,
            "name": it.name,
            "updated_at": it.updated_at,
        })
    return datas

def ExpansionWithToken(token):
    req = aigc_ext_pb2.AigcDeviceExpansionReq()
    req.DeviceToken = token
    req.DeviceKey = utils.generate_unique_id()

    rsp = aigc_ext_pb2.AigcDeviceExpansionRes()
    r1, r2, r3 = _aigc_post(req, "DeviceExpansion")
    if r1 == 11000:
        return False, r1
    elif r1 != 0:
        return ""
    rsp.ParseFromString(r3)

    if len(rsp.groupUUID) > 0:
        sp = store.Store()
        data = sp.read()
        data["groupUUID"] = rsp.groupUUID
        data["token"] = rsp.deviceToken
        sp.write(data)
        return True, 0
    return False, -1
   
def GetWidgetOssUrl(widgetid):
    req = aigc_ext_pb2.UploadWidgetUrlReq()
    req.version = constant.app_version
    req.widgetUUID = widgetid

    rsp = aigc_ext_pb2.UploadWidgetUrlRes()
    r1, r2, r3 = _aigc_post(req, "UploadWidgetUrl")
    if r1 != 0:
        return "", ""
    rsp.ParseFromString(r3)
    return rsp.url, rsp.contentType

def WidgetUploadEnd(url):
    req = aigc_ext_pb2.UploadWidgetReq()
    req.version = constant.app_version
    req.fileUrl = url
    
    rsp = aigc_ext_pb2.UploadWidgetRes()
    r1, r2, r3 = _aigc_post(req, "UploadWidget")
    if r1 != 0:
        return 0
    rsp.ParseFromString(r3)
    return rsp.checkId
    
def UploadWidgetCheck(checkId):
    req = aigc_ext_pb2.UploadWidgetCheckReq()
    req.version = constant.app_version
    req.checkId = checkId

    rsp = aigc_ext_pb2.UploadWidgetCheckRes()
    r1, r2, r3 = _aigc_post(req, "UploadWidgetCheck")
    if r1 != 0:
        return 0
    rsp.ParseFromString(r3)
    if rsp.status == aigc_ext_pb2.UploadWidgetStatus.UWS_SUCCESS:
        return 1
    elif rsp.status == aigc_ext_pb2.UploadWidgetStatus.UWS_FAILURE:
        print(f"widget pulish fail msg => {rsp.failReason}")
        return 0
    else:
        return -1
    
#======================================== Task Function ==============================
def createTask(country, widget_id, params):
    req = aigc_ext_pb2.CreateTaskReq()
    req.taskType = 0
    req.labelType = common_ext_pb2.LT_Public#LT_NONE
    req.labelValue = 1
    req.user_id = 1
    req.widget_id = widget_id
    req.widget_data = json.dumps(params)
    req.parentTaskId = 0

    rsp = aigc_ext_pb2.CreateTaskRes()
    if store.is_product():
        r1, r2, r3 = _aigc_post_product(country, req, "CreateTask")
    else:
        r1, r2, r3 = _aigc_post(req, "CreateTask")
    if r1 != 0:
        raise Exception(f"create task fail!, reason={r2}")
    rsp.ParseFromString(r3)
    return rsp.taskUUID

def findWidget(country, name):
    req = aigc_ext_pb2.WidgetOptionReq()
    rsp = aigc_ext_pb2.WidgetOptionRes()
    if store.is_product():
        r1, r2, r3 = _aigc_post_product(country, req, "WidgetOption")
    else:
        r1, r2, r3 = _aigc_post(req, "WidgetOption")
    if r1 != 0:
        return 0
    rsp.ParseFromString(r3)
    for it in rsp.items:
        widget_id = it.id
        widget_name = it.name
        if widget_name.strip().lower() == name.strip().lower():
            return widget_id
    return 0

def checkTask(country, checkUUID):
    req = aigc_ext_pb2.TaskInfoReq()
    req.taskUUID = checkUUID
    req.findTaskResult = True

    rsp = aigc_ext_pb2.TaskInfoRes()
    if store.is_product():
        r1, r2, r3 = _aigc_post_product(country, req, "TaskInfo")
    else:
        r1, r2, r3 = _aigc_post(req, "TaskInfo")
    if r1 != 0:
        return False, False, "server fail"
    rsp.ParseFromString(r3)
    if rsp.taskStatus < 3:
        return False, False, ""
    elif rsp.taskStatus == 3:
        return True, True, json.loads(rsp.taskResult)
    elif rsp.taskStatus == 4:
        return True, False, rsp.failReason