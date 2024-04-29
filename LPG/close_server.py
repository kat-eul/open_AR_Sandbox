import subprocess,os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from tkinter import *

def separate_pid(server_pid):
    all_server_pid = [""]
    i = 0
    for carac in server_pid :
        if(carac == '\n'):
            i+=1
            all_server_pid.append("")
        else :
            all_server_pid[i]+=carac
    return all_server_pid
            
cmd = ['/home/sandbox/.config/jupyterlab-desktop/jlab_server/bin/panel serve /home/sandbox/Documents/open_AR_Sandbox/LPG/server_sensor_calibration.py --show',
       '/home/sandbox/.config/jupyterlab-desktop/jlab_server/bin/panel serve /home/sandbox/Documents/open_AR_Sandbox/LPG/server_projector_calibration.py --show',
       '/home/sandbox/.config/jupyterlab-desktop/jlab_server/bin/panel serve /home/sandbox/Documents/open_AR_Sandbox/LPG/server_sandbox.py --show']

for each in cmd :
    ps_command = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
    grep_command = subprocess.Popen(['grep', each], stdin=ps_command.stdout, stdout=subprocess.PIPE)
    awk_command = subprocess.Popen(['awk', '{print $2}'], stdin=grep_command.stdout, stdout=subprocess.PIPE)
    server_pid = separate_pid(awk_command.communicate()[0].decode().strip())

    if len(server_pid)!=0:
        for pid in server_pid :
            os.kill(int(pid), 15)

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Popup")

# Création d'un libellé
label = Label(fenetre, text="Serveurs correctement clôts")
label.pack(padx=20, pady=20)

# Lancement de la boucle principale
fenetre.mainloop()