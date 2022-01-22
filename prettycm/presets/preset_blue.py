colors_rgb = [
    (204,209,225),
    (120,143,176),
    (100,120,155),
    (80,104,140),
    (56,76,111),
    (44,60,91),
    (32,48,77),
    (21,37,63),
    (14,30,55),
    (8,24,4)
]

class preset_blue:
    def __init__(self, max_num):
        if max_num ==0:
            raise ValueError(f"max_num must be bigger than 1, but now it is {max_num}")
        self.max_num = int(max_num)

    def __call__(self, num):
        idx = int((int(num)/self.max_num)*9)
        print(idx)
        return colors_rgb[idx]
        
    def text(self, num):
        idx = int((int(num)/self.max_num)*9)
        if idx > 5:
            return (255,255,255)
        else:
            return (0,0,0)
