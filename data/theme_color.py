import dataclasses


@dataclasses.dataclass
class ThemeColor:
    light: str
    dark: str


def fromJson(data):
    return ThemeColor(light=data.get('light'), dark=data.get('dark'))
