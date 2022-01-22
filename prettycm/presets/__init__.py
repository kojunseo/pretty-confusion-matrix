from .preset_blue import preset_blue

possible_presets = ["blue"]

def get_preset(color):
    if color == "blue":
        return preset_blue
    else:
        raise ValueError(f"{color} is not a possible preset.")