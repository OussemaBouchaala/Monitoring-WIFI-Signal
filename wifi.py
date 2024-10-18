import platform
class Wifi:
    def __init__(self,ssid,signal):
        self.ssid=ssid
        self.signal=signal
    def __str__(self):
        return("ssid= "+self.ssid+"\nsignal strength= "+self.signal)
