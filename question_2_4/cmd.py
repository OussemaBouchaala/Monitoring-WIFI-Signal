import subprocess
import re
import platform
def detect_networks():
    p = subprocess.Popen("netsh wlan show networks mode=bssid", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read().decode('unicode_escape').strip()
    #print(out)
    if platform.system() == 'Linux':
        m = re.findall('(wlan [0-9]+).*?Signal level=(-[0-9]+) dBm', out, re.DOTALL)
    elif platform.system() == 'Windows':
        #m = re.findall('SSID.*?:.*? ([A-z0-9- ]*).*?Signal.*?:.*?([0-9]*%)', out, re. DOTALL)
        m = re.findall(r"SSID.*?:.*? ([A-z0-9- ']*).*?Signal.*?:.*?([0-9]*%)", out, re.DOTALL)
    else:
        raise Exception('reached else of if statement')
    p.communicate()
    #print(m)
    return m

def connect_wifi(ssid):
    p = subprocess.Popen(f"netsh wlan connect name={ssid}",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read().decode('utf-8').strip()
    print(out)
    p.communicate()
    return out