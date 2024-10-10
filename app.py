import PySimpleGUI as psg
import math
psg.theme("Dark Amber")
layout=[[psg.Text("Calculate Volume of sphere")],
        [psg.InputText(key='--NAME--')],
        [psg.InputText(key='--RADIUS--')],
        [psg.Submit(),psg.Cancel()]]
window=psg.Window('zeraas first window',layout)
event,values=window.read()
window.close()
psg.popup(values['--NAME--'],'entered',values['--RADIUS--'])

def calculate_sphere_volume(radius):
        volume=(4/3)*math.pi*(radius**3)
        return volume

print(type(values['--RADIUS--'])) #to find datatype it have to be float

float_radius=float(values['--RADIUS--'])
volume_of_sphere=calculate_sphere_volume(float_radius)
psg.popup("The Volume is",volume_of_sphere)