import requests
from INTEST_GPS_trans_API import GPS_FIX_WGS84
from Time_to_UTC import utc_mktime


def GPS_to_road_information(csvdata, i):
    csvdata = csvdata[['Longitude', 'Latitude', 'Direction', 'Date', 'Time', 'Veh_Spd_NonDrvn']]
    # csvdata = csvdata[csvdata['Longitude'] > 0]
    GPS = csvdata[['Longitude', 'Latitude']]
    Time = csvdata[['Date', 'Time']]
    Dirction = csvdata['Direction']
    Vspd = csvdata['Veh_Spd_NonDrvn']

    # # 另一种写法
    # server = 'http://restapi.amap.com/v3/autograsp'
    # parameters = {'key': '42f165dabcfcb28c1c0290058adee399', 'carid': 'e399123456',
    #               'locations': '116.496167,39.917066|116.496149,39.917205|116.496149,39.917326',
    #               'time': '1502242820,1502242823,1502242830', 'direction': '1,1,2',
    #               'speed': '1,1,2'}
    # r = requests.get(server, params=parameters)
    # print(r.url)

    # 每次取点
    base = 'http://restapi.amap.com/v3/autograsp?key=42f165dabcfcb28c1c0290058adee399&carid=e399123456'
    Gps1 = GPS_FIX_WGS84(GPS.iloc[i][0], GPS.iloc[i][1])
    Gps2 = GPS_FIX_WGS84(GPS.iloc[i + 50][0], GPS.iloc[i + 50][1])
    Gps3 = GPS_FIX_WGS84(GPS.iloc[i + 100][0], GPS.iloc[i + 100][1])
    location = '&locations=' + str(Gps1[0]) + ',' + str(Gps1[1]) + '|' + str(Gps2[0]) + ',' + str(
        Gps2[1]) + '|' + str(
        Gps3[0]) + ',' + str(Gps3[1])
    Time1 = utc_mktime(Time.iloc[i][0], Time.iloc[i][1])
    Time2 = utc_mktime(Time.iloc[i + 50][0], Time.iloc[i + 50][1])
    Time3 = utc_mktime(Time.iloc[i + 100][0], Time.iloc[i + 100][1])
    time = '&time=' + str(Time1) + ',' + str(Time2) + ',' + str(Time3)
    direction = '&direction=' + str(Dirction.iloc[i]) + ',' + str(Dirction.iloc[i + 50]) + ',' + str(
        Dirction.iloc[i + 100])
    speed = '&speed=' + str(Vspd.iloc[i]) + ',' + str(Vspd.iloc[i + 50]) + ',' + str(Vspd.iloc[i + 100])
    url = base + location + time + direction + speed
    r = requests.get(url)
    answer = r.json()
    if answer['infocode'] == '10000':  # 请求成功
        if answer['roads'] != []:
            road = answer['roads'][0]['roadname']
            maxspeed = answer['roads'][0]['maxspeed']
            level = answer['roads'][0]['roadlevel']
        else:
            road = 'Unknown'
            maxspeed = '60'
            level = 'Unknown'
    else:
        road = 'GPS_error'
        maxspeed = '120'
        level = 'GPS_error'
    return road, maxspeed, level

        # # 一并取点，每次最多20条.
        # base = 'http://restapi.amap.com/v3/autograsp?key=42f165dabcfcb28c1c0290058adee399&carid=e399123456'
        # location = '&locations='
        # time = '&time='
        # direction = '&direction='
        # speed = '&speed='
        # for i in range(3000, 5000, 200):
        #     Gps = GPS_FIX_WGS84(GPS.iloc[i][0], GPS.iloc[i][1])
        #     location = location + str(Gps[0]) + ',' + str(Gps[1]) + '|'
        #     TIME = utc_mktime(Time.iloc[i][0], Time.iloc[i][1])
        #     time = time + str(TIME) + ','
        #     direction = direction + str(Dirction.iloc[i]) + ','
        #     speed = speed + str(Vspd.iloc[i]) + ','
        #
        # url = base + location[0:-1] + time[0:-1] + direction[0:-1] + speed[0:-1]
        # r = requests.get(url)
        # answer = r.json()
        # print(answer)



