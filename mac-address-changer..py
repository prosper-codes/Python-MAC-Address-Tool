#!/usr/bin/env python3

import subprocess
import optparse
import re
import os
import sys
import signal

# ---------------------- Utility Checks ----------------------


def is_root():
    return os.geteuid() == 0


def is_valid_mac(mac):
    return re.fullmatch(r"[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}", mac) is not None


def interface_exists(interface):
    result = subprocess.run(
        ["ip", "link", "show", interface],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


# ---------------------- Argument Parsing ----------------------


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Network interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, _) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for info")
    if not options.new_mac:
        parser.error("[-] Please specify a new MAC address")
    if not is_valid_mac(options.new_mac):
        parser.error("[-] Invalid MAC address format (XX:XX:XX:XX:XX:XX)")

    return options


# ---------------------- MAC Operations ----------------------


def get_current_mac(interface):
    output = subprocess.check_output(["ip", "link", "show", interface], text=True)
    match = re.search(r"link/ether\s([0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5})", output)
    if match:
        return match.group(1)
    return None


def change_mac(interface, new_mac):
    subprocess.run(["ip", "link", "set", interface, "down"], check=True)
    subprocess.run(["ip", "link", "set", interface, "address", new_mac], check=True)
    subprocess.run(["ip", "link", "set", interface, "up"], check=True)


# ---------------------- Signal Handler ----------------------


def setup_restore(original_mac, interface):
    def restore(sig, frame):
        print("\n[+] Restoring original MAC address...")
        change_mac(interface, original_mac)
        sys.exit(0)

    signal.signal(signal.SIGINT, restore)


# ---------------------- Main Logic ----------------------


def main():
    if not is_root():
        print("[-] Please run this script as root")
        sys.exit(1)

    options = get_arguments()

    if not interface_exists(options.interface):
        print(f"[-] Interface {options.interface} does not exist")
        sys.exit(1)

    current_mac = get_current_mac(options.interface)
    if not current_mac:
        print("[-] Could not read current MAC address")
        sys.exit(1)

    print(f"[+] Current MAC: {current_mac}")

    setup_restore(current_mac, options.interface)

    print(f"[+] Changing MAC address of {options.interface} to {options.new_mac}")
    change_mac(options.interface, options.new_mac)

    new_mac = get_current_mac(options.interface)

    if new_mac and new_mac.lower() == options.new_mac.lower():
        print(f"[+] MAC successfully changed to {new_mac}")
    else:
        print("[-] MAC address change failed")


if __name__ == "__main__":
    main()
