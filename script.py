import subprocess,time,os,wmi

#TODO: MEJORAR EL CODIGO; CREAR INTERFAZ PARA SELECCIONAR RESOLUCION;
# def SetResolution(width, height):
#     os.popen("xrandr -s "+str(width)+'x'+str(height))
# FILENAME=r'C:\Users\Lead\Desktop'
# def openSteamAndDeadByDaylight():
#         subprocess.Popen([r'C:\Program Files (x86)\Steam\steam.exe'])
#         subprocess.call([r'resolution1024x768.bat'])
#         time.sleep(10)
#         os.startfile("steam://rungameid/381210%22")
    # subprocess.Popen(["C:\Program Files (x86)\Steam\steam.exe"])
    # time.sleep(10)
    # subprocess.Popen(["start steam://rungameid/381210%22])

# def isProcess(nameProcess):
#     c = wmi.WMI ()
#     for process in c.Win32_Process ():
#         if(process.Name == nameProcess):
#             return True
         

def open():
            subprocess.call([r'resolution1024x768.bat'])
            time.sleep(12)
            os.startfile("steam://rungameid/381210%22")
            
               
# [15:57, 27/6/2020] Mati Bro: Que cuando se abra el proceso del dbd
# [15:58, 27/6/2020] Mati Bro: Se me cambie la resolución a 1024x768
# [15:58, 27/6/2020] Mati Bro: Y cuando cierre el proceso se me cambie a 1366x768
open()