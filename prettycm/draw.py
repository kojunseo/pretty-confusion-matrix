import os
from typing import Type
from PIL import Image, ImageDraw, ImageFont
from .presets import possible_presets, get_preset
from .presets.meta import preset_meta

class palette:
    def __init__(self, size=5, color="blue"):
        self.size = size
        self.pixel = self.size * 300
        if type(color) == str:
            self.preset = get_preset(color)
        elif issubclass(color, preset_meta):
            self.preset = color
        else:
            raise TypeError(f"Color parameter must be {possible_presets} or preset object")

        self.title_font = ImageFont.truetype(f"{os.path.dirname(__file__)}/font/gmarket.ttf", self.pixel//30, encoding="UTF-8")
        self.tick_font = ImageFont.truetype(f"{os.path.dirname(__file__)}/font/gmarket.ttf", self.pixel//40, encoding="UTF-8")
        self.label_font_small = ImageFont.truetype(f"{os.path.dirname(__file__)}/font/title.ttf", self.pixel//50, encoding="UTF-8")
        self.label_font_normal = ImageFont.truetype(f"{os.path.dirname(__file__)}/font/title.ttf", self.pixel//45, encoding="UTF-8")
        self.data_font = ImageFont.truetype(f"{os.path.dirname(__file__)}/font/gmarket.ttf", self.pixel//35, encoding="UTF-8")


    def make_font(self, max_length):
        factor = max_length*5-13
        return ImageFont.truetype(f"{os.path.dirname(__file__)}/font/title.ttf", self.pixel//factor, encoding="UTF-8")
    
    def draw(self, confusion_matrix, path):
        img = Image.new("RGB", (self.pixel, self.pixel), (255,255,255))
        standard = self.pixel//25

        # 원형으로 그리는거
        d = ImageDraw.Draw(img)
        d.text((standard*3, standard*1.5), confusion_matrix.title, font=self.title_font, fill=(0,0,0))
        d.text((self.pixel/2,self.pixel-standard*1.2), "Predicted", font=self.tick_font, fill=(0,0,0))

        rec_size = int((self.pixel*0.6) /(confusion_matrix.n_classes))
        term_size = rec_size//10
        for cls in range(confusion_matrix.n_classes):
            x_start = standard*6 + rec_size*(cls) + term_size*(cls)
            y_start = self.pixel-standard*4
            x_end =  standard*6 + rec_size*(cls+1) + term_size*(cls) 
            y_end = self.pixel-standard*4+standard*2
            xy = (x_start, y_start, x_end, y_end)
            d.rounded_rectangle(xy, 20, fill=(235,235,235))
            cls_name = confusion_matrix.classnames[cls]
            d.text((x_start+(rec_size/2), y_start+standard),cls_name,anchor="mm", align="center", font=self.label_font_normal, fill=(0,0,0))

        thispreset = self.preset(confusion_matrix.max_value)
        for i in range(confusion_matrix.n_classes):
            for j in range(confusion_matrix.n_classes):
                x_start = standard*6 + rec_size*(i) + term_size*(i)
                y_start = standard*4 + rec_size*(j) + term_size*(j)
                x_end =  standard*6 + rec_size*(i+1) + term_size*(i) 
                y_end = standard*4 + rec_size*(j+1) + term_size*(j)

                value = confusion_matrix(i, j)
                xy = (x_start, y_start, x_end, y_end)
                d.rounded_rectangle(xy, 20, fill=thispreset(value))
                d.text((x_start+(rec_size/2), y_start+(rec_size/2)), str(value), anchor="mm", align="center", font=self.data_font, fill=thispreset.text(value))

        # 돌려서 그리는거
        img = img.rotate(270, expand=1)
        d = ImageDraw.Draw(img)
        d.text(xy=(self.pixel/2,standard*1.5), text="Actual", font=self.tick_font, fill=(0,0,0))
        for cls in range(confusion_matrix.n_classes):
            x_start = standard*5 + rec_size*(cls) + term_size*(cls)
            y_start = standard*3
            x_end =  standard*5 + rec_size*(cls+1) + term_size*(cls) 
            y_end = standard*3 +standard*2
            xy = (x_start, y_start, x_end, y_end)
            cls_name = confusion_matrix.classnames[cls]
            d.rounded_rectangle(xy, 20, fill=(235,235,235))
            d.text((x_start+(rec_size/2), y_start+standard),cls_name,anchor="mm", align="center", font=self.label_font_normal, fill=(0,0,0))

        img = img.rotate(90, expand=1)
        # img = ImageDraw

        self.__save__(img, path)

    def __save__(self, img, path):
        img.save(path, "PNG")
