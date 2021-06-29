
from win32com.client.dynamic import Dispatch
import xml.etree.ElementTree as ET
import datetime

oPERCo = Dispatch("PERCo_S20_SDK.ExchangeMain")
domEvent = Dispatch('Msxml2.DOMDocument.6.0')

def createEventXml(xmlFileName):
    dataS = datetime.date.today()
    requestType = ET.Element('documentrequest')

    beginperiod = f'{dataS.day}.{dataS.month-5}.{dataS.year}'
    endinperiod = f'{dataS.day}.{dataS.month-5}.{dataS.year}'

    beginperiodtime = '00:00:00'
    endperiodtime = '23:50:00'

    requestType.set('type','regevents')
    eventsreportSub = ET.SubElement(requestType,'eventsreport')
    eventsreportSub.set('beginperiod',beginperiod)
    eventsreportSub.set('endperiod',endinperiod)
    eventsreportSub.set('beginperiodtime',beginperiodtime)
    eventsreportSub.set('endperiodtime',endperiodtime)
    mydata = ET.tostring(requestType,encoding='unicode')
    myfile = open(xmlFileName,'w')
    myfile.write(mydata)

def connectServer():
    Host = "127.0.0.1"
    Port = "211"
    Login = "ADMIN"
    Pass = "123456qA"
    iRet = oPERCo.SetConnect(Host, Port, Login, Pass)

    return iRet


def loadEvents():
    events = []
    connectServer()
    createEventXml('getEventsMain.xml')
    domEvent.load('getEventsMain.xml')
    oPERCo.GetData(domEvent)
    domEvent.save('getEvents.xml')
    root_node = ET.parse('getEvents.xml').getroot()
    for tag in root_node.findall("eventsreport/events/event"): 
        f_areas_nameN = tag.get('f_areas_name')
        if f_areas_nameN == "Неконтролируемая территория":
            f_areas_name = "0"
        else:
            f_areas_name = "1"
        f_name_ev = tag.get('f_name_ev')
        f_subdiv_id_internal = tag.get('f_subdiv_id_internal')
        f_fio = tag.get('f_fio')
        f_date_ev = tag.get('f_date_ev')
        f_time_ev = tag.get('f_time_ev')
        f_identifier = tag.get('f_identifier')
        f_unic_id = f_subdiv_id_internal+f_date_ev+f_time_ev+f_identifier
        event = {
            'f_areas_name':f_areas_name,
            'f_name_ev':f_name_ev,
            'f_subdiv_id_internal':f_subdiv_id_internal,
            'f_fio':f_fio,
            'f_time_ev':f_time_ev,
            'f_identifier':f_identifier,
            'f_date_ev':f_date_ev,
            'f_unic_id':f_unic_id
        }
        if f_name_ev == 'Проход':
            events.append(event)
    
    return events


def loadTest():
    events = []
    connectServer()
    createEventXml('getEventsMain.xml')
    domEvent.load('getEventsMain.xml')
    oPERCo.GetData(domEvent)
    domEvent.save('getEvents.xml')
    root_node = ET.parse('getEvents.xml').getroot()
    for tag in root_node.findall("eventsreport/events/event"):
        f_areas_nameN = tag.get('f_areas_name')
        if f_areas_nameN == "Неконтролируемая территория":
            f_areas_name = "0"
        else:
            f_areas_name = "1"

        f_name_ev = tag.get('f_name_ev')
        f_fio = tag.get('f_fio')
        f_date_ev = tag.get('f_date_ev')
        f_time_ev = tag.get('f_time_ev')
        f_identifier = tag.get('f_identifier')

        event = {
            'f_areas_name': f_areas_name,
            'f_name_ev': f_name_ev,
            'f_fio': f_fio,
            'f_time_ev': f_time_ev,
            'f_identifier': f_identifier,
            'f_date_ev': f_date_ev,
        }
        if f_name_ev == 'Проход':
            events.append(event)

    return events






