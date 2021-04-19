
from win32com.client.dynamic import Dispatch
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET


oPERCo = Dispatch("PERCo_S20_SDK.ExchangeMain")

def connectServer():
    Host = "127.0.0.1"
    Port = "211"
    Login = "Admin"
    Pass = "123456qA"
    iRet = oPERCo.SetConnect(Host, Port, Login, Pass)

    return iRet

def loadEvents():
    events = []
    connectServer()
    domEvent = Dispatch('Msxml2.DOMDocument.6.0')
    domEvent.load('getEventsMain.xml')
    oPERCo.GetData(domEvent)
    b = domEvent.save('getEvents.xml')
    root_node = ET.parse('getEvents.xml').getroot()
    for tag in root_node.findall("eventsreport/events/event"): 
        f_name_resource = tag.get('f_name_resource')
        f_name_ev = tag.get('f_name_ev')
        f_name_obj = tag.get('f_name_obj')
        f_name_subdiv = tag.get('f_name_subdiv')
        f_name_appoint = tag.get('f_name_appoint')
        f_fio = tag.get('f_fio')
        f_date_ev = tag.get('f_date_ev')
        f_time_ev = tag.get('f_time_ev')
        f_identifier = tag.get('f_identifier')
        f_unic_id = f_name_subdiv+f_date_ev+f_time_ev+f_identifier

        
        event = {
            'f_name_resource':f_name_resource,
            'f_name_ev':f_name_ev,
            'f_name_obj':f_name_obj,
            'f_name_subdiv':f_name_subdiv,
            'f_name_appoint':f_name_appoint,
            'f_fio':f_fio,
            'f_time_ev':f_time_ev,
            'f_identifier':f_identifier,
            'f_date_ev':f_date_ev,
            'f_unic_id':f_unic_id
        }
        events.append(event)
    
    return events


def loadStaff():
    staffs = []
    connectServer()
    doc = minidom.Document()
    dom = Dispatch('Msxml2.DOMDocument.6.0')
    dom.load('main.xml')
    oPERCo.GetData(dom)
    b = dom.save('getstaff.xml')
    root_node = ET.parse('getstaff.xml').getroot()
    for tag in root_node.findall("staff/staffnode"): 
        first_name = tag.get("first_name") 
        last_name = tag.get('last_name')
        middle_name = tag.get('middle_name')
        staff = {
            'first_name': first_name,
            'last_name':last_name,
            'middle_name':middle_name,
        }
        staffs.append(staff)
    
    return staffs

def loadUnits():
    units = []
    connectServer()
    doc = minidom.Document()
    dom = Dispatch('Msxml2.DOMDocument.6.0')
    dom.load('getSubDiv.xml')
    oPERCo.GetData(dom)
    b = dom.save('loadSubDiv.xml')
    root_node = ET.parse('loadSubDiv.xml').getroot()
    for tag in root_node.findall("subdiv/subdivnode"): 
        displayname = tag.get("displayname") 
        staff = {
            'first_name': first_name,
            'last_name':last_name,
            'middle_name':middle_name,
        }
        units.append(staff)
    
    return units


