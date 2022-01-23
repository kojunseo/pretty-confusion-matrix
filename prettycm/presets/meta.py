import numpy as np

class preset_meta:
    def __init__(self, max_num, colors_rgb, text_reverse_point=4):
        self.text_reverse = text_reverse_point
        self.colors_rgb = colors_rgb
        if max_num ==0:
            raise ValueError(f"max_num must be bigger than 1, but now it is {max_num}")
        self.max_num = int(max_num)
        self.max_color = np.array(self.colors_rgb[0])
        self.min_color = np.array(self.colors_rgb[1])
        self.sub_stract = self.max_color - self.min_color

    def __call__(self, num):
        idx = float(num)/self.max_num
        return tuple((self.max_color - self.sub_stract*idx).astype("int"))
        
    def text(self, num):
        idx = int((int(num)/self.max_num)*9)
        if idx > self.text_reverse:
            return (255,255,255)
        else:
            return (0,0,0)
