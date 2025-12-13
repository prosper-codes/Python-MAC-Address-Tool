import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option(
        "-i",
        "--interface",
        dest="interface",
        help="Interface to change its mac address",
    )
    parser.add_option("-m", "--mac", dest="new_mac_add", help="New Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(
            "[+] Please specify the interface you wish to change the mac address, use --help for more info"
        )
    elif not options.new_mac_add:
        parser.error("[+] Please specify a new mac, use --help for more info")
    return options


def mac_changer(interface, new_mac_add):
    print(f"[+] changing mac address of {interface} to {new_mac_add}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_add])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()

mac_changer(options.interface, options.new_mac_add)

ifconf_output = subprocess.check_output(["ifconfig", options.interface], text=True)
mac_address_regrex_result = re.search(
    r"\b[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}\b", ifconf_output
)
if mac_address_regrex_result:
    print(mac_address_regrex_result.group(0))
else:
    print("[+] mac address not found")
