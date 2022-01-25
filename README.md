# Pretty Confusion Matrix

## 🤔 Why pretty confusion matrix?
* We can make confusion matrix by using matplotlib.
* However it is not so pretty. I want to make confusion matrix prettier.
* Also, it is not easy to use. It is easy to draw confusion matrix. 

## Design Contributors
* 황동호(Dongho Hwang, [hhdh12@naver.com](hhdh12@naver.com))
* 김다한(Dahan Kim, [dahan0811@gmail.com](dahan0811@gmail.com))

## Code Contributors
* 고준서(Junseo Ko, [Korkite](github.com/Korkite), [sta06167@naver.com](sta06167@naver.com))

## 📥 How to Install?
```python
pip install prettycm
```

## 🗞 Full Code Example
```python
from prettycm import confusion_matrix
from prettycm import palette

# Define confusion matrix 
cm = confusion_matrix([[400,0,0,0],[0,156,8,14],[0,18,131,30],[0,60,28,75]])
cm.set_classname(["Acute", "Non-resolving","Normal","Inactive"])
cm.set_title("Retinal Specialist2")

# Define Palette and draw
pset = palette()
pset.draw(cm, "place_to_save.png")
```

## 📦 Result of generated confusion matrix
<img width="400" alt="generated-confusion-matrix" src="https://user-images.githubusercontent.com/50725139/150660626-54afae22-bc74-4fd8-a34b-936d9ea66f01.png">

## 📰 How to Use?
### 1. import package from prettycm
```python
from prettycm import confusion_matrix
from prettycm import palette
```

### 2. build confusion matrix object
```python
cm = confusion_matrix([[400,0,0,0],[0,156,8,14],[0,18,131,30],[0,60,28,75]])
cm.set_classname(["Acute", "Non-resolving","Normal","Inactive"]) # You can set the class name.
cm.set_title("Retinal Specialist2") # You can set the title.
```
* the input of the confusion_matrix must be two-dimensional array
* Python list or numpy array are both allowed
* You can set the name of the class and title.

### 3. define palette object
```python
pset = palette(size=5, color="blue")
```
* size = the quality and size of output confusion matrix image
* color = the color of confusion matrix. (Now only blue is supported)
* Both parameters are not needed. size 5, color blue is defaultly set.

### 4. draw confusion matrix and save
```python
pset.draw(confusion_matrix=cm, path="place_to_save.png")
```
* confusion_matrix: put confusion matrix object
* path: path to save
#### Done

### 5. Generate Confusion matrix object by confusion_matrix_by_cal
* You can also generate confusion matrix object by y_pred, y_true.


### 6. Special Printer of Confusion Matrix
```python
print(cm)
```
* When you print confusion_matrix object, than python will print the confusion matrix like below
<img width="380" alt="cli" src="https://user-images.githubusercontent.com/50725139/150660624-ed90dc6e-c852-472e-acb0-f03f8eabb58b.png">

### 7. Custom Your own color presets
```python
from prettycm import palette
from prettycm.presets import preset_meta

class custom_green(preset_meta):
    def __init__(self, max_num):
        colors_rgb = [(204,244,202),(10,30,12)]
        super().__init__(max_num,colors_rgb)

pset = palette(size=5, color=custom_green)
```
* You can customize your own color preset
* Make your own class and inherit prettycm.presets.preset_meta
* And You have to write custom object same as this.
* colors_rgb consists of two 'tuple', which is brightest color RGB and darkest color RGB.
* Other colors will automatically be calculated by preset_meta object.


## 📆 Update Plans
### 1. More color presets
- [x] Blue (👍 Best)
- [x] Red
- [ ] Green
- [ ] Purple
- [x] Custom Preset

### 2. Confusion matrix concat
- [ ] Concat two confusion matrix

### 3. Pallet Function
- [ ] Text Size control
- [ ] Cleaning the code

## 🙏🏻 PLEASE Contribute to this project 
1. Pull requests after you modify code.
2. Make more color presets.
