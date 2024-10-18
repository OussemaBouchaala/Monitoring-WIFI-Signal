import subprocess
import re
import platform
from wifi import *
class Terminal:

    def read_data_from_cmd(self):
        p = subprocess. Popen("netsh wlan show networks mode=bssid", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.stdout.read().decode("unicode_escape").strip()
        h= re.findall('SSID.*?ÿ:.([A-z0-9- ]*).*?Signal.*?:.*?([0-9]*)%', out, re. DOTALL)
        wifis=[]
        for i in h:
            wifi=Wifi(i[0],i[1])
            wifis.append(wifi)
        return wifis

        p.communicate()
        
    def read_data(self):
        p = subprocess. Popen("netsh wlan show interfaces", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.stdout.read().decode("unicode_escape").strip()
        if(platform.system()=='Linux'):
            m= re.findall('(wlan[0-9]+).?Signal level=(-[0-9]+) dBm',out,re.DOTALL)
        elif platform.system() == 'Windows':
            m = re.findall('SSID.*?ÿ:.([A-z0-9- ]*).*?Signal.*?ÿ:.*?([0-9]*)%', out, re. DOTALL)
        else:
            raise Exception('reached else of if statement')
        p.communicate()
        wifi=Wifi(m[0][0],m[0][1])
        return(wifi)
       

