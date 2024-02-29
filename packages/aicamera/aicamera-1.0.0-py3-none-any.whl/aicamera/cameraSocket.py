'''
Date: 2024-02-18 15:37:29
author: zjs
'''
import asyncio
import websockets
import socket
import util
import json
import udp
# 摄像头业务 socket 端口号
CAMERA_WS_PORT = 55555

# 摄像头业务socket
cameraServiceSocket = None

# 客户端业务socket
clientServiceSocket = None


# 改成两个客户端 通讯代理
'''
Date: 2024-02-18 15:46:25
author: zjs
description:获取摄像头业务 sokect
'''


async def runCameraSocket(cameraIp):
    print(cameraIp, '摄像头ip')
    if cameraIp is None:
        print('摄像头ip不存在 runCameraSocket')
        return
    global cameraServiceSocket, clientServiceSocket
    try:
        cameraServiceSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cameraServiceSocket.connect((cameraIp, CAMERA_WS_PORT))
        print('摄像头连接成功')
        while True:
            serverMsg = cameraServiceSocket.recv(1024)
            print(serverMsg, '来自摄像头的消息，转发给客户端', '='*10)
            await clientServiceSocket.send(serverMsg)
            await asyncio.sleep(0.05)
    except Exception as e:
        print('gewu sokect 读写错误1', e)


'''
Date: 2024-02-19 17:43:27
author: zjs
description:  启动 socket 接口(http) 服务
'''


async def runSocketApi(sokectPort):
    async with websockets.connect(f'ws://127.0.0.1:{sokectPort}') as cilentWs:
        global cameraServiceSocket, clientServiceSocket
        clientServiceSocket = cilentWs
        try:
            while True:
                # # 50ms接收数据
                clientMsg = await cilentWs.recv()
                if not clientMsg or clientMsg == 'jump':
                    continue
                # key value
                jsonResult = json.loads(clientMsg)
                print(jsonResult, '来自客户端消息', '*'*10)
                key, value = jsonResult['key'], jsonResult['value']
                config = {
                    'useMode': lambda: use_mode(),
                    'reTrain': lambda: __reTrain(),
                    'get_res': lambda: get_res(),
                    'getRtspUrl': lambda: __getRtspUrl()
                }
                activeMethod = config[key]
                if activeMethod:
                    activeMethod(value)
                await asyncio.sleep(0.05)
        except Exception as e:
            print('gewu sokect 读写错误2', e)

# 模型cmd
modeType = {
    'face_detect': 0x01,  # 人脸检测
    'traffic_sign': 0x02,  # 交通标志
    'qr_code': 0x03,  # 二维码
    'bar_code': 0x04,  # 条形码
    'face_recognition': 0x05,  # 人脸识别
    'classify': 0x06,  # 分类
    'gesture': 0x07,  # 手势
    'car_number': 0x08,  # 车牌
    'trace': 0x09,  # 物体追踪
}


'''
Date: 2024-02-22 11:58:38
author: zjs
description: 设置算法使用
'''


def use_mode(mode):
    if not any(el == mode for el in list(modeType.keys())):
        return print(f'没有 {mode} 模式')
    cmd = 0x01
    cameraServiceSocket.sendall(
        util.genSendPack(cmd, modeType[mode], 0x00))


'''
Date: 2024-02-22 11:58:38
author: zjs
description: 重新训练模型
'''


def __reTrain(val):
    mode, url = val['mode'], val['url']
    if not any(el == mode for el in [
        modeType['classify'],
        modeType['face_detect']
    ]):
        return print(f'没有 {mode} 模式')
    cmd = 0x02
    cameraServiceSocket.sendall(
        util.genSendPack(cmd, modeType[mode], url))


'''
Date: 2024-02-22 13:55:46
author: zjs
description: 获取识别结果 [(x,y,w,h,p,result)]
0x00 结果
0x01 标签
'''

resultType = {
    'result': 0x00,  # 结果
    '其他都是对应模型标签': 0x01,  # 标签
}


def get_res():
    cmd = 0x03
    cameraServiceSocket.sendall(
        util.genSendPack(cmd, resultType['result'], 0x00))


'''
Date: 2024-02-23 18:56:47
author: zjs
description: 获取人脸标签
'''


def get_face_tags():
    cmd = 0x03
    cameraServiceSocket.sendall(
        util.genSendPack(cmd, modeType['face_detect'], 0x00))


'''
Date: 2024-02-23 18:56:47
author: zjs
description: 获取分类标签
'''


def get_class_tags():
    cmd = 0x03
    cameraServiceSocket.sendall(
        util.genSendPack(cmd, modeType['classify'], 0x00))


'''
Date: 2024-02-22 17:41:35
author: zjs
description: 获取rtsp 地址
'''


async def __getRtspUrl():
    await clientServiceSocket.send(udp.getRtspUrl().encode())
    await asyncio.sleep(0.05)
