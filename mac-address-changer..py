

import subprocess

interface="eth0",
new_mac_add="00:22:33:55:77:99"
print (f"[+] changing mac address of {interface} to {new_mac_add} ")
subprocess.call(f"ifconfig {interface} down" , shell=True)
subprocess.call(f"ifconfig {interface} hw ether {new_mac_add}" , shell=True)
subprocess.call(f"ifconfig {interface} up" , shell=True)


