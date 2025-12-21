
MAC Address Changer 🛠️

Description:
A simple Python script for changing the MAC address of a network interface on Linux.
The script validates inputs, checks interface availability, and restores the original
MAC address if interrupted.

Features:
- Validates MAC address format (XX:XX:XX:XX:XX:XX)
- Verifies that the network interface exists
- Safely changes the MAC address
- Restores the original MAC address on Ctrl+C
- Requires root privileges

Requirements:
- Python 3.x
- Linux environment
- Root access (sudo)
- ip command available on the system

Installation:
1. Clone the repository:
   git clone https://github.com/prosper-codes/Python-MAC-Address-Tool.git
   cd mac_changer

2. Make the script executable:
   chmod +x mac_changer.py

Usage:
Run the script as root and provide the interface and new MAC address:

   sudo ./mac_changer.py -i <interface> -m <new_mac>

Examples:
   sudo ./mac_changer.py -i eth0  -m 00:11:22:33:44:55
   sudo ./mac_changer.py -i wlan0 -m AA:BB:CC:DD:EE:FF

Notes:
- Bring the interface down or ensure it is not heavily in use.
- Linux systems only.
- Root privileges are required.
- Press Ctrl+C to restore the original MAC address.

License:
MIT License

