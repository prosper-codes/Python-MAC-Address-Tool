import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i","--interface",dest="interface",help="Interface to change its mac address")
parser.add_option("-m","--mac",dest="new_mac_add",help="New Mac address")

(options ,arguments)=parser.parse_args()

interface=options.interface
new_mac_add=options.new_mac_add

print (f"[+] changing mac address of {interface} to {new_mac_add} ")


subprocess.call(["ifconfig" , interface ,"down"])
subprocess.call(["ifconfig" , interface, "hw","ether",new_mac_add])
subprocess.call(["ifconfig", interface,"up"])
