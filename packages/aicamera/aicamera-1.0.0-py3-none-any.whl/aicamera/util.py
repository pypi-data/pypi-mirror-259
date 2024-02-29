import http.server
import threading
import socket
import random
import zipfile
import time
import os
import sys


'''
Date: 2024-02-21 18:15:26
author: zjs
description: 校验端口是否被占用
'''


def checkPort(port, host='localhost'):
    s = socket.socket()
    try:
        s.connect((host, port))
        return True
    except Exception as e:
        e
        return False
    finally:
        s.close()


'''
Date: 2024-02-21 18:24:21
author: zjs
description: 随机生成一个端口
'''


def randomPort():
    port = random.randint(10000, 49000)
    return port if not checkPort(port) else randomPort()


'''
Date: 2024-02-21 18:02:48
author: zjs
description: 创建静态资源服务器的线程内部方法
'''


def __creatStaticServer(CUSTOM_DIRECTORY):
    # 指定静态文件目录
    DIRECTORY = CUSTOM_DIRECTORY if CUSTOM_DIRECTORY else './'

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

    PORT = randomPort()
    HOST = "127.0.0.1"
    # 直接启动服务器
    with http.server.HTTPServer((HOST, PORT), CustomHandler) as server:
        print(f"静态资源资源服务器启动在http://{HOST}:{PORT}, 资源路径为{DIRECTORY}")
        server.serve_forever()


'''
Date: 2024-02-21 18:02:48
author: zjs
description: 创建静态资源服务器
'''


def creatStaticServer(path=None):
    threading.Thread(target=__creatStaticServer, args=(path,)).start()


'''
Date: 2024-02-21 18:36:13
author: zjs
description: 指定路径生成zip
'''


def genZipByDirOrFile(path, name=str(time.time())+'.zip'):
    if not os.path.exists(path):
        return print('文件不存在')
    zipObj = zipfile.ZipFile(name, 'w')
    zipObj.write(path, compress_type=zipfile.ZIP_DEFLATED)
    zipObj.close()
    return name


'''
Date: 2024-02-23 11:42:47
author: zjs
description: 包装发送数据包
'''


def genSendPack(cmd, subcmd, data):
    dataLen = len(data)
    packLen = dataLen + 4
    head = [0x7e, 0x7e]
    end = [0xee, 0xee]
    result = head+[packLen, cmd, subcmd,
                   packLen]+[data]+end
    return ''.join(result)


'''
Date: 2024-01-11 19:16:55
author: zjs
description: 获取终端参数
'''


def getArg(key='---sokectPort'):
    for i, arg in enumerate(sys.argv):
        if (arg.startswith(key)):
            port = arg.split('=')
            return port[1]
