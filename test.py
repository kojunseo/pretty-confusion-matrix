from prettycm import confusion_matrix, confusion_matrix_by_cal
from prettycm import palette
from prettycm.presets import preset_meta

class custom_preset(preset_meta):
    def __init__(self, max_num):
        colors_rgb = [(204,244,202),(10,30,12)]
        super().__init__(max_num,colors_rgb)

pset = palette(size=5, color="purple")

cm = confusion_matrix([[200,0,0,0],[0,156,8,14],[0,18,131,30],[0,60,28,75]])
cm.set_classname(["Acute", "Non-resolving","Normal","Inactive"])
cm.set_title("Retinal Specialist2")
print(cm)
pset.draw(cm, "./temp.png")

import numpy as np
y_true = np.array([1,1,1,1,0,0,0,0,1,1,1])
y_pred = np.array([1,1,0,1,0,0,0,1,1,0,1])
cm =confusion_matrix_by_cal(y_true, y_pred)

cm.set_classname(["Acute", "Inactive"])
cm.set_title("Retinal Specialist1")
print(cm)
pset.draw(cm, "./temp2.png")