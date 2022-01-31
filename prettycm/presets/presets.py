from .meta import preset_meta

possible_presets = ["blue", "red", "purple", "green"]

def presets(colors):
    if colors == "blue":
        return preset_blue
    elif colors == "red":
        return preset_red


class preset_blue(preset_meta):
    def __init__(self, max_num):
        self.colors_rgb  = ((204,209,225),(8,12,30))
        self.text_reverse = 4
        super().__init__(max_num, self.colors_rgb, self.text_reverse)


class preset_red(preset_meta):
    def __init__(self, max_num):
        self.colors_rgb  = ((225,209,204),(30,12,10))
        self.text_reverse = 4
        super().__init__(max_num, self.colors_rgb, self.text_reverse)


class preset_purple(preset_meta):
    def __init__(self, max_num):
        colors_rgb = [(235,200,250),(36,10,72)]
        super().__init__(max_num,colors_rgb)


class preset_green(preset_meta):
    def __init__(self, max_num):
        colors_rgb = [(204,244,202),(10,30,12)]
        super().__init__(max_num,colors_rgb)