import serial
from serial import SerialException
import time
import os
from urllib import request,error
import json
import time

data = {'roomid': None, 'datatype': None, 'roomdata': None}

url = "https://icube.apps.bosch-iot-cloud.com/PostRoomData/"

#ipAdd = socket.gethostbyname(url)

headers = {
    "Accept-Encoding": "utf-8",
    "Connection": "keep-alive",
    "content-type": "application/json",
    "User-Ageng": "Mozilla"
}

##data_list.append(GLOBAL_DATA)
try:
    ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
except SerialException:
    f = open("/home/pi/PortDignose", "a")
    f.write("Port open error")
    print('Port open error')

try:
    while True:

        response = ser.readline().decode('utf-8').strip()
        ##        post(response)

        if len(response) == 2:
            ##          clear data
            data_list1 = data_list2 = data_list3 = data_list4 = data_list5 = data_list6 = data_list7 = data_list8 = []
            Motion = None

            ##          define Room number
            Room_number = int(response[:1])

            ##          define Motion
            Motion_original = response[1:2]
            if Motion_original == 'N':
                Motion = 0
            elif Motion_original == 'Y':
                Motion = 1

            localtime = time.asctime( time.localtime(time.time()) )

            f = open("/home/pi/ReceiveDignose", "a")
            f.write(Motion + localtime)

            ##          fill data into 8 Room list for posting
            if Room_number == 1:
                data_list1.append({'roomid': Room_number, 'datatype': 'Motion', 'roomdata': Motion})
            elif Room_number == 2:
                data_list2.append({'roomid': Room_number, 'datatype': 'Motion', 'roomdata': Motion})
            elif Room_number == 3:
                data_list3.append({'roomid': Room_number, 'datatype': 'Motion', 'roomdata': Motion})
            elif Room_number == 4:
                data_list4.append({'roomid': Room_number, 'datatype': 'Motion', 'roomdata': Motion})
            elif Room_number == 5:
                data_list5.append({'roomid': Room_number, 'datatype': 'Motion', 'roomdata': Motion})
            elif Room_number == 6:
                data_list6.append({'roomid': Room_number, 'datatype': 'Motion', 'roomdata': Motion})
            elif Room_number == 7:
                data_list7.append({'roomid': Room_number, 'datatype': 'Motion', 'roomdata': Motion})
            else: 
                data_list8.append({'roomid': Room_number, 'datatype': 'Motion', 'roomdata': Motion})
                        
            ##          encode data
            postdata1 = json.dumps(data_list1).encode('utf-8')
            postdata2 = json.dumps(data_list2).encode('utf-8')
            postdata3 = json.dumps(data_list3).encode('utf-8')
            postdata4 = json.dumps(data_list4).encode('utf-8')
            postdata5 = json.dumps(data_list5).encode('utf-8')
            postdata6 = json.dumps(data_list6).encode('utf-8')
            postdata7 = json.dumps(data_list7).encode('utf-8')
            postdata8 = json.dumps(data_list8).encode('utf-8')

            ##          post(postdata)
            post_request1 = request.Request(url=url, data=postdat1, headers=headers, method='POST')
            post_request2 = request.Request(url=url, data=postdat2, headers=headers, method='POST')
            post_request3 = request.Request(url=url, data=postdat3, headers=headers, method='POST')
            post_request4 = request.Request(url=url, data=postdat4, headers=headers, method='POST')
            post_request5 = request.Request(url=url, data=postdat5, headers=headers, method='POST')
            post_request6 = request.Request(url=url, data=postdat6, headers=headers, method='POST')
            post_request7 = request.Request(url=url, data=postdat7, headers=headers, method='POST')
            post_request8 = request.Request(url=url, data=postdat8, headers=headers, method='POST')

            time.sleep(1)
            try:
                result1 = request.urlopen(post_request1)
                result2 = request.urlopen(post_request2)
                result3 = request.urlopen(post_request3)
                result4 = request.urlopen(post_request4)
                result5 = request.urlopen(post_request5)
                result6 = request.urlopen(post_request6)
                result7 = request.urlopen(post_request7)
                result8 = request.urlopen(post_request8)
            except error.URLError:
                time.sleep(1)
                f = open("/home/pi/URLErrorDignose", "a")
                f.write(result1.read().decode('utf-8'))
                f.write(result2.read().decode('utf-8'))
                f.write(result3.read().decode('utf-8'))
                f.write(result4.read().decode('utf-8'))
                f.write(result5.read().decode('utf-8'))
                f.write(result6.read().decode('utf-8'))
                f.write(result7.read().decode('utf-8'))
                f.write(result8.read().decode('utf-8'))
                
                os.system('sudo reboot')

except KeyboardInterrupt:
    ser.close()
