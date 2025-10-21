import socket
import urllib.request
import uuid
import subprocess
import re
name = input("please enter your name: ")
class SystemInfo:
    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def get_public_ip(self):
        data = urllib.request.urlopen("https://api.ipify.org").read()
        return data.decode()

    def get_mac_address(self):
        mac = uuid.getnode()
        return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
#so tired :(
    def get_wifi_password(self):
        profiles = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
        names = re.findall("All User Profile     : (.*)", profiles)
        for name in names:
            results = subprocess.check_output(f'netsh wlan show profile name="{name}" key=clear', shell=True).decode(errors="ignore")
            password = re.search("Key Content            : (.*)", results)
            if password:
                print(name, ":", password.group(1))
            else:
                print(name, ": No password found")
#almost done! :D
info = SystemInfo()
print(f"Hello Mr, {name}, Here's your network info:")
print("this program was written by: ")
print("Feras Hussein Farouq")
print("Your Local IP is:", info.get_local_ip())
print("Your Public IP is:", info.get_public_ip())
print("Your MAC Address is:", info.get_mac_address())
print("Your Wi-Fi Passwords are:", info.get_wifi_password())
print("Thank you for using :)")