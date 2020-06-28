import subprocess,time,os,wmi
def SetResolution(width, height):
    os.popen("xrandr -s "+str(width)+'x'+str(height))

# FILENAME=r'C:\Users\Lead\Desktop'
def openSteanAndDeadByDaylight():
        subprocess.Popen([r'C:\Program Files (x86)\Steam\steam.exe'])
        time.sleep(10)
        os.startfile("steam://rungameid/381210%22")
    # subprocess.Popen(["C:\Program Files (x86)\Steam\steam.exe"])
    # time.sleep(10)
    # subprocess.Popen(["start steam://rungameid/381210%22])

def isProcess(nameProcess):
    c = wmi.WMI ()
    for process in c.Win32_Process ():
        if(process.Name == nameProcess):
            return True
         

def open():
            if(isProcess("steam.exe")):
                print("ENTRO")
                os.startfile("steam://rungameid/381210%22")
            else:
                print("ENTRO al else")
                openSteanAndDeadByDaylight()

def main():
    width = input("width?")
    height = input("height?")
    time.sleep(10)
    SetResolution(width,height)
    
main()