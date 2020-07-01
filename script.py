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
               
# [15:57, 27/6/2020] Mati Bro: Que cuando se abra el proceso del dbd
# [15:58, 27/6/2020] Mati Bro: Se me cambie la resolución a 1024x768
# [15:58, 27/6/2020] Mati Bro: Y cuando cierre el proceso se me cambie a 1366x768
open()
