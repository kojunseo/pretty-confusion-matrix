from prettycm import confusion_matrix
from prettycm import palette

pset = palette(size=5, color="blue")

cm = confusion_matrix([[10,20],[30,3]])
cm.set_classname(["Acute", "Non-resolving"])
cm.set_title("Binary Class")
print(cm)
pset.draw(cm, "./temp3.png")


cm = confusion_matrix([[10,20,30],[30,3,34],[100,2,3]])
cm.set_classname(["Acute", "Chronf", "Normal"])
cm.set_title("Three Class")
print(cm)
pset.draw(cm, "./temp2.png")


cm = confusion_matrix([[400,0,0,0],[0,156,8,14],[0,18,131,30],[0,60,28,75]])
cm.set_classname(["Acute", "Non-resolving","Normal","Inactive"])
cm.set_title("Retinal Specialist2")
print(cm)
pset.draw(cm, "./temp.png")
