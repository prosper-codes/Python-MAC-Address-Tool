

import subprocess

interface="Type the interface>",
new_mac_add=input("Enter the new MAC>")
print (f"[+] changing mac address of {interface} to {new_mac_add} ")
subprocess.call(f"ifconfig {interface} down" , shell=True)
subprocess.call(f"ifconfig {interface} hw ether {new_mac_add}" , shell=True)
subprocess.call(f"ifconfig {interface} up" , shell=True)


