PROJECT_STRUCTURE:

mac_changer/

├── mac_changer.py

├── README.md

├── .gitignore

└── LICENSE
# MAC Address Changer

A simple Python script to change the MAC address of a network interface on Linux.  
It supports restoring the original MAC if interrupted (Ctrl+C) and validates inputs for safety.

## Features

- Validate MAC address format (XX:XX:XX:XX:XX:XX)
- Check if network interface exists
- Change MAC address safely
- Restore original MAC on interrupt (Ctrl+C)
- Works only with root privileges

## Requirements

- Python 3.x
- Linux environment
- Root privileges (`sudo`)

## Installation

Clone the repository:

```bash
git clone https://github.com/prosper-codes/Python-MAC-Address-Tool.git
cd mac_changer
