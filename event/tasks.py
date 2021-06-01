from celery import shared_task
from .models import EventUser,Unit,TestDB
from django.core.exceptions import ObjectDoesNotExist
import string,random
import requests
import arrow
from datetime import datetime,date



@shared_task
def loadUnitsandSave():
    from .utils import loadEvents
    events = loadEvents()
    for event in events:
        if event['f_fio'] != "":
            try:
                eventD = EventUser.objects.get(f_unic_id=event['f_unic_id'])
        
            except ObjectDoesNotExist:

                try:
                    unit = Unit.objects.get(id_internal=event['f_subdiv_id_internal'])
                    eventD = EventUser(
                        f_unic_id = event['f_unic_id'],
                        f_areas_name = event['f_areas_name'],
                        f_identifier = event['f_identifier'],
                        f_name_ev = event['f_name_ev'],
                        f_name_subdiv = unit.displayname or unit,
                        f_subdiv_id_internal = unit.id_internal or unit,
                        f_fio = event['f_fio'],
                        f_date_ev = event['f_date_ev'],
                        f_time_ev = event['f_time_ev'],
                        bin = unit.bin or unit
                    )
                    eventD.save()
                except ObjectDoesNotExist:
                    
                    pass
                
        else:
            pass

@shared_task
def sendRequestToAonit():
    today = datetime.now()
    url = 'http://10.61.40.133:9012/bip-sync/?wsdl'
    headers = {'content-type': 'application/soap+xml; charset=utf-8'}
    dateTObody = arrow.get(datetime.now())
    login = 'SKUDPERCO'
    password = '123456qA'
    dateString = f'{today.day}.{today.month}.{today.year}'
    events = EventUser.objects.filter(created_at__date=date.today())
    def rfidIterable():
        string = ''
        for event in events:
            string += f"<value>{event.f_identifier}</value>"

        return string

    def eventCodeIterable():
        string = ''
        for event in events:
            string += f"<value>{event.f_areas_name}</value>"

        return string

    def datetimeIterable():
        string = ''
        for event in events:
            string += f"<value>{event.f_date_ev} {event.f_time_ev}</value>"

        return string

    def binIterable():
        string = ''
        for event in events:
            string += f"<value>{event.bin}</value>"

    def testItrable():
        string = ''
        for event in events:
            string += f"<value>Не задано</value>"

        return string

    body = f"""
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
	<SOAP-ENV:Body>
		<m:SendMessage xmlns:m="http://bip.bee.kz/SyncChannel/v10/Types">
			<request>
				<requestInfo>
					<messageId>String</messageId>
					<serviceId>EKyzmetUniversalService</serviceId>
					<messageDate>{dateTObody}</messageDate>
					<sender>
						<senderId>{login}</senderId>
						<password>{password}</password>
					</sender>
					<properties>
						<key></key>
						<value></value>
					</properties>
				</requestInfo>
				<requestData>
					<data>
					<Request serviceName="sendEventFromACSList" xsi:noNamespaceSchemaLocation="EKyzmetUniversalService.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
					<param>
						<key>RFID</key>
						<type>String</type>
						<values>
							{rfidIterable()}							
						</values>
             
					</param>
					<param>
						<key>Событие</key>
						<type>String</type>
						<values>
							{eventCodeIterable()}
						</values>
					</param>					
					<param>
						<key>Время</key>
						<type>String</type>
						<values>
							{datetimeIterable()}
						</values>
					</param>					
					<param>
						<key>БИН</key>
						<type>String</type>
						<values>
							{binIterable()}
						</values>
					</param>	
                    <param>
						<key>Номер этажа</key>
						<type>String</type>
						<values>
							{testItrable()}
						</values>
					</param>
					<param>
						<key>Наименование здания</key>
						<type>String</type>
						<values>
							{testItrable()}
						</values>
					</param>												
				</Request>
					</data>
				</requestData>
			</request>
		</m:SendMessage>
	</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""
   
    body = body.encode('utf-8')
    response = requests.post(url,data=body, headers=headers)

    if response.status_code == 200:
        print(f'Сообщение успешно отправлено КОД:{response.status_code}')
        print(response.text)
    else:
        print(response.text)
        print(f'Есть ошибка КОД:{response.status_code}')


