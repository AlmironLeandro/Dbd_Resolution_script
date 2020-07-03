import subprocess,time,os,wmi

def isProcess(nameProcess):
     c = wmi.WMI ()
     for process in c.Win32_Process ():
         if(process.Name == nameProcess):
             return True
         
def open():
    subprocess.call(['resolution1024x768.bat'])
    time.sleep(5)
    os.startfile("steam://rungameid/381210")
    time.sleep(13)
    verification()
    

def verification():
    while True:
        if(isProcess("DeadByDaylight-Win64-Shipping.exe" or "DeadByDaylight.exe")):
            print("isProcess-->True")
            
        else:
            subprocess.call([r'resolution1366x768.bat'])
            print("isProcess-->True")
            return False        
               

open()
