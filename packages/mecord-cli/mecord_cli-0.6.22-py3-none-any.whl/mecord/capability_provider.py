import sys
import os
from mecord.public_tools.decorator_tools import singleton
from mecord import xy_user
from mecord import mecord_service
from mecord import mecord_widget
from mecord import store
from mecord import utils
from mecord import taskUtils
from mecord import xy_pb

from pkg_resources import get_distribution
import threading


@singleton
class CapabilityProvider:

    def __init__(self):
        self.max_check_device_count = 300  # loop waiting 5min
        self.cur_check_device_count = 0

    def service(self):
        if len(sys.argv) <= 2:
            print('please set command!')
            utils.show_help()
            return

        command = sys.argv[2]
        service = mecord_service.MecordService()
        if command == 'start':
            if xy_user.User().isLogin() == False:
                print('please login first! \nUsage: mecord deviceid & Use Mecord Application scan it')
                utils.show_help()
                return
            wid_map = store.widgetMap()
            if len(wid_map) == 0:
                print("please add widget first!")
                utils.show_help()
                return
            if service.is_running():
                print('Service is already running.')
            else:
                print(f'Starting service...[args = {" ".join(sys.argv)}]')
                isProduct = False
                threadNum = 1
                idx = 2      
                while idx < len(sys.argv):
                    if sys.argv[idx] == "-thread":
                        threadNum = int(sys.argv[idx+1])
                        if threadNum < 1 or threadNum > 500:
                            print('multi thread number must be 1~500')
                            return
                    if sys.argv[idx] in ["prod","product"]:
                        isProduct = True
                    idx+=1
                service.start(isProduct, threadNum)
        elif command == 'stop':
            if not service.is_running():
                print('Service is not running.')
            else:
                print('Stopping service...')
                service.stop()
        elif command == 'status': 
            runningStr = "Service is not running."
            env = ""        
            if service.is_running():
                runingTask = taskUtils.getCurrentTask()
                runningStr = 'Service is running.'
                threadNum = store.get_multithread()
                if threadNum > 1:
                    runningStr += f"[thread={threadNum}]"
                if len(runingTask) > 0:
                    runningStr += f'\n\nProcessing {runingTask}'
                else:
                    runningStr += f'\n\nWaiting Task...'
                env = " test"
                if store.is_product():
                    env = ' product'
            receiveWidget = ""
            map = store.widgetMap()
            for it in map:
                is_block = False
                if isinstance(map[it], (dict)):
                    is_block = map[it]["isBlock"]
                if is_block == False:
                    receiveWidget += f", {it}"
            receiveWidget = receiveWidget[1:]
            if len(receiveWidget) > 0:
                runningStr += f'\n\nreceive{env} widget is [{receiveWidget} ]'
                
            print(runningStr)
        else:
            print("Unknown command:", command)
            utils.show_help()

    def widget(self):
        if xy_user.User().isLogin() == False:
            print('please login first! \nUsage: mecord deviceid & Use Mecord Application scan it')
            return
        if len(sys.argv) <= 2:
            print('please set command! Usage: mecord widget [init|publish]')
            return

        command = sys.argv[2]
        work_path = os.getcwd()
        if len(sys.argv) > 3:
            work_path = sys.argv[3]
        if command == 'init':
            mecord_widget.createWidget(work_path)
        elif command == 'publish':
            mecord_widget.publishWidget(work_path)
        elif command == 'list':
            map = store.widgetMap()
            if len(map) == 0:
                print("local widget is empty")
            maxJust = 20
            for it in map:
                if len(it) > maxJust:
                    maxJust = len(it)
            maxJust += 10
            showStatus = ""
            if len(sys.argv) > 3:
                showStatus = sys.argv[3]
            for it in map:
                path = ""
                is_block = False
                if isinstance(map[it], (dict)):
                    path = map[it]["path"]
                    is_block = map[it]["isBlock"]
                else:
                    path = map[it]
                end_args = ""
                if is_block:
                    end_args = " [X]"
                ss = f"{it}{end_args}"
                if showStatus in ["disable", "enable"]:
                    if is_block and showStatus == "disable":
                        print(f'{ss.ljust(maxJust + 4)} {path}')
                    elif is_block == False and showStatus == "enable":
                        print(f'{ss.ljust(maxJust + 4)} {path}')
                else:
                    print(f'{ss.ljust(maxJust + 4)} {path}')
        elif command == 'add':
            mecord_widget.addWidgetToEnv(work_path)
        elif command == 'remove':
            mecord_widget.remove(work_path)
        elif command == 'enable':
            mecord_widget.enable(work_path)
        elif command == 'disable':
            mecord_widget.disable(work_path)
        elif command == 'pending_task':
            mecord_widget.getTaskCount(work_path)
        else:
            print("Unknown command:", command)
            utils.show_help()

    def checkDeviceInfo(self):
        if self.cur_check_device_count > self.max_check_device_count:
            return
        if xy_pb.GetAigcDeviceInfo():
            if store.isCreateWidget():
                mecord_widget.createDemoWidget()
        else:
            self.cur_check_device_count += 1
            threading.Timer(1, self.checkDeviceInfo, ()).start()

    def unbind(self):
        xy_pb.DeviceUnbind()
        # store.clear() #do not clear local data
        print(f"your device is return to initialization state!")

    def deviceid(self):
        store.writeDeviceInfo(utils.deviceInfo())
        xy_user.User().loginIfNeed()
        uuid = utils.generate_unique_id()
        qrcode_str = f"https://main_page.html?action=scanbind&deviceId={uuid}"
        utils.displayQrcode(qrcode_str)
        print(f"deviceid    : {uuid}")
        print(f"scan-qrcode : {qrcode_str}")
        if xy_user.User().isLogin() == False:
            print(f"waiting for scan...")
        self.cur_check_device_count = 0
        self.checkDeviceInfo()

    def joinToken(self):
        if len(sys.argv) <= 2:
            print('can not found token! Usage: mecord add_token {token}')
            return
        service = mecord_service.MecordService()
        if service.is_running():
            print('Service is running, stop service and continue')
            return
        success, errCode = xy_pb.ExpansionWithToken(sys.argv[2])
        if success:
            print('joinToken success')
        else:
            if errCode == 11000:
                #device id bined, get device token once, and retry join token
                xy_user.User().loginIfNeed()
                success, errCode = xy_pb.ExpansionWithToken(sys.argv[2])
                if success:
                    print('joinToken success')
                else:
                    print(f'joinToken fail! errCode = {errCode}')

    def showToken(self):
        t = store.token()
        if len(t) > 0:
            print(f"your token is : {t}")
            utils.displayQrcode(t)
        else:
            print(f"not have token")

    def setMultitaskNum(self):
        if len(sys.argv) <= 2:
            print('please set multitasking number')
            return
        if sys.argv[2].isdigit() == False:
            print('multitasking number is not digit')
            return
        if sys.argv[2] < 1:
            print(f'multitasking number illegal, {sys.argv[2]} must be greater than 1')
            return
        store.setMultitaskNum(sys.argv[2])
        print(f"multitasking number is {sys.argv[2]}")

    def getMultitaskNum(self):
        t = store.multitaskNum()
        print(f"multitasking number is {t}")

    def report(self):
        utils.reportLog()
        print(f"report success")

    def version(self):
        ver = get_distribution("mecord-cli").version
        print(f"version is {ver}")

    def handle_action(self, str_n):
        if str_n == "widget":
            self.widget()
        elif str_n == "service":
            self.service()
        elif str_n == "deviceid":
            self.deviceid()
        elif str_n == "unbind":
            self.unbind()
        elif str_n == "show_token":
            self.showToken()
        elif str_n == "add_token":
            self.joinToken()
        elif str_n == "set_multitask_num":
            self.setMultitaskNum()
        elif str_n == "get_multitask_num":
            self.getMultitaskNum()
        elif str_n == "report":
            self.report()
        elif str_n == "version":
            self.version()
        else:
            utils.show_help()

