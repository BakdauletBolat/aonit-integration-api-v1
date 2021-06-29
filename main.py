from win32com.client.dynamic import Dispatch
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET

import datetime

oPERCo = Dispatch("PERCo_S20_SDK.ExchangeMain")

def connectServer():
    Host = "127.0.0.1"
    Port = "211"
    Login = "ADMIN"
    Pass = "123456qA"
    iRet = oPERCo.SetConnect(Host, Port, Login, Pass)

    return iRet

print(connectServer())