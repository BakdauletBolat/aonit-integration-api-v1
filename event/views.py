from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from event.models import EventUser, Unit
from datetime import date


def index(request):
    return render(request, 'main/index.html')

def eventView(request):
    events = EventUser.objects.all()
    data = {
        'events':events
    }
    return render(request, 'main/event.html', data)

def unitView(request):
    units = Unit.objects.all()
    data = {
        'units':units
    }
    return render(request, 'main/unit.html', data)





import requests
import arrow
from datetime import datetime
url='http://10.61.40.133:9012/bip-sync/?wsdl'
headers = {'content-type': 'application/soap+xml; charset=utf-8'}

login = 'SKUDPERCO'
password = '123456qA'




def todayView(request):
    today = datetime.now()
    dateTObody = arrow.get(datetime.now())
    dateString = f'{today.day}.{today.month}.{today.year}'
    print(dateString)
    events = EventUser.objects.filter(created_at__date=date.today())
    data = {
        'events': events
    }

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

    return render(request, 'main/event.html', data)