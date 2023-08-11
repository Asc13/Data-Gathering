from config import W_KEY, T_KEY

from datetime import datetime
from time import sleep
import requests
import re


lat = ['38.7071', '41.14961', '37.019356']
lon = ['-9.13549', '-8.61099', '-7.93044']


cities = ['Lisboa', 'Porto', 'Faro']

# Lisboa - 0, Porto - 1, Faro - 2
w_call = [f'https://api.openweathermap.org/data/2.5/weather?lat={lat[0]}&lon={lon[0]}&appid={W_KEY}&units=metric', 
          f'https://api.openweathermap.org/data/2.5/weather?lat={lat[1]}&lon={lon[1]}&appid={W_KEY}&units=metric', 
          f'https://api.openweathermap.org/data/2.5/weather?lat={lat[2]}&lon={lon[2]}&appid={W_KEY}&units=metric']

t_call = [f'https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key={T_KEY}&point={lat[0]},{lon[0]}', 
          f'https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key={T_KEY}&point={lat[1]},{lon[1]}', 
          f'https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key={T_KEY}&point={lat[2]},{lon[2]}']

ap_call = [f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat[0]}&lon={lon[0]}&appid={W_KEY}',
           f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat[1]}&lon={lon[1]}&appid={W_KEY}', 
           f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat[2]}&lon={lon[2]}&appid={W_KEY}']


w_f = open('../TP2/weather.json', 'a')
t_f = open('../TP2/traffic.json', 'a')
ap_f = open('../TP2/air_pollution.json', 'a')
d_f = open('../TP2/data.json', 'a')

while 1:
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")

    for i in range(0, 3):

        city = cities[i]

        # Weather Call
        call1 = re.sub(r'\'', r'"', str(requests.get(w_call[i]).json()))

        sleep(5)

        # Traffic Call
        call2 = re.sub(r'True', r'"True"', 
                re.sub(r'False', r'"False"', 
                re.sub(r'\'', r'"', str(requests.get(t_call[i]).json()))))

        sleep(5)

        # AirPollution Call
        call3 = re.sub(r'\'', r'"', str(requests.get(ap_call[i]).json()))

        d_f.write('{\"datetime\": ' + '\"' + date + '\"' + 
                  ', \"city\": ' + '\"' + city + '\"' + 
                  ', \"lat\": ' + '\"' + lat[i] + '\"' + 
                  ', \"lon\": ' + '\"' + lon[i] + '\"' + 
                  ', \"weather\": ' + call1 + 
                  ', \"traffic\": ' + call2 + 
                  ', \"airPollution\": ' + call3 + '}\n')

        sleep(5)

    # 10 mins no total
    sleep(555)