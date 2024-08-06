import os

def set_monitor_mode(interface):
    print(F"Setting {interface} to monitor mode")
    os.system(F"sudo ip link set {interface} down")
    os.system(f"sudo iw dev {interface} set type monitor")
    os.system(f"sudo ip link set {interface} up")

def main():
    interface = input("Enter the wireless interface: ")
    set_monitor_mode(interface)
    print(f"{interface} is now in monitor mode")

    