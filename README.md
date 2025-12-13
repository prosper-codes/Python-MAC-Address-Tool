

````markdown
# MAC Address Changer 🛠️

A simple Python script to change the MAC address of a network interface on Linux.  
It supports restoring the original MAC if interrupted (Ctrl+C) and validates inputs for safety.

## Features

- ✅ Validate MAC address format (`XX:XX:XX:XX:XX:XX`)
- ✅ Check if network interface exists
- ✅ Change MAC address safely
- ✅ Restore original MAC if interrupted (Ctrl+C)
- ✅ Works only with root privileges

## Requirements

- Python 3.x
- Linux environment
- Root privileges (`sudo`)

## Installation

Clone the repository:

```bash
git clone https://github.com/prosper-codes/Python-MAC-Address-Tool.git
cd mac_changer
````

Make the script executable:

```bash
chmod +x mac_changer.py
```

## Usage

Run the script as root and specify the network interface and new MAC address:

```bash
sudo ./mac_changer.py -i <interface> -m <new_mac>
```

**Examples:**

Change the MAC address of `eth0`:

```bash
sudo ./mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

Change the MAC address of `wlan0`:

```bash
sudo ./mac_changer.py -i wlan0 -m AA:BB:CC:DD:EE:FF
```

### Notes

* Ensure the network interface is down or not in heavy use during the change.
* Only works on Linux systems with the `ip` command installed.
* Always run as root.
* Press `Ctrl+C` to restore the original MAC address safely if interrupted.

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

```

---

If you want, I can also **add badges and a slightly more stylish GitHub-ready version** to make it stand out. Do you want me to do that?
```
