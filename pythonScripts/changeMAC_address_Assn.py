import os
import subprocess

        
def change_mac(interface, new_mac):
    print(f" Changing MAC address for {interface} to {new_mac}")
    os.system(f"sudo ifconfig {interface} down")
    os.system(f"sudo ifconfig {interface} hw ether {new_mac}")
    os.system(F"sudo ifconfig {interface} up")

def main():
    interface = (f"ifconfig wlan0")
    new_mac = (f"45:52:93:94:19:f2")

    if __name__ == "__main__":
        main()

