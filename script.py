import subprocess,time,os,wmi

def isProcess(nameProcess):
     c = wmi.WMI ()
     for process in c.Win32_Process ():
         if(process.Name == nameProcess):
             return True
         
def open():
    subprocess.call([r'resolution1024x768.bat'])
    time.sleep(10)
    os.startfile("steam://rungameid/381210")
    time.sleep(15)
    verification()
    

def verification():
    while True:
        if(isProcess("DeadByDaylight-Win64-Shipping.exe")):
            print("FUE TRUE")
            
        else:
            subprocess.call([r'resolution1366x768.bat'])
            print("FUE FALSE")
            return False        
               

open()
