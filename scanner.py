import pywifi
from pywifi import const
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(3)

    results = iface.scan_results()
    networks = []

    for network in results:
        ssid = network.ssid
        bssid = network.bssid
        signal = network.signal
        auth = network.auth
        akm = network.akm

        auth_type = "OPEN"
        if const.AUTH_ALG_OPEN not in auth or akm:
            auth_type = "SECURED"


        networks.append({
            "SSID": ssid,
            "BSSID": bssid,
            "SIGNAL": f"{signal} dbm",
            "SECURITY": auth_type
        })


    return networks


if __name__ == "__main__":
    wifi_list = scan_wifi()
    for i, net in enumerate(wifi_list, 1):
        print(f"{i}. SSID: {net['SSID']}")
        print(f"     BSSID: {net['BSSID']}")
        print(f"     SIGNAL: {net['SIGNAL']}")
        print(f"     SECURITY: {net['SECURITY']}\n")