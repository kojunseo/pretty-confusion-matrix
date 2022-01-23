from .presets import presets, possible_presets
from .meta import preset_meta

def get_preset(color):
    if color in possible_presets:
        return presets(color)
    else:
        raise ValueError(f"{color} is not a possible preset.")