import os
import random
import time
import requests
import ntplib
import json

def check_internet_connection(url='1.asia.pool.ntp.org', timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False
def get_ntp_time(server='1.asia.pool.ntp.org'):
    try:
        client = ntplib.NTPClient()
        response = client.request(server, version=3)
        return response
    except Exception as e:
        return f"Failed to get time from NTP server: {e}"

if check_internet_connection:
    rand_num = random.randint(100,999)

    while rand_num != int(input("Please Enter "+str(rand_num)+": ")):
        pass

    cmp_name = os.environ['COMPUTERNAME']
    cmp_time = os.popen('systeminfo | find "System Boot Time"').read()
    ntp_time = get_ntp_time()
    ntp_time_readable = time.ctime(ntp_time.tx_time)
    data = []
    data.append(cmp_name)
    data.append(cmp_time)
    data.append(ntp_time.tx_time)
    data.append(ntp_time_readable)
    print(json.dumps({'results': data}))
    
else:
    print("Code 0: Please Check Internet Connection")
